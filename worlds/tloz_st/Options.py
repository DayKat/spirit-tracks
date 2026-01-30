from dataclasses import dataclass
from datetime import datetime

from Options import Choice, DeathLink, DefaultOnToggle, PerGameCommonOptions, Range, Toggle, StartInventoryPool, \
    ItemDict, ItemsAccessibility, ItemSet, Visibility, NamedRange, OptionGroup
from worlds.tloz_st.data.Items import ITEMS_DATA

# YAML options

class SpiritTracksGoal(Choice):
    """
    The goal to accomplish in order to complete the seed.
    - ToS Section 1: Finish the 1st section of Tower of Spirits and retrieve the Forest Glyph
    - ToS Section 2: Finish the 2nd section of Tower of Spirits and retrieve the Snow Glyph
    """
    display_name = "Goal"
    option_beat_ToS_section_1 = 0
    option_beat_ToS_section_2 = 1
    option_beat_wooded_temple = 2
    option_beat_blizzard_temple = 3
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
    - in_own_dungeon: Keys can be found in their own dungeon
    - anywhere: Keysanity. Keys can be found anywhere
    """
    display_name = "Key Settings"
    option_vanilla = 0
    option_in_own_dungeon = 1
    option_anywhere = 2
    default = 1


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
    If rabbitsanity is vanilla, this is ignored as vanilla assigns it's own pack sizes.
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

@dataclass
class SpiritTracksOptions(PerGameCommonOptions):
    # Accessibility
    accessibility: ItemsAccessibility

    # Goal
    goal: SpiritTracksGoal

    #dungeons_required: SpiritTracksDungeonsRequired
    #exclude_non_required_dungeons: SpiritTracksExcludeNonRequiredDungeons

    # Logic options
    logic: SpiritTracksLogic
    #phantom_combat_difficulty: SpiritTracksPhantomCombatDifficulty
    #train_requires_forest_glyph: SpiritTracksTrainRequiresForestGlyph

    # Item Randomization
    keysanity: SpiritTracksKeyRandomization
    #randomize_frogs: SpiritTracksFrogRandomization

    # Hint Options
    #dungeon_hints: SpiritTracksDungeonHints
    #shop_hints: SpiritTracksShopHints

    # World Options

    # Rabbit Options
    rabbitsanity: SpiritTracksRabbitsanity
    rabbit_max_location_count: SpiritTracksMaxRabbitLocationCount
    rabbit_location_count_distribution: SpiritTracksRabbitCountDistribution
    rabbit_pack_size: SpiritTracksRabbitPackSize
    rabbit_extra_items: SpiritTracksExtraRabbits
    rabbit_hints: SpiritTracksRabbitHints

    # Generic
    start_inventory_from_pool: StartInventoryPool
    remove_items_from_pool: SpiritTracksRemoveItemsFromPool
    death_link: DeathLink

st_option_groups = [
    OptionGroup("Rabbit Options", [
        SpiritTracksRabbitsanity,
        SpiritTracksMaxRabbitLocationCount,
        SpiritTracksRabbitCountDistribution,
        SpiritTracksRabbitPackSize,
        SpiritTracksExtraRabbits,
        SpiritTracksRabbitHints
    ])
]

