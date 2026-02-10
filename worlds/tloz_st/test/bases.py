from BaseClasses import LocationProgressType
from test.bases import *


class TestGeneration(WorldTestBase):
    game = "The Legend of Zelda - Spirit Tracks"
    options = {
        "rabbitsanity": "no_rabbits",
        "rabbit_max_location_count": 10,
        "rabbit_location_count_distribution": "on_twos",
        "rabbit_pack_size": "random_mixed",
        "rabbit_extra_items": 5,
        "goal": "defeat_malladus"
    }
