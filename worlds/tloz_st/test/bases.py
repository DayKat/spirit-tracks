from BaseClasses import LocationProgressType
from test.bases import *


class TestGeneration(WorldTestBase):
    game = "The Legend of Zelda - Spirit Tracks"
    options = {
        "rabbitsanity": "vanilla",
        "rabbit_max_location_count": 1,
        "rabbit_location_count_distribution": "for_each",
        "rabbit_pack_size": 1,
        "rabbit_extra_items": 5
    }
