from BaseClasses import LocationProgressType
from test.bases import *


class TestGeneration(WorldTestBase):
    game = "The Legend of Zelda - Spirit Tracks"
    options = {
        "rabbitsanity": "on_total",
        "rabbit_max_location_count": "random",
        "rabbit_location_count_distribution": "random_uniform",
        "rabbit_pack_size": "random",
        "rabbit_extra_items": 1
    }
