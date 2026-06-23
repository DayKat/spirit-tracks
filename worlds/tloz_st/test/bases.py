from BaseClasses import LocationProgressType
from test.bases import *


class TestGeneration(WorldTestBase):
    game = "Spirit Tracks"
    options = {
        "rabbitsanity": "both",
        "rabbit_max_location_count": 1,
        "rabbit_location_count_distribution": "for_each",
        "rabbit_pack_size": 3,
        "rabbit_extra_items": 0,
        "goal": "beat_tos_section_6",
        "dark_realm_access": "both",

        "dungeons_required": 12,
        "tos_dungeon_options": "all_sections",

        "randomize_tears": "in_own_section",
        "tear_size": "large",
        "tear_sections": "unique_sections",
        "spirit_weapons": "final_tear",
        "shuffle_tos_sections": "no_shuffle",
        "exclude_sections": "remove",
        "plando_dungeon_pool": {"ToS 1", "ToS 3", "ToS 5"},

        "keysanity": "vanilla",
        "randomize_boss_keys": "anywhere",
        "keyrings": "all",


        "shopsanity": {"all"},
        "rupee_farming_logic": "no_farming",
        "excess_random_treasure": "nothing",
        "logic": "normal",
        "randomize_passengers": "randomize",
        "randomize_cargo": "randomize",
        "randomize_stamps": "randomize",
        "stamp_pack_sizes": 1,
        "randomize_minigames": "hard",
        "exclude_dungeons": "remove",

        "track_pool": "mixed_small",
        "start_with_train": True,
        "cannon_logic": "open_train",
        "portal_behavior": "always_open",
        "start_inventory_from_pool": {
            "Big Tear of Light (ToS 1)": 1
        }

    }