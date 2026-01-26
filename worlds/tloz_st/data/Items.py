from BaseClasses import ItemClassification
from .Addresses import *
from ..Subclasses import STItem
from typing import Any


ITEMS_DATA: dict[str, dict[str, Any]] = {
    #   "No Item": {
    #   'classification': ItemClassification,   # classification category
    #   'address': int,                         # address in memory
    #   'value': int,                           # value to set in memory, if incremental added else bitwise or
    #   'size': int,                            # size in bytes
    #   'set_bit': list[tuple[int, int]],       # for setting additional bits on acquisition
    #   'incremental': bool                     # true for positive, False for negative
    #   'progressive': list[list[int, int]]     # address, value for each progressive stage
    #   'give_ammo': list[int]                  # how much ammo to give for each progressive stage
    #   'ammo_address: int                      # address for ammo
    #    },

    # ======= Regular Items==========

    "Sword (Progressive)": {
        'classification': ItemClassification.progression,
        'progressive': [[addr_items_2, 0x02], [addr_items_2, 0x04]],
        #'set_bit': [(0x1BA644, 1)]  # Means that sending sword if sword breaks gives the base layer
    },
    "Shield": {
        'classification': ItemClassification.progression,
        'address': addr_items_2,
        'value': 0x01
    },
    "Whirlwind": {
        'classification': ItemClassification.progression,
        'address': addr_items_0,
        'value': 0x01,
    },
    "Bombs (Progressive)": {
        'classification': ItemClassification.progression,
        "progressive": [[addr_items_0, 0x10], [0x265331, 0x20]],
        "tags": ["progressive_overwrite"],
        "give_ammo": [10, 20, 30],
        "ammo_address": addr_bomb_count
    },
    "Bow (Progressive)": {
        'classification': ItemClassification.progression,
        "progressive": [[addr_items_0, 0x08], [addr_arrow_capacity, 0x20]],
        "give_ammo": [20, 30, 50],
        "ammo_address": addr_arrow_count,
        "tags": ["progressive_overwrite"]
    },
    "Whip": {
        'classification': ItemClassification.progression,
        'address': addr_items_0,
        'value': 0x04,
    },
    "Boomerang": {
        'classification': ItemClassification.progression,
        'address': addr_items_0,
        'value': 0x02,
    },
    "Sand Wand": {
        'classification': ItemClassification.progression,
        'address': addr_items_0,
        'value': 0x20,
    },
    "Spirit Flute": {
        'classification': ItemClassification.progression,
        'address': addr_items_2,
        'value': 0x80,
    },

    # ======= Misc Items==========

    "Recruit Uniform": {
        'classification': ItemClassification.progression,
        #'address': 0x1BA645,
        #'value': 0x01,
        #'set_bit': [(0x1BA6C8, 1)]
    },
    "Engineer's Clothes": {
        'classification': ItemClassification.filler,
        #'address': 0x1BA645,
        #'value': 0x01,
        #'set_bit': [(0x1BA6C8, 1)]
    },
    "Compass of Light": {
        'classification': ItemClassification.progression,
        'address': addr_rail_restorations,
        'value': 0x40,  # also set adv flag?
    },
    "Royal Engineer's Certificate": {
        'classification': ItemClassification,
        'address': addr_adv_flags_3,
        'value': 0x01,
    },
    "Rabbit Net": {
        'classification': ItemClassification.progression,
        'address': addr_adv_flags_1a,
        'value': 0x40,
    },
    "Stamp Book": {
        'classification': ItemClassification.progression,
        'address': addr_adv_flags_25,
        'value': 0x02,
    },

    # ======= Songs ==========

    "Song of Awakening": {
        'classification': ItemClassification.progression,
        'address': addr_songs,
        'value': 0x01,
    },
    "Song of Healing": {
        'classification': ItemClassification.useful,
        'address': addr_songs,
        'value': 0x02,
    },
    "Song of Birds": {
        'classification': ItemClassification.progression,
        'address': addr_songs,
        'value': 0x04,
    },
    "Song of Light": {
        'classification': ItemClassification.progression,
        'address': addr_songs,
        'value': 0x08,
    },
    "Song of Discovery": {
        'classification': ItemClassification.progression,
        'address': addr_songs,
        'value': 0x10,
    },

    # ============= Spirits and Upgrades =============


    "Heart Container": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'address': addr_heart_count,
        'value': 4,
        "tags": ["incremental"]
    },
    "Sword Beam Swordsman's Scroll": {
        'classification': ItemClassification.useful,
        'address': addr_items_2,
        'value': 0x0010,
    },
    "Great Spin Swordsman's Scroll": {
        'classification': ItemClassification.useful,
        'address': addr_items_2,
        'value': 0x0020,
    },

    # ============= Train Items =============

    "Cannon": {
        'classification': ItemClassification.progression,
        'address': addr_adv_flags_3,
        'value': 0x80
    },
    # "SW Snow Realm Portal": {
    #     'classification': ItemClassification.progression,
    #     'address': 0x265744,
    #     'value': 0x08,
    # },

    # ========== Rail Maps ============

    "Forest Glyph": {
        'classification': ItemClassification.progression,
        'address': addr_adv_flags_1,
        'value': 0x80,
    },
    "Snow Glyph": {
        'classification': ItemClassification.progression,
        'address': addr_adv_flags_2,
        'value': 0x01,
    },
    "Ocean Glyph": {
        'classification': ItemClassification.progression,
        'address': addr_adv_flags_2,
        'value': 0x02,
    },
    "Fire Glyph": {
        'classification': ItemClassification.progression,
        'address': addr_adv_flags_2,
        'value': 0x04,
    },
    "Wooded Temple Tracks":{
        'classification': ItemClassification.progression,
        'address': addr_rail_restorations,
        'value': 0x02,
    },
    "Blizzard Temple Tracks": {
        'classification': ItemClassification.progression,
        'address': addr_rail_restorations,
        'value': 0x04,
    },
    "Snowdrift Station Tracks": {
        'classification': ItemClassification.progression,
        'address': addr_tracks_1,
        'value': 0x04,
    },
    "Slippery Station Tracks": {
        'classification': ItemClassification.progression,
        'address': addr_tracks_1,
        'value': 0x20,
    },
    "Forest Realm Ocean Shortcut Tracks": {
        'classification': ItemClassification.progression,
        'address': addr_tracks_0,
        'value': 0x02,
    },
    "E Mayscore Bridge Tracks": {
        'classification': ItemClassification.progression,
        'address': addr_tracks_0,
        'value': 0x04,
    },
    "Forest Realm SE Portal Tracks": {
        'classification': ItemClassification.progression,
        'address': addr_tracks_0,
        'value': 0x08,
    },
    "W Castle Town Tracks": {
        'classification': ItemClassification.useful,
        'address': addr_tracks_0,
        'value': 0x20,
    },
    "W Forest Realm Tracks": {
        'classification': ItemClassification.progression,
        'address': addr_tracks_0,
        'value': 0x40,
    },
    "Forest Realm SW Cave Tracks": {
        'classification': ItemClassification.progression,
        'address': addr_tracks_0,
        'value': 0x80,
    },
    "W Wooded Temple Tracks": {
        'classification': ItemClassification.useful,
        'address': addr_tracks_1,
        'value': 0x01,
    },
    "N Castle Town Tracks": {
        'classification': ItemClassification.useful,
        'address': addr_tracks_1,
        'value': 0x02,
    },
    "Snow Realm Bridge Tracks": { # has portal to ocean realm
        'classification': ItemClassification.progression,
        'address': addr_tracks_1,
        'value': 0x08,
    },
    "N Icy Spring Tracks": {
        'classification': ItemClassification.progression,
        'address': addr_tracks_1,
        'value': 0x10,
    },

    # ========= Force Gems ==============

    "Forest Source": {
      'classification': ItemClassification.progression,
        "address": addr_adv_flags_0,
        'value': 0x10,
        'set_bit': [[addr_source_rails, 2]]
    },
    "Snow Source": {
      'classification': ItemClassification.progression,
        "address": addr_adv_flags_0,
        'value': 0x20,
        'set_bit': [[addr_source_rails, 4]]
    },
    "Ocean Source": {
      'classification': ItemClassification.progression,
        "address": addr_adv_flags_0,
        'value': 0x40,
        'set_bit': [[addr_source_rails, 8]]
    },
    "Fire Source": {
      'classification': ItemClassification.progression,
        "address": addr_adv_flags_0,
        'value': 0x80,
        'set_bit': [[addr_source_rails, 0x10]]
    },

    # TODO bridge repair 265752 0x10

    # Warp gates require cannon
    "Force Gem 1": {
        'classification': ItemClassification.progression,
        #'address': 0x265716,
        #'value': 0x40
    },

    # ========== Rabbits ============

    "Forest Rabbit": {
        'classification': ItemClassification.progression,
        "tags": ["incremental"],
        'dummy': True,
    },
    "Snow Rabbit": {
        'classification': ItemClassification.progression,
        "tags": ["incremental"],
        'dummy': True,
    },
    # "Water Rabbit": {
    #     'classification': ItemClassification.progression,
    #     'address': 0x262032,
    #     'value': 1,
    #     'incremental': True,
    #     'size': 1
    # },
    # "Fire Rabbit": {
    #     'classification': ItemClassification.progression,
    #     'address': 0x262034,
    #     'value': 1,
    #     'incremental': True,
    #     'size': 1
    # },
    # "Sand Rabbit": {
    #     'classification': ItemClassification.progression,
    #     'address': 0x262035,
    #     'value': 1,
    #     'incremental': True,
    #     'size': 1
    # },

    # ========== Rupees and filler =============

    "Green Rupee (1)": {
        'classification': ItemClassification.filler,
        'address': 0x265328,
        'value': 1,
        "tags": ["incremental"]
    },
    "Blue Rupee (5)": {
        'classification': ItemClassification.filler,
        'address': addr_rupees,
        'value': 5,
        "tags": ["incremental"]
    },
    "Red Rupee (20)": {
        'classification': ItemClassification.filler,
        'address': addr_rupees,
        'value': 20,
        "tags": ["incremental"]
    },
    "Big Green Rupee (100)": {
        'classification': ItemClassification.progression_skip_balancing,
        'address': addr_rupees,
        'value': 100,
        "tags": ["incremental", 'backup_filler']
    },
    "Big Red Rupee (200)": {
        'classification': ItemClassification.progression_skip_balancing,
        'address': addr_rupees,
        'value': 200,
        "tags": ["incremental", 'backup_filler']
    },
    "Gold Rupee (300)": {
        'classification': ItemClassification.progression_skip_balancing,
        'address': addr_rupees,
        'value': 300,
        "tags": ["incremental", 'backup_filler']
    },
    "Pre-Alpha Rupee (5000)": {
        'classification': ItemClassification.progression,
        'address': addr_rupees,
        'value': 5000,
        "tags": ["incremental"]
    },
    "Train Part": {
        'classification': ItemClassification.filler,
        'train_part': True
    },
    "Red Potion": {
        'classification': ItemClassification.filler,
        'address': addr_potion_0, #this is potion slot 1
        'value': 1,
    },
    "Purple Potion": {
        'classification': ItemClassification.filler,
        'address': addr_potion_0, #this is potion slot 1
        'value': 2,
    },
    "Yellow Potion": {
        'classification': ItemClassification.filler,
        'address': addr_potion_0, #this is potion slot 1
        'value': 3,
    },
    "Nothing!": {
        'classification': ItemClassification.filler,
        'dummy': True
    },
    "Tear of Light": {
        'classification': ItemClassification.filler,
        "address": addr_tears_of_light,
        "dummy": True,
        'value': 1,
        "tags": ["incremental"]
    },
    "Refill: Bombs": {
        'classification': ItemClassification.filler,
        "give_ammo": [10, 20, 30],
        "address": addr_bomb_count,
        "refill": "Bombs (Progressive)",
        "tags": ["incremental"]
    },
    "Refill: Arrows": {
        'classification': ItemClassification.filler,
        "give_ammo": [20, 30, 50],
        "address": addr_arrow_count,
        "refill": "Bow (Progressive)",
        "tags": ["incremental"]
    },

    # ========= Treasure ============= TODO collection menu still seems inaccurate to what you should/shouldn't have

    "Treasure": {
        'classification': ItemClassification.filler,
        'dummy': True
    },
    "Treasure: Demon Fossil": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': addr_demon_fossil_count,
    },
    "Treasure: Stalfos Skull": {
        'classification': ItemClassification.filler,
        'address': addr_stalfos_skull_count,
        "tags": ['treasure', 'backup_filler', 'incremental']
    },
    "Treasure: Star Fragment": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': addr_star_fragment_count,
    },
    "Treasure: Bee Larvae": {
        'classification': ItemClassification.filler,
        'address': addr_bee_larvae_count,
        "tags": ['treasure', 'backup_filler', 'incremental']
    },
    "Treasure: Wood Heart": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': addr_wood_heart_count,
    },
    "Treasure: Dark Pearl Loop": {
        'classification': ItemClassification.filler,
        'address': addr_dark_pearl_loop_count,
        "tags": ['treasure', 'backup_filler', 'incremental']
    },
    "Treasure: White Pearl Loop": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': addr_white_pearl_loop_count,
    },
    "Treasure: Ruto Crown": {
        'classification': ItemClassification.filler,
        'address': addr_ruto_crown_count,
        "tags": ['treasure', 'backup_filler', 'incremental']
    },
    "Treasure: Dragon Scale": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': addr_dragon_scale_count,
    },
    "Treasure: Pirate's Necklace": {
        'classification': ItemClassification.filler,
        'address': addr_pirates_necklace_count,
        "tags": ['treasure', 'backup_filler', 'incremental']
    },
    "Treasure: Palace Dish": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': addr_palace_dish_count,
    },
    "Treasure: Goron Amber": {
        'classification': ItemClassification.filler,
        'address': addr_goron_amber_count,
        "tags": ['treasure', 'backup_filler', 'incremental']
    },
    "Treasure: Mystic Jade": {
        'classification': ItemClassification.filler,
        'address': addr_mystic_jade_count,
        "tags": ['treasure', 'backup_filler', 'incremental']
    },
    "Treasure: Ancient Coin": {
        'classification': ItemClassification.filler,
        'address': addr_ancient_coin_count,
        "tags": ['treasure', 'backup_filler', 'incremental']
    },
    "Treasure: Priceless Stone": {
        'classification': ItemClassification.filler,
        'address': addr_priceless_stone_count,
        "tags": ['treasure', 'backup_filler', 'incremental']
    },
    "Treasure: Regal Ring": {
        'classification': ItemClassification.filler,
        'address': addr_regal_ring_count,
        "tags": ['treasure', 'backup_filler', 'incremental']
    },

    # =========== Keys ============

     "Small Key (Tunnel to ToS)": {
         'classification': ItemClassification.progression,
         'address': 0x26532F,
         'dungeon': 0x18,
         'incremental': True
     },
    "Small Key (Wooded Temple)": {
        'classification': ItemClassification.progression,
        'address': 0x26532F,
        'dungeon': 0x19,
        'incremental': True
     },
    "Boss Key (Wooded Temple)": {
         'classification': ItemClassification.progression,
         'dungeon': 0x19,
         'incremental': False
     },
    "Small Key (ToS)": {
        'classification': ItemClassification.progression,
        'address': 0x26532F,
        'dungeon': 0x13,
        'incremental': True
    },
    "Small Key (Blizzard Temple)": {
        'classification': ItemClassification.progression,
        'address': 0x26532F,
        'dungeon': 0x1A,
        'incremental': True
    },
    "Boss Key (Blizzard Temple)": {
        'classification': ItemClassification.progression,
        'dungeon': 0x1A
    },
    # "Regal Necklace": {
    #     'classification': ItemClassification.progression,
    #     'address': 0x1B5582,
    #     'value': 0x08
    # },

    # Trade Quest and misc

    # Warp Gates

    # Trains
    "Train: Bright Train": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'train': 1
    },
    "Train: Iron Train": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'train': 2
    },
    "Train: Stone Train": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'train': 3
    },
    "Train: Vintage Train": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'train': 4
    },
    "Train: Demon Train": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'train': 5
    },
    "Train: Tropical Train": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'train': 6
    },
    "Train: Dignified Train": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'train': 7
    },
    "Train: Golden Train": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'train': 8
    },

    "_UT_Glitched_Logic": {  # Shows yellow logic in UT
        "classification": ItemClassification.progression,
        "dummy": True,
        "id": 189,
    },
}

ITEMS: dict[str, "STItem"] = {}

# IDs need to be stabilized at some point, not today
for i, k in enumerate(ITEMS_DATA.items()):
    item_name, item_data = k
    item_data["id"] = i+1
    ITEMS[item_name] = STItem(item_name, item_data, ITEMS)

