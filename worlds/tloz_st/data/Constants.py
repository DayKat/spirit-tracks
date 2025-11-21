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
    [0x26571F, 0x98],  # blizzard stuff
    [0x265720, 0xE2],  # convos
    [0x265723, 0xC0],  # ToS 4F 1st time entry
    [0x265724, 0x50],  # anjean section text
    [0x265726, 0x1B],  # zelda 1st phantom possession + mayascore bugs
    [0x265729, 0x58],  # post fleeing ToS 1F
    [0x26572A, 0x08],  # ready for FS duet
    [0x26572C, 0x07],  # HC intro Zelda
    [0x26572D, 0x01],  # steem
    [0x26572F, 0x02],  # initial train cutscene skip
    [0x26572E, 0x1C],  # rabbitland rock text
    [0x265738, 0x08],  # move HC guards
    [0x265743, 0x40],  # linebeck 1st convo
    [0x26574B, 0x10],  # teacher text skip
    [0x265751, 0x60],  # ToS safe zone tutorial
    [0x265754, 0x04],  # 1st portal text
    [0x265756, 0x80],  # board with zelda
    [0x26575C, 0x10],  # alfonzo giving cannon
    [0x265762, 0x80],  # blizzard void out
    [0x265766, 0x80],  # ToS Staircase cutscene skip
    [0x265767, 0x01],  # ToS Staircase 2 zelda text skip
    [0x265768, 0x28],  # first spirit train journey+portal
    [0x26576B, 0x40],  # first song statue text

    # Set treasures to 0
    [0x269000, 0, 0],
    [0x269002, 0, 0],
    [0x269004, 0, 0],
    [0x269006, 0, 0],
    [0x269008, 0, 0],
    [0x26900A, 0, 0],
    [0x26900C, 0, 0],
    [0x26900E, 0, 0],
    [0x269010, 0, 0],
    [0x269012, 0, 0],
    [0x269014, 0, 0],
    [0x269016, 0, 0],
    [0x269018, 0, 0],
    [0x26901A, 0, 0],
    [0x26901C, 0, 0],
    [0x26901E, 0, 0]
]

STAGE_FLAGS = {

    0x04: [0x02, 0x00, 0x00, 0x00], # Forest Realm
    0x2F: [0x9E, 0x00, 0x00, 0x00], # Outset Village
    0x29: [0x10, 0x00, 0x00, 0x00], # Castle Town
    0x28: [0x08, 0x00, 0x00, 0x00],  # Hyrule Castle
    0x13: [0xFE, 0x06, 0x00, 0x00],  # Tower of Spirits (Main)
    # 0x14: [0x00, 0x00, 0x00, 0x14], # Tower of Spirits (Base)
    # 0x17: [0x00, 0x00, 0x00, 0x17],  # Tower of Spirits (Stairs)
    0x18: [0x04, 0x00, 0x00, 0x00], # Tunnel to ToS
    0x19: [0x00, 0x00, 0x00, 0x0D],  # Wooded Temple
    # 0x1E: [0x00, 0x00, 0x00, 0x1E], # Stagnox
    0x2A: [0x02, 0x00, 0x00, 0x00],  # Mayscore/Whittleton
    0x30: [0x04, 0x00, 0x00, 0x20],  # Forest Sanctuary
    # 0x38: [0x00, 0x00, 0x00, 0x38],  # Mayscore Forest
    0x3E: [0x00, 0x08, 0x00, 0x00],  # Rabbit Haven
    0x37: [0x86, 0x00, 0x00, 0x00],  # Trading Post
    # 0x05: [0x00, 0x00, 0x00, 0x05], # Snow Realm
    0x2B: [0x02, 0x04, 0x00, 0x00], # Anouki Village
    0x31: [0x02, 0x00, 0x00, 0x00], # Snow Sanctuary
    0x1A: [0x00, 0x40, 0x20, 0x40], # Blizzard Temple
    0x1F: [0x00, 0x00, 0x00, 0xC0], # Fraaz
    0x35: [0x10, 0x00, 0x00, 0x00], # Icy Spring
    # 0x36: [0x00, 0x00, 0x00, 0x36], # Bridge Worker's Home
    0x3F: [0x00, 0xE0, 0x01, 0x00], # Slippery/snowdrift Station
}

STAGES = {
    4: "Forest Realm",
    0x2F: "Outset Village",
    0x29: "Castle Town",
    0x28: "Hyrule Castle",
    0x13: "ToS",
    0x14: "ToS Base",
    0x17: "ToS Stairs",
    0x18: "Tunnel to ToS",
    0x19: "Wooded Temple",
    0x1E: "Stagnox",
    0x2A: "Mayscore",
    0x30: "Forest Sanctuary",
    0x38: "Mayscore Forest",
    0x3E: "Rabbit Haven",
    0x37: "Trading Post",
    5: "Snow Realm",
    0x2B: "Anouki Village",
    0x31: "Snow Sanctuary",
    0x1A: "Blizzard Temple",
    0x1F: "Fraaz",
    0x35: "Icy Spring",
    0x36: "Bridge Worker's Home",
    0x3F: "Snowdrift Station",
    0x3F0A: "Slippery Station",
    6: "Ocean Realm",
    7: "Fire Realm",
    0x79: "ToS Base",
}

ITEM_GROUPS = {
     "Small Keys": [
         "Small Key (Tunnel to ToS)",
         "Small Key (Wooded Temple)",
         "Small Key (ToS)",
         "Small Key (Blizzard Temple)",

         #     "Small Key (Temple of Fire)",
    #     "Small Key (Temple of Fire)",
    #     "Small Key (Temple of Wind)",
    #     "Small Key (Temple of Courage)",
    #     "Small Key (Temple of Ice)",
    #     "Small Key (Mutoh's Temple)"
     ],
    "Boss Keys": [
        "Boss Key (Wooded Temple)",
        "Boss Key (Blizzard Temple)",
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
        "Treasure: Priceless Stone",
        "Treasure: Regal Ring",
    ],
     "Ammo Refills": [
        "Refill: Bombs",
        "Refill: Arrows",
     ]
}

LOCATION_GROUPS = {
    "Forest Realm": [],
    "Outset Village": ["Outset Clear Rocks", "Outset Bee Tree", "Outset Stamp Station", "Outset Far Right Tree", "Outset Niko's House Tree", "Outset Receive Stamp Book"],
    "Castle Town": ["Castle Town Stamp Station", "Castle Town Left Wall Chest", "Castle Town Right Wall Chest", "Castle Town Minigame Roof", "Castle Town Ramp House Chest", "Castle Town Empty House Roof Chest"],
    "Hyrule Castle": ["Hyrule Castle NW Outside Chest", "Hyrule Castle 2F Indoors Chest", "Hyrule Castle 1F Back Chest"],
    "Tunnel to ToS": ["Tunnel to ToS Block Chest", "Tunnel to ToS 2F Chest"],
    "ToS": [
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
        "Wooded Temple Song Statue",
        "Wooded Temple Stamp Station",
        "Wooded Temple 1F Enemy Chest",
        "Wooded Temple 1F Key",
        "Wooded Temple 1F Switch Chest",
        "Wooded Temple 2F Enemy Chest",
        "Wooded Temple 2F Poison Chest",
        "Wooded Temple 3F Chestnut Chest",
        "Wooded Temple 3F SE Chest",
        #"Wooded Temple 3F Boss Key Chest",
        #"Wooded Temple Boss Heart Container",
        "Wooded Temple Dungeon Reward"
    ],
    "Rabbit Haven": ["Rabbit Haven Net Gift", "Rabbit Haven Chest"],
    "Trading Post": ["Trading Post Stamp Station", "Trading Post Chest"],
    "Snow Realm": [],
    "Anouki Village": [],
    "Snow Sanctuary": [],
    "Blizzard Temple": [],
    "Icy Spring": [],
    "Snowdrift Station": [],
    "Slippery Station": [],
    "Bridge Worker's Home": [],
}

DUNGEON_NAMES = [
    "Tunnel to ToS",
    "ToS", #Tower of Spirits
    "Wooded Temple",
    "Blizzard Temple"
]

DUNGEON_TO_BOSS_ITEM_LOCATION = {
    "ToS": "ToS Forest Rail Glyph",
    "Wooded Temple": "Wooded Temple Dungeon Reward",
    "Blizzard Temple": "Blizzard Temple Dungeon Reward",
}


DUNGEON_KEY_DATA = {
    0x13: {
        "name": "ToS",
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
    0x1A: {
        "name": "Blizzard Temple",
        "address": 0x265784,
        "filter": 0x08,
        "value": 0x08,
        "size": 1,
    },
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
