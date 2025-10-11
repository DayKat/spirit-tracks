VERSION = "0.3.0"
ROM_HASH = "f2dc6c4e093e4f8c6cbea80e8dbd62cb"


STARTING_FLAGS = [
    # Starting flags (these are in the same memory block so can be simplified, but it's called once and this is
    # easier to bugfix)

    [0x265714, 0x04],  # restore spirit train cutscene skip
    [0x265715, 0x01],  # forest restoration duet done
    [0x265716, 0xF0],  # sword tutorial and intro stuff
    [0x265717, 0x47],  # split ToS and zelda 1st convo
    [0x265718, 0x34],  # load train to ToS
    [0x265719, 0x74],  # train quill tutorial skip
    [0x26571A, 0xFC],  # Intro stuff
    [0x26571B, 0x13],  # postman & get zelda's letter
    [0x265720, 0xC0],  # convos
    [0x265723, 0xC0],  # ToS 4F 1st time entry
    [0x265726, 0x13],  # zelda 1st phantom possession
    [0x265729, 0x58],  # post fleeing ToS 1F
    [0x26572A, 0x08],  # ready for FS duet
    [0x265724, 0x50],  # anjean section text
    [0x26572C, 0x07],  # HC intro Zelda
    [0x26572F, 0x02],  # initial train cutscene skip
    [0x26572E, 0x0C],  # rabbitland rock text
    [0x265738, 0x08],  # move HC guards
    [0x265743, 0x40],  # linebeck 1st convo
    [0x26574B, 0x10],  # teacher text skip
    [0x265751, 0x20],  # ToS safe zone tutorial
    [0x265756, 0x80],  # board with zelda
    [0x265766, 0x80],  # ToS Staircase cutscene skip
    [0x265768, 0x20],  # first spirit train journey
    [0x26576B, 0x40],  # first song statue text
    [0x26575C, 0x10],  # alfonzo giving cannon

    # Set treasures to 0
    [0x269000, 1],
    [0x269002, 1],
    [0x269004, 1],
    [0x269006, 1],
    [0x269008, 1],
    [0x26900A, 1],
    [0x26900C, 1],
    [0x26900E, 1],
    [0x269010, 1],
    [0x269012, 1],
    [0x269014, 1],
    [0x269016, 1],
    [0x269018, 1],
    [0x26901A, 1],
    [0x26901B, 1],
    [0x26901C, 1]
]

STAGE_FLAGS = {
    0x04: [0x00, 0x00, 0x00, 0x04], # Forest Realm
    0x2F: [0x00, 0x00, 0x00, 0x2F], # Outset Village
    0x29: [0x00, 0x00, 0x00, 0x29], # Castle Town
    0x28: [0x00, 0x00, 0x00, 0x28],  # Hyrule Castle
    0x13: [0x00, 0x00, 0x00, 0x13],  # Tower of Spirits (Main)
    0x14: [0x00, 0x00, 0x00, 0x14], # Tower of Spirits (Base)
    0x17: [0x00, 0x00, 0x00, 0x17],  # Tower of Spirits (Stairs)
    0x18: [0x00, 0x00, 0x00, 0x18], # Tunnel to ToS
    0x19: [0x00, 0x00, 0x00, 0x19],  # Wooded Temple
    0x1E: [0x00, 0x00, 0x00, 0x1E], # Stagnox
    0x2A: [0x00, 0x00, 0x00, 0x2A],  # Mayscore/Whittleton
    0x30: [0x00, 0x00, 0x00, 0x20],  # Forest Sanctuary
    0x38: [0x00, 0x00, 0x00, 0x38],  # Mayscore Forest
    0x3E: [0x00, 0x00, 0x00, 0x3E],  # Rabbit Haven
    0x37: [0x00, 0x00, 0x00, 0x37],  # Trading Post

    # 37: [0xFE, 0xBE, 0xFB, 0xAF],  # TotOK
    # 0: [0x82, 0xFC, 0x66, 0xED],  # Sea
    # 13: [0xEC, 0x18, 0x17, 0x00],  # Ember
    # 28: [0x8E, 0xB9, 0x00, 0x00],  # ToF
    # 12: [0x34, 0x01, 0x00, 0x00],  # Molida
    # 14: [0x02, 0x02, 0x00, 0x00],  # Gusts
    # 29: [0x00, 0x10, 0x00, 0x00],  # ToW
    # 30: [0x0, 0x0, 0x2, 0x0],  # ToC
    # 41: [0xC2, 0x10, 0xED, 0x00],  # Ghost Ship
    # 16: [0x84, 0x13, 0x00, 0xE0],  # Goron Island
    # 32: [0x00, 0x00, 0x30, 0xF0],  # Goron Temple
    # 15: [0x00, 0x3C, 0x00, 0x40],  # Isle of Frost
    # 31: [0x00, 0x00, 0xD0, 0x00],  # Temple of Ice
    # 21: [0xB6, 0x01, 0x00, 0x00],  # Isle of the Dead
    # 17: [0x12, 0x4C, 0x43, 0x00],  # Isle of ruins
    # 18: [0x10, 0x4C, 0x43, 0x00],  # Isle of ruins
    # 36: [0x20, 0x00, 0x00, 0x00],  # Bremeur's Temple
    # 33: [0x00, 0x26, 0x00, 0x00],  # Mutoh's Temple
}

STAGES = {
    4: "Forest Realm",
    0x2F: "Outset Village",
    0x29: "Castle Town",
    0x28: "Hyrule Castle",
    0x13: "Tower of Spirits",
    0x14: "Tower of Spirits Base",
    0x17: "Tower of Spirits Stairs",
    0x18: "Tunnel to ToS",
    0x19: "Wooded Temple",
    0x1E: "Stagnox",
    0x2A: "Mayscore",
    0x30: "Forest Sanctuary",
    0x38: "Mayscore Forest",
    0x3E: "Rabbit Haven",
    0x37: "Trading Post",
}

ITEM_GROUPS = {
     "Small Keys": [
         "Small Key (Tunnel to ToS)",
         "Small Key (Wooded Temple)",
         "Small Key (ToS)",

    #     "Small Key (Temple of Fire)",
    #     "Small Key (Temple of Fire)",
    #     "Small Key (Temple of Wind)",
    #     "Small Key (Temple of Courage)",
    #     "Small Key (Temple of Ice)",
    #     "Small Key (Mutoh's Temple)"
     ],
    "Boss Keys": [
        "Boss Key (Wooded Temple)"
    ],
    "Common Treasures": [
        "Treasure: Demon Fossil",
        "Treasure: Stalfos Skull",
        "Treasure: Star Fragment",
        "Treasure: Bee Larvae",
        "Treasure: Wood Heart",
    ],
    "Uncommon Treasures": [
        "Treasure: Dark Pearl Loop",
        "Treasure: White Pearl Loop",
        "Treasure: Ruto Crown",
        "Treasure: Dragon Scale",
        "Treasure: Pirate's Necklace",
    ],
    "Rare Treasures": [
        "Treasure: Ancient Coin",
        "Treasure: Mystic Jade",
        "Treasure: Goron Amber",
        "Treasure: Palace Dish",

    ],
    "Super Rare Treasures": [
        "Treasure: Alchemy Stone",
        "Treasure: Regal Ring",
    ],
     "Ammo Refills": [
        "Refill: Bombs",
        "Refill: Arrows",
     ]
}

LOCATION_GROUPS = {
    "Outset Village": ["Outset Clear Rocks", "Outset Bee Tree", "Outset Stamp Station", "Outset Far Right Tree", "Outset Niko's House Tree", "Outset Receive Stamp Book"],
    "Castle Town": ["Castle Town Stamp Station", "Castle Town Left Wall Chest", "Castle Town Right Wall Chest", "Castle Town Minigame Roof", "Castle Town Ramp House Chest", "Castle Town Empty House Roof Chest"],
    "Hyrule Castle": ["Hyrule Castle NW Outside Chest", "Hyrule Castle 2F Indoors Chest", "Hyrule Castle 1F Back Chest"],
    "Tunnel to ToS": ["Tunnel to ToS Block Chest", "Tunnel to ToS 2F Chest"],
    "Tower of Spirits": [
        "ToS 1F Chest",
        "ToS 2F Raised Chest",
        "ToS 2F Whirlwind Chest",
        "ToS 2F Bomb Wall Chest",
        "ToS Forest Rail Glyph",
        "ToS 4F Central Chest",
        "ToS 4F NE Chest",
        "ToS 5F Island Chest",
        "ToS 5F Spinnit Key",
        "ToS 5F Bomb Wall Chest",
        "ToS 6F Enemy Chest 1",
        "ToS 6F Enemy Chest 2",
        "ToS 6F Enemy Chest 3",
        "ToS 6F Enemy Big Chest",
        "ToS 6F Key",
        "ToS Snow Rail Glyph"
    ],
    "Mayscore": ["Mayscore Stamp Station", "Mayscore Whip Race 1st Reward", "Mayscore Whip Race 2nd Reward", "Mayscore Whip Chest"],
    "Forest Sanctuary": ["Forest Sanctuary Stamp Station", "Forest Sanctuary Song Statue", "Forest Sanctuary Gage Duet", "Forest Sanctuary Chest"],
    "Wooded Temple": [
        #"Wooded Temple Song Statue",
        "Wooded Temple Stamp Station",
        "Wooded Temple 1F Enemy Chest",
        "Wooded Temple 1F Key",
        "Wooded Temple 1F Switch Chest",
        "Wooded Temple 2F Enemy Chest",
        "Wooded Temple 2F Poison Chest",
        "Wooded Temple 3F Chestnut Chest",
        "Wooded Temple 3F SE Chest",
        "Wooded Temple 3F Boss Key Chest",
        "Wooded Temple Boss Heart Container",
        "Wooded Temple Dungeon Reward"
    ],
    "Rabbit Haven": ["Rabbit Haven Net Gift", "Rabbit Haven Chest"],
    "Trading Post": ["Trading Post Stamp Station", "Trading Post Chest"],
    # "Goron Temple": [],
    # "Temple of Ice": [],
    # "Mutoh's Temple": [],
    # "Ghost Ship": []
}

DUNGEON_NAMES = [
    "Tunnel to ToS",
    "Tower of Spirits",
    "Wooded Temple"
]

DUNGEON_TO_BOSS_ITEM_LOCATION = {
    "Tower of Spirits": "ToS Forest Rail Glyph",
    "Wooded Temple": "Wooded Temple Dungeon Reward",
}


DUNGEON_KEY_DATA = {
    0x13: {
        "name": "Tower of Spirits",
        "address": 0x265785,
        "filter": 0xFF,
        "value": 1,
        "size": 8,
        # 'entrances': {
        #     0xB01: {
        #         "max_z": 0x12800,
        #         # "max_z": 0xFFFF7000
        #     },
        #     0xB03: {
        #         "max_z": 0xB200,
        #         "min_z": 0x5000
        #     }}
    },
    0x18: {
        "name": "Tunnel to ToS",
        "address": 0x265784,
        "filter": 0x01,
        "value": 1,
        "size": 1,
        # 'entrances': {
        #     0xB01: {
        #         "max_z": 0x12800,
        #         # "max_z": 0xFFFF7000
        #     },
        #     0xB03: {
        #         "max_z": 0xB200,
        #         "min_z": 0x5000
        #     }}
    },
    0x19: {
        "name": "Wooded Temple",
        "address": 0x265784,
        "filter": 0x06,
        "value": 0x02,
        "size": 2,
        # 'entrances': {
        #     0x2600: {
        #         "max_z": 0x11800,
        #         "min_z": 0x0
        #     }
        # }
    },
    # 372: {
    #     "name": "Temple of the Ocean King",
    #     "address": 0x1BA64F,
    #     "filter": 0xC0,
    #     "value": 0x40,
    #     "size": 2,
    #     'entrances': {
    #         0x2600: {
    #             "max_z": 0x11800,
    #             "min_z": 0x0}
    #     }
    # },
    # 0x1C: {
    #     "name": "Temple of Fire",
    #     "address": 0x1BA64E,
    #     "value": 1,
    #     "size": 2,
    #     "filter": 0x03,
    #     "entrances": {
    #         0xD01: {
    #             "max_z": 0x10800,
    #             "min_z": 0x8000},
    #         0x2B00: {
    #             "min_z": 0x800,
    #             "max_z": 0xF000}
    #     }
    # },
    # 0x1E: {
    #     "name": "Temple of Courage",
    #     "address": 0x1BA64F,
    #     "value": 0x10,
    #     "size": 2,
    #     "filter": 0x30,
    # },
    # 0x1D: {
    #     "name": "Temple of Wind",
    #     "address": 0x1BA64E,
    #     "value": 0x10,
    #     "size": 1,
    #     "filter": 0x10
    # },
    # 0x1F: {
    #     "name": "Temple of Ice",
    #     "address": 0x1BA64F,
    #     "value": 0x1,
    #     "size": 2,
    #     "filter": 0x03
    # },
    # 0x21: {
    #     "name": "Mutoh's Temple",
    #     "address": 0x1BA64F,
    #     "value": 0x4,
    #     "size": 2,
    #     "filter": 0x0C
    # },
}

HINTS_ON_SCENE = {
    # 0xB11: {  # Mercay Shop
    #     "island_shop": True
    # },
    # 0xC0E: {  # Molida Shop
    #     "island_shop": True
    # },
    # 0x1014: {  # Goron Shop
    #     "island_shop": True
    # },
    # 0x130B: {  # Eddo Cannon Island
    #     "unique": ["Cannon Island Cannon", "Cannon Island Salvage Arm"]
    # },
    # 0x500: {  # Beedle Shop
    #     "unique": ["Beedle Shop Wisdom Gem"],
    #     "beedle": True  # TODO: make this modular, instead of hard coding item requirements
    # },
    # 0xb0A: {  # Oshus Dungeon hints
    #     "dungeon_hints": 1
    # },
    # 0x2600: {  # TotOK Dungeon hints
    #     "dungeon_hints": 2
    # },
    # 0x1701: {
    #     "spirit_island_hints": True
    # },
}

HINTS_ON_TRIGGER = {
    #"Masked Beedle": ["Masked Beedle Courage Gem", "Masked Beedle Heart Container"]
}

# Train sets
TRAINS = [
    "S.S. Linebeck",
    "Train: Bright Train",
    "Train: Iron Train",
    "Train: Stone Train",
    "Train: Vintage Train",
    "Train: Demon Train",
    "Train: Tropical Train",
    "Train: Dignified Train",
    "Train: Golden Train",
]

# Stamp stuff
STAMPS = []

# Decode classification for humans
CLASSIFICATION = {
    1: "Progression",
    2: "Useful",
    4: "Trap",
    9: "Prog Skip Balancing",
    0: "Filler"
                  }

#TREASURE_READ_LIST = {i: (0x1BA5AC + i * 4, 4, "Main RAM") for i in range(8)}
