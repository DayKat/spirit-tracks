from .Addresses import STAddr
from .Items import ITEM_GROUPS

VERSION = "0.3.0"
ROM_HASH = "f2dc6c4e093e4f8c6cbea80e8dbd62cb"


STARTING_FLAGS = [
    # Starting flags (these are in the same memory block so can be simplified, but it's called once and this is
    # easier to bugfix)

    [STAddr.adv_flags_0, 0x04],  # restore spirit train cutscene skip
    [STAddr.adv_flags_1, 0x00],  # forest restoration duet done
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
    [STAddr.adv_flags_13, 0x08],  # whip minigame tutorial
    [STAddr.adv_flags_15, 0x58],  # post fleeing ToS 1F
    [STAddr.adv_flags_16, 0x38],  # ready for FS duet
    [STAddr.adv_flags_17, 0xCA],  # Skip an Anjean dialogue
    [STAddr.adv_flags_18, 0x07],  # HC intro Zelda
    [STAddr.adv_flags_19, 0x63],  # steem
    [STAddr.adv_flags_1a, 0x1C],  # rabbitland rock text
    [STAddr.adv_flags_1b, 0xE2],  # initial train cutscene skip, tos 3 zelda text
    [STAddr.adv_flags_1c, 0x25],  # ToS 3 zelda text
    [STAddr.adv_flags_1d, 0xF4],  # ToS 3 zelda text
    [STAddr.adv_flags_24, 0x40],  # teao tutorial
    [STAddr.adv_flags_24, 0x08],  # move HC guards
    [STAddr.adv_flags_2a, 0x02],  # ToS 6 zelda text
    [STAddr.adv_flags_2b, 0x01],  # ToS 7 zelda text
    [STAddr.adv_flags_2f, 0x40],  # linebeck 1st convo
    [STAddr.adv_flags_37, 0x10],  # teacher text skip
    [STAddr.adv_flags_3d, 0x60],  # ToS safe zone tutorial
    [STAddr.adv_flags_40, 0x04],  # 1st portal text
    [STAddr.adv_flags_41, 0x03],  # ToS 6 Zelda Text
    [STAddr.adv_flags_42, 0x86],  # board with zelda
    [STAddr.adv_flags_46, 0x20],  # 7f zelda collapse
    [STAddr.adv_flags_48, 0x10],  # alfonzo giving cannon
    [STAddr.adv_flags_4e, 0x80],  # blizzard void out
    [STAddr.adv_flags_51, 0x03],  # ToS Staircase cutscene skip
    [STAddr.adv_flags_52, 0x80],  # ToS Staircase cutscene skip
    [STAddr.adv_flags_53, 0x77],  # ToS Staircase 2 zelda text skip
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
    0x28: [0x08, 0x01, 0x00, 0x00],  # Hyrule Castle
    0x13: [0xFE, 0x06, 0x00, 0x00],  # Tower of Spirits (Main)
    # 0x14: [0x00, 0x00, 0x00, 0x14], # Tower of Spirits (Base)
    # 0x17: [0x00, 0x00, 0x00, 0x17],  # Tower of Spirits (Stairs)
    0x18: [0x04, 0x00, 0x00, 0x00], # Tunnel to ToS
    0x19: [0x00, 0x00, 0x00, 0x0D],  # Wooded Temple
    # 0x1E: [0x00, 0x00, 0x00, 0x1E], # Stagnox
    0x2A: [0x02, 0x00, 0x00, 0x00],  # Mayscore/Whittleton
    0x30: [0x3C, 0x00, 0x00, 0x20],  # Forest Sanctuary
    # 0x38: [0x00, 0x00, 0x00, 0x38],  # Mayscore Forest
    0x3E: [0x00, 0x08, 0x00, 0x00],  # Rabbit Haven
    0x37: [0x86, 0x00, 0x00, 0x00],  # Trading Post
    # 0x05: [0x00, 0x00, 0x00, 0x05], # Snow Realm
    0x2B: [0x02, 0x04, 0x00, 0x00], # Anouki Village
    0x31: [0x0A, 0x00, 0x00, 0x00], # Snow Sanctuary
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
    0xb: "SR Rocktite Tunnel",
    0xF: "Dark Realm",
    0x10: "Demon Train",
    0x11: "Demon Train P2",
    0x12: "Demon Train P3",
    0x13: "ToS",
    0x14: "ToS Base",
    0x15: "ToS Summit",
    0x17: "ToS Stairs",
    0x18: "Tunnel to ToS",
    0x19: "Wooded Temple",
    0x1A: "Blizzard Temple",
    0x1E: "Stagnox",
    0x1F: "Fraaz",
    0x23: "Staven Fight",
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
    0x45: "Beedle, Train NPCs",
    0x46: "Take 'em all on Forest theme",
    0x47: "Take 'em all on Snow theme",
    0x48: "Take 'em all on Ocean theme",
    0x49: "Take 'em all on Fire theme",
    0x4A: "Take 'em all on Sand theme",
    0x4B: "TEAO Stagnox",
    0x4C: "TEAO Fraaz",
    0x4D: "TEAO Cactops",
    0x4E: "TEAO Vulcano",
    0x4F: "TEAO Capbone",
    0x79: "From Menu",
}

# ITEM_GROUPS = {
    #  "Small Rupees": [
    #      "Green Rupee (1)",
    #      "Blue Rupee (5)",
    #      "Red Rupee (20)",
    #  ],
    # "Big Rupees": [
    #     "Big Green Rupee (100)",
    #     "Big Red Rupee (200)",
    #     "Gold Rupee (300)",
    #     "Pre-Alpha Rupee (5000)"
    # ],
    #  "Small Keys": [
    #      "Small Key (Tunnel to ToS)",
    #      "Small Key (Wooded Temple)",
    #      "Small Key (ToS)",
    #      "Small Key (Blizzard Temple)",
    #  ],
    # "Boss Keys": [
    #     "Boss Key (Wooded Temple)",
    #     "Boss Key (Blizzard Temple)",
    # ],
    # "Common Treasures": [
    #     "Treasure: Demon Fossil",
    #     "Treasure: Stalfos Skull",
    #     "Treasure: Star Fragment",
    #     "Treasure: Bee Larvae",
    #     "Treasure: Wood Heart",
    # ],
    # "Uncommon Treasures": [
    #     "Treasure: Dark Pearl Loop",
    #     "Treasure: White Pearl Loop",
    #     "Treasure: Ruto Crown",
    #     "Treasure: Dragon Scale",
    #     "Treasure: Pirate's Necklace",
    # ],
    # "Rare Treasures": [
    #     "Treasure: Palace Dish",
    #     "Treasure: Goron Amber",
    #     "Treasure: Mystic Jade",
    #     "Treasure: Ancient Coin",
    # ],
    # "Super Rare Treasures": [
    #     "Treasure: Priceless Stone",
    #     "Treasure: Regal Ring",
    # ],
    #  "Ammo Refills": [
    #     "Refill: Bombs",
    #     "Refill: Arrows",
    #  ],
    # "Grass Rabbits": [
    #     "Grass Rabbit",
    #     "Grass Rabbits (2)",
    #     "Grass Rabbits (3)",
    #     "Grass Rabbits (4)",
    #     "Grass Rabbits (5)",
    #     "Grass Rabbits (10)"
    # ],
    # "Snow Rabbits": [
    #     "Snow Rabbit",
    #     "Snow Rabbits (2)",
    #     "Snow Rabbits (3)",
    #     "Snow Rabbits (4)",
    #     "Snow Rabbits (5)",
    #     "Snow Rabbits (10)"
    # ],
    # "Glyphs": [
    #     "Forest Glyph",
    #     "Snow Glyph",
    #     "Ocean Glyph"
    # ],
    # "Forest Tracks": [
    #     "Forest Realm Ocean Shortcut Tracks",
    #     "E Mayscore Bridge Tracks",
    #     "Forest Realm SE Portal Tracks",
    #     "W Castle Town Tracks",
    #     "W Forest Realm Tracks",
    #     "Forest Realm SW Cave Tracks",
    #     "W Wooded Temple Tracks",
    #     "N Castle Town Tracks",
    #     "Wooded Temple Tracks"
    # ],
    # "Snow Tracks": [
    #     "Snowdrift Station Tracks",
    #     "Slippery Station Tracks",
    #     "Snow Realm Bridge Tracks",
    #     "N Icy Spring Tracks",
    #     "Blizzard Temple Tracks"
    # ],
    # "Portal Unlocks": [
    #     "Portal Unlock: Hyrule Castle to Anouki Village",
    #     "Portal Unlock: Trading Post to E Snow Realm"
    # ],
    # "Tears of Light": [
    #     "Tear of Light",
    #     "Tear of Light (ToS 1)",
    #     "Tear of Light (ToS 2)",
    #     "Tear of Light (ToS 3)",
    #     "Tear of Light (ToS 4)",
    #     "Tear of Light (ToS 5)",
    #     "Tear of Light (All Sections)",
    #     "Tear of Light (Progressive)",
    #     "Big Tear of Light (ToS 1)",
    #     "Big Tear of Light (ToS 2)",
    #     "Big Tear of Light (ToS 3)",
    #     "Big Tear of Light (ToS 4)",
    #     "Big Tear of Light (ToS 5)",
    #     "Big Tear of Light (All Sections)",
    #     "Big Tear of Light (Progressive)",
    # ]
# }

# Combo groups
# ITEM_GROUPS |= {
#     "All Treasures": ITEM_GROUPS["Common Treasures"] + ITEM_GROUPS["Uncommon Treasures"] +
#                     ITEM_GROUPS["Rare Treasures"] + ITEM_GROUPS["Super Rare Treasures"],
#     "Rabbits": ITEM_GROUPS["Grass Rabbits"] + ITEM_GROUPS["Snow Rabbits"],
#     "All Tracks": ITEM_GROUPS["Forest Tracks"] + ITEM_GROUPS["Snow Tracks"]
# }
# ITEM_GROUPS["Rupee Items"] = ITEM_GROUPS["Small Rupees"] + ITEM_GROUPS["Big Rupees"]
# ITEM_GROUPS["Uncommon Plus Treasure"] = ITEM_GROUPS["Uncommon Treasures"] + ITEM_GROUPS["Rare Treasures"] + ITEM_GROUPS["Super Rare Treasures"]


TREASURE_PRICES = {t: value for treasure_type, value in zip(["Common", "Uncommon", "Rare", "Super Rare"], [50, 150, 500, 2500]) for t in ITEM_GROUPS[treasure_type + " Treasures"]}

LOCATION_GROUPS: dict[str, set[str]] = {}

grass_rabbits = [
    "Grass Rabbit",
    "Grass Rabbits (2)",
    "Grass Rabbits (3)",
    "Grass Rabbits (4)",
    "Grass Rabbits (5)",
    "Grass Rabbits (10)"
]
snow_rabbits = [
    "Snow Rabbit",
    "Snow Rabbits (2)",
    "Snow Rabbits (3)",
    "Snow Rabbits (4)",
    "Snow Rabbits (5)",
    "Snow Rabbits (10)"
],

DUNGEON_NAMES = [
    "Tunnel to ToS",
    "ToS", #Tower of Spirits
    "Wooded Temple",
    "Blizzard Temple"
]

DUNGEON_TO_BOSS_ITEM_LOCATION = {
    "ToS 1": "ToS 3F Forest Rail Glyph",
    "ToS 2": "ToS 7F Snow Rail Glyph",
    "ToS 3": "ToS 12F Ocean Rail Glyph",
    "ToS 4": "ToS 17F Fire Rail Glyph",
    "ToS 5": "ToS 23F Defeat Staven",
    "ToS 6": "ToS 24F Final Chest",
    "Wooded Temple": "Wooded Temple Dungeon Reward",
    "Blizzard Temple": "Blizzard Temple Dungeon Reward",
}

BOSS_LOCATION_TO_EVENT_REGION = {
    "Wooded Temple Dungeon Reward": "wt stagnox",
    "Blizzard Temple Dungeon Reward": "bt fraaz",
    "ToS 3F Forest Rail Glyph": "tos 3f rail map",
    "ToS 7F Snow Rail Glyph": "tos 7f rail map",
    "ToS 12F Ocean Rail Glyph": "tos 11f",
    "ToS 17F Fire Rail Glyph": "tos 16f",
    "ToS 23F Defeat Staven": "tos staven",
    "ToS 24F Final Chest": "tos 24f"
}

DUNGEON_KEY_DATA = {
    0x13: {
        "name": "ToS",
        "address": STAddr.key_storage_tos,
        "filter": 0xFF,
        "value": 1,
        "size": 8,
    },
    0x132: {
        "name": "ToS 2",
        "address": STAddr.key_storage_tos,
        "filter": 0x3,
        "value": 1,
        "size": 2,
    },
    0x134: {
        "name": "ToS 4",
        "address": STAddr.key_storage_tos,
        "filter": 0xC,
        "value": 4,
        "size": 2,
    },
    0x135: {
        "name": "ToS 5",
        "address": STAddr.key_storage_tos,
        "filter": 0x30,
        "value": 0x10,
        "size": 2,
    },
    0x136: {
        "name": "ToS 6",
        "address": STAddr.key_storage_tos,
        "filter": 0xC0,
        "value": 0x40,
        "size": 2,
    },
    0x18: {
        "name": "Tunnel to ToS",
        "address": STAddr.key_storage_0,
        "filter": 0x01,
        "value": 1,
        "size": 1,
    },
    0x19: {
        "name": "Wooded Temple",
        "address": STAddr.key_storage_0,
        "filter": 0x06,
        "value": 0x02,
        "size": 2,
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

SHOP_TREASURE_DATA = {
    0x290a: [{
        "locations": ["Castle Town Shop Treasure 1", "Castle Town Shop Treasure 2"],
        "group": "Uncommon"
    }],
    0x2a05: [{
        "locations": ["Mayscore Shop Treasure 1", "Mayscore Shop Treasure 2"],
        "group": "Common"
    }],
    0x4503: [{
        "locations": ["Beedle Buy Uncommon Treasure"],
        "group": "Uncommon"
    }, {
        "locations": ["Beedle Buy Rare Treasure"],
        "group": "Rare"
    }],
}



tear_lookup = {1: 3, 4: 6, 9: 9, 13: 12, 18: 15, 30: 16}
big_tear_lookup = {1:1, 4:2, 9: 3, 13: 4, 18: 5, 30: 6}

DUNGEON_STAGES_TO_ENTRANCE_SCENE = {
    0x13: 0x1401,
    0x15: 0x1401,
    0x17: 0x1401,
    0x23: 0x1401,
    0x1A: 0x1A00,
    0x19: 0x1900,
    0x1E: 0x1900,
    0x1F: 0x1A00
}

# Used by rule builder
ITEM_MAPPING = {
        i: "Rupees" for i in ITEM_GROUPS["Rupee Items"]
    } | {
        f"Grass Rabbits ({i})": "Grass Rabbit" for i in list(range(2, 6)) + [10]
    } | {
        f"Snow Rabbits ({i})": "Snow Rabbit" for i in list(range(2, 6)) + [10]
    } | {
        t : "Treasure" for t in ITEM_GROUPS["All Treasures"]
    }

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
    0x2900: [{"address": STAddr.adv_flags_11,
           "value": 0x40,
           "entrance": "EVENT: Pick up Alfonzo"}],
    0x3700: [{"address": STAddr.adv_flags_24,
              "value": 0x10,
              "entrance": "EVENT: Give Regal Ring to Linebeck"}]
}

ENTRANCE_TO_TOS_ORDER = {
"Tower of Spirits Exit Staven": 6,
"Tower of Spirits Summit Enter Altar": 7,
"Tower of Spirits Enter Section 1": 1,
"Tower of Spirits Enter Section 2": 2,
"Tower of Spirits Enter Section 3": 3,
"Tower of Spirits Enter Section 4": 4,
"Tower of Spirits Enter Section 5": 5,
}

EXIT_TO_TOS_SECTION = {
    "ToS 30F Exit": 6,
    "ToS 18F Exit": 5,
    "ToS 13F Exit": 4,
    "ToS 8F Exit": 3,
    "ToS 4F Exit": 2,
    "ToS 1F Exit": 1,
}

BOSS_WARP_SCENE_LOOKUP = {
    0x1302: "ToS 1F Exit",
    0x1306: "ToS 4F Exit",
    0x130b: "ToS 8F Exit",
    0x130f: "ToS 13F Exit",
    0x1314: "ToS 18F Exit",
    0x1323: "ToS 30F Exit",
}

TOS_FLOOR_TO_SECTION = {
    0: 1,
    1: 1,
    2: 1,
    3: 2,
    4: 2,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 3,
    0xA: 3,
    0xB: 3,
    0xC: 4,
    0xD: 4,
    0xE: 4,
    0xF: 4,
    0x10: 4,
    0x11: 5,
    0x12: 5,
    0x13: 5,
    0x14: 5,  # 23F
    0x17: 5,  # 21F
    0x18: 5,  # 22F

    0x15: 3,
    0x16: 3,

    0x28: 1,
    0x29: 2,
    0x2A: 3,
    0x2B: 4,
    0x2C: 6,
    0x2D: 6,

    0x1d: 6,  # 31F
    0x1e: 6,  # 30F
    0x1f: 6,  # 29F
    0x20: 6,  # 28F
    0x21: 6,  # 27F
    0x22: 6,  # 26F
    0x23: 6,  # 24F
    0x24: 6,  # 25F
}

#TREASURE_READ_LIST = {i: (0x1BA5AC + i * 4, 4, "Main RAM") for i in range(8)}
