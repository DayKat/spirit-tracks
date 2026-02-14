
from .Constants import ITEM_GROUPS, LOCATION_GROUPS
from .Addresses import STAddr

# TODO: Add sram data for saveslot 2
# TODO: Add the rest of sram data in bulk

LOCATIONS_DATA = {

    #Outset Village
    "Outset Clear Rocks": {
        "region_id": "outset village",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x2F,
        "room_id": 0,
        "address": STAddr.adv_flags_2f,
        "value": 0x20,
    },
    "Outset Bee Tree": {
        "region_id": "outset village",
        "vanilla_item": ITEM_GROUPS["Common Treasures"], #TODO check removal of treasure
        "stage_id": 0x2F,
        "room_id": 0,
        "x_min": 34192,
        "x_max": 52960,
        "z_min": -34890,
        "z_max": -10024,
    }, #TODO make location trigger on actual stamping
    "Outset Stamp Station": {
        "region_id": "outset village stamp station",
        #"vanilla_item": "Outset Village Stamp",
        "vanilla_item": "Treasure",
        "stage_id": 0x2F,
        "room_id": 0,
        "stamp": True,
        "require_item": ["Stamp Book"],
        # 02271CD8 is array of stamp IDs
        # 02271CF4 is bitfield of all stamps found
    },
    "Outset Far Right Tree": {
        "region_id": "outset village trees",
        "vanilla_item": ITEM_GROUPS["Uncommon Treasures"],
        "stage_id": 0x2F,
        "room_id": 0,
        "x_min": 27449,
        "x_max": 43663,
        "z_min": 11490,
        "z_max": 33968,
    },
    "Outset Niko's House Tree": {
        "region_id": "outset village trees",
        "vanilla_item": ITEM_GROUPS["Uncommon Treasures"],
        "stage_id": 0x2F,
        "room_id": 0,
        "x_min": -60427,
        "x_max": -41317,
        "z_min": 10523,
        "z_max": 28762,
    },
    "Outset Receive Stamp Book": { # TODO: if using address read it triggers if you receive stamp book at start
        "region_id": "outset village stamp book",
        "vanilla_item": "Stamp Book",
        "stage_id": 0x2F,
        "room_id": 0x0A,
        "address": STAddr.adv_flags_25,
        "value": 0x2,
        "x_min": -9816,
        "x_max": 12156,
        "z_min": -22938,
        "z_max": 2247,
    },

    # Castle Town
    "Castle Town Stamp Station": {
        "region_id": "castle town stamp station",
        "vanilla_item": "Treasure",
        #"vanilla_item": "Castle Town Stamp",
        "stage_id": 0x29,
        "room_id": 0,
        "stamp": True,
        "require_item": ["Stamp Book", "Bombs (Progressive)"],
        "item_override": "Song of Birds"
    },
    "Castle Town Left Wall Chest": {
        "region_id": "castle town wall",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x29,
        "room_id": 0,
        "x_min": -48215,
        "x_max": -34406,
        "z_min": 46694,
        "z_max": 59802,
        "require_item": ["Bombs (Progressive)"],
        "item_override": "Whip"
    },
    "Castle Town Right Wall Chest": {
        "region_id": "castle town wall",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x29,
        "room_id": 0,
        "x_min": 34406,
        "x_max": 49328,
        "z_min": 46694,
        "z_max": 59802,
        "require_item": ["Bombs (Progressive)"],
        "item_override": "Spirit Flute"
    },
    "Castle Town Minigame Roof": {
        "region_id": "castle town cuccos",
        "vanilla_item": ITEM_GROUPS["Uncommon Treasures"],
        "stage_id": 0x29,
        "room_id": 0,
        "x_min": 69100,
        "x_max": 74138,
        "z_min": 13914,
        "z_max": 24835,
    },
    "Castle Town Ramp House Chest": {
        "region_id": "castle town cuccos",
        "vanilla_item": ITEM_GROUPS["Common Treasures"],
        "stage_id": 0x29,
        "room_id": 0,
        "x_min": -76411,
        "x_max": -66503,
        "z_min": 18672,
        "z_max": 28116,
        "require_item": ["Bombs (Progressive)", "Song of Birds" "Spirit Flute"],
        "item_override": "Sword (Progressive)"
    },
    "Castle Town Empty House Roof Chest": {
        "region_id": "castle town cuccos",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "stage_id": 0x29,
        "room_id": 0,
        "x_min": -43484,
        "x_max": -32916,
        "z_min": -43563,
        "z_max": -33114,
    },

    # Hyrule Castle
    "Hyrule Castle NW Outside Chest": {
        "region_id": "hyrule castle nw chest",
        "vanilla_item": ITEM_GROUPS["Common Treasures"],
        "stage_id": 0x28,
        "room_id": 0,
        "entrance_id": 6,
        "y": 9830,
        "x_max": -70000,
        "item_override": "Bow (Progressive)"
    },
    "Hyrule Castle 2F Indoors Chest": {
        "region_id": "hyrule castle 2f indoors chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x28,
        "room_id": 2,
    },
    "Hyrule Castle 1F Back Chest": {
        "region_id": "hyrule castle 1f back chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x28,
        "room_id": 1,
        "entrance_id": 7,
        "x_min": 20640,
        "x_max": 40000,
        "z_min": -55000,
        "z_max": -35000,
        "item_override": "Sand Wand"
    },
    # "Hyrule Castle Sword Training Minigame": {
    #     "region_id": "hyrule castle sword training",
    #     "vanilla_item": "Red Rupee (20)",
    #     "stage_id": 0x28,
    #     "room_id": 0,
    # }, TODO check flags

    # Tunnel to Tower
    "Tunnel to ToS Block Chest": {
        "region_id": "tower tunnel block chest",
        "vanilla_item": "Small Key (Tunnel to ToS)",
        "stage_id": 0x18,
        "room_id": 0,
        'dungeon': "Tunnel to ToS",
    },
    "Tunnel to ToS 2F Chest": {
        "region_id": "tower tunnel 2f chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x18,
        "room_id": 1,
        'dungeon': "Tunnel to ToS"
    },

    # # ========== Tower of Spirits ==============

    "Tear 1F Top":{
        "region_id": "tear 1f top",
        "vanilla_item": "Tear of Light",
        "stage_id": 0x13,
        "room_id": 0,
        "x_min": -6554,
        "x_max": 6554,
        "z_min": -72090,
        "z_max": -59101,
        'dungeon': "ToS",
        "conditional": True,
        "item_override": "Tear of Light",
        "delay_pickup": "ToS 1F Chest"
    },
    "ToS 1F Chest": {
        "region_id": "tos 1f chest",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "item_override": "Bombs (Progressive)",
        "stage_id": 0x13,
        "room_id": 0,
        "x_min": -6554,
        "x_max": 6554,
        "z_min": -72090,
        "z_max": -59101,
        'dungeon': "ToS",
        "delay_pickup": "Tear 1F Top"
        #'set_bit': [(0x265715, 0x80)]
    },
    "ToS 2F Raised Chest": {
        "region_id": "tos 2f raised chests",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "item_override": "Cannon",
        "stage_id": 0x13,
        "room_id": 1,
        "x_min": -5786,
        "x_max": 10650,
        "z_min": -39322,
        "z_max": -29710,
        'dungeon': "ToS",
        #'set_bit': [(0x265715, 0x80)]
    },
    "ToS 2F Whirlwind Chest": {
        "region_id": "tos 2f raised chests",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "stage_id": 0x13,
        "room_id": 1,
        "x_min": 21028,
        "x_max": 40042,
        "z_min": -63898,
        "z_max": -54886,
        'dungeon': "ToS",
    },
    "ToS 2F Bomb Wall Chest": {
        "region_id": "tos 2f bomb wall",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "stage_id": 0x13,
        "room_id": 0x28,
        "x_min": -14760,
        "x_max": 14760,
        "z_min": -18842,
        "z_max": 10650,
        'dungeon': "ToS",
    },
    "ToS 3F Forest Rail Glyph": {
        "region_id": "tos 3f rail map",
        "vanilla_item": "Forest Glyph",
        "stage_id": 0x13,
        "room_id": 2,
        "goal": True,
        "x_min": -6390,
        "x_max": 6390,
        "z_min": -8438,
        "z_max": 4506,
        'dungeon': "ToS",
        "require_item": ["Sword (Progressive)"],
        "ut_connect": "EVENT: Reach ToS 3F",
        #'set_bit': [(0x265715, 0x80)]
    },
    "ToS 4F Central Chest": {
        "region_id": "tos 4f",
        "vanilla_item": ITEM_GROUPS["Common Treasures"],
        "stage_id": 0x13,
        "room_id": 3,
        "x_min": -8703,
        "x_max": 6560,
        "z_min": 1600,
        "z_max": 10670,
        'dungeon': "ToS",
    },
    "ToS 4F NE Chest": {
        "region_id": "tos 4f ne chest",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "stage_id": 0x13,
        "room_id": 3,
        "entrance_id": 2,
        "x_min": 38520,
        "x_max": 51177,
        "z_min": -55720,
        "z_max": -42600,
        'dungeon': "ToS",
    },
    "ToS 5F Island Chest": {
        "region_id": "tos 5f island chest",
        "vanilla_item": "Big Green Rupee (100)",
        "stage_id": 0x13,
        "room_id": 4,
        "x_min": -35240,
        "x_max": -22990,
        "z_min": 42350,
        "z_max": 52230,
        'dungeon': "ToS",
    },
    "ToS 5F Spinnit Key": {
        "region_id": "tos 5f spinnit key",
        "vanilla_item": "Small Key (ToS)",
        "stage_id": 0x13,
        "room_id": 4,
        "x_max": -45000,
        "z_min": 0,
        'dungeon': "ToS",
    },
    "ToS 5F Bomb Wall Chest": {
        "region_id": "tos 5f secret chest",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "stage_id": 0x13,
        "room_id": 0x29,
        "x_min": -8965,
        "x_max": 9061,
        "z_min": -17693,
        "z_max": 8481,
        'dungeon': "ToS",
    },
    "ToS 6F Enemy Chest 1": {
        "region_id": "tos 6f chests",
        "vanilla_item": ITEM_GROUPS["Common Treasures"],
        "stage_id": 0x13,
        "room_id": 5,
        "entrance_id": 2,
        "x_min": 34420,
        "x_max": 48753,
        "z_min": -10660,
        "z_max": -4354,
        "delay_pickup": ["ToS 6F Enemy Big Chest"],
        'dungeon': "ToS",
    },
    "ToS 6F Enemy Chest 2": {
        "region_id": "tos 6f chests",
        "vanilla_item": ITEM_GROUPS["Common Treasures"],
        "stage_id": 0x13,
        "room_id": 5,
        "entrance_id": 2,
        "x_min": 60910,
        "x_max": 80112,
        "z_min": -4151,
        "z_max": 6570,
        'dungeon': "ToS",
    },
    "ToS 6F Enemy Chest 3": {
        "region_id": "tos 6f chests",
        "vanilla_item": ITEM_GROUPS["Common Treasures"],
        "stage_id": 0x13,
        "room_id": 5,
        "entrance_id": 2,
        "x_min": 63492,
        "x_max": 80310,
        "z_min": -10660,
        "z_max": -4152,
        'dungeon': "ToS",
    },
    "ToS 6F Enemy Big Chest": {
        "region_id": "tos 6f chests",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "item_override": "Refill: Arrows",
        "stage_id": 0x13,
        "room_id": 5,
        "entrance_id": 2,
        "x_min": 41795,
        "x_max": 57985,
        "z_min": -10660,
        "z_max": 6560,
        "delay_pickup": ["ToS 6F Enemy Chest 1"],
        'dungeon': "ToS",
    },
    "ToS 6F Key": {
        "region_id": "tos 6f key",
        "vanilla_item": "Small Key (ToS)",
        "stage_id": 0x13,
        "room_id": 5,
        "x_min": 46710,
        "x_max": 80290,
        "z_min": 26220,
        "z_max": 68000,
        'dungeon': "ToS",
        # "require_item": ["Sword (Progressive)", "Whirlwind", "Forest Source"]
    },
    "ToS 7F Snow Rail Glyph": {
        "region_id": "tos 7f rail map",
        "vanilla_item": "Snow Glyph",
        "stage_id": 0x13,
        "room_id": 6,
        "x_min": -6400,
        "x_max": 6400,
        "z_min": -8450,
        "z_max": 4515,
        'dungeon': "ToS",
        "require_item": ["Sword (Progressive)", "Whirlwind", "Forest Source"],
        "goal": True,
        "ut_connect": "EVENT: Reach ToS 7F"
    },

    # =============================================

    # Mayscore
    "Mayscore Stamp Station": {
        "region_id": "mayscore stamp station",
        #"vanilla_item": "Mayscore Stamp",
        "stage_id": 0x38,
        "room_id": 0,
        "stamp": True,
        "require_item": ["Stamp Book"],
        "vanilla_item": "Treasure"
    },
    # "Mayscore Whip Race 1st Reward": { TODO make minigame option & find win address
    #     "region_id": "mayscore whip race bomb bag",
    #     "vanilla_item": "Bombs (Progressive)",
    #     "minigame": True,
    #     "stage_id": 0x38,
    #     "room_id": 0,
    #     "entrance_id": 2,
    #     "require_item": ["Whip"],
    #     "item_override": "Refill: Arrows"
    #},
    # "Mayscore Whip Race 2nd Reward": {
    #     "region_id": "mayscore whip race heart container",
    #     "vanilla_item": "Heart Container",
    #     "minigame": True,
    #     "stage_id": 0x38,
    #     "room_id": 0,
    #     "entrance_id": 2,
    #     "require_item": ["Whip"],
    # },
    "Mayscore Whip Chest": {
        "region_id": "mayscore whip chest",
        "vanilla_item": ITEM_GROUPS["Uncommon Treasures"],
        "stage_id": 0x38,
        "room_id": 0,
        "x_min": -63898,
        "x_max": -46389,
        "z_min": -59335,
        "z_max": -41068,
    },

    # Forest Sanctuary
    "Forest Sanctuary Stamp Station": {
        "region_id": "fos stamp station",
        "vanilla_item": "Treasure",
        #"vanilla_item": "Forest Sanctuary Stamp",
        "stage_id": 0x30,
        "room_id": 0,
        "stamp": True,
    },
    "Forest Sanctuary Song Statue": {
        "region_id": "fos song statue",
        "vanilla_item": "Song of Awakening",
        "stage_id": 0x30,
        "room_id": 0,
        "x_min": -32764,
        "x_max": -18104,
        "z_min": 5734,
        "z_max": 18842,
    },
    # "Forest Sanctuary Gage Duet": {
    #     "region_id": "fos gage",
    #     "stage_id": 0x30,
    #     "room_id": 1,
    #     "address": 0x0B92D8,
    #     "value": 18,
    #     "vanilla_item": "Wooded Temple Tracks",
    #     "require_item": ["Spirit Flute"],
    #     "duet": True,
    # },
    "Forest Sanctuary Chest": {
        "region_id": "fos chest",
        "vanilla_item": "Big Red Rupee (200)",
        "x_min": 9228,
        "x_max": 18778,
        "z_min": 39028,
        "z_max": 52120,
        "stage_id": 0x30,
        "room_id": 0,
    },

    # Wooded Temple

    "Wooded Temple Song Statue": {
        "region_id": "wt song statue",
        "vanilla_item": "Song of Healing",
        "stage_id": 0x19,
        "room_id": 0x0A,
        "x_min": -35240,
        "x_max": -14885,
        "z_min": -51620,
        "z_max": -39275,
        "dungeon": "Wooded Temple",
    },
    "Wooded Temple Stamp Station": {
        "region_id": "wt stamp station",
        "vanilla_item": "Treasure",
        #"vanilla_item": "Forest Station Stamp",
        "stage_id": 0x19,
        "room_id": 0,
        "stamp": True,
        "dungeon": "Wooded Temple",
    },
    "Wooded Temple 1F Enemy Chest": {
        "region_id": "wt 1f enemy chest",
        "vanilla_item": "Big Green Rupee (100)",
        "stage_id": 0x19,
        "room_id": 0,
        "x_min": 22118,
        "x_max": 34012,
        "z_min": 30310,
        "z_max": 39600,
        "dungeon": "Wooded Temple",
    },
    "Wooded Temple 1F Key": {
        "region_id": "wt 1f key",
        "vanilla_item": "Small Key (Wooded Temple)",
        "stage_id": 0x19,
        "room_id": 0,
        "x_max": -13926,
        "z_min": -63898,
        "z_max": -20000,
        "dungeon": "Wooded Temple",
    },
    "Wooded Temple 1F Switch Chest": {
        "region_id": "wt 1f switch chest",
        "vanilla_item": "Big Green Rupee (100)",
        "stage_id": 0x19,
        "room_id": 0,
        "x_min": 30327,
        "x_max": 43418,
        "z_min": -39322,
        "z_max": -30077,
        "dungeon": "Wooded Temple",
    },
    "Wooded Temple 2F Enemy Chest": {
        "region_id": "wt 2f enemy chest",
        "vanilla_item": "Whirlwind",
        "stage_id": 0x19,
        "room_id": 1,
        "x_min": 63078,
        "z_max": -53204,
        "dungeon": "Wooded Temple",
    },
    "Wooded Temple 2F Poison Chest": {
        "region_id": "wt 2f poison chest",
        "vanilla_item": ITEM_GROUPS["Common Treasures"],
        "stage_id": 0x19,
        "room_id": 1,
        "x_min": 42450,
        "x_max": 55113,
        "z_min": -14900,
        "z_max": -258,
        "dungeon": "Wooded Temple",
    },
    "Wooded Temple 3F Chestnut Chest": {
        "region_id": "wt 3f chestnut chest",
        "vanilla_item": "Small Key (Wooded Temple)",
        "stage_id": 0x19,
        "room_id": 2,
        "x_min": -47514,
        "x_max": -42598,
        "z_min": -59820,
        "z_max": -52296,
        "dungeon": "Wooded Temple",
    },
    "Wooded Temple 3F SE Chest": {
        "region_id": "wt 3f se chest",
        "vanilla_item": ITEM_GROUPS["Common Treasures"],
        "stage_id": 0x19,
        "room_id": 2,
        "x_min": 42646,
        "x_max": 55982,
        "z_min": -2458,
        "z_max": 7485,
        "dungeon": "Wooded Temple",
    },
    # "Wooded Temple 3F Boss Key Chest": {
    #     "region_id": "wt 3f boss key chest",
    #     "vanilla_item": "Boss Key (Wooded Temple)",
    #     "stage_id": 0x19,
    #     "room_id": 2,
    #     "x_min": 54886,
    #     "x_max": 76186,
    #     "z_min": -63898,
    #     "z_max": -50790,
    #     "dungeon": "Wooded Temple",
    #     "require_item": ["Whirlwind"],
    # }, TODO heart container processes on loop, causing heart loss. doesn't occur for other ones
    "Wooded Temple Boss Heart Container": {
        "region_id": "wt stagnox",
        "vanilla_item": "Heart Container",
        "stage_id": 0x1E,
        "room_id": 0,
        "dungeon": "Wooded Temple",
    },
    "Wooded Temple Dungeon Reward": {
        "region_id": "wt stagnox",
        "vanilla_item": "Forest Source",
        "address": STAddr.adv_flags_0,
        "value": 0x10,
        "stage_id": 0x1E,
        "room_id": 0,
        "dungeon": "Wooded Temple",
        "goal": True,
        "ut_connect": "EVENT: Defeat Stagnox"
    },

    # Rabbit Haven
    "Rabbit Haven Net Gift": {
        "region_id": "rabbit haven",
        "vanilla_item": "Rabbit Net",
        "stage_id": 0x3E,
        "room_id": 0,
        "address": STAddr.adv_flags_1a,
        "value": 0x40,
    },
    "Rabbit Haven Chest": {
        "region_id": "rabbit haven",
        "vanilla_item": ITEM_GROUPS["Common Treasures"],
        "stage_id": 0x3E,
        "room_id": 0,
        "x_min": 11447,
        "x_max": 23070,
        "z_min": -18940,
        "z_max": -9020,
        "item_override": "Ocean Glyph"
    },
    "Rabbit Haven Rescue 5 Rabbits": {
        "region_id": "rabbit haven 5 rabbits",
        "vanilla_item": "Heart Container",
        "stage_id": 0x3E,
        "room_id": 0,
        'address': STAddr.adv_flags_51,
        'value': 0x8,
        "conditional": True
    },
    "Rabbit Haven Rescue 10 Forest Rabbits": {
        "region_id": "rabbit haven 10 forest rabbits",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "stage_id": 0x3E,
        "room_id": 0,
        "require_item": ["Forest Rabbit"],
        'address': STAddr.adv_flags_51,
        'value': 0x20,
        "conditional": True
    },
    "Rabbit Haven Rescue 10 Snow Rabbits": {
        "region_id": "rabbit haven 10 snow rabbits",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "stage_id": 0x3E,
        "room_id": 0,
        "require_item": ["Snow Rabbit"],
        'address': STAddr.adv_flags_51,
        'value': 0x40,
        "conditional": True
    },
    # "Rabbit Haven Rescue 50 Rabbits": {
    #     "region_id": "rabbit haven 50 rabbits",
    #     "vanilla_item": "Sword Beam Swordsman's Scroll",
    #     "stage_id": 0x3E,
    #     "room_id": 0,
    # },

    # Trading Post
    "Trading Post Stamp Station": {
        "region_id": "trading post stamp station",
        #"vanilla_item": "Trading Post Stamp",
        "vanilla_item": "Treasure",
        "stage_id": 0x37,
        "room_id": 0x01,
        "stamp": True,
    },
    # "Trading Post 1st Song Statue": { *only if not already have song*
    #     "region_id": "trading post discovery song statue",
    #     "vanilla_item": "Song of Discovery",
    #     "stage_id": 0x37,
    #     "room_id": 0,
    #     "require_item": ["Spirit Flute"],
    #     "x_min": -75630,
    #     "x_max": -58636,
    #     "z_min": 46500,
    #     "z_max": 57443,
    # },
    "Trading Post Song of Light Statue": {
        "region_id": "trading post light song statue",
        "vanilla_item": "Song of Light",
        "stage_id": 0x37,
        "room_id": 0,
        "x_min": -64094,
        "x_max": -45666,
        "z_min": -55626,
        "z_max": -35679,
    },
    "Trading Post Chest": {
        "region_id": "trading post chest",
        "vanilla_item": "Treasure: Regal Ring",
        "stage_id": 0x37,
        "room_id": 0x02,
        "address": STAddr.adv_flags_3e,
        "value": 0x10,
    },

    # Anouki Village
    "Anouki Village Stamp Station": {
        "region_id": "anouki village stamp station",
        "vanilla_item": "Treasure",
        "stage_id": 0x2B,
        "room_id": 0,
        "stamp": True,
    },
    "Anouki Village Song Statue": {
        "region_id": "anouki village song statue",
        "vanilla_item": "Song of Discovery",
        "stage_id": 0x2B,
        "room_id": 0,
        "x_min": -10441,
        "x_max": 6441,
        "z_min": -59643,
        "z_max": -43683,
        "delay_pickup": ["Anouki Village Song Statue Chest"],
    },
    "Anouki Village Song Statue Chest": { #TODO check if consistently sending check
        "region_id": "anouki village song statue",
        "vanilla_item": ["Red Potion", "Big Green Rupee (100)"],
        "stage_id": 0x2B,
        "room_id": 0,
        "x_min": -10441,
        "x_max": 9130,
        "z_min": -59643,
        "z_max": -43683,
        "delay_pickup": ["Anouki Village Song Statue"],
    },
    "Anouki Village Bomb Cave Chest": {
        "region_id": "anouki village bomb cave chest",
        "vanilla_item": "Big Red Rupee (200)",
        "stage_id": 0x2B,
        "room_id": 0x07,
        "x_min": 10380,
        "x_max": 23020,
        "z_min": -42922,
        "z_max": -19997,
    },
    "Anouki Village Lake Chest": {
        "region_id": "anouki village lake chest",
        "vanilla_item": "Big Green Rupee (100)",
        "stage_id": 0x2B,
        "room_id": 0,
        "x_min": -96434,
        "x_max": -83560,
        "z_min": -55900,
        "z_max": -47180,
    },

    # Snow Sanctuary
    "Snow Sanctuary Stamp Station": {
        "region_id": "ss stamp station",
        "vanilla_item": "Treasure",
        "stage_id": 0x31,
        "room_id": 0,
        "stamp": True,
    },
    # "Snow Sanctuary Steem Duet": {
    #     "region_id": "ss steem duet",
    #     "stage_id": 0x31,
    #     "room_id": 2,
    #     "address": 0x0B92D8,
    #     "value": 18,
    #     "vanilla_item": "Blizzard Temple Tracks",
    #     "require_item": ["Spirit Flute"],
    #     "duet": True,
    # },

    # Blizzard Temple
    "Blizzard Temple B1 SE Chest": {
        "region_id": "bt b1 se chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x1A,
        "room_id": 1,
        "x_min": 42800,
        "x_max": 51630,
        "z_min": 39300,
        "z_max": 47530,
        "dungeon": "Blizzard Temple",
    },
    "Blizzard Temple B1 E Enemy Chest": {
        "region_id": "bt b1 e enemy chest",
        "vanilla_item": ITEM_GROUPS["Uncommon Treasures"],
        "stage_id": 0x1A,
        "room_id": 1,
        "x_min": 73520,
        "x_max": 92474,
        "z_min": -28212,
        "z_max": -13300,
        "dungeon": "Blizzard Temple",
    },
    "Blizzard Temple B1 NE Enemy Chest": {
        "region_id": "bt b1 ne enemy chest",
        "vanilla_item": "Boomerang",
        "stage_id": 0x1A,
        "room_id": 1,
        "x_min": 11761,
        "x_max": 28782,
        "z_min": -72090,
        "z_max": -53453,
        "dungeon": "Blizzard Temple",
    },
    "Blizzard Temple 1F NE Chest": {
        "region_id": "bt 1f ne chest",
        "vanilla_item": ITEM_GROUPS["Uncommon Treasures"],
        "stage_id": 0x1A,
        "room_id": 0,
        "x_min": 74030,
        "x_max": 88474,
        "z_min": -68000,
        "z_max": -58982,
        "dungeon": "Blizzard Temple",
    },
    "Blizzard Temple B1 SW Chest": {
        "region_id": "bt b1 sw chest",
        "vanilla_item": "Small Key (Blizzard Temple)",
        "stage_id": 0x1A,
        "room_id": 1,
        "x_min": -17527,
        "x_max": -1638,
        "z_min": 51643,
        "z_max": 72090,
        "dungeon": "Blizzard Temple",
    },
    "Blizzard Temple Stamp Station": {
        "region_id": "bt stamp station",
        "vanilla_item": "Treasure",
        "stage_id": 0x1A,
        "room_id": 1,
        "stamp": True,
        "dungeon": "Blizzard Temple",
    },
    "Blizzard Temple B1 NW Enemy Chest": {
        "region_id": "bt b1 nw enemy chest",
        "vanilla_item": "Big Green Rupee (100)",
        "stage_id": 0x1A,
        "room_id": 1,
        "x_min": -88490,
        "x_max": -72624,
        "z_min": -62715,
        "z_max": -42615,
        "dungeon": "Blizzard Temple",
    },
    "Blizzard Temple 1F NW Chest": {
        "region_id": "bt 1f nw chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x1A,
        "room_id": 0,
        "x_min": -50967,
        "x_max": -38600,
        "z_min": -68000,
        "z_max": -56082,
        "dungeon": "Blizzard Temple",
    },
    "Blizzard Temple 1F Torch Chest": {
        "region_id": "bt 1f torch chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x1A,
        "room_id": 0,
        "x_min": -8700,
        "x_max": 8172,
        "z_min": -68020,
        "z_max": -58982,
        "dungeon": "Blizzard Temple",
    },
    "Blizzard Temple Boss Heart Container": {
        "region_id": "bt fraaz",
        "vanilla_item": "Heart Container",
        "stage_id": 0x1F,
        "room_id": 0,
        "x_min": -9609,
        "x_max": 9792,
        "z_min": 4707,
        "z_max": 24840,
        "dungeon": "Blizzard Temple",
    },
    "Blizzard Temple Dungeon Reward": {
        "region_id": "bt fraaz",
        "vanilla_item": "Snow Source", #TODO tracks did not get removed, and check sent on room entry
        "address": STAddr.adv_flags_0,
        "value": 0x20,
        "stage_id": 0x1F,
        "room_id": 0,
        "dungeon": "Blizzard Temple",
        "goal": True,
        "ut_connect": "EVENT: Defeat Fraaz"
    },

    # Icy Spring
    "Icy Spring Whip Chest": {
        "region_id": "icyspring whip chest",
        "vanilla_item": "Big Green Rupee (100)",
        "stage_id": 0x35,
        "room_id": 0,
        "x_min": 50054,
        "x_max": 64770,
        "z_min": -58730,
        "z_max": -42650,
    },
    "Icy Spring Stamp Station": {
        "region_id": "icyspring stamp station",
        "vanilla_item": "Treasure",
        "stage_id": 0x35,
        "room_id": 0,
        "stamp": True,
        "item_override": "Shield",
    },

    # Snowdrift Station
    "Snowdrift Station Puzzle Reward": {
        "region_id": "snowdrift reward",
        "vanilla_item": ITEM_GROUPS["Super Rare Treasures"],
        "stage_id": 0x3F,
        "room_id": 1,
        "x_min": -10650,
        "x_max": 10650,
        "z_min": -55800,
        "z_max": -38083,
    },

    # Slippery Station
    "Slippery Station Amateur Reward": {
        "region_id": "slippery amateur",
        "vanilla_item": "Gold Rupee (300)",
        "stage_id": 0x3F,
        "room_id": 0x06,
        "x_min": -1930,
        "x_max": 14746,
        "z_min": -68303,
        "z_max": -50810,
    },
    "Slippery Station Pro Reward": {
        "region_id": "slippery pro",
        "vanilla_item": ITEM_GROUPS["Rare Treasures"],
        "stage_id": 0x3F,
        "room_id": 0x06,
        "x_min": 87833,
        "x_max": 104858,
        "z_min": -65036,
        "z_max": -46800,
    },
    "Slippery Station Champion Reward": {
        "region_id": "slippery champion",
        "vanilla_item": ITEM_GROUPS["Super Rare Treasures"],
        "stage_id": 0x3F,
        "room_id": 0x06,
        "x_min": 72800,
        "x_max": 88000,
        "z_min": 45579,
        "z_max": 64500,
        "conditional": True
    },

    # Bridge Worker's Home
    "Bridge Worker's Home Chest": {
        "region_id": "bridge workers chest",
        "vanilla_item": "Big Green Rupee (100)",
        "stage_id": 0x36,
        "room_id": 0,
        "x_min": 63278,
        "x_max": 72232,
        "z_min": -43618,
        "z_max": -28439,
    },

    # ========= Rabbits ==========

    "Rabbit near Castle Town": {
        "region_id": "forest realm rabbits",
        "vanilla_item": "Forest Rabbit",
        "stage_id": 0x04,
        "address": STAddr.rabbits_0,
        "value": 1,
        "rabbit": True,
        "location_groups": ["Unique Forest Rabbits"]
    },
    "Rabbit near Ocean Shortcut": {
        "region_id": "forest ocean shortcut rabbit",
        "vanilla_item": "Forest Rabbit",
        "stage_id": 0x04,
        "address": STAddr.rabbits_0,
        "value": 2,
        "rabbit": True,
        "location_groups": ["Unique Forest Rabbits"]
    },
    "Rabbit E Mayscore": {
        "region_id": "e mayscore rabbits",
        "vanilla_item": "Forest Rabbit",
        "stage_id": 0x04,
        "address": STAddr.rabbits_0,
        "value": 4,
        "rabbit": True,
        "location_groups": ["Unique Forest Rabbits"]
    },
    "Rabbit SW Trading Post": {
        "region_id": "sw trading post rabbit",
        "vanilla_item": "Forest Rabbit",
        "stage_id": 0x04,
        "address": STAddr.rabbits_0,
        "value": 8,
        "rabbit": True,
        "location_groups": ["Unique Forest Rabbits"]
    },
    "Rabbit E Outset": {
        "region_id": "forest realm rabbits",
        "vanilla_item": "Forest Rabbit",
        "stage_id": 0x04,
        "address": STAddr.rabbits_0,
        "value": 0x10,
        "rabbit": True,
        "location_groups": ["Unique Forest Rabbits"]
    },
    "Rabbit SW Rabbit Haven": {
        "region_id": "s rabbit haven rabbits",
        "vanilla_item": "Forest Rabbit",
        "stage_id": 0x04,
        "address": STAddr.rabbits_0,
        "value": 0x20,
        "rabbit": True,
        "location_groups": ["Unique Forest Rabbits"]
    },
    "Rabbit near Wooded Temple": {
        "region_id": "wt rabbit",
        "vanilla_item": "Forest Rabbit",
        "stage_id": 0x04,
        "address": STAddr.rabbits_0,
        "value": 0x40,
        "rabbit": True,
        "location_groups": ["Unique Forest Rabbits"]
    },
    "Rabbit near Rabbit Haven": {
        "region_id": "nr rabbit haven rabbit",
        "vanilla_item": "Forest Rabbit",
        "stage_id": 0x04,
        "address": STAddr.rabbits_0,
        "value": 0x80,
        "rabbit": True,
        "location_groups": ["Unique Forest Rabbits"]
    },
    "Rabbit past wooden bridge": {
        "region_id": "e mayscore rabbits",
        "vanilla_item": "Forest Rabbit",
        "stage_id": 0x04,
        "address": STAddr.rabbits_1,
        "value": 1,
        "rabbit": True,
        "location_groups": ["Unique Forest Rabbits"]
    },
    "Rabbit S Rabbit Haven": {
        "region_id": "s rabbit haven rabbits",
        "vanilla_item": "Forest Rabbit",
        "stage_id": 0x04,
        "address": STAddr.rabbits_1,
        "value": 2,
        "rabbit": True,
        "location_groups": ["Unique Forest Rabbits"]
    },

    "Rabbit NE Blizzard": {
        "region_id": "snow realm early blizzard rabbits",
        "vanilla_item": "Snow Rabbit",
        "stage_id": 0x05,
        "address": STAddr.rabbits_1,
        "value": 4,
        "rabbit": True,
        "location_groups": ["Unique Snow Rabbits"]
    },
    "Rabbit SE Blizzard": {
        "region_id": "snow realm blizzard rabbits",
        "vanilla_item": "Snow Rabbit",
        "stage_id": 0x05,
        "address": STAddr.rabbits_1,
        "value": 8,
        "rabbit": True,
        "location_groups": ["Unique Snow Rabbits"]
    },
    "Rabbit W Anouki Village": {
        "region_id": "snow realm rabbits",
        "vanilla_item": "Snow Rabbit",
        "stage_id": 0x05,
        "address": STAddr.rabbits_1,
        "value": 0x10,
        "rabbit": True,
        "location_groups": ["Unique Snow Rabbits"]
    },
    "Rabbit SW Blizzard": {
        "region_id": "snow realm blizzard rabbits",
        "vanilla_item": "Snow Rabbit",
        "stage_id": 0x05,
        "address": STAddr.rabbits_1,
        "value": 0x20,
        "rabbit": True,
        "location_groups": ["Unique Snow Rabbits"]
    },
    "Rabbit E Anouki Village": {
        "region_id": "blizzard temple tracks rabbits",
        "vanilla_item": "Snow Rabbit",
        "stage_id": 0x05,
        "address": STAddr.rabbits_1,
        "value": 0x40,
        "rabbit": True,
        "location_groups": ["Unique Snow Rabbits"]
    },
    "Rabbit near Snowdrift Station": {
        "region_id": "snowdrift station rabbit",
        "vanilla_item": "Snow Rabbit",
        "stage_id": 0x05,
        "address": STAddr.rabbits_1,
        "value": 0x80,
        "rabbit": True,
        "location_groups": ["Unique Snow Rabbits"]
    },
    "Rabbit W Icy Spring Station": {
        "region_id": "icyspring rabbits",
        "vanilla_item": "Snow Rabbit",
        "stage_id": 0x05,
        "address": STAddr.rabbits_2,
        "value": 1,
        "rabbit": True,
        "location_groups": ["Unique Snow Rabbits"]
    },
    "Rabbit N Icy Spring Station": {
        "region_id": "icyspring rabbits",
        "vanilla_item": "Snow Rabbit",
        "stage_id": 0x05,
        "address": STAddr.rabbits_2,
        "value": 2,
        "rabbit": True,
        "location_groups": ["Unique Snow Rabbits"]
    },
    "Rabbit NW Blizzard": {
        "region_id": "snow realm early blizzard rabbits",
        "vanilla_item": "Snow Rabbit",
        "stage_id": 0x05,
        "address": STAddr.rabbits_2,
        "value": 4,
        "rabbit": True,
        "location_groups": ["Unique Snow Rabbits"]
    },
    "Rabbit Central Blizzard": {
        "region_id": "snow realm early blizzard rabbits",
        "vanilla_item": "Snow Rabbit",
        "stage_id": 0x05,
        "address": STAddr.rabbits_2,
        "value": 8,
        "rabbit": True,
        "location_groups": ["Unique Snow Rabbits"]
    },

    # Total count rabbits
    "Catch 1 Forest Rabbit": {
        "region_id": "Forest Rabbit Count 1",
        "rabbit": True,
        "count": 1,
        "location_groups": ["Total Forest Rabbits"]
    },
    "Catch 2 Forest Rabbits": {
        "region_id": "Forest Rabbit Count 2",
        "rabbit": True,
        "count": 2,
        "location_groups": ["Total Forest Rabbits"]
    },
    "Catch 3 Forest Rabbits": {
        "region_id": "Forest Rabbit Count 3",
        "rabbit": True,
        "count": 3,
        "location_groups": ["Total Forest Rabbits"]
    },
    "Catch 4 Forest Rabbits": {
        "region_id": "Forest Rabbit Count 4",
        "rabbit": True,
        "count": 4,
        "location_groups": ["Total Forest Rabbits"]
    },
    "Catch 5 Forest Rabbits": {
        "region_id": "Forest Rabbit Count 5",
        "rabbit": True,
        "count": 5,
        "location_groups": ["Total Forest Rabbits"]
    },
    "Catch 6 Forest Rabbits": {
        "region_id": "Forest Rabbit Count 6",
        "rabbit": True,
        "count": 6,
        "location_groups": ["Total Forest Rabbits"]
    },
    "Catch 7 Forest Rabbits": {
        "region_id": "Forest Rabbit Count 7",
        "rabbit": True,
        "count": 7,
        "location_groups": ["Total Forest Rabbits"]
    },
    "Catch 8 Forest Rabbits": {
        "region_id": "Forest Rabbit Count 8",
        "rabbit": True,
        "count": 8,
        "location_groups": ["Total Forest Rabbits"]
    },
    "Catch 9 Forest Rabbits": {
        "region_id": "Forest Rabbit Count 9",
        "rabbit": True,
        "count": 9,
        "location_groups": ["Total Forest Rabbits"]
    },
    "Catch 10 Forest Rabbits": {
        "region_id": "Forest Rabbit Count 10",
        "rabbit": True,
        "count": 10,
        "location_groups": ["Total Forest Rabbits"]
    },
    "Catch 1 Snow Rabbit": {
        "region_id": "Snow Rabbit Count 1",
        "rabbit": True,
        "count": 1,
        "location_groups": ["Total Snow Rabbits"]
    },
    "Catch 2 Snow Rabbits": {
        "region_id": "Snow Rabbit Count 2",
        "rabbit": True,
        "count": 2,
        "location_groups": ["Total Snow Rabbits"]
    },
    "Catch 3 Snow Rabbits": {
        "region_id": "Snow Rabbit Count 3",
        "rabbit": True,
        "count": 3,
        "location_groups": ["Total Snow Rabbits"]
    },
    "Catch 4 Snow Rabbits": {
        "region_id": "Snow Rabbit Count 4",
        "rabbit": True,
        "count": 4,
        "location_groups": ["Total Snow Rabbits"]
    },
    "Catch 5 Snow Rabbits": {
        "region_id": "Snow Rabbit Count 5",
        "rabbit": True,
        "count": 5,
        "location_groups": ["Total Snow Rabbits"]
    },
    "Catch 6 Snow Rabbits": {
        "region_id": "Snow Rabbit Count 6",
        "rabbit": True,
        "count": 6,
        "location_groups": ["Total Snow Rabbits"]
    },
    "Catch 7 Snow Rabbits": {
        "region_id": "Snow Rabbit Count 7",
        "rabbit": True,
        "count": 7,
        "location_groups": ["Total Snow Rabbits"]
    },
    "Catch 8 Snow Rabbits": {
        "region_id": "Snow Rabbit Count 8",
        "rabbit": True,
        "count": 8,
        "location_groups": ["Total Snow Rabbits"]
    },
    "Catch 9 Snow Rabbits": {
        "region_id": "Snow Rabbit Count 9",
        "rabbit": True,
        "count": 9,
        "location_groups": ["Total Snow Rabbits"]
    },
    "Catch 10 Snow Rabbits": {
        "region_id": "Snow Rabbit Count 10",
        "rabbit": True,
        "count": 10,
        "location_groups": ["Total Snow Rabbits"]
    },

    # Portal Checks
    "Forest Realm Shoot SW Portal": {
        "stage_id": 0x04,
        "region_id": "forest cave tracks",
        "address": STAddr.activate_portals,
        "value": 0x40,
        "location_groups": ["Portal Checks"],
        "conditional": True
    },
    "Forest Realm Shoot SE Portal": {
        "stage_id": 0x04,
        "region_id": "forest realm se portal track",
        "address": STAddr.activate_portals,
        "value": 0x20,
        "location_groups": ["Portal Checks"],
        "conditional": True
    },
    "Snow Realm Shoot SW Portal": {
        "stage_id": 0x05,
        "region_id": "snow realm",
        "address": STAddr.activate_portals,
        "value": 0x8,
        "location_groups": ["Portal Checks"],
        "conditional": True
    },
    "Snow Realm Shoot Bridge Portal": {
        "stage_id": 0x05,
        "region_id": "snow bridge",
        "address": STAddr.activate_portals,
        "value": 0x10,
        "location_groups": ["Portal Checks"],
        "conditional": True
    },
    "Snow Realm Shoot N Portal": {
        "stage_id": 0x05,
        "region_id": "icyspring tracks",
        "address": STAddr.adv_flags_31,
        "value": 0x2,
        "location_groups": ["Portal Checks"],
        "conditional": True
    },
}
## ========== remember to add item override!! =============


for i, loc_data in enumerate(LOCATIONS_DATA.items()):
    name, data = loc_data
    LOCATIONS_DATA[name]["name"] = name
    LOCATIONS_DATA[name]["id"] = i+1
    loc_groups = data.get("location_groups", [])
    for loc_group in loc_groups:
        LOCATION_GROUPS.setdefault(loc_group, []).append(name)

# print(f"Location Groups:")
# for group, locs in LOCATION_GROUPS.items():
#     print(f"\t{group}: {locs}")

if __name__ == "__main__":
    for location, data in LOCATIONS_DATA.items():
        # print(f"{location} | {data['region_id']} | id: {data['id']} | stage: {data['stage_id']} | room: {data['room_id']}")
        print(location)