

# TODO: Add sram data for saveslot 2
# TODO: Add the rest of sram data in bulk

## ========== remember to add item override!! =============

LOCATIONS_DATA = {

    #Outset Village
    "Outset Clear Rocks": {
        "region_id": "outset village rocks",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x2F,
        "room_id": 0,
        "address": 0x265743,
        "value": 0x20,
    },
    "Outset Bee Tree": {
        "region_id": "outset village bees",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x2F,
        "room_id": 0,
        "x_min": 34192,
        "x_max": 52960,
        "z_min": -34890,
        "z_max": -10024,
        "item_override": "Stamp Book",

}, #TODO make location trigger on actual stamping
    "Outset Stamp Station": {
        "region_id": "outset village stamp station",
        #"vanilla_item": "Outset Village Stamp",
        #"vanilla_item": "Treasure",
        "item_override": "Song of Discovery",
        "stage_id": 0x2F,
        "room_id": 0,
        "stamp": True,
        "require_item": ["Stamp Book"],
        # 02271CD8 is array of stamp IDs
        # 02271CF4 is bitfield of all stamps found
    },
    "Outset Far Right Tree": {
        "region_id": "outset right tree",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x2F,
        "room_id": 0,
        "x_min": 27449,
        "x_max": 43663,
        "z_min": 11490,
        "z_max": 33968,
        "require_item": ["Spirit Flute", "Song of Discovery"]
    },
    "Outset Niko's House Tree": {
        "region_id": "outset left tree",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x2F,
        "room_id": 0,
        "x_min": -60427,
        "x_max": -41317,
        "z_min": 10523,
        "z_max": 28762,
        "require_item": ["Spirit Flute", "Song of Discovery"]
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
        "region_id": "castle town L wall chest",
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
        "region_id": "castle town R wall chest",
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
        "region_id": "castle town minigame roof",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x29,
        "room_id": 0,
        "x_min": 69100,
        "x_max": 74138,
        "z_min": 13914,
        "z_max": 24835,
        "require_item": ["Bombs (Progressive)", "Song of Birds"],
    },
    "Castle Town Ramp House Chest": {
        "region_id": "castle town ramp house chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x29,
        "room_id": 0,
        "x_min": -76411,
        "x_max": -66503,
        "z_min": 18672,
        "z_max": 28116,
        "require_item": ["Bombs (Progressive)", "Song of Birds"],
        "item_override": "Sword (Progressive)"
    },
    "Castle Town Empty House Roof Chest": {
        "region_id": "castle town empty house roof",
        "vanilla_item": "Treasure",
        "stage_id": 0x29,
        "room_id": 0,
        "x_min": -43484,
        "x_max": -32916,
        "z_min": -43563,
        "z_max": -33114,
        "require_item": ["Bombs (Progressive)", "Song of Birds"],
        "item_override": "Whirlwind"
    },

    # # Shops
    # "Masked Beedle Courage Gem": {
    #     "region_id": "masked ship gem",
    #     "vanilla_item": "Courage Gem",
    #     "stage_id": 5,
    #     "room_id": 0,
    #     "address": 0x1B558A,
    #     "value": 0x02,
    #     "conditional": True,
    #     "delay_reset": True
    # },

    # Hyrule Castle
    "Hyrule Castle NW Outside Chest": {
        "region_id": "hyrule castle nw chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x28,
        "room_id": 0,
        "entrance_id": 6,
        "item_override": "Bow (Progressive)"
    },
    "Hyrule Castle 2F Indoors Chest": {
        "region_id": "hyrule castle 2f indoors chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x28,
        "room_id": 2,
        "item_override": "Boomerang"
    },
    "Hyrule Castle 1F Back Chest": {
        "region_id": "hyrule castle 1f back chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x28,
        "room_id": 1,
        "entrance_id": 7,
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
        "vanilla_item": "Treasure",
        "stage_id": 0x18,
        "room_id": 1,
        'dungeon': "Tunnel to ToS"
    },

    # # ========== Tower of Spirits ==============
    "ToS 1F Chest": {
        "region_id": "tos 1f chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 0,
        "x_min": -6554,
        "x_max": 6554,
        "z_min": -72090,
        "z_max": -67990,
        'dungeon': "Tower of Spirits",
        #'set_bit': [(0x265715, 0x80)]
    },
    "ToS 2F Raised Chest": {
        "region_id": "tos 2f raised chest",
        "vanilla_item": "Treasure",
        "item_override": "Cannon",
        "stage_id": 0x13,
        "room_id": 1,
        "x_min": -5786,
        "x_max": 10650,
        "z_min": -39322,
        "z_max": -29710,
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Whirlwind"]
        #'set_bit': [(0x265715, 0x80)]
    },
    "ToS 2F Whirlwind Chest": {
        "region_id": "tos 2f whirlwind",
        "vanilla_item": "Bombs (Progressive)",
        #"vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 1,
        "x_min": 21028,
        "x_max": 40042,
        "z_min": -63898,
        "z_max": -54886,
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Whirlwind"]
    },
    "ToS 2F Bomb Wall Chest": {
        "region_id": "tos 2f bomb wall",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x13,
        "room_id": 28,
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Bombs (progressive)"]
    },
    "ToS Forest Rail Glyph": {
        "region_id": "tos 3f rail map",
        "vanilla_item": "Forest Glyph",
        "stage_id": 0x13,
        "room_id": 2,
        "goal": True,
        "x_min": -6390,
        "x_max": 6390,
        "z_min": -8438,
        "z_max": 4506,
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)"]
        #'set_bit': [(0x265715, 0x80)]
    },
    "ToS 4F Central Chest": {
        "region_id": "tos 4f central chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 3,
        "x_min": -8703,
        "x_max": 6560,
        "z_min": 1650,
        "z_max": 10670,
        'dungeon': "Tower of Spirits",
        "require_item": ["Forest Source"]
    },
    "ToS 4F NE Chest": {
        "region_id": "tos 4f ne chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 3,
        "entrance_id": 2,
        "x_min": 38520,
        "x_max": 51177,
        "z_min": -55720,
        "z_max": -42600,
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Forest Source", "Whirlwind", "Boomerang", "Bombs (Progressive)"]
    },
    "ToS 5F Island Chest": {
        "region_id": "tos 5f island chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 4,
        "x_min": -35240,
        "x_max": -22990,
        "z_min": 42350,
        "z_max": 52230,
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Forest Source"]
    },
    "ToS 5F Spinnit Key": {
        "region_id": "tos 5f spinnit key",
        "vanilla_item": "Small Key (ToS)",
        "stage_id": 0x13,
        "room_id": 4,
        #"delay_pickup"
        "x_min": -100790,
        "x_max": -46720,
        "z_min": 9850,
        "z_max": 63920,
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Whirlwind", "Forest Source"]
    },
    "ToS 5F Bomb Wall Chest": {
        "region_id": "tos 5f secret chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 0x29,
        "x_min": -8965,
        "x_max": 9061,
        "z_min": -17693,
        "z_max": 8481,
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Whirlwind", "Forest Source", "Boomerang", "Bombs (Progressive)"]
    },
    "ToS 6F Enemy Chest 1": {
        "region_id": "tos 6f ne chest 1",
        "vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 5,
        "entrance_id": 2,
        "x_min": 34420,
        "x_max": 48753,
        "z_min": -10660,
        "z_max": -4354,
        # "delay_pickup"
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Whirlwind", "Forest Source", "Boomerang"]
    },
    "ToS 6F Enemy Chest 2": {
        "region_id": "tos 6f ne chest 2",
        "vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 5,
        "entrance_id": 2,
        "x_min": 60910,
        "x_max": 80112,
        "z_min": -4646,
        "z_max": 6570,
        # "delay_pickup"
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Whirlwind", "Forest Source", "Boomerang"]
    },
    "ToS 6F Enemy Chest 3": {
        "region_id": "tos 6f ne chest 3",
        "vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 5,
        "entrance_id": 2,
        "x_min": 63492,
        "x_max": 80310,
        "z_min": -10660,
        "z_max": -4354,
        # "delay_pickup"
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Whirlwind", "Forest Source", "Boomerang"]
    },
    "ToS 6F Enemy Big Chest": {
        "region_id": "tos 6f ne big chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 5,
        "entrance_id": 2,
        "x_min": 41795,
        "x_max": 57985,
        "z_min": -10660,
        "z_max": 6560,
        # "delay_pickup"
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Whirlwind", "Forest Source", "Boomerang"]
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
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Whirlwind", "Forest Source"]
    },
    "ToS Snow Rail Glyph": {
        "region_id": "tos 7f rail map",
        "vanilla_item": "Snow Glyph",
        "stage_id": 0x13,
        "room_id": 6,
        "x_min": -6400,
        "x_max": 6400,
        "z_min": -8450,
        "z_max": 4515,
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Whirlwind", "Forest Source"]
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
        "vanilla_item": "Red Rupee (20)",
        "item_override": "Refill: Bombs"
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
        "vanilla_item": "Treasure",
        "stage_id": 0x38,
        "room_id": 0,
        "x_min": -63898,
        "x_max": -46389,
        "z_min": -59335,
        "z_max": -41068,
        "require_item": ["Whip"],
    },

    # Forest Sanctuary
    "Forest Sanctuary Stamp Station": {
        "region_id": "fos stamp station",
        "vanilla_item": "Treasure",
        #"vanilla_item": "Forest Sanctuary Stamp",
        "stage_id": 0x30,
        "room_id": 0,
        "stamp": True,
        "require_item": ["Stamp Book"],
        "item_override": "Forest Temple Tracks"
    },
    #TODO bad address for flute stuff
    # "Forest Sanctuary Song Statue": {
    #     "region_id": "fos song statue",
    #     "vanilla_item": "Song of Awakening",
    #     "stage_id": 0x30,
    #     "room_id": 0,
    #     "x_min": -32764,
    #     "x_max": -18104,
    #     "z_min": 5734,
    #     "z_max": 18842,
    #     "address": 0x0B92D8,
    #     "value": 18,
    #     "require_item": ["Spirit Flute"],
    # },
    # "Forest Sanctuary Gage Duet": {
    #     "region_id": "fos gage",
    #     "stage_id": 0x30,
    #     "room_id": 1,
    #     "address": 0x0B92D8,
    #     "value": 18,
    #     "vanilla_item": "Forest Temple Tracks",
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
        "require_item": ["Whirlwind", "Spirit Flute", "Song of Birds"],
    },

    # Forest Temple
    # "Forest Temple Song Statue": {
    #     "region_id": "fot song statue",
    #     "vanilla_item": "Song of Healing",
    #     "stage_id": 0x19,
    #     "room_id": 0x0A,
    #     "dungeon": "Forest Temple",
    #     "require_item": ["Spirit Flute"],
    # },
    "Forest Temple Stamp Station": {
        "region_id": "fot stamp station",
        "vanilla_item": "Treasure",
        #"vanilla_item": "Forest Station Stamp",
        "stage_id": 0x19,
        "room_id": 0,
        "stamp": True,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind", "Stamp Book"],
    },
    "Forest Temple 1F Enemy Chest": {
        "region_id": "fot 1f enemy chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 0,
        "x_min": 22118,
        "x_max": 34012,
        "z_min": 30310,
        "z_max": 39600,
        "dungeon": "Forest Temple",
    },
    "Forest Temple 1F Key": {
        "region_id": "fot 1f key",
        "vanilla_item": "Small Key (Forest Temple)",
        "stage_id": 0x19,
        "room_id": 0,
        "x_min": -58352,
        "x_max": -19702,
        "z_min": -63898,
        "z_max": -22118,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple 1F Switch Chest": {
        "region_id": "fot 1f switch chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 0,
        "x_min": 30327,
        "x_max": 43418,
        "z_min": -39322,
        "z_max": -30077,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple 2F Enemy Chest": {
        "region_id": "fot 2f enemy chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 1,
        "x_min": 63078,
        "x_max": 76186,
        "z_min": -63898,
        "z_max": -53204,
        "dungeon": "Forest Temple",
    },
    "Forest Temple 2F Poison Chest": {
        "region_id": "fot 2f poison chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 1,
        "x_min": 42598,
        "x_max": 55113,
        "z_min": -14746,
        "z_max": -258,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple 3F Chestnut Chest": {
        "region_id": "fot 3f chestnut chest",
        "vanilla_item": "Small Key (Forest Temple)",
        "stage_id": 0x19,
        "room_id": 2,
        "x_min": -47514,
        "x_max": -42598,
        "z_min": -59802,
        "z_max": -52296,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple 3F SE Chest": {
        "region_id": "fot 3f se chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 2,
        "x_min": 42646,
        "x_max": 55982,
        "z_min": -2458,
        "z_max": 7485,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    # "Forest Temple 3F Boss Key Chest": {
    #     "region_id": "fot 3f boss key chest",
    #     "vanilla_item": "Boss Key (Forest Temple)",
    #     "stage_id": 0x19,
    #     "room_id": 2,
    #     "x_min": 54886,
    #     "x_max": 76186,
    #     "z_min": -63898,
    #     "z_max": -50790,
    #     "dungeon": "Forest Temple",
    #     "require_item": ["Whirlwind"],
    # },
    "Forest Temple Boss Heart Container": {
        "region_id": "fot heart container",
        "vanilla_item": "Heart Container",
        "stage_id": 0x1E,
        "room_id": 0,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple Dungeon Reward": {
        "region_id": "fot stagnox",
        "vanilla_item": "Forest Source",
        "address": 0x265714,
        "value": 0x10,
        "stage_id": 0x1E,
        "room_id": 0,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
        "goal": True
    },

    # Rabbitland Rescue
    "Rabbitland Rescue Net Gift": {
        "region_id": "rabbitland net",
        "vanilla_item": "Rabbit Net",
        "stage_id": 0x3E,
        "room_id": 0,
    },
    "Rabbitland Rescue Chest": {
        "region_id": "rabbitland chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x3E,
        "room_id": 0,
    },

    # Trading Post
    "Trading Post Stamp Station": {
        "region_id": "trading stamp station",
        #"vanilla_item": "Trading Post Stamp",
        "stage_id": 0x37,
        "room_id": 0,
        "stamp": True,
        "require_item": ["Stamp Book"],
        "vanilla_item": "Red Rupee (20)",
    },
    # "Trading Post Outside Song Statue": {
    #     "region_id": "trading post discovery song statue",
    #     "vanilla_item": "Song of Discovery",
    #     "stage_id": 0x37,
    #     "room_id": 0,
    #     "require_item": ["Spirit Flute"],
    # },
    # "Trading Post Cave Song Statue": {
    #     "region_id": "trading post light song statue",
    #     "vanilla_item": "Song of Light",
    #     "stage_id": 0x37,
    #     "room_id": 0,
    #     "require_item": ["Spirit Flute"],
    # },
    "Trading Post Chest": {
        "region_id": "trading post chest",
        "vanilla_item": "Treasure: Regal Ring",
        "stage_id": 0x37,
        "room_id": 0,
        "require_item": ["Boomerang", "Song of Discovery"],
    },
}

for i, name in enumerate(LOCATIONS_DATA):
    LOCATIONS_DATA[name]["id"] = i+1

if __name__ == "__main__":
    for location, data in LOCATIONS_DATA.items():
        print(f"{location} | {data['region_id']} | id: {data['id']} | stage: {data['stage_id']} | room: {data['room_id']}")
