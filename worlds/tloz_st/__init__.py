import math
from typing import List, Union, ClassVar, Any, Optional, Tuple
import settings
from BaseClasses import Tutorial, Region, Location, LocationProgressType, Item, ItemClassification, Entrance
from Fill import fill_restrictive, FillError
from Options import Accessibility, OptionError
from worlds.AutoWorld import WebWorld, World
from entrance_rando import randomize_entrances

from .Util import *
from .Options import *

from .data import LOCATIONS_DATA
from .data.Items import ITEMS
from .data.Constants import *
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
    raise ModuleNotFoundError
except ModuleNotFoundError:
    # print(f"Spirit Tracks is using legacy logic")
    WorldParent = World
    from .Logic import create_connections

try:
    DEPRIORITIZED_SKIP_BALANCING_FALLBACK = ItemClassification.progression_deprioritized_skip_balancing
    DEPRIORITIZED_FALLBACK = ItemClassification.progression_deprioritized
except AttributeError:
    DEPRIORITIZED_SKIP_BALANCING_FALLBACK = ItemClassification.progression_skip_balancing
    DEPRIORITIZED_FALLBACK = ItemClassification.progression

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

dev_prints = False

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
                     "map_page_locations": ["locations/overworld.json", "entrances/entrances.json"]}
    found_entrances_datastorage_key = ["st_checked_entrances_{player}_{team}"]

    # Rule builder attributes
    item_mapping = ITEM_MAPPING

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

        self.pre_fill_items: List[Item] = []
        self.required_dungeons = []
        self.dungeon_name_groups = {}
        self.locations_to_exclude = set()
        self.ut_locations_to_exclude = set()
        self.extra_filler_items = []
        self.excluded_dungeons = []
        self.active_rabbit_locations: list[str] = []
        self.rabbit_counts: list[int] = []
        self.rabbit_item_dict: dict[str, int] = {}
        self.rabbit_realm_items: dict[str, dict[str, int]] = {"Grass": {}, "Snow": {}}
        self.item_mapping_collect: dict[str, tuple[str, int]] = {}

        self.ut_checked_entrances = set()
        self.ut_pairings = {}
        self.ut_events = []
        self.is_ut = getattr(self.multiworld, "generation_is_fake", False)

        self.ut_map_page_hidden_entrances = {"Overview": []}

        self.er_placement_state = None
        self.valid_entrances: list["Entrance"] = []
        self.plando_pairings = {}  # int: int pairing
        self.tower_pairings = []  # zip object of entrance strings
        self.tower_section_lookup = {i:i for i in range(1, 7)}  # tower section lookup for logic

        self.stamp_items = []
        self.stamp_pack_order = []
        self.model_lookup = {}

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
            self.ut_pairings = slot_data["er_pairings"]
            self.tower_section_lookup = {int(k): v for k, v in slot_data["tower_section_lookup"].items()}
            self.hide_ut_map_stuff()
            self.pick_ut_events()
        else:
            self.required_dungeons = self.pick_required_dungeons()
            # print(f"Required Dungeons: {self.required_dungeons}")
            self.restrict_non_local_items()
            self.active_rabbit_locations = self.choose_rabbit_locations()
            self.rabbit_item_dict = self.choose_rabbit_items()
            self.choose_stamp_items()
            # print(f"Rabbit items: {self.rabbit_item_dict}")
            self.plando_tos_sections()

            # Starting Train
            if self.options.start_with_train:
                self.options.start_inventory_from_pool.value.update({"Forest Glyph": 1})
                if self.options.cannon_logic.value in [0, 1]:
                    self.options.start_inventory_from_pool.value.update({"Cannon": 1})
            # Tear conditions
            if self.options.randomize_tears.value <= 0:  # Vanilla/no tears
                self.options.tear_size.value = 0  # force small tears
                self.options.tear_sections.value = 0  # force per-section grouping when vanilla
            if self.options.tear_sections.value == 0:
                self.options.spirit_weapons.value = 0  # no spirit weapons if not progressive/all sections
            if self.options.tear_sections.value > 0 and self.options.randomize_tears == "in_own_section":
                self.options.randomize_tears.value = 2  # all sections/progressive can't be in own section, make in_tos

            if self.options.starting_train == "random_train":
                self.options.starting_train.value = self.random.randint(0, 7)
            if "all" in self.options.shopsanity.value:
                self.options.shopsanity.value = self.options.shopsanity.valid_keys
            # print(f"Shopsanity {self.options.shopsanity.value}")
        self.create_item_mappings()

    def plando_tos_sections(self):
        """Plando ToS Shuffle early so we can use the ordering in logic"""
        if not self.options.shuffle_tos_sections:
            return

        # Sophisticated shuffle to avoid loops
        entrances = list(ENTRANCE_TO_TOS_ORDER.keys())
        exits = list(EXIT_TO_TOS_SECTION.keys()) + ["ToS Summit Lower Exit"]
        banned_connections = {"Tower of Spirits Exit Staven": ["ToS 18F Exit"],
                              "Tower of Spirits Summit Enter Altar": ["ToS Summit Lower Exit"]}
        self.random.shuffle(exits)
        for entrance in entrances:
            if exits[0] in banned_connections.get(entrance, []):
                self.tower_pairings.append((entrance, exits.pop(1)))
            else:
                self.tower_pairings.append((entrance, exits.pop(0)))
            if entrance == "Tower of Spirits Exit Staven" and self.tower_pairings[0][1] == "ToS Summit Lower Exit":
                banned_connections["Tower of Spirits Summit Enter Altar"].append("ToS 18F Exit")

        # print(f"Tower pairings: {list(self.tower_pairings)}")
        self.plando_pairings |= {ENTRANCES[e1].id: ENTRANCES[e2].id for e1, e2 in self.tower_pairings}
        self.plando_pairings |= {e2: e1 for e1, e2 in self.plando_pairings.items()}

        # Get lookup table for logic progressive tear sections
        sort_filter = {}
        for pair, entr in self.tower_pairings:
            if entr in EXIT_TO_TOS_SECTION and pair in ENTRANCE_TO_TOS_ORDER:
                sort_filter[EXIT_TO_TOS_SECTION[entr]] = ENTRANCE_TO_TOS_ORDER[pair]
        to_sort = [i for i in sort_filter]
        to_sort.sort(key=lambda i: sort_filter[i])
        self.tower_section_lookup = {section: i + 1 for i, section in enumerate(to_sort)}
        # print(f"Section lookup: {self.tower_section_lookup}")

    def hide_ut_map_stuff(self):
        self.tracker_world["map_page_locations"].append("locations/tos_singles.json")
        if not self.options.shuffle_tos_sections:
            self.ut_map_page_hidden_entrances["Overview"] += [e.name for e in ENTRANCES.values()
                                                              if e.category_group == EntranceGroups.TOS_SECTION]

    def pick_ut_events(self):
        events = ["EVENT: Give Regal Ring to Linebeck",
                  goal_event_lookup[self.options.goal.value]]

        if self.options.randomize_passengers == "vanilla":
            events += ["EVENT: Pick up Alfonzo"]
        if self.options.randomize_cargo == "vanilla":
            pass
        if self.options.randomize_cargo.value > 0:
            events += ["EVENT: Bring Ice to Kagoron"]

        if self.options.goal == "defeat_malladus":
            if self.options.dungeon_hints or not self.options.require_specific_dungeons:
                events += [location_event_lookup[loc] for loc in self.required_dungeons]
            else:
                events += ["EVENT: Defeat Stagnox", "EVENT: Defeat Fraaz", "EVENT: Defeat Cactops", "EVENT: Defeat Vulcano", "EVENT: Defeat Skeldritch"]
                if self.options.tos_dungeon_options == "final_section":
                    events += ["EVENT: Defeat Staven"]
                elif self.options.tos_dungeon_options == "all_sections":
                    events += ["EVENT: Reach ToS 3F", "EVENT: Reach ToS 7F", "EVENT: Reach ToS 12F", "EVENT: Reach ToS 17F", "EVENT: Defeat Staven", "EVENT: Reach ToS 24F"]

        self.ut_events = events
        self.ut_map_page_hidden_entrances["Overview"] += [e.name for e in ENTRANCES.values() if
                                             e.category_group == EntranceGroups.EVENT and e.name not in self.ut_events and not e.name.startswith("Unnamed")]
        print(f"UT Events: {events} hidden: {self.ut_map_page_hidden_entrances}")
        for e in events:
            event = ENTRANCES[e]
            self.ut_pairings[str(event.id)] = event.vanilla_reciprocal.id

    def create_item_mappings(self):
        self.item_mapping_collect = {
            i: ("Rupees", ITEMS[i].value) for i in ITEM_GROUPS["Rupee Items"]
        } | {
            r: ("Grass Rabbit", ITEMS[r].value) for r in grass_rabbits[1:]
        } | {
            r: ("Snow Rabbit", ITEMS[r].value) for r in snow_rabbits[1:]
        } | {
            r: ("Mountain Rabbit", ITEMS[r].value) for r in mountain_rabbits[1:]
        } | {
            r: ("Sand Rabbit", ITEMS[r].value) for r in sand_rabbits[1:]
        } | {
            t: ("Treasure", price) for t, price in TREASURE_PRICES.items()
        } | {
            i: ("Stamp", ITEMS[i].value) for i in ITEM_GROUPS["Stamp Packs"]
        } | {
            i: ("Stamp", 1) for i in ITEM_GROUPS["Stamps"]
        } | {

        # Events
            "_stamp_stand": ("Stamp", 1)
        }

    def pick_required_dungeons(self) -> list[str]:
        if self.options.goal != "defeat_malladus" or self.options.dark_realm_access != "dungeons":
            return []
        if self.options.plando_dungeon_pool:
            case_compare = {k.lower(): v for k, v in DUNGEON_TO_BOSS_ITEM_LOCATION.items()}
            required_dungeons = [case_compare[dung.lower()] for dung in self.options.plando_dungeon_pool.value]
        else:
            required_dungeons = ["Wooded Temple Dungeon Reward", "Blizzard Temple Dungeon Reward",
                                 "Marine Temple Dungeon Reward", "Mountain Temple Dungeon Reward",
                                 "Desert Temple Dungeon Reward"]
            implemented_tos = ["ToS 3F Forest Rail Glyph", "ToS 7F Snow Rail Glyph",
                               "ToS 12F Ocean Rail Glyph", "ToS 17F Fire Rail Glyph",
                               "ToS 23F Defeat Staven", "ToS 24F Final Chest"]
            if self.options.tos_dungeon_options == "final_section":
                required_dungeons.append(implemented_tos[-1])
            elif self.options.tos_dungeon_options == "all_sections":
                required_dungeons += implemented_tos

        self.options.dungeons_required.value = min(self.options.dungeons_required.value, len(required_dungeons))
        # print(f"Required dungeons: {required_dungeons}")
        if not self.options.require_specific_dungeons:
            return required_dungeons

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

        if "Portal" in location_name:
            return self.options.portal_checks
        if "Rabbit Haven" in location_name:
            return self.options.rabbitsanity
        if location_name.endswith("Boss Key"):
            return self.options.randomize_boss_keys
        if location_data["conditional"] == "tears":
            return self.options.randomize_tears.value != -1  # not vanilla
        if "minigame" in location_data and self.options.randomize_minigames:
            return self.options.randomize_minigames.value in location_data["minigame"]
        if location_name in LOCATION_GROUPS["Stamp Stands"]:
            return self.options.randomize_stamps.value in [2, 3]
        if location_name in LOCATION_GROUPS["Niko"]:
            return self.options.randomize_stamps
        if self.options.shopsanity and location_name in LOCATION_GROUPS["Shop Locations"]:
            if location_name in LOCATION_GROUPS["Shop Restock Locations"]:
                if "uniques" in self.options.shopsanity.value:
                    return False
                if location_name == "Beedle Buy Purple Potion":
                    return "potions" in self.options.shopsanity.value
                if location_name == "Snow Sanctuary Shop Treasure":
                    return "treasure" in self.options.shopsanity.value
                if location_name == "Goron Shop Postcards":
                    return "postcards" in self.options.shopsanity.value
            if location_name in LOCATION_GROUPS["Shop Treasure Locations"]:
                return "treasure" in self.options.shopsanity.value
            if location_name in LOCATION_GROUPS["Shop Unique Locations"]:
                return "uniques" in self.options.shopsanity.value
            if location_name in LOCATION_GROUPS["Shop Potion Locations"]:
                return "potions" in self.options.shopsanity.value
            if location_name in LOCATION_GROUPS["Shop Shield Locations"]:
                return "shields" in self.options.shopsanity.value
            if location_name in LOCATION_GROUPS["Shop Postcard Locations"]:
                return "postcards" in self.options.shopsanity.value
            if location_name in LOCATION_GROUPS["Shop Ammo Locations"]:
                return "ammo" in self.options.shopsanity.value
        if location_name == "Anouki Village Repair Fence":
            return self.options.randomize_passengers.value or self.options.randomize_cargo.value
        if location_name == "Anouki Village Fence Progress Gift":
            return self.options.randomize_passengers.value and self.options.randomize_cargo.value
        if self.options.randomize_passengers and location_name in LOCATION_GROUPS["Passenger Locations"]:
            if "slot_data" in location_data:
                for option, values, *args in location_data["slot_data"]:
                    if option != "randomize_passengers":
                        continue
                    values = values if isinstance(values, list) else [values]
                    if self.options.randomize_passengers.value not in values:
                        return False
                return True
        if self.options.randomize_cargo and location_name in LOCATION_GROUPS["Cargo Locations"]:
            if "slot_data" in location_data:
                for option, values, *args in location_data["slot_data"]:
                    if option != "randomize_cargo":
                        continue
                    values = values if isinstance(values, list) else [values]
                    if self.options.randomize_cargo.value not in values:
                        return False
                return True
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
            mountain_regions = {"fire realm rabbits": 2,
                                "mountain rabbits": 4,
                                "fire source rabbits": 1,
                                "disorientation rabbits": 1,
                                "eote rabbits": 1,
                                "s mountain temple rabbit": 1}
            sand_regions = {"sand realm rabbits": 4,
                            "sand restoration rabbits": 5,
                            "sand connection rabbit": 1}
            [self.create_multiple_events(reg, f"_caught_{realm}_rabbits", count)
             for regions, realm in zip([forest_regions, snow_regions, mountain_regions, sand_regions], ["grass", "snow", "mountain", "sand"])
             for reg, count in regions.items()]

        if self.options.randomize_stamps.value in [1, 4]:
            [self.create_event(LOCATIONS_DATA[loc]["region_id"], "_stamp_stand") for loc in LOCATION_GROUPS["Stamp Stands"]]

        # Create rupee farming events
        rupee_farming_regions = ["mayscore whip chest", "mayscore leaves", "trading post leaves",
                                 "hyrule castle sword minigame", "castle town"]
        [self.create_event(reg, "_rupee_farming_spot") for reg in rupee_farming_regions]
        # Passenger Events
        if self.options.randomize_passengers == "vanilla":
            self.create_event("pick up bridge worker", "_kenzo_1")
            self.create_event("trading post pick up kenzo", "_kenzo_2")
            self.create_event("av noko", "_noko")
            self.create_event("castle town mona", "_mona")
            self.create_event("outset joe", "_joe")
            self.create_event("alfonzo event", "_picked_up_alfonzo")
            self.create_event("mayscore dovok", "_dovok")
            self.create_event("av kofu", "_kofu")
            self.create_event("pick up gorons", "_goron")
            self.create_event("goron ice event", "_goron_ice")
        if self.options.randomize_cargo == "vanilla":
            self.create_event("mayscore lumber", "_buy_lumber")
            self.create_event("icyspring ice", "_buy_ice")
            self.create_event("castle town buy cuccos", "_buy_cuccos")
            self.create_event("papuzia buy cargo", "_buy_fish")
            self.create_event("dark ore mine ore", "_buy_ore")
            self.create_event("goron steel", "_buy_steel")
        # UT Events
        # self.create_event("alfonzo event", "_picked_up_alfonzo")
        self.create_event("linebeck event", "_can_sell_treasure")


    def exclude_locations_automatically(self):
        locations_to_exclude = set()

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
        if self.options.shopsanity and name in ITEM_GROUPS["Uncommon Plus Treasure"] | ITEM_GROUPS["Big Rupees"]:
            # print(f"Changing classification for item {name}")
            classification = DEPRIORITIZED_SKIP_BALANCING_FALLBACK

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
            # print(f"New Location: {loc_name} {filler_item_count}")
            if not self.location_is_active(loc_name, loc_data):
                # print(f"{loc_name} is not active")
                continue
            # If no defined vanilla item, fill with filler
            if "vanilla_item" not in loc_data:
                # print(f"\t{loc_name} has no defined vanilla item")
                filler_item_count += 1
                continue

            item_name = loc_data.get("item_override", loc_data["vanilla_item"])
            if isinstance(item_name, list | set):
                item_name = self.random.choice(list(item_name))
            item_data = ITEMS[item_name]
            if item_name in removed_item_quantities and removed_item_quantities[item_name] > 0:
                # If item was put in the "remove_items_from_pool" option, replace it with a random filler item
                removed_item_quantities[item_name] -= 1
               # print(f"\triq")
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
                # print(f"\trabbit")
                filler_item_count += 1
                continue
            if "Tear of Light" in item_name:
                if self.options.randomize_tears.value < 0:
                    forced_item = self.create_item(item_name)
                    self.multiworld.get_location(loc_name, self.player).place_locked_item(forced_item)
                    continue
                # print(f"\ttear")
                filler_item_count += 1
                continue
            if "stamp" in loc_data and self.options.randomize_stamps.value == 2:
                forced_item = self.create_item(item_name)
                self.multiworld.get_location(loc_name, self.player).place_locked_item(forced_item)
                # print(f"Locking stamp item {item_name} to {loc_name}")
                continue
            if any([
                item_name in ["Filler Item", "Treasure", "Sword Beam Scroll",
                              "Heart Container", "Tear of Light", "Small Key (ToS)",
                              "Bombs (Progressive)", "Bow (Progressive)", "Shield",
                              "Prize Postcards (10)"],
                item_name.startswith("Stamp"),
                item_name in ITEM_GROUPS["Add Rails to Pool"],
                self.options.randomize_cargo.value == 3 and item_name in ["Cargo: Cuccos", "Cargo: Mega Ice"]
                ]):
                # print(f"\tBig listicle {item_name}")
                filler_item_count += 1
                continue
            if any([
                "Small Key" in item_name and self.options.keysanity == "vanilla",
                loc_name.endswith("Boss Key") and self.options.randomize_boss_keys == "vanilla_abstract",
                "force_vanilla" in loc_data and loc_data["force_vanilla"],
                self.options.randomize_passengers == "vanilla_abstract" and item_name.startswith("Passenger:"),
                self.options.randomize_cargo == "vanilla_abstract" and item_name.startswith("Cargo:")
            ]):
                forced_item = self.create_item(item_name)
                self.multiworld.get_location(loc_name, self.player).place_locked_item(forced_item)
                continue
            if item_data.classification == ItemClassification.filler:  # Regen all filler items for now
                # print(f"\tFiller items {item_name}")
                filler_item_count += 1
                continue

            item_pool_dict[item_name] = item_pool_dict.get(item_name, 0) + 1
            #print(f"Location {loc_name} has {item_name} item")

        # TODO Fill filler count with consistent amounts of items, when filler count is empty it won't add any more items
        # so add progression items first
        add_items = [("Bombs (Progressive)", 3), ("Bow (Progressive)", 3),
                     ("Repair Trading Post Bridge", 1), ("Shield", 2)]
        if self.options.rabbitsanity: add_items += [("Rabbit Net", 1)]
        if self.options.randomize_cargo: add_items += [("Wagon", 1)]
        if self.options.randomize_cargo.value == 3: add_items += [("Cargo: Mega Ice", 3), ("Cargo: Cuccos (5)", 3)]
        # if self.options.shopsanity: add_items += [("Treasure: Regal Ring", 1), ("Treasure: Priceless Stone", 2)]
        if self.options.randomize_stamps: add_items += self.stamp_items
        add_items += [("Small Key (ToS 2)", 2), ("Small Key (ToS 4)", 3), ("Small Key (ToS 5)", 2), ("Small Key (ToS 6)", 3)]
        add_items += self.choose_tos_items()
        add_items += [(i, 1) for i in ITEM_GROUPS["Add Rails to Pool"]]
        if self.options.portal_behavior.value == 2:
            add_items += [(i, 1) for i in ITEM_GROUPS["Portal Unlocks"]]
        add_items += self.choose_tear_items()
        add_items += [i for i in self.rabbit_item_dict.items()]
        add_items += [("Sword Beam Scroll", 1), ("Great Spin Scroll", 1), ("Heart Container", 13)]
        print(f"Add items: ({sum([i for _, i in add_items])}/{filler_item_count})")
        for i, count in add_items:
            # print(f"\t{i}: {count}")
            item_pool_dict, filler_item_count = add_items_from_filler(item_pool_dict, filler_item_count, i, count)

        # Add as many filler items as required
        for _ in range(filler_item_count):
            random_filler_item = self.get_filler_item_name()
            item_pool_dict[random_filler_item] = item_pool_dict.get(random_filler_item, 0) + 1

        return item_pool_dict

    def choose_tos_items(self):
        res = []
        if self.options.tos_section_unlocks in ["progressive"]:
            prog_count = 4
            if self.options.tos_unlock_base_item:
                prog_count = 5
            res += [("Progressive ToS Section", prog_count)]
        elif self.options.tos_unlock_base_item:
            res += [("Tower of Spirits Base", 1)]
        return res

    def choose_rabbit_locations(self):
        if not self.options.rabbitsanity:
            return []
        rabbit_locations = []
        # Figure out rabbit counts for different pools
        max_count = self.options.rabbit_max_location_count.value
        rabbit_counts = [max_count]*4
        if self.options.rabbit_location_count_distribution.value == -1:
            rabbit_counts = [self.random.randint(1, max_count) for _ in range(4)]
        self.rabbit_counts = rabbit_counts

        def pick_random_locs(loc_lists):
            [self.random.shuffle(i) for i in loc_lists]
            return [loc for rl, c in zip(loc_lists, rabbit_counts) for loc in rl[:c]]

        # Figure out pools
        if self.options.rabbitsanity.value in [1, 2, 4]: # Vanilla or unique
            forest_rabbits = list(LOCATION_GROUPS["Unique Grass Rabbits"])
            snow_rabbits = list(LOCATION_GROUPS["Unique Snow Rabbits"])
            mountain_rabbits = list(LOCATION_GROUPS["Unique Mountain Rabbits"])
            sand_rabbits = list(LOCATION_GROUPS["Unique Sand Rabbits"])
            rabbit_locations += pick_random_locs([forest_rabbits, snow_rabbits, mountain_rabbits, sand_rabbits])

        if self.options.rabbitsanity.value in [3, 4]:  # total count
            forest_rabbits = list(LOCATION_GROUPS["Total Grass Rabbits"])
            snow_rabbits = list(LOCATION_GROUPS["Total Snow Rabbits"])
            mountain_rabbits = list(LOCATION_GROUPS["Total Mountain Rabbits"])
            sand_rabbits = list(LOCATION_GROUPS["Total Sand Rabbits"])
            sort_func = lambda loc: f"0{loc.split()[1]}"[-2:]  # wth python
            forest_rabbits.sort(key=sort_func)
            snow_rabbits.sort(key=sort_func)
            mountain_rabbits.sort(key=sort_func)
            sand_rabbits.sort(key=sort_func)
            interval = self.options.rabbit_location_count_distribution.value
            if interval >= 0:
                intervals = [interval]*4 if interval else [self.random.randint(1, 3) for _ in range(3)]
                for i, realm_locs in zip(intervals, [forest_rabbits, snow_rabbits, mountain_rabbits, sand_rabbits]):
                    if i > max_count:
                        rabbit_locations.append(realm_locs[max_count-1])
                    else:
                        rabbit_locations += realm_locs[i-1:max_count:i]
                # print(f"Rabbit Locations: {rabbit_counts} {intervals} {rabbit_locations}")
                return rabbit_locations
            if self.options.rabbitsanity == "both":  # Randomize each pool count separately
                self.rabbit_counts = [self.random.randint(1, max_count), self.random.randint(1, max_count)]
            rabbit_locations += pick_random_locs([forest_rabbits, snow_rabbits, mountain_rabbits, sand_rabbits])

        # print(f"Rabbit Locations: {rabbit_counts} {rabbit_locations}")
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
            # print(f"Filling vanilla rabbits {realm} {max_count}")
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

        realms = rabbit_realms
        rabbit_items = {}
        if self.options.rabbitsanity.value == 1:  # Vanilla
            # print(f"Vanilla rabbits {self.rabbit_counts}")
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
        # print(f"Uniform Packs {pack_sizes}")
        for r, s in zip(realms, pack_sizes):
            item_count = math.ceil(10 / s) + self.options.rabbit_extra_items.value
            rabbit_items |= create_items_from_count_list(r, [s]*item_count)
        return rabbit_items

    def choose_tear_items(self):
        size_index = self.options.tear_size.value
        spirit_weapon = self.options.spirit_weapons.value
        size_str = ["", "Big "][size_index]
        sections = range(1, 6)
        add_items = []
        tear_sections = self.options.tear_sections.value
        count_normal = [3, 1][size_index]

        if tear_sections == 0 and self.options.randomize_tears not in ["no_tears", "vanilla"]:  # unique section
            add_items += [(f"{size_str}Tear of Light (ToS {section})", count_normal) for section in sections]
        elif tear_sections == 1:  # All Sections
            add_items += [(f"{size_str}Tear of Light (All Sections)", count_normal + spirit_weapon)]
        elif tear_sections == 2: # progressive
            count_prog = [15, 5][size_index]
            add_items += [(f"{size_str}Tear of Light (Progressive)", count_prog + spirit_weapon)]

        if not spirit_weapon:
            add_items += [("Sword (Progressive)", 2), ("Bow of Light", 1)]
        else:
            add_items += [("Sword", 1)]

        # print(f"New Tear Items: {add_items}")
        return add_items

    def choose_stamp_items(self):
        if self.options.randomize_stamps.value == 0:
            return
        self.stamp_items = [("Stamp Book", 1)]
        if self.options.randomize_stamps.value in [1, 2, 4]:
            return
        if self.options.stamp_pack_sizes.value == 1:
            self.stamp_items += [(s, 1) for s in ITEM_GROUPS["Stamps"]]
            return

        self.stamp_pack_order = list(range(20))
        self.random.shuffle(self.stamp_pack_order)
        if self.options.stamp_pack_sizes.value > 1:
            item_count = math.ceil(20/self.options.stamp_pack_sizes.value)
            self.stamp_items += [(f"Stamp Pack ({self.options.stamp_pack_sizes.value})", item_count)]
        elif self.options.stamp_pack_sizes.value == -1:
            sizes = []
            while sum(sizes) < 20:
                sizes.append(math.floor(self.random.triangular(1, 6, 1)))
            stamp_value_lookup = {ITEMS[name].value: name for name in ITEM_GROUPS["Stamps"]}
            stamp_dict = {i: 0 for i in range(2, 6)}
            for s in sizes:
                if s == 1:
                    self.stamp_items.append((stamp_value_lookup[self.stamp_pack_order.pop()], 1))
                else:
                    stamp_dict[s] += 1
            self.stamp_items += [(f"Stamp Pack ({size})", count) for size, count in stamp_dict.items() if count > 0]


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

    # Based on the messenger's plando connection by Aaron Wagner
    def connect_plando(self, plando_pairings) -> None:
        def remove_dangling_exit(region: Region) -> None:
            # find the disconnected exit and remove references to it
            for _exit in region.exits:
                if not _exit.connected_region:
                    break
            else:
                raise ValueError(f"Unable to find randomized transition for {region}")

            region.exits.remove(_exit)

        def remove_dangling_entrance(region: Region) -> None:
            # find the disconnected entrance and remove references to it
            for _entrance in region.entrances:
                if not _entrance.parent_region:
                    break
            else:
                raise ValueError(f"Invalid target region for {region}")
            region.entrances.remove(_entrance)

        for entr_name, exit_name in plando_pairings:
            # get the connecting regions
            r1 = ENTRANCES[entr_name]
            reg1 = self.get_region(r1.entrance_region)
            remove_dangling_exit(reg1)

            r2 = ENTRANCES[exit_name]
            reg2 = self.get_region(r2.entrance_region)
            remove_dangling_entrance(reg2)
            # connect the regions
            reg1.connect(reg2)
            if dev_prints:
                print(f"Plando Connecting {r1} => {r2} with regions {reg1} => {reg2}")

            # pretend the user set the plando direction as "both" regardless of what they actually put on coupled
            if True:
                remove_dangling_exit(reg2)
                remove_dangling_entrance(reg1)
                reg2.connect(reg1)
                if dev_prints:
                    print(f"Connecting backwards {r2} => {r1}")

    @staticmethod
    def create_er_target_groups(type_option_lookup):
        directions = [5, 6]
        entr_types = [11 << 3]

        return {5 + (11 << 3): [6 + (11 << 3)],
                6 + (11 << 3): [5 + (11 << 3)]}

    def connect_entrances(self) -> None:
        if self.is_ut:
            disconnect_ids = {int(i) for i in self.ut_pairings.keys()}
            for e in self.valid_entrances:
                if ENTRANCES[e.name].id in disconnect_ids:
                    # print(f"Disconnecting {e.name}")
                    target_name = ENTRANCES[e.name].vanilla_reciprocal.name
                    disconnect_entrance_for_randomization(e, one_way_target_name=target_name)
            if getattr(self.multiworld, "enforce_deferred_connections", "default") == "off":
                print(f"Reconnecting entrances {self.ut_pairings}")
                for i, pairing in self.ut_pairings.items():
                    _exit: "Entrance" = self.get_entrance(entrance_id_to_entrance[int(i)].name)
                    entrance_region: "Region" = self.get_region(entrance_id_to_region[pairing])
                    _exit.connect(entrance_region)
            return

        # Choose entrances to shuffle based on settings
        type_option_lookup = {
            11: self.options.shuffle_tos_sections
        }
        entrances_to_shuffle: list["Entrance"] = []
        for e in self.valid_entrances:
            # print(f"ER: {e.name} {bin(e.randomization_group)} {bin(EntranceGroups.AREA_MASK)} {(e.randomization_group & EntranceGroups.AREA_MASK) >> 3}")
            if type_option_lookup.get((e.randomization_group & EntranceGroups.AREA_MASK) >> 3, False):
                entrances_to_shuffle.append(e)


        # Disconnect entrances to shuffle
        for entrance in entrances_to_shuffle:
            if dev_prints:
                print(f"Disconnecting {entrance.name}")
            target_name = ENTRANCES[entrance.name].vanilla_reciprocal.name
            disconnect_entrance_for_randomization(entrance, one_way_target_name=target_name)

        # Get target groups
        groups = self.create_er_target_groups(type_option_lookup)
        # print(f"Shuffling Entrances {entrances_to_shuffle} with groups {groups}")

        # Entrance Rando
        if self.tower_pairings:
            self.connect_plando(self.tower_pairings)
        self.er_placement_state = randomize_entrances(self, True, groups)
        # print(f"ER Placements: {self.er_placement_state.pairings}")

        # Get lookup for logic stuff. Doesn't work cause logic is cemented earlier
        # self.create_tower_section_lookup()

    def create_tower_section_lookup(self):
        # Get lookup for logic stuff
        tower_pairings = {i: pair for i, pair in self.er_placement_state.pairings if i in ENTRANCE_TO_TOS_ORDER}
        # print(f"Tower Pairings: {tower_pairings}")
        sort_filter = {}
        for pair, entr in tower_pairings.items():
            if entr in EXIT_TO_TOS_SECTION and pair in ENTRANCE_TO_TOS_ORDER:
                sort_filter[EXIT_TO_TOS_SECTION[entr]] = ENTRANCE_TO_TOS_ORDER[pair]
        to_sort = [i for i in sort_filter]
        to_sort.sort(key=lambda i: sort_filter[i])
        self.tower_section_lookup = {section: i + 1 for i, section in enumerate(to_sort)}
        # print(f"{self.tower_section_lookup}")

    def get_pre_fill_items(self):
        return self.pre_fill_items

    def pre_fill(self) -> None:
        self.pre_fill_tos_sections()
        self.pre_fill_dungeon_items()

    def filter_confined_dungeon_items_from_pool(self, items: List[Item]):
        confined_dungeon_items = []

        # Confine small keys and boss key to own dungeon if option is enabled
        if self.options.keysanity in ["in_own_dungeon", "in_own_section"]:
            confined_dungeon_items.extend([item for item in items if item.name.startswith("Small Key")])

        if self.options.randomize_boss_keys in ["in_own_dungeon", "in_own_section"]:
            confined_dungeon_items.extend([item for item in items if item.name in ITEM_GROUPS["Boss Keys"]])

        if self.options.randomize_tears in ["in_own_section", "in_tos"]:
            confined_dungeon_items.extend([item for item in items if item.name in ITEM_GROUPS["Tears of Light"]])

        for item in confined_dungeon_items:
            items.remove(item)
        self.pre_fill_items.extend(confined_dungeon_items)

    def pre_fill_tos_sections(self):
        floor_lookup = {1: 1, 2: 4, 3: 9, 4: 13, 5: 18, 6: 29}
        for section in range(1, 7):
            section_names = [name for name, loc in LOCATIONS_DATA.items()
                             if loc.get("tos_section", 0) == section]
            section_locations = [loc for loc in self.multiworld.get_locations(self.player)
                                 if loc.name in section_names and not loc.locked]

            section_items = []
            if self.options.keysanity == "in_own_section":
                section_items += [item for item in self.pre_fill_items if item.name == f"Small Key (ToS {section})"]
            if self.options.randomize_boss_keys == "in_own_section":
                section_items += [item for item in self.pre_fill_items if item.name == f"Boss Key (ToS {section})"]
            if self.options.randomize_tears == "in_own_section":
                section_items += [item for item in self.pre_fill_items if item.name.endswith(f"Tear of Light (ToS {section})")]

            if len(section_locations) == 0:
                continue
            # print(f"Pre filling section {section}: {section_items}")
            # print(f"\tlocations {section_locations}")
            # Remove from the all_state the items we're about to place
            for item in section_items:
                self.pre_fill_items.remove(item)
            collection_state = self.multiworld.get_all_state(False)
            # Perform a prefill to place confined items inside locations of this dungeon
            self.random.shuffle(section_locations)
            # print(f"Pre filling section {section}: {section_items} to {section_locations}")
            fill_restrictive(self.multiworld, collection_state, section_locations, section_items,
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
            if dung_name == "ToS":
                if self.options.keysanity == "in_own_dungeon":
                    confined_dungeon_items += [item for item in self.pre_fill_items
                                          if item.name.startswith("Small Key (ToS")]
                if self.options.randomize_boss_keys == "in_own_dungeon":
                    confined_dungeon_items += [item for item in self.pre_fill_items
                                          if item.name.startswith("Boss Key (ToS")]
                if self.options.randomize_tears == "in_tos":
                    confined_dungeon_items += [item for item in self.pre_fill_items
                                          if "Tear of Light" in item.name]
            # print(f"pre filling {dung_name}: {confined_dungeon_items}")
            # print(f"\tlocations {dungeon_location_names}")
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
        filler_item_names = list(ITEM_GROUPS["Common Treasures"] |
                             ITEM_GROUPS["Uncommon Treasures"] |
                             ITEM_GROUPS["Refill Items"] |
                             ITEM_GROUPS["Small Rupees"] |
                             ITEM_GROUPS["Potions"]
                             ) + ["Big Green Rupee (100)"]
        rare_filler_items = list( ITEM_GROUPS["Rare Treasures"]) + [
            "Big Red Rupee (200)", "Gold Rupee (300)"]

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
            # print(f"Mapping {mapping} {state.prog_items[self.player][mapping[0]]} for item {item.name}")
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

    def post_fill(self) -> None:
        # get item placement models to send to client
        location_models = {}
        for loc in self.get_locations():
            item = loc.item
            if item is not None and item.game in ["The Legend of Zelda - Spirit Tracks", "Generic"]:
                loc_data = LOCATIONS_DATA.get(loc.name, {})
                if not loc_data or 'stamp' in loc_data or 'no_model' in loc_data or ITEMS[item.name].model is None:
                    continue
                location_models[loc_data['id']] = ITEM_MODEL_LOOKUP[ITEMS[item.name].model].offset
        self.model_lookup = location_models
        print(f"Location Models: {location_models}")

    def fill_slot_data(self) -> dict:
        options = ["goal",
                   "logic", "cannon_logic",
                   "keysanity", "randomize_boss_keys",
                   "randomize_minigames", "minigame_hints",
                   "rabbitsanity", # "rabbit_hints",
                   "randomize_passengers", "randomize_cargo",
                   "exclude_locations",
                   "portal_behavior", "portal_checks",
                   "randomize_tears", "spirit_weapons", "tear_sections",
                   "dark_realm_access", "endgame_scope", "dungeons_required",
                   "starting_train",
                   "randomize_stamps",
                   "tos_section_unlocks", "tos_unlock_base_item", "shuffle_tos_sections",
                   "shopsanity", "shop_hints", "rupee_farming_logic", "excess_random_treasure"]
        slot_data = self.options.as_dict(*options)
        slot_data["active_rabbit_locs"] = [LOCATIONS_DATA[loc]["id"] for loc in self.active_rabbit_locations]
        slot_data["required_dungeons"] = self.required_dungeons
        slot_data["stamp_pack_order"] = self.stamp_pack_order
        slot_data["model_lookup"] = self.model_lookup
        pairings = {}
        if self.er_placement_state:
            for e1, e2 in self.er_placement_state.pairings:
                pairings[ENTRANCES[e1].id] = ENTRANCES[e2].id
        pairings |= self.plando_pairings
        slot_data["er_pairings"] = pairings
        slot_data["tower_section_lookup"] = self.tower_section_lookup
        print(f"ER Pairings: {pairings}")

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
