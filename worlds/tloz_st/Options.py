from dataclasses import dataclass
from datetime import datetime

from Options import Choice, DeathLink, DefaultOnToggle, PerGameCommonOptions, Range, Toggle, StartInventoryPool, \
    ItemDict, ItemsAccessibility, ItemSet, Visibility, NamedRange, OptionGroup, OptionSet
from worlds.tloz_st.data.Items import ITEMS_DATA
from .data.Constants import DUNGEON_TO_BOSS_ITEM_LOCATION

# YAML options

class SpiritTracksGoal(Choice):
    """
    The goal to accomplish in order to complete the seed.
    - defeat_malladus: enter the dark realm and defeat the demon king.
    - ToS Section 1: Finish the 1st section of Tower of Spirits and retrieve the Forest Glyph
    - ToS Section 2: Finish the 2nd section of Tower of Spirits and retrieve the Snow Glyph
    """
    display_name = "Goal"
    option_defeat_malladus = -1
    option_beat_tos_section_1 = 0
    option_beat_tos_section_2 = 1
    option_beat_wooded_temple = 2
    option_beat_blizzard_temple = 3
    default = -1

class SpiritTracksDarkRealmUnlock(Choice):
    """
    What unlocks the dark realm?
    - compass_of_light: only the compass of light is required. malladus also requires a sword, bow of light and spirit pipes.
    - dungeons: find the compass of light and finish a specified number of dungeons to gain access to the dark realm.
    - shattered_compass: triforce hunt! find a specified number of compass shards to unlock the dark realm. Not implemented!
    """
    display_name = "Dark Realm Unlock"
    option_compass_of_light = 0
    option_dungeons = 1
    # option_shattered_compass = 2
    default = 1

class SpiritTracksDungeonCount(Range):
    """
    How many dungeons are required to unlock the dark realm?
    Will not go higher than the number of valid locations in dungeon pool
    """
    range_start = 1
    range_end = 8
    default = 2

class SpiritTracksTowerOfSpiritsDungeonOptions(Choice):
    """
    How does tower of spirits count towards the dungeon pool?
    - not_in_dungeon_pool: tower of spirits does not count as a dungeon
    - final_section: the last implemented section of ToS gets added to the dungeon pool. Currently B7.
    - all_sections: completing each implemented section of ToS gets added to the dungeon pool. Currently, that is 2.
    """
    option_not_in_dungeon_pool = 0
    option_final_section = 1
    option_all_sections = 2

class SpiritTracksDungeonPoolPlando(OptionSet):
    """
    Choose what dungeons appear in the required dungeon pool.
    Leave blank to ignore.
    Valid options are: 'Wooded Temple', 'Blizzard Temple', 'Marine Temple', 'ToS 1'...'ToS 6'
    Overrides tos_dungeon_options.
    """
    display_name = "Plando Dungeon Pool"
    default = set()
    valid_keys = [k.lower() for k in DUNGEON_TO_BOSS_ITEM_LOCATION] + list(DUNGEON_TO_BOSS_ITEM_LOCATION.keys())


class SpiritTracksEndgameScope(Choice):
    """
    How much of the dark realm do you get to play?
    - full_dark_realm: everything!
    - skip_dark_trains: skip the first phase with the dark trains
    - skip_demon_train: only fight cole and malladus, skipping the demon train fight
    - malladus_only: only fight the final boss
    - malladus_p2: skip the boulder phase and the spirit duet, and go straight to the final phase
    """
    display_name = "Endgame Scope"
    option_full_dark_realm = 0
    option_skip_dark_trains = 1
    option_skip_demon_train = 2
    option_malladus_only = 3
    option_malladus_p2 = 4
    default = 0

class SpiritTracksRequireSpecificDungeons(Toggle):
    """
    Specific dungeons are required to enter the dark realm.
    """
    display_name = "Require Specific Dungeons"
    default = 1

class SpiritTracksRequiredDungeonHints(Toggle):
    """
    Get hints for what dungeons are required.
    """
    display_name = "Dungeon Hints"
    default = 1

class SpiritTracksRemoveItemsFromPool(ItemDict):
    """
    Removes specified amount of given items from the item pool, replacing them with random filler items.
    This option has significant chances to break generation if used carelessly, so test your preset several times
    before using it on long generations. Use at your own risk!
    """
    display_name = "remove_items_from_pool"
    verify_item_name = False


class SpiritTracksLogic(Choice):
    """
    Logic options:
    - Normal: Glitches not in logic.
    - Hard: Includes some cool uses of pots aren't hard, but unconventional
    - Glitched: Clever use of items in logic and glitches
    Be careful, using glitches on normal logic can cause key-related softlocks

    Please let me (@DayKat) know if you know of any glitches or non-normal logic!
    """
    display_name = "logic"
    option_normal = 0
    option_hard = 1
    option_glitched = 2
    default = 0


class SpiritTracksKeyRandomization(Choice):
    """
    Small Key Logic options:
    - vanilla: Keys are not randomized
    - in_own_section: Keys can be found in their own dungeon or tower of spirits section
    - in_own_dungeon: Keys can be found in their own dungeon
    - anywhere: Keysanity. Keys can be found anywhere
    """
    display_name = "Key Settings"
    option_vanilla = 0
    option_in_own_section = 3
    option_in_own_dungeon = 1
    option_anywhere = 2
    default = 3


class SpiritTracksRabbitsanity(Choice):
    """
    Rabbits received are separated into realms, while each rabbit catch is a check based on options.
    Also includes Bunnio's rewards for 5 total rabbits, 10 of each rabbit type and 50 total rabbits. Might manually add locations for 5 of each rabbit type hmm...
    - no_rabbits: rabbits are not randomized
    - vanilla: rabbit locations always give rabbit items of their rabbit type. They still count as locations in archipelago for hint cost purposes.
    - unique_checks: each rabbit in the overworld is a unique location.
    - on_total: the total number of rabbits caught of each type gives a check, ex. "Catch 3 Snow Rabbits".
    - both: get locations both on specific rabbits and total rabbits.
    """
    display_name = "Rabbitsanity"
    default = 0
    option_no_rabbits = 0
    option_vanilla = 1
    option_unique_checks = 2
    option_on_total = 3
    option_both = 4

class SpiritTracksMaxRabbitLocationCount(Range):
    """
    The maximum number of rabbit locations for each type if rabbitsanity is enabled.
    Also affects rabbit_location_count_distribution.
    If rabbitsanity option is unique_checks or vanilla, it will pick this many unique locations of each type at random.
    If rabbitsanity is vanilla, rabbit pack size gets assigned automatically to make everything work.
    """
    display_name = "Rabbitsanity Max Location Count"
    range_start = 1
    range_end = 10
    default = 10

class SpiritTracksRabbitCountDistribution(Choice):
    """
    How to distribute rabbit count with the on_total rabbitsanity option, for a maximum defined in rabbit_max_location_count.
    - for_each: creates one location per rabbit.
    - on_twos: creates a location for every 2 rabbits.
    - on_threes: creates a location for every 3 rabbits.
    - random_uniform: will roll an interval between 1 and 3 for each rabbit type
    - random_mixed: will first roll how many locations to create for each rabbit type, from 1 to rabbit_max_location_count, and then randomly pick from available rabbit locations.
    If rabbitsanity is vanilla or unique_checks, it defaults to for_each, but if combined with random_mixed it will randomize unique location count between 1 and rabbit_max_location_count for each rabbit type individually.
    """
    display_name = "Rabbitsanity Location Count Distribution"
    option_for_each = 1
    option_on_twos = 2
    option_on_threes = 3
    option_random_uniform = 0
    option_random_mixed = -1
    default = 1

class SpiritTracksRabbitHints(Toggle):
    """
    Get hints for Bunnio's locations on entering rabbit haven.
    """
    default = 0

class SpiritTracksRabbitPackSize(NamedRange):
    """
    Number of rabbits received per rabbit item for each rabbit type with rabbitsanity.
    Setting it to 0 or random_uniform will randomize between 1 and 5 for each rabbit type.
    Setting it to -1 or random_mixed will keep rolling random pack size items for each rabbit type until you have enough. It rolls a discrete triangular distribution between 1 and 5 with mode 2.
    If rabbitsanity is vanilla, this is ignored as vanilla assigns its own pack sizes.
    """
    display_name = "Rabbit Pack Size"
    range_end = 5
    range_start = 1
    option_random_uniform = 0
    option_random_mixed = -1
    default = 1
    special_range_names = {
        "random_uniform": 0,
        "random_mixed": -1
    }

class SpiritTracksExtraRabbits(Range):
    """
    How many extra rabbit items to create for each rabbit type.
    Is affected by rabbit_pack_size
    If rabbitsanity is vanilla, this will add extra rabbit items to the normal item pool.
    """
    default = 0
    range_start = 0
    range_end = 5

class SpiritTracksRandomizePortals(Choice):
    """
    How to handle the train portals.
    - always_open: You can always take the portals, as long as you have the tracks on both sides
    - open_one_way: You can always take the portals, but you have to unlock them from the side with the gem first
    - open_with_items: creates an item for each portal pair, that is required to use each portal.
    """
    display_name = "Portal Behavior"
    option_open_one_way = 0
    option_always_open = 1
    option_open_with_items = 2
    default = 0

class SpiritTracksPortalLocations(Toggle):
    """
    Creates locations on shooting the gem on each portal.
    Also works with portals not yet implemented
    """
    display_name = "Portal Checks"
    default = 0

class SpiritTracksStartWithTrain(Toggle):
    """
    Starts you with forest glyph and cannon, giving you train access from the start.
    On by default to give people more checks in the beginning
    """
    display_name = "Start With Train"
    default = 1

class SpiritTracksRandomizeTears(Choice):
    """
    Randomize Tears of Light
    - vanilla: tears of light are not randomized
    - vanilla_items: tears of light are vanilla, but you don't need to collect them more than once and they count as archipelago locations for hint costs.
    - in_own_section: tears of light are randomized in their own tower sections. progressive tears count towards all sections
    - in_tos: tears of light are randomized anywhere in Tower of Spirits
    - anywhere: tears of light are randomized anywhere
    - no_tears: you need to find either two swords or bow of light + bow to possess phantoms, tears are still locations.
    """
    display_name = "Randomize Tears of Light"
    option_vanilla = -1
    option_vanilla_items = -2
    option_in_own_section = 1
    option_in_tos = 2
    option_anywhere = 3
    option_no_tears = 0
    default = -1

class SpiritTracksTearSize(Choice):
    """
    Tears of light size
    - small: you need 3 tears for each tower section
    - large: you need one big tear per section
    """
    display_name = "Tears of Light Size"
    option_small = 0
    option_large = 1
    default = 0

class SpiritTracksTearGroup(Choice):
    """
    tears_of_light_grouping:
    - unique_sections: tears of light only work in one section
    - all_sections: tears fill each section from bottom to top, totalling 15 small items or 5 big ones.
    - progressive_spirit_items: tears fill each section from bottom to top. Works with shuffle_tos_section.
    """
    display_name = "Tears of Light Sectionality"
    option_unique_sections = 0
    option_all_sections = 1
    option_progressive = 2

class SpiritTracksSpiritItems(Choice):
    """
    Lokomo Sword and Bow of Light can be combined with certain tear of light groupings
    - items: Lokomo Sword is the second progressive sword; and Bow of Light is its own item, but requires a progressive bow to use.
    - final_tear: if tear_group is all_sections or progressive, the final tear item will unlock both the Lokomo Sword and the Bow of Light.
    """
    display_name = "Tears of Light Progressiveness"
    option_items = 0
    option_final_tear = 1

class SpiritTracksStartingTrain(Choice):
    """
    What train to start with. Train parts will be randomized later.
    Different trains have different health, but i want this to more be a fun cosmetic thing.
    - all_parts: start with all parts, and customize freely in Alfonzo's Workshop on outset.
    - random_train: picks 1 random train to start with
    """
    display_name = "Starting Train"
    option_all_parts = -1
    option_random_train = -2
    option_spirit_train = 0
    option_wooden_train = 1
    option_refined_train = 2
    option_demon_train = 3
    option_stagecoach = 4
    option_dragon_train = 5
    option_sweet_train = 6
    option_golden_train = 7
    default = 0

class SpiritTracksRandomizeMinigames(Choice):
    """
    Randomize Minigames.
    Includes Mayscore Whip game, Take 'em All On, Hyrule Castle Sword Training, Slippery Station and Restoration Duets.
    - no_minigames: minigames are not randomized
    - easy: the easiest difficulty of each minigame is randomized
    - hardest_reasonable: only the hardest difficulty of each minigame is randomized, excluding Take 'em all On 3
    - all_reasonable: all minigame rewards are randomized, excluding Take 'em all On 3
    - everything: all minigame rewards are randomized, including Take 'em all On 3
    """
    display_name = "Randomize Minigames"
    option_no_minigames = 0
    option_easy = 1
    option_hardest_reasonable = 2
    option_all_reasonable = 3
    option_everything = 4

    default = 1

class SpiritTracksMinigameHints(Toggle):
    """
    Hint for minigames
    """
    display_name = "Minigame Hints"
    default = 0

class SpiritTracksToSSectionUnlocks(Choice):
    """
    What unlocks tower of spirits sections?
    open: all sections are open from the start
    sources: each source unlocks a new section
    progressive: adds "Progressive Tower Section" items, that unlock sections one at a time. ToS 1 is always available.
    """
    display_name = "ToS Section Unlocks"
    option_open = 0
    option_sources = 1
    option_progressive = 2
    default = 1

class SpiritTracksToSBase(Toggle):
    """
    If True, Prevents Tower of Spirit access until you have the "Tower of Spirits Base" item
    Instead creates an additional progressive tower section item if you play with progressive tower sections.
    """
    display_name = "ToS Unlock Base Item"
    default = 0

class SpiritTracksShuffleToSSections(Choice):
    """
    Shuffle Tower of Spirits Sections.
    Also includes the summit as its own section.
    Progressive tears will respect the new ordering.
    """
    display_name = "Shuffle ToS Sections"
    option_no_shuffle = 0
    option_shuffle = 1

class SpiritTracksShopsanity(Choice):
    """
    Randomize Shops.
    - no_shops: don't randomize shops. Unique items give nothing.
    - major_items: only unique items like bomb bags or heart containers are locations
    - treasures: only treasures from shops are locations
    - all_above: all possible shop items are locations
    """
    display_name = "Shopsanity"
    option_no_shops = 0
    option_major_items = 1
    option_treasures = 2
    option_all_above = 3
    default = 0

class SpiritTracksShopHints(Toggle):
    """
    Know what you're buying before you buy
    """
    display_name = "Shop Hints"
    default = 1

class SpiritTracksRupeeFarming(Choice):
    """
    What is required for rupee farming?
    - no_farming: All rupees are accounted for in the item pool.
    - unlimited_farming: Once you have access to Linebeck, or rupees from excess treasures, you are logically expected to farm for rupees.
    - capped_farming: The amount of rupees you're expected to farm depends on how many farming hotspots you have in logic.
    """
    display_name = "Rupee Farming Logic"
    option_no_farming = 0
    option_unlimited_farming = 1
    # option_capped_farming = 2
    default = 0

class SpiritTracksExcessTreasures(Choice):
    """
    There are random treasures everywhere, in pots, leaves, from minigames, shops and prize postcards.
    What happens when you get them?
    - nothing: random treasures give you nothing.
    - vanilla: You get what you get
    - convert_to_rupees: Instantly converts to Linebeck's sell price.
    """
    display_name = "Excess Random Treasure"
    option_nothing = 0
    option_vanilla = 1
    option_convert_to_rupees = 2
    default = 1

@dataclass
class SpiritTracksOptions(PerGameCommonOptions):
    # Accessibility
    accessibility: ItemsAccessibility

    # Goal options
    goal: SpiritTracksGoal
    dark_realm_access: SpiritTracksDarkRealmUnlock
    endgame_scope: SpiritTracksEndgameScope
    dungeons_required: SpiritTracksDungeonCount
    tos_dungeon_options: SpiritTracksTowerOfSpiritsDungeonOptions
    plando_dungeon_pool: SpiritTracksDungeonPoolPlando
    require_specific_dungeons: SpiritTracksRequireSpecificDungeons
    dungeon_hints: SpiritTracksRequiredDungeonHints

    # Logic options
    logic: SpiritTracksLogic
    #train_requires_forest_glyph: SpiritTracksTrainRequiresForestGlyph

    # Item Randomization
    keysanity: SpiritTracksKeyRandomization
    randomize_minigames: SpiritTracksRandomizeMinigames
    minigame_hints: SpiritTracksMinigameHints
    start_with_train: SpiritTracksStartWithTrain

    tos_section_unlocks: SpiritTracksToSSectionUnlocks
    tos_unlock_base_item: SpiritTracksToSBase
    shuffle_tos_sections: SpiritTracksShuffleToSSections

    randomize_tears: SpiritTracksRandomizeTears
    tear_size: SpiritTracksTearSize
    tear_sections: SpiritTracksTearGroup
    spirit_weapons: SpiritTracksSpiritItems

    # Portals
    portal_behavior: SpiritTracksRandomizePortals
    portal_checks: SpiritTracksPortalLocations

    # Hint Options
    #dungeon_hints: SpiritTracksDungeonHints
    #shop_hints: SpiritTracksShopHints

    # World Options

    # Shops, treasure and rupees
    shopsanity: SpiritTracksShopsanity
    shop_hints: SpiritTracksShopHints
    rupee_farming_logic: SpiritTracksRupeeFarming
    excess_random_treasure: SpiritTracksExcessTreasures

    # Rabbit Options
    rabbitsanity: SpiritTracksRabbitsanity
    rabbit_max_location_count: SpiritTracksMaxRabbitLocationCount
    rabbit_location_count_distribution: SpiritTracksRabbitCountDistribution
    rabbit_pack_size: SpiritTracksRabbitPackSize
    rabbit_extra_items: SpiritTracksExtraRabbits
    # rabbit_hints: SpiritTracksRabbitHints

    # Cosmetic
    starting_train: SpiritTracksStartingTrain

    # Generic
    start_inventory_from_pool: StartInventoryPool
    remove_items_from_pool: SpiritTracksRemoveItemsFromPool
    # death_link: DeathLink

st_option_groups = [
    OptionGroup("Goal Options", [
        SpiritTracksGoal,
        SpiritTracksDarkRealmUnlock,
        SpiritTracksDungeonCount,
        SpiritTracksRequireSpecificDungeons,
        SpiritTracksEndgameScope,
        SpiritTracksTowerOfSpiritsDungeonOptions,
        SpiritTracksDungeonPoolPlando,
        SpiritTracksRequiredDungeonHints,
    ]),
    OptionGroup("Misc Options", [
        SpiritTracksLogic,
        SpiritTracksKeyRandomization,
        SpiritTracksRandomizeMinigames,
        SpiritTracksMinigameHints,
        SpiritTracksRandomizePortals,
        SpiritTracksPortalLocations,
        SpiritTracksStartWithTrain,
    ]),
    OptionGroup("ToS Options", [
        SpiritTracksToSSectionUnlocks,
        SpiritTracksToSBase,
        SpiritTracksShuffleToSSections,
        SpiritTracksRandomizeTears,
        SpiritTracksTearSize,
        SpiritTracksTearGroup,
        SpiritTracksSpiritItems
    ]),
    OptionGroup("Shops, Treasure and Rupees", [
        SpiritTracksShopsanity,
        SpiritTracksShopHints,
        SpiritTracksRupeeFarming,
        SpiritTracksExcessTreasures
    ]),
    OptionGroup("Rabbit Options", [
        SpiritTracksRabbitsanity,
        SpiritTracksMaxRabbitLocationCount,
        SpiritTracksRabbitCountDistribution,
        SpiritTracksRabbitPackSize,
        SpiritTracksExtraRabbits,
        SpiritTracksRabbitHints
    ]),
    OptionGroup("Cosmetic Options", [
        SpiritTracksStartingTrain
    ])

]

