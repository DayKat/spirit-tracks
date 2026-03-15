from BaseClasses import LocationProgressType
from test.bases import *


class TestGeneration(WorldTestBase):
    game = "The Legend of Zelda - Spirit Tracks"
    options = {
        "rabbitsanity": "unique_checks",
        "rabbit_max_location_count": 10,
        # "rabbit_location_count_distribution": "random_mixed",
        "rabbit_pack_size": "random_mixed",
        "rabbit_extra_items": 2,
        "goal": "defeat_malladus",
        "dark_realm_access": "dungeons",

        "dungeons_required": 11,
        "tos_dungeon_options": "all_sections",

        "randomize_tears": "in_tos",
        "tear_size": "large",
        "tear_sections": "progressive",
        "spirit_weapons": "final_tear",

        "keysanity": "in_own_section",
        "shuffle_tos_sections": "shuffle",
        # "plando_dungeon_pool": {"ToS 6", "ToS 4", "tos 1", "Desert Temple"},

        "shopsanity": {"all"},
        "rupee_farming_logic": "no_farming",
        "excess_random_treasure": "nothing",
        "logic": "normal",
        "randomize_passengers": "no_passengers",
        "randomize_cargo": "no_cargo",
        "randomize_stamps": "vanilla",
        "stamp_pack_sizes": 1,
        "randomize_minigames": "everything",
        "exclude_dungeons": "exclude",
        "exclude_sections": "exclude",
        "track_pool": "mixed_small",
        "start_with_train": True,
        "cannon_logic": "open_train",
        "portal_behavior": "always_open"
    }