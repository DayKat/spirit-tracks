from BaseClasses import LocationProgressType
from test.bases import *


class TestGeneration(WorldTestBase):
    game = "The Legend of Zelda - Spirit Tracks"
    options = {
        "rabbitsanity": "both",
        "rabbit_max_location_count": 10,
        "rabbit_location_count_distribution": "random_mixed",
        "rabbit_pack_size": "random_mixed",
        "rabbit_extra_items": 0,
        "goal": "defeat_malladus",
        "dark_realm_access": "dungeons",
        "dungeons_required": 4,
        "tos_dungeon_options": "all_sections"
    }
