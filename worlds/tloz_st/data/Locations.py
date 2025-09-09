from .Constants import ITEM_GROUPS

# TODO: Add sram data for saveslot 2
# TODO: Add the rest of sram data in bulk

## ========== remember to add item override!! =============

LOCATIONS_DATA = {

    #Aboda Village
    "Aboda Clear Rocks": {
        "region_id": "aboda village rocks",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x2F,
        "room_id": 0,
        "address": 0x265743,
        "value": 0x20,
    },
    "Aboda Bee Tree": {
        "region_id": "aboda village bees",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x2F,
        "room_id": 0,
        "x_min": 34192,
        "x_max": 52960,
        "z_min": -34890,
        "z_max": -10024,
        "item_override": "Stamp Book",

}, #TODO make location trigger on actual stamping
    "Aboda Stamp Station": {
        "region_id": "aboda village stamp station",
        #"vanilla_item": "Aboda Village Stamp",
        "vanilla_item": "Treasure",
        #"item_override": "Bombs (Progressive)",
        "stage_id": 0x2F,
        "room_id": 0,
        "stamp": True,
        "require_item": ["Stamp Book"],
        # 02271CD8 is array of stamp IDs
        # 02271CF4 is bitfield of all stamps found
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

    "Tear 1F Top":{
        "region_id": "tear 1f top",
        "vanilla_item": "Tear of Light",
        "stage_id": 0x13,
        "room_id": 0,
        "x_min": -6554,
        "x_max": 6554,
        "z_min": -72090,
        "z_max": -59101,
        'dungeon': "Tower of Spirits",
        "conditional": True,
        "item_override": "Tear of Light",
        "delay_pickup": "ToS 1F Chest"
    },

    "ToS 1F Chest": {
        "region_id": "tos 1f chest",
        "vanilla_item": ITEM_GROUPS["Rare Treasure Items"],
        "stage_id": 0x13,
        "room_id": 0,
        "x_min": -6554,
        "x_max": 6554,
        "z_min": -72090,
        "z_max": -59101,
        'dungeon': "Tower of Spirits",
        "delay_pickup": "Tear 1F Top"
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
        #'set_bit': [(0x265715, 0x80)]
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
        "item_override": "Wooded Temple Tracks"
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
        "require_item": ["Whirlwind", "Spirit Flute", "Song of Birds"],
    },

    # Wooded Temple
    # "Wooded Temple Song Statue": {
    #     "region_id": "wt song statue",
    #     "vanilla_item": "Song of Healing",
    #     "stage_id": 0x19,
    #     "room_id": 0x0A,
    #     "dungeon": "Wooded Temple",
    #     "require_item": ["Spirit Flute"],
    # },
    "Wooded Temple Stamp Station": {
        "region_id": "wt stamp station",
        "vanilla_item": "Treasure",
        #"vanilla_item": "Forest Station Stamp",
        "stage_id": 0x19,
        "room_id": 0,
        "stamp": True,
        "dungeon": "Wooded Temple",
        "require_item": ["Whirlwind", "Stamp Book"],
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
        "x_min": -63603,
        "x_max": -13926,
        "z_min": -17192,
        "z_max": -22118,
        "dungeon": "Wooded Temple",
        "require_item": ["Whirlwind"],
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
        "require_item": ["Whirlwind"],
    },
    "Wooded Temple 2F Enemy Chest": {
        "region_id": "wt 2f enemy chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 1,
        "x_min": 63078,
        "x_max": 76186,
        "z_min": -63898,
        "z_max": -53204,
        "dungeon": "Wooded Temple",
    },
    "Wooded Temple 2F Poison Chest": {
        "region_id": "wt 2f poison chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 1,
        "x_min": 42450,
        "x_max": 55113,
        "z_min": -14900,
        "z_max": -258,
        "dungeon": "Wooded Temple",
        "require_item": ["Whirlwind"],
    },
    "Wooded Temple 3F Chestnut Chest": {
        "region_id": "wt 3f chestnut chest",
        "vanilla_item": "Small Key (Wooded Temple)",
        "stage_id": 0x19,
        "room_id": 2,
        "x_min": -47514,
        "x_max": -42598,
        "z_min": -59802,
        "z_max": -52296,
        "dungeon": "Wooded Temple",
        "require_item": ["Whirlwind"],
    },
    "Wooded Temple 3F SE Chest": {
        "region_id": "wt 3f se chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 2,
        "x_min": 42646,
        "x_max": 55982,
        "z_min": -2458,
        "z_max": 7485,
        "dungeon": "Wooded Temple",
        "require_item": ["Whirlwind"],
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
    # },
    "Wooded Temple Boss Heart Container": {
        "region_id": "wt heart container",
        "vanilla_item": "Heart Container",
        "stage_id": 0x1E,
        "room_id": 0,
        "dungeon": "Wooded Temple",
        "require_item": ["Whirlwind"],
    },
    "Wooded Temple Dungeon Reward": {
        "region_id": "wt stagnox",
        "vanilla_item": "Treasure",
        "address": 0x265714,
        "value": 0x10,
        "stage_id": 0x1E,
        "room_id": 0,
        "dungeon": "Wooded Temple",
        "require_item": ["Whirlwind"],
        "goal": True
    },


    # Whittleton

    # Rabbitland Rescue

    # Forest Sanctuary

    # Wooded Temple

    # Trading Post

}

for i, name in enumerate(LOCATIONS_DATA):
    LOCATIONS_DATA[name]["id"] = i+1

if __name__ == "__main__":
    for location, data in LOCATIONS_DATA.items():
        print(f"{location} | {data['region_id']} | id: {data['id']} | stage: {data['stage_id']} | room: {data['room_id']}")
