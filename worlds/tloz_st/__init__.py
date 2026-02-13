import math
from typing import List, Union, ClassVar, Any, Optional, Tuple
import settings
from BaseClasses import Tutorial, Region, Location, LocationProgressType, Item, ItemClassification, Entrance
from Fill import fill_restrictive, FillError
from Options import Accessibility, OptionError
from worlds.AutoWorld import WebWorld, World

from .Util import *
from .Options import *

from .data import LOCATIONS_DATA
from .data.Constants import *
from .data.Items import ITEMS
from .data.Regions import REGIONS
from .data.LogicPredicates import *
from .data.Entrances import (ENTRANCES, entrance_id_to_region, entrance_id_to_entrance,
                             location_event_lookup, goal_event_lookup)
from entrance_rando import disconnect_entrance_for_randomization

from .Client import SpiritTracksClient  # Unused, but required to register with BizHawkClient
from .Subclasses import EntranceGroups

try:  # Backwards compatibility yay
    from rule_builder.cached_world import CachedRuleBuilderWorld as WorldParent
    from .LogicRB import create_connections
except ModuleNotFoundError:
    print(f"Using legacy logic")
    WorldParent = World
    from .Logic import create_connections

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

class SpiritTracksSettings(settings.Group):
    class STTrainSpeed(list[int]):
        """
        Train speed for each of the 4 gears, from lowest (reverse) to highest.
        defaults are -143, 0, 115, 193
        """
    class STTrainInstantStation(str):
        """
        Allows entering stations immediately on the stop gear, no matter your speed.
        """
    class STTrainSnapSpeed(str):
        """
        The train will instantly switch to the new speed when changing gears, no acceleration required.
        Does not apply to your stop gear.
        """

    train_speed: STTrainSpeed = STTrainSpeed([-143, 0, 115, 193])
    train_snap_speed: Union[STTrainSnapSpeed, bool] = True
    train_quick_station: Union[STTrainInstantStation, bool] = True


class SpiritTracksWorld(WorldParent):
    """
    The Legend of Zelda: Spirit Tracks is the train bound handheld sequel to Phantom Hourglass.
    """
    game = "The Legend of Zelda - Spirit Tracks"
    options_dataclass = SpiritTracksOptions
    options: SpiritTracksOptions
    settings: ClassVar[SpiritTracksSettings]
    required_client_version = (0, 6, 1)
    web = SpiritTracksWeb()
    topology_present = True

    settings_key = "tloz_st_options"

    # UT Attributes
    location_name_to_id = build_location_name_to_id_dict()
    item_name_to_id = build_item_name_to_id_dict()
    item_name_groups = ITEM_GROUPS
    location_name_groups = LOCATION_GROUPS
    origin_region_name = "outset village"
    glitches_item_name = "_UT_Glitched_Logic"
    ut_can_gen_without_yaml = True
    tracker_world = {"map_page_folder": "tracker",
                     "map_page_maps": "maps/maps.json",
                     "map_page_locations": "locations/overworld.json"}
    found_entrances_datastorage_key = ["st_checked_entrances_{player}_{team}"]

    # Rule builder attributes
    item_mapping = ITEM_MAPPING

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
        self.rabbit_realm_items: dict[str, dict[str, int]] = {"Forest": {}, "Snow": {}}
        self.item_mapping_collect: dict[str, tuple[str, int]] = {}

        self.ut_checked_entrances = set()
        self.ut_pairings = {}
        self.ut_events = []
        self.is_ut = getattr(self.multiworld, "generation_is_fake", False)

        self.ut_map_page_hidden_entrances = []

    def generate_early(self):
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            # Get the passed through slot data from the real generation
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]
            print(slot_data)
            # slot_options: dict[str, Any] = slot_data.get("options", {})
            # Set all your options here instead of getting them from the yaml
            for key, value in slot_data.items():
                opt = getattr(self.options, key, None)
                if opt is not None:
                    # You can also set .value directly but that won't work if you have OptionSets
                    setattr(self.options, key, opt.from_any(value))
            lookup = build_rabbit_location_id_to_name_dict()
            self.active_rabbit_locations = [lookup[i] for i in slot_data["active_rabbit_locs"]]
            self.required_dungeons = slot_data["required_dungeons"]
            self.pick_ut_events()
        else:
            self.required_dungeons = self.pick_required_dungeons()
            self.restrict_non_local_items()
            self.active_rabbit_locations = self.choose_rabbit_locations()
            self.rabbit_item_dict = self.choose_rabbit_items()
            print(f"Rabbit items: {self.rabbit_item_dict}")
            if self.options.start_with_train:
                self.options.start_inventory_from_pool.value.update({"Forest Glyph": 1, "Cannon": 1})
        self.create_item_mappings()

    def pick_ut_events(self):
        events = ["EVENT: Pick up Alfonzo",
                  goal_event_lookup[self.options.goal.value]]


        if self.options.goal == "defeat_malladus":
            if self.options.dungeon_hints or not self.options.require_specific_dungeons:
                events += [location_event_lookup[loc] for loc in self.required_dungeons]
            else:
                events += ["EVENT: Defeat Stagnox", "EVENT: Defeat Fraaz"]
                if self.options.tos_dungeon_options == "final_section":
                    events += ["EVENT: Reach ToS 7F"]
                elif self.options.tos_dungeon_options == "all_sections":
                    events += ["EVENT: Reach ToS 3F", "EVENT: Reach ToS 7F"]

        self.ut_events = events
        self.ut_map_page_hidden_entrances = {"Overview": [e.name for e in ENTRANCES.values() if
                                             e.category_group == EntranceGroups.EVENT and e.name not in self.ut_events]}
        for e in events:
            event = ENTRANCES[e]
            self.ut_pairings[str(event.id)] = event.vanilla_reciprocal.id

    def create_item_mappings(self):
        self.item_mapping_collect = {
            i: ("Rupees", ITEMS[i].value) for i in ITEM_GROUPS["Rupees"]
        } | {
            r: ("Forest Rabbit", ITEMS[r].value) for r in ITEM_GROUPS["Forest Rabbits"][1:]
        } | {
            r: ("Snow Rabbit", ITEMS[r].value) for r in ITEM_GROUPS["Snow Rabbits"][1:]
        }

    def pick_required_dungeons(self) -> list[str]:
        if self.options.goal != "defeat_malladus" or self.options.dark_realm_access != "dungeons":
            return []

        required_dungeons = ["Wooded Temple Dungeon Reward", "Blizzard Temple Dungeon Reward"]
        implemented_tos = ["ToS 3F Forest Rail Glyph", "ToS 7F Snow Rail Glyph"]
        if self.options.tos_dungeon_options == "final_section":
            required_dungeons.append(implemented_tos[-1])
        elif self.options.tos_dungeon_options == "all_sections":
            required_dungeons += implemented_tos

        if not self.options.require_specific_dungeons:
            return required_dungeons

        self.options.dungeons_required.value = min(self.options.dungeons_required.value, len(required_dungeons))
        self.random.shuffle(required_dungeons)
        required_dungeons = required_dungeons[:self.options.dungeons_required.value]
        if self.options.dungeon_hints:
            self.options.start_location_hints.value.update(required_dungeons)
        return required_dungeons

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
        region = self.get_region(region_name)
        location = Location(self.player, region_name + ".event", None, region)
        region.locations.append(location)
        location.place_locked_item(Item(event_item_name, ItemClassification.progression, None, self.player))

    # When you want multiple copies of the same event in the same region
    def create_multiple_events(self, region_name, event_item_name, count):
        region = self.get_region(region_name)
        locations = [Location(self.player, region_name + f"{i}.event", None, region) for i in range(count)]
        for loc in locations:
            region.locations.append(loc)
            loc.place_locked_item(Item(event_item_name, ItemClassification.progression, None, self.player))

    def location_is_active(self, location_name, location_data):
        if not location_data.get("conditional", False) and "rabbit" not in location_data:
            return True
        if "rabbit" in location_data:
            return location_name in self.active_rabbit_locations
        if location_name == "Slippery Station Champion Reward":
            return self.options.logic
        if "Portal" in location_name:
            return self.options.portal_checks
        if "Rabbit Haven" in location_name:
            return self.options.rabbitsanity

        return False

    def create_events(self):
        if self.options.goal == "defeat_malladus":
            for loc in self.required_dungeons:
                self.create_event(BOSS_LOCATION_TO_EVENT_REGION[loc], "_dungeon_reward")
            self.create_event("malladus goal", "_beaten_game")
        else:
            if self.options.goal == "beat_tos_section_1":
                goal_loc = "goal_forest_glyph"
            elif self.options.goal == "beat_tos_section_2":
                goal_loc = "goal_snow_glyph"
            elif self.options.goal == "beat_wooded_temple":
                goal_loc = "goal_stagnox"
            elif self.options.goal == "beat_blizzard_temple":
                goal_loc = "goal_fraaz"
            self.create_event(goal_loc, "_beaten_game")

        if self.options.rabbitsanity.value in [3, 4]:
            forest_regions = {"forest ocean shortcut rabbit": 1,
                              "e mayscore rabbits": 2,
                              "sw trading post rabbit": 1,
                              "wt rabbit": 1,
                              "s rabbit haven rabbits": 2,
                              "nr rabbit haven rabbit": 1,
                              "forest realm rabbits": 2}
            snow_regions = {"snow realm blizzard rabbits": 2,
                            "snow realm early blizzard rabbits": 3,
                            "blizzard temple tracks rabbits": 1,
                            "snow realm rabbits": 1,
                            "snowdrift station rabbit": 1,
                            "icyspring rabbits": 2}
            [self.create_multiple_events(reg, f"_caught_{realm}_rabbits", count)
             for regions, realm in zip([forest_regions, snow_regions], ["forest", "snow"])
             for reg, count in regions.items()]

        # UT Events
        self.create_event("alfonzo event", "_picked_up_alfonzo")


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
        self.locations_to_exclude = locations_to_exclude

        # Take item off goal location
        if self.options.goal == SpiritTracksGoal(0):
            current_goal = "ToS 3F Forest Rail Glyph"
            self.locations_to_exclude.add(current_goal)
        elif self.options.goal == SpiritTracksGoal(1):
            current_goal = "ToS 7F Snow Rail Glyph"
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
        create_connections(self, self.player, self.origin_region_name, self.options)

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

        def pop_item_from_dict(item_dict, item):
            item_dict[item] -= 1
            if item_dict[item] <= 0:
                item_dict.pop(item)

        def pop_random_item_from_dict(item_dict):
            i_name = self.random.choice([i for i in item_dict])
            pop_item_from_dict(item_dict, i_name)
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
                if self.options.rabbitsanity == "vanilla" and not hasattr(self.multiworld, "generation_is_fake"):  # Force vanilla rabbits randomly
                    realm = item_name.split()[0]
                    realm_pool = self.rabbit_realm_items[realm]
                    popped_item = pop_random_item_from_dict(realm_pool)
                    pop_item_from_dict(self.rabbit_item_dict, popped_item)

                    forced_item = self.create_item(popped_item)
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

            item_pool_dict[item_name] = item_pool_dict.get(item_name, 0) + 1
            #print(f"Location {loc_name} has {item_name} item")

        # TODO Fill filler count with consistent amounts of items, when filler count is empty it won't add any more items
        # so add progression items first
        add_items = [("Compass of Light", 1), ("Bow of Light", 1)]
        add_items += [(i, 1) for i in ITEM_GROUPS["All Tracks"]]
        if self.options.portal_behavior.value == 2:
            add_items += [(i, 1) for i in ITEM_GROUPS["Portal Unlocks"]]
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

        def pick_random_locs(loc_lists):
            [self.random.shuffle(i) for i in loc_lists]
            return [loc for rl, c in zip(loc_lists, rabbit_counts) for loc in rl[:c]]

        # Figure out pools
        if self.options.rabbitsanity.value in [1, 2, 4]: # Vanilla or unique
            forest_rabbits = LOCATION_GROUPS["Unique Forest Rabbits"]
            snow_rabbits = LOCATION_GROUPS["Unique Snow Rabbits"]
            rabbit_locations += pick_random_locs([forest_rabbits, snow_rabbits])

        if self.options.rabbitsanity.value in [3, 4]:  # total count
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
            if self.options.rabbitsanity == "both":  # Randomize each pool count separately
                self.rabbit_counts = [self.random.randint(1, max_count), self.random.randint(1, max_count)]
            rabbit_locations += pick_random_locs([forest_rabbits, snow_rabbits])

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
                vanilla_pool = fill_vanilla(r, c)
                rabbit_items |= vanilla_pool
                self.rabbit_realm_items[r] = vanilla_pool
            return rabbit_items

        if self.options.rabbit_pack_size == -1:  # random_mixed
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

    def connect_entrances(self) -> None:
        if self.is_ut:
            disconnect_ids = {int(i) for i in self.ut_pairings.keys()}
            for event in self.ut_events:
                e = self.get_entrance(event)
                if ENTRANCES[e.name].id in disconnect_ids:
                    target_name = ENTRANCES[e.name].vanilla_reciprocal.name
                    disconnect_entrance_for_randomization(e, one_way_target_name=target_name)

    def get_pre_fill_items(self):
        return self.pre_fill_items

    def pre_fill(self) -> None:
        # self.pre_fill_boss_rewards()
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
            # print(f"Pre-filling {dung_name}")
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

    def collect(self, state: CollectionState, item: Item) -> bool:
        # Code borrowed from Ishigh's early Rule Builder implementation
        change = super().collect(state, item)
        if not change:
            return False

        mapping = self.item_mapping_collect.get(item.name, None)
        if mapping is not None:
            #print(f"Mapping {mapping} {state.prog_items[self.player][mapping[0]]} for item {item.name}")
            state.prog_items[self.player][mapping[0]] += mapping[1]

        return True

    def remove(self, state: CollectionState, item: Item) -> bool:
        change = super().remove(state, item)
        if not change:
            return False

        mapping = self.item_mapping_collect.get(item.name, None)
        if mapping is not None:
            state.prog_items[self.player][mapping[0]] -= mapping[1]

        return True

    def fill_slot_data(self) -> dict:
        options = ["goal", "logic", "keysanity",
                   "rabbitsanity", # "rabbit_hints",
                   "exclude_locations",
                   "portal_behavior", "portal_checks",
                   "dark_realm_access", "endgame_scope", "dungeons_required"]
        slot_data = self.options.as_dict(*options)
        slot_data["active_rabbit_locs"] = [LOCATIONS_DATA[loc]["id"] for loc in self.active_rabbit_locations]
        slot_data["required_dungeons"] = self.required_dungeons
        return slot_data

    def write_spoiler(self, spoiler_handle):
        if self.options.dark_realm_access == "dungeons":
            title_str = "Required Dungeons" if self.options.require_specific_dungeons else "Dungeon Locations"
            spoiler_handle.write(f"\n\n{title_str} ({self.multiworld.player_name[self.player]}):\n")
            for dung in self.required_dungeons:
                spoiler_handle.write(f"\t- {dung}\n")

    # UT stuff
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]):
        return slot_data

    def reconnect_found_entrances(self, key, stored_data):
        print(f"UT Tried to defer entrances! key {key}"
              f" {stored_data}"
              )

        if getattr(self.multiworld, "enforce_deferred_connections", "default") == "off":
            print(f"Don't defer entrances when off")

        if "st_checked_entrances" in key and stored_data:
            new_connections = set(stored_data) - self.ut_checked_entrances
            self.ut_checked_entrances |= new_connections

            for i in new_connections:
                pairing = self.ut_pairings.get(str(i), None)
                # print(f"Pairing {pairing} {entrance_id_to_entrance[i].name}")
                if pairing is not None:
                    _exit: "Entrance" = self.get_entrance(entrance_id_to_entrance[i].name)
                    entrance_region: "Region" = self.get_region(entrance_id_to_region[pairing])
                    print(f"Connecting: {_exit} => {entrance_region} | {i}: {pairing}")
                    _exit.connect(entrance_region)