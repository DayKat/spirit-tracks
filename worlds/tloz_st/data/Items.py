from BaseClasses import ItemClassification

ITEMS_DATA = {
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
        'progressive': [[0x265322, 0x02], [0x265322, 0x04]],
        #'set_bit': [(0x1BA644, 1)]  # Means that sending sword if sword breaks gives the base layer
    },
    "Shield": {
        'classification': ItemClassification.useful,
        'address': 0x265322,
        'value': 0x01
    },
    "Whirlwind": {
        'classification': ItemClassification.progression,
        'address': 0x265320,
        'value': 0x01,
    },
    "Bombs (Progressive)": {
        'classification': ItemClassification.progression,
        "progressive": [[0x265320, 0x10], [0x265331, 0x20]],
        "progressive_overwrite": True,
        "give_ammo": [10, 20, 30],
        "ammo_address": 0x265333
    },
    "Bow (Progressive)": {
        'classification': ItemClassification.progression,
        "progressive": [[0x265320, 0x08], [0x265330, 0x20]],
        "progressive_overwrite": True,
        "give_ammo": [20, 30, 50],
        "ammo_address": 0x265332,
    },
    "Whip": {
        'classification': ItemClassification.progression,
        'address': 0x265320,
        'value': 0x04,
    },
    "Boomerang": {
        'classification': ItemClassification.progression,
        'address': 0x265320,
        'value': 0x02,
    },
    "Sand Wand": {
        'classification': ItemClassification.progression,
        'address': 0x265320,
        'value': 0x20,
    },
    "Spirit Flute": {
        'classification': ItemClassification.progression,
        'address': 0x265322,
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
        'address': 0x265739,
        'value': 0x20,
    },
    "Royal Engineer's Certificate": {
        'classification': ItemClassification,
        'address': 0x265717,
        'value': 0x01,
    },
    "Rabbit Net": { #TODO find net address
        'classification': ItemClassification.progression,
        'address': 0x26572E,
        'value': 0x40,
    },
    "Stamp Book": {
        'classification': ItemClassification.progression,
        'address': 0x265739,
        'value': 0x02,
    },

    # ======= Songs ==========

    "Song of Awakening": {
        'classification': ItemClassification.progression,
        'address': 0x268FB0,
        'value': 0x01,
    },
    "Song of Healing": {
        'classification': ItemClassification.useful,
        'address': 0x268FB0,
        'value': 0x02,
    },
    "Song of Birds": {
        'classification': ItemClassification.progression,
        'address': 0x268FB0,
        'value': 0x04,
    },
    "Song of Light": {
        'classification': ItemClassification.progression,
        'address': 0x268FB0,
        'value': 0x08,
    },
    "Song of Discovery": {
        'classification': ItemClassification.progression,
        'address': 0x268FB0,
        'value': 0x10,
    },

    # ============= Spirits and Upgrades =============


    "Heart Container": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'address': 0x2651BD,
        'value': 4,
        'incremental': True,
        'size': 2
    },
    "Sword Beam Swordsman's Scroll": {
        'classification': ItemClassification.useful,
        'address': 0x265322,
        'value': 0x0010,
    },
    "Great Spin Swordsman's Scroll": {
        'classification': ItemClassification.useful,
        'address': 0x265322,
        'value': 0x0020,
    },

    # ============= Train Items =============

    "Cannon": {
        'classification': ItemClassification.progression,
        'address': 0x265717,
        'value': 0x80
    },
    "SW Snow Realm Portal": {
        'classification': ItemClassification.progression,
        'address': 0x265744,
        'value': 0x08,
    },

    # ========== Rail Maps ============

    "Forest Glyph": {
        'classification': ItemClassification.progression,
        'address': 0x265715,
        'value': 0x80,
    },
    "Snow Glyph": {
        'classification': ItemClassification.progression,
        'address': 0x265716,
        'value': 0x01,
    },
    "Ocean Glyph": {
        'classification': ItemClassification.progression,
        'address': 0x265716,
        'value': 0x02,
    },
    "Fire Glyph": {
        'classification': ItemClassification.progression,
        'address': 0x265716,
        'value': 0x04,
    },
    "Wooded Temple Tracks":{
        'classification': ItemClassification.progression,
        'address': 0x2653B0,
        'value': 0x02,
    },
    "Blizzard Temple Tracks": {
        'classification': ItemClassification.progression,
        'address': 0x2653B0,
        'value': 0x04,
    },
    "Snowdrift Station Tracks": {
        'classification': ItemClassification.progression,
        'address': 0x2653B5,
        'value': 0x04,
    },
    "Slippery Station Tracks": {
        'classification': ItemClassification.progression,
        'address': 0x2653B5,
        'value': 0x20,
    },
    "W Wooded Temple Tracks": {
        'classification': ItemClassification.useful,
        'address': 0x2653B5,
        'value': 0x01,
    },
    # "W Castle Town Tracks": {
    #     'classification': ItemClassification.progression,
    #     'address': 0x2653B5,
    #     'value': 0x02,
    # },

    # ========= Force Gems ==============

    "Forest Source": {
      'classification': ItemClassification.progression,
        "address": 0x265714,
        'value': 0x10,
    },
    "Snow Source": {
      'classification': ItemClassification.progression,
        "address": 0x265714,
        'value': 0x20,
    },
    "Ocean Source": {
      'classification': ItemClassification.progression,
        "address": 0x265714,
        'value': 0x40,
    },
    "Fire Source": {
      'classification': ItemClassification.progression,
        "address": 0x265714,
        'value': 0x80,
    },

    # Warp gates require cannon
    "Force Gem 1": {
        'classification': ItemClassification.progression,
        #'address': 0x265716,
        #'value': 0x40
    },

    # ========== Rupees and filler =============

    "Green Rupee (1)": {
        'classification': ItemClassification.filler,
        'address': 0x265328,
        'value': 1,
        'incremental': True,
        'size': 2
    },
    "Blue Rupee (5)": {
        'classification': ItemClassification.filler,
        'address': 0x265328,
        'value': 5,
        'incremental': True,
        'size': 2
    },
    "Red Rupee (20)": {
        'classification': ItemClassification.filler,
        'address': 0x265328,
        'value': 20,
        'incremental': True,
        'size': 2
    },
    "Big Green Rupee (100)": {
        'classification': ItemClassification.progression_skip_balancing,
        'backup_filler': True,
        'address': 0x265328,
        'value': 100,
        'incremental': True,
        'size': 2
    },
    "Big Red Rupee (200)": {
        'classification': ItemClassification.progression_skip_balancing,
        'backup_filler': True,
        'address': 0x265328,
        'value': 200,
        'incremental': True,
        'size': 2
    },
    "Gold Rupee (300)": {
        'classification': ItemClassification.progression_skip_balancing,
        'backup_filler': True,
        'address': 0x265328,
        'value': 300,
        'incremental': True,
        'size': 2
    },
    "Pre-Alpha Rupee (5000)": {
        'classification': ItemClassification.progression,
        'address': 0x265328,
        'value': 5000,
        'incremental': True,
        'size': 2
    },
    "Train Part": {
        'classification': ItemClassification.filler,
        'train_part': True
    },
    "Potion": {
        'classification': ItemClassification.filler,
        'dummy': True
    },
    "Red Potion": {
        'classification': ItemClassification.filler,
        'address': 0x265334, #this is potion slot 1
        'value': 1,
        'size': 1
    },
    "Purple Potion": {
        'classification': ItemClassification.filler,
        'address': 0x265334, #this is potion slot 1
        'value': 2,
        'size': 1
    },
    "Yellow Potion": {
        'classification': ItemClassification.filler,
        'address': 0x265334, #this is potion slot 1
        'value': 3,
        'size': 1
    },
    "Nothing!": {
        'classification': ItemClassification.filler,
        'dummy': True
    },
    "Tear of Light": {
        'classification': ItemClassification.filler,
        "address": 0x26532E,
        "dummy": True,
        'value': 1,
        'incremental': True,
        'size': 1
    },
    "Refill: Bombs": {
        'classification': ItemClassification.filler,
        "give_ammo": [10, 20, 30],
        "address": 0x265333,
        "refill": "Bombs (Progressive)",
        "incremental": True,
        "size": 2
    },
    "Refill: Arrows": {
        'classification': ItemClassification.filler,
        "give_ammo": [20, 30, 50],
        "address": 0x265332,
        "refill": "Bow (Progressive)",
        "incremental": True,
    },

    # ========= Treasure =============

    "Treasure": {
        'classification': ItemClassification.filler,
        'dummy': True
    },
    "Treasure: Demon Fossil": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x269000,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Stalfos Skull": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x269002,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Star Fragment": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x269004,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Bee Larvae": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x269006,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Wood Heart": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x269008,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Dark Pearl Loop": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x26900A,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: White Pearl Loop": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x26900C,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Ruto Crown": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x26900E,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Dragon Scale": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x269010,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Pirate's Necklace": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x269012,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Palace Dish": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x269014,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Goron Amber": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x269016,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Mystic Jade": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x269018,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Ancient Coin": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x26901A,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Priceless Stone": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x26901C,
        'incremental': True,
        'value': 1,
        'size': 2,
    },
    "Treasure: Regal Ring": {
        'classification': ItemClassification.filler,
        'backup_filler': True,
        'treasure': True,
        'address': 0x26901E,
        'incremental': True,
        'value': 1,
        'size': 2,
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
        'dungeon': 0x1A,
        'incremental': False
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
}


# Oops apparently not a constant lul (it will be after this)
for i, k in enumerate(ITEMS_DATA.keys()):
    ITEMS_DATA[k]["id"] = i+1

