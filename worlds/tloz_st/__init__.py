import math
import os
import logging
import random
from typing import List, Union, ClassVar, Any, Optional, Tuple
import settings
from BaseClasses import Tutorial, Region, Location, LocationProgressType, Item, ItemClassification
from Fill import fill_restrictive, FillError
from Options import Accessibility, OptionError
from worlds.AutoWorld import WebWorld, World

from .Util import *
from .Options import *
from .Logic import create_connections
from .data import LOCATIONS_DATA
from .data.Constants import *
from .data.Items import ITEMS
from .data.Regions import REGIONS
from .data.LogicPredicates import *
from .data.Entrances import ENTRANCES

from .Client import SpiritTracksClient  # Unused, but required to register with BizHawkClient


class SpiritTracksWeb(WebWorld):
    theme = "grass"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Spirit Tracks for Archipelago on your computer.",
        "English",
        "st_setup_en.md",
        "st_setup/en",
        ["DayKat"]
    )

    tutorials = [setup_en]
    option_groups = st_option_groups

# Adds a consistent count of items to pool, independent of how many are from locations
def add_items_from_filler(item_pool_dict: dict, filler_item_count: int, item: str, count: int):
    count_addable = count-item_pool_dict.setdefault(item,0)
    if filler_item_count >= count_addable:
        item_pool_dict[item] += count_addable
        filler_item_count = filler_item_count - count_addable
    else:
        item_pool_dict[item] += filler_item_count
        filler_item_count = 0
        print(f"Ran out of filler items! at {item}")

    return item_pool_dict, filler_item_count

class SpiritTracksWorld(World):
    """
    The Legend of Zelda: Spirit Tracks is the train bound handheld sequel to Phantom Hourglass.
    """
    game = "The Legend of Zelda - Spirit Tracks"
    options_dataclass = SpiritTracksOptions
    options: SpiritTracksOptions
    required_client_version = (0, 6, 1)
    web = SpiritTracksWeb()
    topology_present = True

    settings_key = "tloz_st_options"

    location_name_to_id = build_location_name_to_id_dict()
    item_name_to_id = build_item_name_to_id_dict()
    item_name_groups = ITEM_GROUPS
    origin_region_name = "outset village"
    glitches_item_name = "_UT_Glitched_Logic"

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

        self.pre_fill_items: List[Item] = []
        self.required_dungeons = []
        self.boss_reward_items_pool = []
        self.boss_reward_location_names = []
        self.dungeon_name_groups = {}
        self.locations_to_exclude = set()
        self.ut_locations_to_exclude = set()
        self.extra_filler_items = []
        self.excluded_dungeons = []
        self.active_rabbit_locations: list[str] = []
        self.rabbit_counts: list[int] = []
        self.rabbit_item_dict: dict[str, int] = {}

    def generate_early(self):
        # self.pick_required_dungeons()
        self.restrict_non_local_items()
        self.active_rabbit_locations = self.choose_rabbit_locations()
        self.rabbit_item_dict = self.choose_rabbit_items()
        print(f"Rabbit items: {self.rabbit_item_dict}")

    def restrict_non_local_items(self):
        # Restrict non_local_items option in cases where it's incompatible with other options that enforce items
        # to be placed locally (e.g. dungeon items with keysanity off)
        if not self.options.keysanity == "anywhere":
            self.options.non_local_items.value -= self.item_name_groups["Small Keys"]
            self.options.non_local_items.value -= self.item_name_groups["Boss Keys"]
        self.options.non_local_items.value -= set(self.boss_reward_items_pool)

    def create_location(self, region_name: str, location_name: str, local: bool):
        region = self.multiworld.get_region(region_name, self.player)
        location = Location(self.player, location_name, self.location_name_to_id[location_name], region)
        region.locations.append(location)

        if local:
            location.item_rule = lambda item: item.player == self.player

    def create_regions(self):
        # Create regions
        for region_name in REGIONS:
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations
        for location_name, location_data in LOCATIONS_DATA.items():
            if not self.location_is_active(location_name, location_data):
                continue

            is_local = "local" in location_data and location_data["local"] is True
            self.create_location(location_data['region_id'], location_name, is_local)

        self.create_events()
        self.exclude_locations_automatically()

    def create_event(self, region_name, event_item_name):
        region = self.multiworld.get_region(region_name, self.player)
        location = Location(self.player, region_name + ".event", None, region)
        region.locations.append(location)
        location.place_locked_item(Item(event_item_name, ItemClassification.progression, None, self.player))

    def location_is_active(self, location_name, location_data):
        if not location_data.get("conditional", False) and "rabbit" not in location_data:
            return True
        if "rabbit" in location_data:
            return location_name in self.active_rabbit_locations
        if location_name == "Slippery Station Champion Reward":
            return self.options.logic

        return False

    def create_events(self):
        # if "Temple of Fire" in self.required_dungeons:
        #     self.create_event("tof blaaz", "_required_dungeon")
        if self.options.goal == 0:
            goal_loc = "goal_forest_glyph"
        elif self.options.goal == 1:
            goal_loc = "goal_snow_glyph"
        elif self.options.goal == 2:
            goal_loc = "goal_stagnox"
        elif self.options.goal == 3:
            goal_loc = "goal_fraaz"
        self.create_event(goal_loc, "_beaten_game")

        if self.options.rabbitsanity == "on_total":
            forest_regions = ["w castle town rabbit",
                              "forest ocean shortcut rabbit",
                              "e mayscore rabbit",
                              "sw trading post rabbit",
                              "e outset rabbit",
                              "sw rabbit haven rabbit",
                              "wt rabbit",
                              "nr rabbit haven rabbit",
                              "forest after bridge rabbit",
                              "s rabbit haven rabbit"]
            snow_regions = ["ne blizzard rabbit",
                            "se blizzard rabbit",
                            "w anouki village rabbit",
                            "sw blizzard rabbit",
                            "e anouki village rabbit",
                            "snowdrift station rabbit",
                            "w icyspring rabbit",
                            "n icyspring rabbit",
                            "nw blizzard rabbit",
                            "central blizzard rabbit"]
            [self.create_event(reg, f"_caught_{realm}_rabbits")
             for regions, realm in zip([forest_regions, snow_regions], ["forest", "snow"])
             for reg in regions]

    def exclude_locations_automatically(self):
        locations_to_exclude = set()

        # If non required dungeons need to be excluded, and not UT
        # if self.options.exclude_non_required_dungeons and not getattr(self.multiworld, "generation_is_fake", False):
        #     # always_include = ["Temple of the Ocean King", "Mountain Passage"]
        #     always_include = []
        #     excluded_dungeons = [d for d in DUNGEON_NAMES
        #                          if d not in self.required_dungeons + always_include]
        #     self.excluded_dungeons = excluded_dungeons
        #     for dungeon in excluded_dungeons:
        #         locations_to_exclude.update(self.dungeon_name_groups[dungeon])

        self.ut_locations_to_exclude = locations_to_exclude.copy()
        # Unexclude locations that have vanilla small keys/dung items cause in excluded dungeons, keys are vanilla
        for location in locations_to_exclude.copy():
            if ("Small Key" in LOCATIONS_DATA[location]["vanilla_item"] or
                    "Boss Key" in LOCATIONS_DATA[location]["vanilla_item"]):
                locations_to_exclude.remove(location)

        self.locations_to_exclude = locations_to_exclude

        # Take item off goal location
        if self.options.goal == SpiritTracksGoal(0):
            current_goal = "ToS Forest Rail Glyph"
            self.locations_to_exclude.add(current_goal)
        elif self.options.goal == SpiritTracksGoal(1):
            current_goal = "ToS Snow Rail Glyph"
            self.locations_to_exclude.add(current_goal)
        elif self.options.goal == SpiritTracksGoal(2):
            current_goal = "Wooded Temple Dungeon Reward"
            self.locations_to_exclude.add(current_goal)
        elif self.options.goal == SpiritTracksGoal(3):
            current_goal = "Blizzard Temple Dungeon Reward"
            self.locations_to_exclude.add(current_goal)

        for name in locations_to_exclude:
            self.multiworld.get_location(name, self.player).progress_type = LocationProgressType.EXCLUDED

    def set_rules(self):
        create_connections(self.multiworld, self.player, self.origin_region_name, self.options)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("_beaten_game", self.player)

    def create_item(self, name: str) -> Item:
        classification = ITEMS[name].classification
        if name in self.extra_filler_items:
            self.extra_filler_items.remove(name)
            classification = ItemClassification.filler

        ap_code = self.item_name_to_id[name]
        return Item(name, classification, ap_code, self.player)

    def build_item_pool_dict(self):
        removed_item_quantities = self.options.remove_items_from_pool.value.copy()
        item_pool_dict = {}
        filler_item_count = 0

        def pop_random_item_from_dict(item_dict):
            i_name = self.random.choice([i for i in item_dict])
            item_dict[i_name] -= 1
            if item_dict[i_name] <= 0:
                item_dict.pop(i_name)
            return i_name

        for loc_name, loc_data in LOCATIONS_DATA.items():
            # print(f"New Location: {loc_name}")
            if not self.location_is_active(loc_name, loc_data):
                # print(f"{loc_name} is not active")
                continue
            # If no defined vanilla item, fill with filler
            if "vanilla_item" not in loc_data:
                # print(f"{loc_name} has no defined vanilla item")
                filler_item_count += 1
                continue

            item_name = loc_data.get("item_override", loc_data["vanilla_item"])
            if isinstance(item_name, list):
                item_name = self.random.choice(item_name)
            item_data = ITEMS[item_name]
            if item_name in removed_item_quantities and removed_item_quantities[item_name] > 0:
                # If item was put in the "remove_items_from_pool" option, replace it with a random filler item
                removed_item_quantities[item_name] -= 1
                filler_item_count += 1
                continue

            if "rabbit" in item_data.tags:
                if self.options.rabbitsanity == "vanilla":  # Force vanilla rabbits randomly
                    forced_item = self.create_item(pop_random_item_from_dict(self.rabbit_item_dict))
                    self.multiworld.get_location(loc_name, self.player).place_locked_item(forced_item)
                    continue
                filler_item_count += 1
                continue
            if item_name in ["Filler Item", "Treasure", "Heart Container"]:
                filler_item_count += 1
                continue
            if "force_vanilla" in loc_data and loc_data["force_vanilla"]:
                forced_item = self.create_item(item_name)
                self.multiworld.get_location(loc_name, self.player).place_locked_item(forced_item)
                continue
            if item_data.classification == ItemClassification.filler:  # Regen all filler items for now
                if item_name not in ITEM_GROUPS["Super Rare Treasures"]:
                    filler_item_count += 1
                    continue
                else:
                    print(f"Saved item {item_name}")

            item_pool_dict[item_name] = item_pool_dict.get(item_name, 0) + 1
            #print(f"Location {loc_name} has {item_name} item")

        # TODO Fill filler count with consistent amounts of items, when filler count is empty it won't add any more items
        # so add progression items first
        add_items = []
        add_items += [(i, 1) for i in ITEM_GROUPS["All Tracks"]]
        add_items += [i for i in self.rabbit_item_dict.items()]
        add_items += [("Heart Container", 13)]
        print(f"Add items: ({sum([i for _, i in add_items])}/{filler_item_count})")
        for i, count in add_items:
            # print(f"\t{i}: {count}")
            item_pool_dict, filler_item_count = add_items_from_filler(item_pool_dict, filler_item_count, i, count)

        # Add as many filler items as required
        for _ in range(filler_item_count):
            random_filler_item = self.get_filler_item_name()
            item_pool_dict[random_filler_item] = item_pool_dict.get(random_filler_item, 0) + 1

        return item_pool_dict

    def choose_rabbit_locations(self):
        if not self.options.rabbitsanity:
            return []
        rabbit_locations = []
        # Figure out rabbit counts for different pools
        max_count = self.options.rabbit_max_location_count.value
        rabbit_counts = [max_count, max_count]
        if self.options.rabbit_location_count_distribution.value == -1:
            rabbit_counts = [self.random.randint(1, max_count), self.random.randint(1, max_count)]
        self.rabbit_counts = rabbit_counts

        # Figure out pools
        if self.options.rabbitsanity.value in [1, 2]: # Vanilla or unique
            forest_rabbits = LOCATION_GROUPS["Unique Forest Rabbits"]
            snow_rabbits = LOCATION_GROUPS["Unique Snow Rabbits"]
        else:
            forest_rabbits = LOCATION_GROUPS["Total Forest Rabbits"]
            snow_rabbits = LOCATION_GROUPS["Total Snow Rabbits"]
            interval = self.options.rabbit_location_count_distribution.value
            if interval >= 0:
                intervals = [interval]*2 if interval else [self.random.randint(1, 3) for _ in range(2)]
                for i, realm_locs in zip(intervals, [forest_rabbits, snow_rabbits]):
                    if i > max_count:
                        rabbit_locations.append(realm_locs[max_count-1])
                    else:
                        rabbit_locations += realm_locs[i-1:max_count:i]
                print(f"Rabbit Locations: {rabbit_counts} {intervals} {rabbit_locations}")
                return rabbit_locations

        # Randomly choose locations
        rabbit_loc_lists = [forest_rabbits, snow_rabbits]
        [self.random.shuffle(i) for i in rabbit_loc_lists]
        rabbit_locations = [loc for rl, c in zip(rabbit_loc_lists, rabbit_counts) for loc in rl[:c]]
        print(f"Rabbit Locations: {rabbit_counts} {rabbit_locations}")
        return rabbit_locations

    def choose_rabbit_items(self):
        if not self.options.rabbitsanity:
            return {}

        def get_rabbit_pack_name(realm, count):
            if count == 1:
                return f"{realm} Rabbit"
            return f"{realm} Rabbits ({count})"

        def create_items_from_count_list(realm, clist):
            res = {}
            for count in clist:
                item_name = get_rabbit_pack_name(realm, count)
                res.setdefault(item_name, 0)
                res[item_name] += 1
            # print(f"Creating rabbit items: {res}")
            return res

        def fill_vanilla(realm, max_count):
            count_distr = [1]*max_count
            if max_count == 1:
                return {get_rabbit_pack_name(realm, 10): 1}

            res_counts = []
            print(f"Filling vanilla rabbits {realm} {max_count}")
            while sum(count_distr) + sum(res_counts) < 10:
                randindex = self.random.randint(0, len(count_distr)-1)
                count_distr[randindex] += 1
                if count_distr[randindex] == 5:
                    res_counts.append(count_distr.pop(randindex))
            res_counts += count_distr
            res_counts += [1]*self.options.rabbit_extra_items.value  # Add bonus items
            return create_items_from_count_list(realm, res_counts)

        def fill_mixed(realm):
            res_counts = []
            while sum(res_counts) < 10:
                res_counts.append(round(self.random.triangular(0.5, 5.5, 2)))
            for i in range(self.options.rabbit_extra_items.value):
                res_counts.append(round(self.random.triangular(0.5, 5.5, 2)))
            return create_items_from_count_list(realm, res_counts)

        realms = ["Forest", "Snow"]
        rabbit_items = {}
        if self.options.rabbitsanity.value == 1:  # Vanilla
            print(f"Vanilla rabbits {self.rabbit_counts}")
            self.options.rabbit_pack_size.value = 1
            for r, c in zip(realms, self.rabbit_counts):
                rabbit_items |= fill_vanilla(r, c)
            return rabbit_items

        if self.options.rabbit_pack_size == -1:  # random_mixed
            print(f"Random Mixed")
            for r in realms:
                rabbit_items |= fill_mixed(r)
            return rabbit_items

        # Uniform packs
        if self.options.rabbit_pack_size == 0:  # Random uniform
            pack_sizes = [self.random.randint(1, 5), self.random.randint(1, 5)]
        else:
            pack_sizes = [self.options.rabbit_pack_size.value]*2
        print(f"Uniform Packs {pack_sizes}")
        for r, s in zip(realms, pack_sizes):
            item_count = math.ceil(10 / s) + self.options.rabbit_extra_items.value
            rabbit_items |= create_items_from_count_list(r, [s]*item_count)
        return rabbit_items

    def create_items(self):
        item_pool_dict = self.build_item_pool_dict()
        self.get_extra_filler_items(item_pool_dict)
        items = []
        for item_name, quantity in item_pool_dict.items():
            for _ in range(quantity):
                items.append(self.create_item(item_name))

        self.filter_confined_dungeon_items_from_pool(items)
        self.multiworld.itempool.extend(items)

    def get_extra_filler_items(self, item_pool_dict):
        # Create a random list of useful or currency items to turn into filler to satisfy all removed locations
        filler_count = 0
        extra_items_list = []
        for item, count in item_pool_dict.items():
            if 'backup_filler' in ITEMS[item].tags:
                extra_items_list.extend([item] * count)
            if ITEMS[item].classification in [ItemClassification.filler, ItemClassification.trap]:
                filler_count += count

        extra_item_count = len(self.locations_to_exclude) - filler_count + 20
        if extra_item_count > 0:
            self.random.shuffle(extra_items_list)
            self.extra_filler_items = extra_items_list[:extra_item_count]

    def get_pre_fill_items(self):
        return self.pre_fill_items

    def pre_fill(self) -> None:
        self.pre_fill_boss_rewards()
        self.pre_fill_dungeon_items()
        pass

    def filter_confined_dungeon_items_from_pool(self, items: List[Item]):
        confined_dungeon_items = []

        # Confine small keys and boss key to own dungeon if option is enabled
        if self.options.keysanity == "in_own_dungeon":
            confined_dungeon_items.extend([item for item in items if item.name.startswith("Small Key")])
            confined_dungeon_items.extend([item for item in items if item.name.startswith("Boss Key")])

        # Remove boss reward items from pool for pre filling
        confined_dungeon_items.extend([item for item in items if item.name in self.boss_reward_items_pool])

        for item in confined_dungeon_items:
            items.remove(item)
        self.pre_fill_items.extend(confined_dungeon_items)

    def pre_fill_boss_rewards(self):
        boss_reward_location_names = [DUNGEON_TO_BOSS_ITEM_LOCATION[dung_name] for dung_name in self.required_dungeons]
        self.boss_reward_location_names = boss_reward_location_names

        boss_reward_locations = [loc for loc in self.multiworld.get_locations(self.player)
                                 if loc.name in boss_reward_location_names]
        boss_reward_items = [item for item in self.pre_fill_items if item.name in self.boss_reward_items_pool]

        # Remove from the all_state the items we're about to place
        for item in boss_reward_items:
            self.pre_fill_items.remove(item)

        collection_state = self.multiworld.get_all_state(False)
        # Perform a prefill to place confined items inside locations of this dungeon
        self.random.shuffle(boss_reward_locations)
        fill_restrictive(self.multiworld, collection_state, boss_reward_locations, boss_reward_items,
                         single_player_placement=True, lock=True, allow_excluded=True)

    def pre_fill_dungeon_items(self):
        # If keysanity is off, dungeon items can only be put inside local dungeon locations, and there are not so many
        # of those which makes them pretty crowded.
        # This usually ends up with generator not having anywhere to place a few small keys, making the seed unbeatable.
        # To circumvent this, we perform a restricted pre-fill here, placing only those dungeon items
        # before anything else.
        for dung_name in DUNGEON_NAMES:
            # Build a list of locations in this dungeon
            print(f"Pre-filling {dung_name}")
            dungeon_location_names = [name for name, loc in LOCATIONS_DATA.items()
                                      if "dungeon" in loc and loc["dungeon"] == dung_name]
            dungeon_locations = [loc for loc in self.multiworld.get_locations(self.player)
                                 if loc.name in dungeon_location_names and not loc.locked]

            # From the list of all dungeon items that needs to be placed restrictively, only filter the ones for the
            # dungeon we are currently processing.
            confined_dungeon_items = [item for item in self.pre_fill_items
                                      if item.name.endswith(f"({dung_name})")]
            if len(confined_dungeon_items) == 0:
                continue  # This list might be empty with some keysanity options

            # Remove from the all_state the items we're about to place
            for item in confined_dungeon_items:
                self.pre_fill_items.remove(item)
            collection_state = self.multiworld.get_all_state(False)
            # Perform a prefill to place confined items inside locations of this dungeon
            self.random.shuffle(dungeon_locations)
            fill_restrictive(self.multiworld, collection_state, dungeon_locations, confined_dungeon_items,
                             single_player_placement=True, lock=True, allow_excluded=True)

    def get_filler_item_name(self) -> str:
        filler_item_names = (ITEM_GROUPS["Common Treasures"] +
                             ITEM_GROUPS["Uncommon Treasures"] +
                             ITEM_GROUPS["Ammo Refills"] +
                             ["Green Rupee (1)",
                              "Blue Rupee (5)",
                              "Red Rupee (20)",
                              "Big Green Rupee (100)"]
                             )
        rare_filler_items = ITEM_GROUPS["Rare Treasures"] + [
            "Big Red Rupee (200)", "Gold Rupee (300)",
        ]
        # 1/20 chance to roll a rare filler item
        if self.random.randint(1, 20) == 1:
            return self.random.choice(rare_filler_items)
        return self.random.choice(filler_item_names)

    def fill_slot_data(self) -> dict:
        options = ["keysanity", "goal", "logic",
                   "rabbitsanity", "rabbit_hints"]
        slot_data = self.options.as_dict(*options)
        return slot_data

    def write_spoiler(self, spoiler_handle):
        return
        
        spoiler_handle.write(f"\n\nRequired Dungeons ({self.multiworld.player_name[self.player]}):\n")
        for dung in self.required_dungeons:
            spoiler_handle.write(f"\t- {dung}\n")

    # UT stuff
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, any]) -> None:
        return slot_data

