from .Addresses import STAddr

VERSION = "0.3.0"
ROM_HASH = "f2dc6c4e093e4f8c6cbea80e8dbd62cb"


STARTING_FLAGS = [
    # Starting flags (these are in the same memory block so can be simplified, but it's called once and this is
    # easier to bugfix)

    [STAddr.adv_flags_0, 0x04],  # restore spirit train cutscene skip
    [STAddr.adv_flags_1, 0x01],  # forest restoration duet done
    [STAddr.adv_flags_2, 0xF0],  # sword tutorial and intro stuff
    [STAddr.adv_flags_3, 0x47],  # split ToS and zelda 1st convo
    [STAddr.adv_flags_4, 0x34],  # load train to ToS
    [STAddr.adv_flags_5, 0x74],  # train quill tutorial skip
    [STAddr.adv_flags_6, 0xFC],  # Intro stuff
    [STAddr.adv_flags_7, 0x13],  # postman & get zelda's letter
    [STAddr.adv_flags_b, 0x98],  # blizzard stuff
    [STAddr.adv_flags_c, 0xE2],  # convos
    [STAddr.adv_flags_f, 0xC0],  # ToS 4F 1st time entry
    [STAddr.adv_flags_10, 0x50],  # anjean section text
    [STAddr.adv_flags_12, 0x1B],  # zelda 1st phantom possession + mayascore bugs
    [STAddr.adv_flags_15, 0x58],  # post fleeing ToS 1F
    [STAddr.adv_flags_16, 0x08],  # ready for FS duet
    [STAddr.adv_flags_17, 0x40],  # Skip an Anjean dialogue
    [STAddr.adv_flags_18, 0x07],  # HC intro Zelda
    [STAddr.adv_flags_19, 0x01],  # steem
    [STAddr.adv_flags_1b, 0x02],  # initial train cutscene skip
    [STAddr.adv_flags_1a, 0x1C],  # rabbitland rock text
    [STAddr.adv_flags_24, 0x08],  # move HC guards
    [STAddr.adv_flags_2f, 0x40],  # linebeck 1st convo
    [STAddr.adv_flags_37, 0x10],  # teacher text skip
    [STAddr.adv_flags_3d, 0x60],  # ToS safe zone tutorial
    [STAddr.adv_flags_40, 0x04],  # 1st portal text
    [STAddr.adv_flags_42, 0x80],  # board with zelda
    [STAddr.adv_flags_48, 0x10],  # alfonzo giving cannon
    [STAddr.adv_flags_4e, 0x80],  # blizzard void out
    [STAddr.adv_flags_52, 0x80],  # ToS Staircase cutscene skip
    [STAddr.adv_flags_53, 0x01],  # ToS Staircase 2 zelda text skip
    [STAddr.adv_flags_54, 0x28],  # first spirit train journey+portal
    [STAddr.adv_flags_57, 0x40],  # first song statue text

    # Set treasures to 0
    [STAddr.all_treasure_count, [0]*32],
]

# You can find the stage flags for a stage by checking the stage data pointer of 0x265164 and adding an offset of 176 (note decimal) to its value
# then endian is opposite of what it usually is cause i like to use spreadsheets to import it.
# check the stage flag page in the spreadsheet to see what each bit corresponds to.
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
    0x30: [0x0C, 0x00, 0x00, 0x20],  # Forest Sanctuary
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
    0x3F: [0x50, 0xE0, 0x01, 0x00], # Slippery/snowdrift Station
}

STAGES = {
    0x4: "Forest Realm",
    0x5: "Snow Realm",
    0x6: "Ocean Realm",
    0x7: "Fire Realm",
    0x8: "Train Tutorial",
    # 0xb: "SR Roktite Tunnel",
    0xF: "Dark Realm",
    0x10: "Demon Train",
    0x11: "Demon Train P2",
    0x12: "Demon Train P3",
    0x13: "ToS",
    0x14: "ToS Base",
    0x17: "ToS Stairs",
    0x18: "Tunnel to ToS",
    0x19: "Wooded Temple",
    0x1A: "Blizzard Temple",
    0x1E: "Stagnox",
    0x1F: "Fraaz",
    0x24: "Cole Fight",
    0x25: "Malladus 1",
    0x26: "Malladus Spirit Duet",
    0x27: "Malladus P2",
    0x28: "Hyrule Castle",
    0x29: "Castle Town",
    0x2A: "Mayscore",
    0x2B: "Anouki Village",
    0x2F: "Outset Village",
    0x30: "Forest Sanctuary",
    0x31: "Snow Sanctuary",
    0x35: "Icy Spring",
    0x36: "Bridge Worker's Home",
    0x37: "Trading Post",
    0x38: "Mayscore Forest",
    0x3E: "Rabbit Haven",
    0x3F: "Snowdrift/Slippery Station",
    # 0x44: "Train Interior CS",
    # 0x50: "Train roof CS",
    0x79: "From Menu",
}

ITEM_GROUPS = {
     "Rupees": [
        "Green Rupee (1)",
        "Blue Rupee (5)",
        "Red Rupee (20)",
        "Big Green Rupee (100)",
        "Big Red Rupee (200)",
        "Gold Rupee (300)",
        "Pre-Alpha Rupee (5000)"
     ],
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
        "Treasure: Palace Dish",
        "Treasure: Goron Amber",
        "Treasure: Mystic Jade",
        "Treasure: Ancient Coin",
    ],
    "Super Rare Treasures": [
        "Treasure: Priceless Stone",
        "Treasure: Regal Ring",
    ],
     "Ammo Refills": [
        "Refill: Bombs",
        "Refill: Arrows",
     ],
    "Forest Rabbits": [
        "Forest Rabbit",
        "Forest Rabbits (2)",
        "Forest Rabbits (3)",
        "Forest Rabbits (4)",
        "Forest Rabbits (5)",
        "Forest Rabbits (10)"
    ],
    "Snow Rabbits": [
        "Snow Rabbit",
        "Snow Rabbits (2)",
        "Snow Rabbits (3)",
        "Snow Rabbits (4)",
        "Snow Rabbits (5)",
        "Snow Rabbits (10)"
    ],
    "Glyphs": [
        "Forest Glyph",
        "Snow Glyph",
        "Ocean Glyph"
    ],
    "Forest Tracks": [
        "Forest Realm Ocean Shortcut Tracks",
        "E Mayscore Bridge Tracks",
        "Forest Realm SE Portal Tracks",
        "W Castle Town Tracks",
        "W Forest Realm Tracks",
        "Forest Realm SW Cave Tracks",
        "W Wooded Temple Tracks",
        "N Castle Town Tracks",
        "Wooded Temple Tracks"
    ],
    "Snow Tracks": [
        "Snowdrift Station Tracks",
        "Slippery Station Tracks",
        "Snow Realm Bridge Tracks",
        "N Icy Spring Tracks",
        "Blizzard Temple Tracks"
    ],
    "Portal Unlocks": [
        "Portal Unlock: Hyrule Castle to Anouki Village",
        "Portal Unlock: Trading Post to E Snow Realm"
    ]
}

# Combo groups
ITEM_GROUPS |= {
    "All Treasures": ITEM_GROUPS["Common Treasures"] + ITEM_GROUPS["Uncommon Treasures"] +
                    ITEM_GROUPS["Rare Treasures"] + ITEM_GROUPS["Super Rare Treasures"],
    "Rabbits": ITEM_GROUPS["Forest Rabbits"] + ITEM_GROUPS["Snow Rabbits"],
    "All Tracks": ITEM_GROUPS["Forest Tracks"] + ITEM_GROUPS["Snow Tracks"]
}

# RABBITS = {
#     "Forest Rabbits": [0x262030, 0xFF, 0x262031, 0x03],
#     "Snow Rabbits": [0x262031, 0xFC, 0x262032, 0x0F],
#     # "Water Rabbits": [0x262032, 0xF0, 0x262033, 0x3F],
#     # "Fire Rabbits": [0x262033, 0xC0, 0x262034, 0xFF],
#     # "Sand Rabbits": [0x262034, 0xFF, 0x262035, 0x03],
# }

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

    "Unique Forest Rabbits": [],
    "Unique Snow Rabbits": []
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

BOSS_LOCATION_TO_EVENT_REGION = {
    "Wooded Temple Dungeon Reward": "wt stagnox",
    "Blizzard Temple Dungeon Reward": "bt fraaz",
    "ToS 3F Forest Rail Glyph": "tos 3f rail map",
    "ToS 7F Snow Rail Glyph": "tos 7f rail map"
}

DUNGEON_KEY_DATA = {
    0x13: {
        "name": "ToS",
        "address": STAddr.key_storage_tos,
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
        "address": STAddr.key_storage_0,
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
        "address": STAddr.key_storage_0,
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
        "address": STAddr.key_storage_0,
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

# Used by rule builder
ITEM_MAPPING = {
        i: "Rupees" for i in ITEM_GROUPS["Rupees"]
    } | {
        f"Forest Rabbits ({i})": "Forest Rabbit" for i in list(range(2, 6)) + [10]
    } | {
        f"Snow Rabbits ({i})": "Snow Rabbit" for i in list(range(2, 6)) + [10]}

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

UT_EVENT_DATA = {
    0x2900: {"address": STAddr.adv_flags_11,
           "value": 0x40,
           "entrance": "EVENT: Pick up Alfonzo"}
}

#TREASURE_READ_LIST = {i: (0x1BA5AC + i * 4, 4, "Main RAM") for i in range(8)}
