from BaseClasses import LocationProgressType
from test.bases import *


class TestGeneration(WorldTestBase):
    game = "The Legend of Zelda - Spirit Tracks"
    options = {
        "rabbitsanity": "both",
        "rabbit_max_location_count": 10,
        # "rabbit_location_count_distribution": "random_mixed",
        "rabbit_pack_size": "random_mixed",
        "rabbit_extra_items": 0,
        "goal": "defeat_malladus",
        "dark_realm_access": "dungeons",
        "dungeons_required": 5,
        "tos_dungeon_options": "final_section",

        "randomize_tears": "in_tos",
        "tear_size": "small",
        "tear_sections": "progressive",
        "spirit_weapons": "items",

        "keysanity": "in_own_section",
        "shuffle_tos_sections": "shuffle",
        # "plando_dungeon_pool": {"ToS 6", "ToS 4", "tos 1", "Blizzard Temple"}

        "shopsanity": {"all"},
        "rupee_farming_logic": "unlimited_farming",
        "excess_random_treasure": "nothing",
        "logic": "normal",
        "randomize_passengers": "randomize",
        "randomize_cargo": "randomize",
    }