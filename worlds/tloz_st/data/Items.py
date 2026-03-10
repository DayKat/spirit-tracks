from BaseClasses import ItemClassification
from .Addresses import STAddr
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
        'progressive': [[STAddr.items_2, 0x02], [STAddr.items_2, 0x04]],
        'item_groups': ["Swords", "Progressive Items", "Equipment"],

        "model": "Sword"
    },
    "Sword": {  # Used when lokomo sword is not progressive, and tied to tears
        'classification': ItemClassification.progression,
        'address': STAddr.items_2,
        "value": 0x02,
        'item_groups': ["Swords", "Equipment"],

        "model": "Sword"
    },
    "Shield": {
        'classification': ItemClassification.progression,
        'address': STAddr.items_2,
        'value': 0x01,
        'item_groups': ["Equipment"],

        "model": "Shield"
    },
    "Whirlwind": {
        'classification': ItemClassification.progression,
        'address': STAddr.items_0,
        'value': 0x01,
        'item_groups': ["Equipment", "Main Items",
                        "Gust"],

        "model": "Whirlwind"
    },
    "Bombs (Progressive)": {
        'classification': ItemClassification.progression,
        "progressive": [[STAddr.items_0, 0x10], [STAddr.bomb_capacity, 0x1], [STAddr.bomb_capacity, 0x2]],
        "tags": ["progressive_overwrite"],
        "give_ammo": [10, 20, 30],
        "ammo_address": STAddr.bomb_count,
        "set_bit": [(STAddr.adv_flags_22, 0x2)],
        'item_groups': ["Equipment", "Progressive Items", "Main Items", "Ammo Items",
                        "Bombs"],

        "model": "Bomb Bag",
        "progressive_model": ["Bomb Bag", "Medium Bomb Bag", "Large Bomb Bag"],
    },
    "Bow (Progressive)": {
        'classification': ItemClassification.progression,
        "progressive": [[STAddr.items_0, 0x08], [STAddr.arrow_capacity, 0x1], [STAddr.arrow_capacity, 0x2]],
        "give_ammo": [20, 30, 50],
        "ammo_address": STAddr.arrow_count,
        "tags": ["progressive_overwrite"],
        'item_groups': ["Equipment", "Progressive Items", "Main Items", "Bows", "Ammo Items",
                        "Bow"],

        "model": "Bow",
        "progressive_model": ["Bow", "Medium Quiver", "Large Quiver"],
    },
    "Bow of Light": {
        'classification': ItemClassification.progression,
        "address": STAddr.adv_flags_16,
        "value": 1,
        'item_groups': ["Equipment", "Main Items", "Bows",
                        "Light Arrows", "Light Bow"],

        "model": "Bow"
    },
    "Whip": {
        'classification': ItemClassification.progression,
        'address': STAddr.items_0,
        'value': 0x04,
        'item_groups': ["Equipment", "Main Items"],

        "model": "Whip"
    },
    "Boomerang": {
        'classification': ItemClassification.progression,
        'address': STAddr.items_0,
        'value': 0x02,
        'item_groups': ["Equipment", "Main Items"],

        "model": "Boomerang"
    },
    "Sand Wand": {
        'classification': ItemClassification.progression,
        'address': STAddr.items_0,
        'value': 0x20,
        'item_groups': ["Equipment", "Main Items",
                        "Sand Rod"],

        "model": "Sand Wand"
    },
    "Spirit Flute": {
        'classification': ItemClassification.progression,
        'address': STAddr.items_2,
        'value': 0x80,
        'item_groups': ["Equipment",
                        "Spirit Pipes", "Pan Flute", "Flute"],
    },

    # ======= Misc Items==========

    "Recruit Uniform": {
        'classification': ItemClassification.progression,
        #'address': 0x1BA645,
        #'value': 0x01,
        #'set_bit': [(0x1BA6C8, 1)]
        "model": "Hero's Clothes"
    },
    "Engineer's Clothes": {
        'classification': ItemClassification.filler,
        #'address': 0x1BA645,
        #'value': 0x01,
        #'set_bit': [(0x1BA6C8, 1)]
        "model": "Engineer's Clothes"
    },
    "Compass of Light": {
        'classification': ItemClassification.progression,
        'address': STAddr.rail_restorations,
        'value': 0x40,  # also set adv flag?
        'set_bit': [(STAddr.adv_flags_25, 0x60)],
        'item_groups': ["Rail Items", "Forest Tracks"],
        "model": "Compass of Light",
    },
    "Royal Engineer's Certificate": {
        'classification': ItemClassification,
        'address': STAddr.adv_flags_3,
        'value': 0x01,
    },
    "Rabbit Net": {
        'classification': ItemClassification.progression,
        'address': STAddr.adv_flags_1a,
        'value': 0x40,
        'item_groups': ["Equipment", "Train Items"],
        "model": "Rabbit Net"
    },
    "Stamp Book": {
        'classification': ItemClassification.progression,
        'address': STAddr.adv_flags_25,
        'value': 0x02,
        'item_groups': ["Equipment"],
        "model": "Stamp Book"
    },

    # ======= Songs ==========

    "Song of Awakening": {
        'classification': ItemClassification.progression,
        'address': STAddr.songs,
        'value': 0x01,
        'item_groups': ["Songs"],
        "model": "SoA"
    },
    "Song of Healing": {
        'classification': ItemClassification.useful,
        'address': STAddr.songs,
        'value': 0x02,
        'item_groups': ["Songs"],
        "model": "SoH"
    },
    "Song of Birds": {
        'classification': ItemClassification.progression,
        'address': STAddr.songs,
        'value': 0x04,
        'item_groups': ["Songs"],
        "model": "SoB"
    },
    "Song of Light": {
        'classification': ItemClassification.progression,
        'address': STAddr.songs,
        'value': 0x08,
        'item_groups': ["Songs"],
        "model": "SoL"
    },
    "Song of Discovery": {
        'classification': ItemClassification.progression,
        'address': STAddr.songs,
        'value': 0x10,
        'item_groups': ["Songs"],
        "model": "SoD"
    },

    # ============= Spirits and Upgrades =============


    "Heart Container": {
        'classification': ItemClassification.useful,
        'backup_filler': True,
        'address': STAddr.heart_count,
        'value': 4,
        "tags": ["monotone_incremental"],
        "base_count": 12,
        'item_groups': ["Upgrade Items"],
        'model': "Heart Container"
    },
    "Sword Beam Scroll": {
        'classification': ItemClassification.progression,
        'address': STAddr.items_2,
        'value': 0x0010,
        'item_groups': ["Upgrade Items", "Equipment"],
        'model': "Green Scroll"
    },
    "Great Spin Scroll": {
        'classification': ItemClassification.useful,
        'address': STAddr.items_2,
        'value': 0x0020,
        'item_groups': ["Upgrade Items", "Equipment"],
        'model': "Purple Scroll"
    },

    # ============= Train Items =============

    "Cannon": {
        'classification': ItemClassification.progression,
        'address': STAddr.adv_flags_3,
        'value': 0x80,
        'item_groups': ["Train Items"],
        'model': "Large Bomb Bag"
    },
    "Portal Unlock: Hyrule Castle to Anouki Village": {
        'classification': ItemClassification.progression,
        # 'address': 0x265744,
        # 'value': 0x08,
        'item_groups': ["Portal Unlocks"],
    },
    "Portal Unlock: Trading Post to E Snow Realm": {
        'classification': ItemClassification.progression,
        # 'address': 0x265744,
        # 'value': 0x40,
        'item_groups': ["Portal Unlocks"],
    },
    "Portal Unlock: Desert Temple to Sand Realm": {
        'classification': ItemClassification.progression,
        'item_groups': ["Portal Unlocks"],
    },
    "Portal Unlock: Fire Sand Connection to Marine Temple": {
        'classification': ItemClassification.progression,
        'item_groups': ["Portal Unlocks"],
    },
    "Portal Unlock: Forest Cave to Goron Village": {
        'classification': ItemClassification.progression,
        'item_groups': ["Portal Unlocks"],
    },
    "Portal Unlock: Icy Spring to Mountain Temple": {
        'classification': ItemClassification.progression,
        'item_groups': ["Portal Unlocks"],
    },

    # ========== Rail Maps ============

    "Forest Glyph": {
        'classification': ItemClassification.progression,
        'address': STAddr.adv_flags_1,
        'value': 0x80,
        'item_groups': ["Glyphs", "Rail Items", "Forest Tracks"],
        'model': "Forest Glyph",
    },
    "Snow Glyph": {
        'classification': ItemClassification.progression,
        'address': STAddr.adv_flags_2,
        'value': 0x01,
        'item_groups': ["Glyphs", "Rail Items", "Snow Tracks"],
        'model': "Snow Glyph",
    },
    "Ocean Glyph": {
        'classification': ItemClassification.progression,
        'address': STAddr.adv_flags_2,
        'value': 0x02,
        'item_groups': ["Glyphs", "Rail Items", "Ocean Tracks"],
        'model': "Ocean Glyph",
    },
    "Fire Glyph": {
        'classification': ItemClassification.progression,
        'address': STAddr.adv_flags_2,
        'value': 0x04,
        'item_groups': ["Glyphs", "Rail Items", "Fire Tracks"],
        'model': "Fire Glyph",
    },
    "Wooded Temple Tracks":{
        'classification': ItemClassification.progression,
        'address': STAddr.rail_restorations,
        'value': 0x02,
        'item_groups': ["Restoration Tracks", "Rail Items", "Forest Tracks",
                        "Forest Restoration", "Forest Realm Restoration"],
        'model': "Forest Glyph 2",
    },
    "Blizzard Temple Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.rail_restorations,
        'value': 0x04,
        'item_groups': ["Restoration Tracks", "Rail Items", "Snow Tracks",
                        "Snow Restoration", "Snow Realm Restoration"],
        'model': "Snow Glyph 2",
    },
    "Marine Temple Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.rail_restorations,
        'value': 0x08,
        'item_groups': ["Restoration Tracks", "Rail Items", "Ocean Tracks",
                        "Ocean Temple Tracks", "Ocean Restoration", "Ocean Realm Restoration"],
        'model': "Ocean Glyph 2",
    },
    "Mountain Temple Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.rail_restorations,
        'value': 0x10,
        'item_groups': ["Restoration Tracks", "Rail Items", "Fire Tracks",
                        "Fire Temple Tracks", "Fire Restoration", "Fire Realm Restoration", "Mountain Restoration"],
        "set_bits": [(STAddr.adv_flags_1, 0x8)],
        'model': "Fire Glyph 2",
    },
    "Desert Temple Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.rail_restorations,
        'value': 0x20,
        'item_groups': ["Restoration Tracks", "Rail Items", "Desert Tracks",
                        "Desert Restoration", "Sand Temple Tracks", "Sand Restoration", "Sand Realm Restoration"],
        'model': "Ocean Glyph 3",
    },
    # Misc Tracks
    "Snowdrift Station Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_1,
        'value': 0x04,
        'item_groups': ["Rail Items", "Snow Tracks", "Misc Tracks",
                        "Snowdrift Tracks"],
        "model": "Snow Glyph",
        "vanilla_model": "Force Gem 51"
    },
    "Slippery Station Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_1,
        'value': 0x20,
        'item_groups': ["Rail Items", "Snow Tracks", "Misc Tracks",
                        "Slippery Tracks"],
        "model": "Snow Glyph",
        "vanilla_model": "Force Gem 54"
    },
    "Pirate Hideout Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_2,
        'value': 0x1,
        'item_groups': ["Rail Items", "Ocean Tracks", "Misc Tracks",
                        "Pirate Tracks"],
        "model": "Ocean Glyph",
        "vanilla_model": "Force Gem 57"
    },
    "Lost at Sea Station Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_1,
        'value': 0x40,
        'item_groups': ["Rail Items", "Ocean Tracks", "Misc Tracks",
                        "LaS Tracks", "Lost at Sea Tracks"],
        "model": "Ocean Glyph",
        "vanilla_model": "Force Gem 55"
    },
    "Forest Realm Ocean Shortcut Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_0,
        'value': 0x02,
        'item_groups': ["Rail Items", "Forest Tracks", "Ocean Tracks", "Misc Tracks"],
        "model": "Ocean Glyph",
        "vanilla_model": "Force Gem 42"
    },
    "E Mayscore Bridge Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_0,
        'value': 0x04,
        'item_groups': ["Rail Items", "Forest Tracks", "Misc Tracks"],
        "model": "Forest Glyph",
        "vanilla_model": "Force Gem 43"
    },
    "Forest Realm SE Portal Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_0,
        'value': 0x08,
        'item_groups': ["Rail Items", "Forest Tracks", "Misc Tracks"],
        "model": "Forest Glyph",
        "vanilla_model": "Force Gem 44"
    },
    "W Castle Town Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_0,
        'value': 0x20,
        'item_groups': ["Rail Items", "Forest Tracks", "Misc Tracks"],
        "model": "Forest Glyph",
        "vanilla_model": "Force Gem 46"
    },
    "W Forest Realm Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_0,
        'value': 0x40,
        'item_groups': ["Rail Items", "Forest Tracks", "Misc Tracks"],
        "model": "Forest Glyph",
        "vanilla_model": "Force Gem 47"
    },
    "Forest Realm SW Cave Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_0,
        'value': 0x80,
        'item_groups': ["Rail Items", "Forest Tracks", "Misc Tracks"],
        "model": "Forest Glyph",
        "vanilla_model": "Force Gem 48"
    },
    "W Wooded Temple Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_1,
        'value': 0x01,
        'item_groups': ["Rail Items", "Forest Tracks", "Snow Tracks", "Misc Tracks"],
        "model": "Forest Glyph",
        "vanilla_model": "Force Gem 49"
    },
    "N Castle Town Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_1,
        'value': 0x02,
        'item_groups': ["Rail Items", "Forest Tracks", "Snow Tracks", "Misc Tracks"],
        "model": "Forest Glyph",
        "vanilla_model": "Force Gem 50"
    },
    "Snow Realm Bridge Tracks": { # has portal to ocean realm
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_1,
        'value': 0x08,
        'item_groups': ["Rail Items", "Forest Tracks", "Snow Tracks", "Misc Tracks"],
        "model": "Snow Glyph",
        "vanilla_model": "Force Gem 52"
    },
    "N Icy Spring Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_1,
        'value': 0x10,
        'item_groups': ["Rail Items", "Snow Tracks", "Misc Tracks"],
        "model": "Snow Glyph",
        "vanilla_model": "Force Gem 53"
    },
    "Ocean Portal Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_1,
        'value': 0x80,
        'item_groups': ["Rail Items", "Ocean Tracks", "Misc Tracks"],
        "model": "Ocean Glyph",
        "vanilla_model": "Force Gem 56"
    },
    "Sand Realm Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_2,
        'value': 0x20,
        'item_groups': ["Rail Items", "Desert Tracks", "Misc Tracks"],
    },
    "Sand to Fire Connection Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_2,
        'value': 0x02,
        'item_groups': ["Rail Items", "Desert Tracks", "Fire Tracks", "Misc Tracks",
                        "Fire to Sand Connection Tracks", "Fire Realm Portal Tracks", "S Fire Realm Portal Tracks"],
        "model": "Fire Glyph",
        "vanilla_model": "Force Gem 58"
    },
    "Dark Ore Mine Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_2,
        'value': 0x04,
        'item_groups': ["Rail Items", "Desert Tracks", "Fire Tracks", "Misc Tracks"],
        "model": "Fire Glyph",
        "vanilla_model": "Force Gem 59"
    },
    "Ends of the Earth Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_0,
        'value': 0x10,
        'item_groups': ["Rail Items", "Fire Tracks", "Misc Tracks"],
        "model": "Fire Glyph",
        "vanilla_model": "Force Gem 45"
    },
    "Disorientation Station Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_2,
        'value': 0x10,
        'item_groups': ["Rail Items", "Fire Tracks", "Misc Tracks",
                        "Disorientation Tracks"],
        "model": "Fire Glyph",
        "vanilla_model": "Force Gem 36"
    },
    "Snow Realm Gorge Tracks": {
        'classification': ItemClassification.progression,
        'address': STAddr.tracks_2,
        'value': 0x08,
        'item_groups': ["Rail Items", "Snow Tracks", "Fire Tracks", "Misc Tracks",
                        "E Snow Realm Tracks", "W Fire Realm Tracks"],
        "model": "Fire Glyph",
        "vanilla_model": "Force Gem 60"
    },

    # ========= Sources ==============

    "Forest Source": {
      'classification': ItemClassification.progression,
        "address": STAddr.adv_flags_0,
        'value': 0x10,
        'set_bit': [[STAddr.source_rails, 2]],
        'item_groups': ["Rail Items", "Sources", "Forest Tracks"],
        'model': "Forest Glyph",
    },
    "Snow Source": {
      'classification': ItemClassification.progression,
        "address": STAddr.adv_flags_0,
        'value': 0x20,
        'set_bit': [[STAddr.source_rails, 4]],
        'item_groups': ["Rail Items", "Sources", "Snow Tracks"],
        'model': "Snow Glyph",
    },
    "Ocean Source": {
      'classification': ItemClassification.progression,
        "address": STAddr.adv_flags_0,
        'value': 0x40,
        'set_bit': [[STAddr.source_rails, 8]],
        'item_groups': ["Rail Items", "Sources", "Ocean Tracks"],
        'model': "Ocean Glyph",
    },
    "Fire Source": {
      'classification': ItemClassification.progression,
        "address": STAddr.adv_flags_0,
        'value': 0x80,
        'set_bit': [[STAddr.source_rails, 0x10]],
        'item_groups': ["Rail Items", "Sources", "Fire Tracks"],
        'model': "Fire Glyph",
    },
    "Sand Source": {  # Only used for TEAO3 unlock?
        'classification': ItemClassification.progression,
        "address": STAddr.adv_flags_1a,
        'value': 0x1,
        'set_bit': [[STAddr.source_rails, 0x20]],
        'item_groups': ["Sources"],
        'model': "Ocean Glyph",
    },

    # ========== Rabbits ============

    "Grass Rabbit": {
        'classification': ItemClassification.progression,
        "tags": ["rabbit"],
        'dummy': True,
        "item_groups": ["Grass Rabbits", "Forest Rabbit"],
        'model': "Rabbit Net",
    },
    "Snow Rabbit": {
        'classification': ItemClassification.progression,
        "tags": ["rabbit"],
        'dummy': True,
        "item_groups": ["Snow Rabbits"],
        'model': "Rabbit Net",
    },
    "Mountain Rabbit": {
        'classification': ItemClassification.progression,
        "tags": ["rabbit"],
        'dummy': True,
        "item_groups": ["Mountain Rabbits", "Fire Rabbit"],
        'model': "Rabbit Net",
    },
    "Sand Rabbit": {
        'classification': ItemClassification.progression,
        "tags": ["rabbit"],
        'dummy': True,
        "item_groups": ["Sand Rabbits", "Desert Rabbit"],
        'model': "Rabbit Net",
    },
}

ITEMS_DATA |= {
    f"{realm} Rabbits ({n})": {
        'classification': ItemClassification.progression,
        "tags": ["rabbit"],
        'dummy': True,
        'value': n,
        "item_groups": [f"{realm} Rabbits"],
        'model': "Rabbit Net",
    } for n in list(range(2, 6)) + [10] for realm in ["Grass", "Snow", "Mountain", "Sand"]
}

    # ========== Rupees and filler =============
ITEMS_DATA |= {
    "Green Rupee (1)": {
        'classification': ItemClassification.filler,
        'address': STAddr.rupees,
        'value': 1,
        "tags": ["incremental"],
        'item_groups': ["Small Rupees"],

        "model": "Green Rupee"
    },
    "Blue Rupee (5)": {
        'classification': ItemClassification.filler,
        'address': STAddr.rupees,
        'value': 5,
        "tags": ["incremental"],
        'item_groups': ["Small Rupees"],

        "model": "Blue Rupee"
    },
    "Red Rupee (20)": {
        'classification': ItemClassification.filler,
        'address': STAddr.rupees,
        'value': 20,
        "tags": ["incremental"],
        'item_groups': ["Small Rupees"],

        "model": "Red Rupee"
    },
    "Big Green Rupee (100)": {
        'classification': ItemClassification.filler,
        'address': STAddr.rupees,
        'value': 100,
        "tags": ["incremental", 'backup_filler'],
        'item_groups': ["Big Rupees"],

        "model": "Big Green Rupee"
    },
    "Big Red Rupee (200)": {
        'classification': ItemClassification.filler,
        'address': STAddr.rupees,
        'value': 200,
        "tags": ["incremental", 'backup_filler'],
        'item_groups': ["Big Rupees"],

        "model": "Big Red Rupee"
    },
    "Gold Rupee (300)": {
        'classification': ItemClassification.filler,
        'address': STAddr.rupees,
        'value': 300,
        "tags": ["incremental", 'backup_filler'],
        'item_groups': ["Big Rupees"],

        "model": "Gold Rupee"
    },
    "Pre-Alpha Rupee (5000)": {
        'classification': ItemClassification.progression,
        'address': STAddr.rupees,
        'value': 5000,
        "tags": ["incremental"],

        "model": "Gold Rupee"
    },
    "Train Part": {
        'classification': ItemClassification.filler,
        'train_part': True
    },
    "Red Potion": {
        'classification': ItemClassification.filler,
        'address': STAddr.potion_0, #this is potion slot 1
        'value': 1,
        'overflow_item': "Big Green Rupee (100)",
        'item_groups': ["Potions"],
        'tags': ["always_process"],
        "model": "Red Potion"
    },
    "Purple Potion": {
        'classification': ItemClassification.filler,
        'address': STAddr.potion_0, #this is potion slot 1
        'value': 2,
        'overflow_item': "Big Green Rupee (100)",
        'item_groups': ["Potions"],
        'tags': ["always_process"],
        "model": "Purple Potion"
    },
    "Yellow Potion": {
        'classification': ItemClassification.filler,
        'address': STAddr.potion_0, #this is potion slot 1
        'value': 3,
        'overflow_item': "Big Red Rupee (200)",
        'item_groups': ["Potions"],
        'tags': ["always_process"],
        "model": "Yellow Potion"
    },
    "Nothing!": {
        'classification': ItemClassification.filler,
        'dummy': True,
    },
    "Refill: Bombs": {
        'classification': ItemClassification.filler,
        "give_ammo": [10, 20, 30],
        "address": STAddr.bomb_count,
        "refill": "Bombs (Progressive)",
        "tags": ["incremental"],
        'item_groups': ["Refill Items", "Ammo Items"],
        'model': "Bomb Refill"
    },
    "Refill: Arrows": {
        'classification': ItemClassification.filler,
        "give_ammo": [20, 30, 50],
        "address": STAddr.arrow_count,
        "refill": "Bow (Progressive)",
        "tags": ["incremental"],
        'item_groups': ["Refill Items", "Ammo Items"],
        'model': "Arrow Refill"
    },

    # ========= Treasure =============

    "Treasure": {
        'classification': ItemClassification.filler,
        'dummy': True
    },
    "Treasure: Demon Fossil": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': STAddr.demon_fossil_count,
        'item_groups': ["Common Treasures"],
        'model': "Demon Fossil"
    },
    "Treasure: Stalfos Skull": {
        'classification': ItemClassification.filler,
        'address': STAddr.stalfos_skull_count,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'item_groups': ["Common Treasures"],
        'model': "Stalfos Skull"
    },
    "Treasure: Star Fragment": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': STAddr.star_fragment_count,
        'item_groups': ["Common Treasures"],
        'model': "Star Fragment"
    },
    "Treasure: Bee Larvae": {
        'classification': ItemClassification.filler,
        'address': STAddr.bee_larvae_count,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'item_groups': ["Common Treasures"],
        'model': "Bee Larvae"
    },
    "Treasure: Wood Heart": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': STAddr.wood_heart_count,
        'item_groups': ["Common Treasures"],
        'model': "Wood Heart"
    },
    "Treasure: Dark Pearl Loop": {
        'classification': ItemClassification.filler,
        'address': STAddr.dark_pearl_loop_count,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'item_groups': ["Uncommon Treasures"],
        'model': "Dark Pearl Loop"
    },
    "Treasure: White Pearl Loop": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': STAddr.white_pearl_loop_count,
        'item_groups': ["Uncommon Treasures"],
        'model': "White Pearl Loop"
    },
    "Treasure: Ruto Crown": {
        'classification': ItemClassification.filler,
        'address': STAddr.ruto_crown_count,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'item_groups': ["Uncommon Treasures"],
        'model': "Ruto Crown"
    },
    "Treasure: Dragon Scale": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': STAddr.dragon_scale_count,
        'item_groups': ["Uncommon Treasures"],
        'model': "Dragon Scale"
    },
    "Treasure: Pirate's Necklace": {
        'classification': ItemClassification.filler,
        'address': STAddr.pirates_necklace_count,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'item_groups': ["Uncommon Treasures"],
        'model': "Pirate Necklace"
    },
    "Treasure: Palace Dish": {
        'classification': ItemClassification.filler,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'address': STAddr.palace_dish_count,
        'item_groups': ["Rare Treasures"],
        'model': "Palace Dish"
    },
    "Treasure: Goron Amber": {
        'classification': ItemClassification.filler,
        'address': STAddr.goron_amber_count,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'item_groups': ["Rare Treasures"],
        'model': "Goron Amber"
    },
    "Treasure: Mystic Jade": {
        'classification': ItemClassification.filler,
        'address': STAddr.mystic_jade_count,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'item_groups': ["Rare Treasures"],
        'model': "Mystic Jade"
    },
    "Treasure: Ancient Coin": {
        'classification': ItemClassification.filler,
        'address': STAddr.ancient_coin_count,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'item_groups': ["Rare Treasures"],
        'model': "Ancient Coin"
    },
    "Treasure: Priceless Stone": {
        'classification': ItemClassification.filler,
        'address': STAddr.priceless_stone_count,
        "tags": ['treasure', 'backup_filler', 'incremental'],
        'item_groups': ["Super Rare Treasures"],
        'model': "Alchemy Stone"
    },
    "Treasure: Regal Ring": {
        'classification': ItemClassification.progression,
        'address': STAddr.regal_ring_count,
        "tags": ['treasure', 'incremental'],
        'item_groups': ["Super Rare Treasures"],
        'model': "Regal Ring"
    },

    # =========== Keys ============

     "Small Key (Tunnel to ToS)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x18,
        "tags": ["incremental"],
        'item_groups': ["Small Keys"],
         "model": "Key"
     },
    "Small Key (Wooded Temple)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x19,
        "tags": ["incremental"],
        'item_groups': ["Small Keys"],
         "model": "Key"
     },
    "Small Key (ToS)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x13,
         "tags": ["incremental"],
        'item_groups': ["Small Keys"],
         "model": "Key"
    },
    "Small Key (ToS 2)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x13,
        "tags": ["incremental"],
        "rooms": [3, 4, 5, 6, 0x29],
        "section": 2,
        'item_groups': ["Small Keys"],
         "model": "Key"
    },
    "Small Key (ToS 4)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x13,
        "tags": ["incremental"],
        "rooms": [0xc, 0xd, 0xe, 0xf, 0x10],
        "section": 4,
        'item_groups': ["Small Keys"],
         "model": "Key"
    },
    "Small Key (ToS 5)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x13,
        "tags": ["incremental"],
        "rooms": [0x11, 0x12, 0x13, 0x14, 0x17, 0x18],
        "section": 5,
        'item_groups': ["Small Keys"],
         "model": "Key"
    },
    "Small Key (ToS 6)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x13,
        "tags": ["incremental"],
        "rooms": [0x1d, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x2c, 0x2d],
        "section": 6,
        'item_groups': ["Small Keys"],
         "model": "Key"
    },
    "Small Key (Blizzard Temple)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x1A,
         "tags": ["incremental"],
        'item_groups': ["Small Keys"],
         "model": "Key"
    },
    "Small Key (Marine Temple)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x1B,
        "tags": ["incremental"],
        'item_groups': ["Small Keys"],
         "model": "Key"
    },
    "Small Key (Mountain Temple)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x1C,
        "tags": ["incremental"],
        'item_groups': ["Small Keys"],
         "model": "Key"
    },
    "Small Key (Desert Temple)": {
        'classification': ItemClassification.progression,
        'address': STAddr.small_keys,
        'dungeon': 0x1D,
        "tags": ["incremental"],
        'item_groups': ["Small Keys"],
         "model": "Key"
    },
    "Boss Key (Blizzard Temple)": {
        'classification': ItemClassification.progression,
        'item_groups': ["Boss Keys"],
        "dummy": True,
        "model": "Boss Key"
    },
    "Boss Key (Wooded Temple)": {
        'classification': ItemClassification.progression,
        'dungeon': 0x19,
        'item_groups': ["Boss Keys"],
        "dummy": True,
        "model": "Boss Key"
    },
    "Boss Key (Marine Temple)": {
        'classification': ItemClassification.progression,
        'item_groups': ["Boss Keys"],
        "dummy": True,
        "model": "Boss Key"
    },
    "Boss Key (Mountain Temple)": {
        'classification': ItemClassification.progression,
        'item_groups': ["Boss Keys"],
        "dummy": True,
        "model": "Boss Key"
    },
    "Boss Key (Desert Temple)": {
        'classification': ItemClassification.progression,
        'item_groups': ["Boss Keys"],
        "dummy": True,
        "model": "Boss Key"
    },
    "Boss Key (ToS 3)": {
        'classification': ItemClassification.progression,
        'item_groups': ["Boss Keys"],
        "dummy": True,
        "model": "Boss Key"
    },
    "Boss Key (ToS 5)": {
        'classification': ItemClassification.progression,
        'item_groups': ["Boss Keys"],
        "dummy": True,
        "model": "Boss Key"
    },

    # Tears
    "Tear of Light": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        'value': 1,
        'item_groups': ["Tears of Light", "Small Tears of Light"],
        'model': "Tear of Light"
    },
    "Tear of Light (ToS 1)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        "rooms": [0, 1, 0x28],
        "tags": ["always_process"],
        'item_groups': ["Unique Tears of Light", "Small Tears of Light"],
        'model': "Tear of Light"
    },
    "Tear of Light (ToS 2)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        "rooms": [3, 4, 5, 0x29],
        "tags": ["always_process"],
        'item_groups': ["Unique Tears of Light", "Small Tears of Light"],
        'model': "Tear of Light"
    },
    "Tear of Light (ToS 3)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        "rooms": [7, 8, 9, 0xa, 0x15, 0x16, 0x2A],
        'item_groups': ["Unique Tears of Light", "Small Tears of Light"],
        'model': "Tear of Light"
    },
    "Tear of Light (ToS 4)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        "rooms": [0xc, 0xd, 0xe, 0xf, 0x10],
        'item_groups': ["Unique Tears of Light", "Small Tears of Light"],
        'model': "Tear of Light"
    },
    "Tear of Light (ToS 5)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        "rooms": [0x11, 0x12, 0x13, 0x14, 0x17, 0x18],
        'item_groups': ["Unique Tears of Light", "Small Tears of Light"],
        'model': "Tear of Light"
    },
    "Tear of Light (All Sections)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        "rooms": range(0x30),
        'item_groups': ["Universal Tears of Light", "Small Tears of Light",
                        "Tear of Light (Global)"],
        'model': "Tear of Light"
    },
    "Tear of Light (Progressive)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        'item_groups': ["Progressive Tears of Light", "Small Tears of Light"],
        'model': "Tear of Light"
    },
    "Big Tear of Light (ToS 1)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        'value': 3,
        "rooms": [0, 1, 0x28],
        'item_groups': ["Unique Tears of Light", "Big Tears of Light"],
        'model': "Tear of Light"
    },
    "Big Tear of Light (ToS 2)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        'value': 3,
        "rooms": [3, 4, 5, 0x29],
        'item_groups': ["Unique Tears of Light", "Big Tears of Light"],
        'model': "Tear of Light"
    },
    "Big Tear of Light (ToS 3)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        'value': 3,
        "rooms": [7, 8, 9, 0xa, 0x15, 0x16, 0x2A],
        'item_groups': ["Unique Tears of Light", "Big Tears of Light"],
        'model': "Tear of Light"
    },
    "Big Tear of Light (ToS 4)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        'value': 3,
        "rooms": [0xc, 0xd, 0xe, 0xf, 0x10],
        'item_groups': ["Unique Tears of Light", "Big Tears of Light"],
        'model': "Tear of Light"
    },
    "Big Tear of Light (ToS 5)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        'value': 3,
        "rooms": [0x11, 0x12, 0x13, 0x14, 0x17, 0x18],
        'item_groups': ["Unique Tears of Light", "Big Tears of Light"],
        'model': "Tear of Light"
    },
    "Big Tear of Light (Progressive)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        'value': 3,
        'item_groups': ["Progressive Tears of Light", "Big Tears of Light"],
        'model': "Tear of Light"
    },
    "Big Tear of Light (All Sections)": {
        'classification': ItemClassification.progression,
        "address": STAddr.tears_of_light,
        "rooms": range(0x30),
        "value": 3,
        'item_groups': ["Universal Tears of Light", "Big Tears of Light",
                        "Big Tear of Light (Global)"],
        'model': "Tear of Light"
    },

    # Trade Quest and misc

    # Warp Gates

    # Trains
    "Train: Bright Train": {
        'classification': ItemClassification.useful,
         "tags": ["backup_filler"],
        'train': 1
    },
    "Train: Iron Train": {
        'classification': ItemClassification.useful,
         "tags": ["backup_filler"],
        'train': 2
    },
    "Train: Stone Train": {
        'classification': ItemClassification.useful,
         "tags": ["backup_filler"],
        'train': 3
    },
    "Train: Vintage Train": {
        'classification': ItemClassification.useful,
         "tags": ["backup_filler"],
        'train': 4
    },
    "Train: Demon Train": {
        'classification': ItemClassification.useful,
         "tags": ["backup_filler"],
        'train': 5
    },
    "Train: Tropical Train": {
        'classification': ItemClassification.useful,
         "tags": ["backup_filler"],
        'train': 6
    },
    "Train: Dignified Train": {
        'classification': ItemClassification.useful,
         "tags": ["backup_filler"],
        'train': 7
    },
    "Train: Golden Train": {
        'classification': ItemClassification.useful,
         "tags": ["backup_filler"],
        'train': 8
    },

    "_UT_Glitched_Logic": {  # Shows yellow logic in UT
        "classification": ItemClassification.progression,
        "dummy": True,
    },


    # IDs are not fixed yet, but determined by order. Put new items here until an update that breaks compatibility, and move them then.
    "Tower of Spirits Base": {
        "classification": ItemClassification.progression,
        "dummy": True,
        'item_groups': ["Tower of Spirit Unlocks"],
        "model": "Forest Glyph"
    },
    "Progressive ToS Section": {
        "classification": ItemClassification.progression,
        "dummy": True,
        'item_groups': ["Tower of Spirit Unlocks"],
        "model": "Forest Glyph"
    },
    # Overworld eventy things
    "Repair Trading Post Bridge": {
        "classification": ItemClassification.progression,
        "address": STAddr.adv_flags_17,
        "value": 0x10,
        "model": "Forest Glyph"
    },
    "Snowfall Sanctuary Cave Key": {
        "classification": ItemClassification.progression,
        "address": STAddr.adv_flags_b,
        "value": 0x10,
        "item_groups": ["Misc Keys"],
        "model": "Key"
    },
    "Prize Postcards (10)": {
        "classification": ItemClassification.filler,
        "address": STAddr.postcard_count,
        "value": 10,
        "tags": ["incremental"],
        "model": "Prize Postcards"
    },
    "Wagon": {  # US Freight Car, Neutral Something else?
        "classification": ItemClassification.progression,
        "address": STAddr.adv_flags_4,
        "value": 0x2,
        'item_groups': ["Train Items"],
        'model': "Engineer's Clothes"
    },
    # Passengers
    "Passenger: Kenzo": {
        "classification": ItemClassification.progression,
        'tags': ["always_process"],
        "item_groups": ["Passengers"],
        "address": STAddr.adv_flags_18,
        "value": 0x20,
        "model": "Letter"
    },
    "Passenger: Kenzo 2": {
        "classification": ItemClassification.progression,
        'tags': ["always_process"],
        "item_groups": ["Passengers"],
        "address": STAddr.adv_flags_3c,
        "value": 0x10,
        "model": "Letter"
    },
    "Passenger: Joe": {
        "classification": ItemClassification.progression,
        "item_groups": ["Passengers"],
        'tags': ["always_process"],
        "address": STAddr.adv_flags_3c,
        "value": 0x2,
        "model": "Letter"
    },
    "Passenger: Noko": {
        "classification": ItemClassification.progression,
        "item_groups": ["Passengers"],
        'tags': ["always_process"],
        "address": STAddr.adv_flags_3a,
        "value": 0x10,
        "model": "Letter"
    },
    "Passenger: Mona": {
        "classification": ItemClassification.progression,
        "item_groups": ["Passengers"],
        'tags': ["always_process"],
        "address": STAddr.adv_flags_3b,
        "value": 0x20,
        "model": "Letter"
    },
    "Passenger: Ferrus": {
        "classification": ItemClassification.progression,
        "item_groups": ["Passengers"],
        'tags': ["always_process"],
        "address": STAddr.adv_flags_3a,
        "value": 0x80,
        "model": "Letter"
    },
    "Passenger: Alfonzo": {
        "classification": ItemClassification.progression,
        "item_groups": ["Passengers"],
        'tags': ["always_process"],
        "address": STAddr.adv_flags_11,
        "value": 0x40,
        "model": "Letter"
    },
    "Passenger: Dovok": {
        "classification": ItemClassification.progression,
        "item_groups": ["Passengers"],
        'tags': ["always_process"],
        "address": STAddr.adv_flags_36,
        "value": 0x4,
        "model": "Letter"
    },
    "Passenger: Snow Goron": {
        "classification": ItemClassification.progression,
        "item_groups": ["Passengers"],
        'tags': ["always_process"],
        "address": STAddr.adv_flags_38,
        "value": 0x2,
        "model": "Letter"
    },
    "Passenger: City Goron": {
        "classification": ItemClassification.progression,
        "item_groups": ["Passengers"],
        'tags': ["always_process"],
        "address": STAddr.adv_flags_3a,
        "value": 0x8,
        "model": "Letter"
    },
    "Passenger: Teacher": {
        "classification": ItemClassification.useful,
        "item_groups": ["Passengers"],
        'tags': ["always_process"],
        "address": STAddr.adv_flags_42,
        "value": 0x10,
        "model": "Letter"
    },
    "Passenger: Kofu": {
        "classification": ItemClassification.progression,
        "item_groups": ["Passengers"],
        'tags': ["always_process"],
        "address": STAddr.adv_flags_37,
        "value": 0x20,
        "model": "Letter"
    },

    # Cargo
    "Cargo: Lumber": {
        "classification": ItemClassification.progression,
        "item_groups": ["Cargo"],
        'tags': ["always_process"],
        "model": "Letter"
    },
    "Cargo: Mega Ice": {
        "classification": ItemClassification.progression,
        "item_groups": ["Cargo"],
        'tags': ["always_process"],
        "model": "Letter"
    },
    "Cargo: Goron Steel": {
        "classification": ItemClassification.progression,
        "item_groups": ["Cargo"],
        'tags': ["always_process"],
        "model": "Letter"
    },
    "Cargo: Fish": {
        "classification": ItemClassification.progression,
        "item_groups": ["Cargo"],
        'tags': ["always_process"],
        "model": "Letter"
    },
    "Cargo: Vessel": {
        "classification": ItemClassification.progression,
        "item_groups": ["Cargo"],
        'tags': ["always_process"],
        "model": "Letter"
    },
    "Cargo: Cuccos": {
        "classification": ItemClassification.progression,
        "item_groups": ["Cargo"],
        'tags': ["always_process"],
        "model": "Letter"
    },
    "Cargo: Cuccos (5)": {
        "classification": ItemClassification.progression,
        "item_groups": ["Cargo"],
        "model": "Letter"
    },
    "Cargo: Dark Ore": {
        "classification": ItemClassification.progression,
        "item_groups": ["Cargo"],
        'tags': ["always_process"],
        "model": "Letter"
    },

    # Stamps
    "Stamp: Castle Town": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 1,
        "model": "Stamp Book"
    },
    "Stamp: Outset Village": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 2,
        "model": "Stamp Book"
    },
    "Stamp: Mayscore": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 3,
        "model": "Stamp Book"
    },
    "Stamp: Woodland Sanctuary": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 4,
        "model": "Stamp Book"
    },
    "Stamp: Anouki Village": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 5,
        "model": "Stamp Book"
    },
    "Stamp: Snowfall Sanctuary": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 6,
        "model": "Stamp Book"
    },
    "Stamp: Papuzia Village": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 7,
        "model": "Stamp Book"
    },
    "Stamp: Ocean Sanctuary": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 8,
        "model": "Stamp Book"
    },
    "Stamp: Goron Village": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 9,
        "model": "Stamp Book"
    },
    "Stamp: Valley Sanctuary": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0xA,
        "model": "Stamp Book"
    },
    "Stamp: Dune Sanctuary": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0xB,
        "model": "Stamp Book"
    },
    "Stamp: Wooded Temple": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0xC,
        "model": "Stamp Book"
    },
    "Stamp: Blizzard Temple": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0xD,
        "model": "Stamp Book"
    },
    "Stamp: Marine Temple": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0xE,
        "model": "Stamp Book"
    },
    "Stamp: Mountain Temple": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0xF,
        "model": "Stamp Book"
    },
    "Stamp: Desert Temple": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0x10,
        "model": "Stamp Book"
    },
    "Stamp: Pirate Hideout": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0x11,
        "model": "Stamp Book"
    },
    "Stamp: Trading Post": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0x12,
        "model": "Stamp Book"
    },
    "Stamp: Icy Spring": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0x13,
        "model": "Stamp Book"
    },
    "Stamp: Tower of Spirits": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamps"],
        "value": 0,
        "model": "Stamp Book"
    },
    "Stamp Pack (2)": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamp Packs"],
        "value": 2,
        "model": "Stamp Book"
    },
    "Stamp Pack (3)": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamp Packs"],
        "value": 3,
        "model": "Stamp Book"
    },
    "Stamp Pack (4)": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamp Packs"],
        "value": 4,
        "model": "Stamp Book"
    },
    "Stamp Pack (5)": {
        "classification": ItemClassification.progression,
        "item_groups": ["Stamp Packs"],
        "value": 5,
        "model": "Stamp Book"
    },
    "Ancient Shield": {
        'classification': ItemClassification.useful,
        'address': STAddr.items_2,
        'value': 0x40,
        'item_groups': ["Equipment"],
        'model': "Ancient Shield"
    },
    "Mountain Temple Snurglar Key": {
        'classification': ItemClassification.progression,
        'dummy': True,
        'item_groups': ["Misc Keys"],
        "model": "Key"
    },
    "Orange Snurglar Key": {
        'classification': ItemClassification.progression,
        "address": STAddr.snurglin_keys,
        "value": 0x02,
        'item_groups': ["Misc Keys"],
        "model": "Key"
    },
    "Purple Snurglar Key": {
        'classification': ItemClassification.progression,
        "address": STAddr.snurglin_keys,
        "value": 0x04,
        'item_groups': ["Misc Keys"],
        "model": "Key"
    },
    "Gold Snurglar Key": {
        'classification': ItemClassification.progression,
        "address": STAddr.snurglin_keys,
        "value": 0x08,
        'item_groups': ["Misc Keys"],
        "model": "Key"
    },
}


ITEMS: dict[str, "STItem"] = {}
ITEM_GROUPS: dict[str, set[str]] = {}

# IDs need to be stabilized at some point, not today
for i, k in enumerate(ITEMS_DATA.items()):
    item_name, item_data = k
    item_data["id"] = i+1
    ITEMS[item_name] = STItem(item_name, item_data, ITEMS)

    # Add items to item groups
    for group in item_data.get("item_groups", []):
        ITEM_GROUPS.setdefault(group, set()).add(item_name)


# Combo Item Groups
ITEM_GROUPS["Rupee Items"] = ITEM_GROUPS["Small Rupees"] | ITEM_GROUPS["Big Rupees"]
ITEM_GROUPS["Uncommon Plus Treasure"] = ITEM_GROUPS["Uncommon Treasures"] | ITEM_GROUPS["Rare Treasures"] | ITEM_GROUPS["Super Rare Treasures"]
ITEM_GROUPS["All Treasures"] = ITEM_GROUPS["Uncommon Plus Treasure"] | ITEM_GROUPS["Common Treasures"]
ITEM_GROUPS["Rabbits"] = ITEM_GROUPS["Grass Rabbits"] | ITEM_GROUPS["Snow Rabbits"]  | ITEM_GROUPS["Sand Rabbits"]
ITEM_GROUPS["Tears of Light"] = ITEM_GROUPS["Big Tears of Light"] | ITEM_GROUPS["Small Tears of Light"]
ITEM_GROUPS["Add Rails to Pool"] = ITEM_GROUPS["Misc Tracks"] | ITEM_GROUPS["Restoration Tracks"]
ITEM_GROUPS["All Rails"] = ITEM_GROUPS["Rail Items"]

# for name, group in ITEM_GROUPS.items():
#     print(f"{name}: {group}")
