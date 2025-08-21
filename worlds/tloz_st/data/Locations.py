

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
        "vanilla_item": "Treasure",
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
        "vanilla_item": "Red Rupee (20)",
        "item_override": "Bombs (Progressive)",
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
        "vanilla_item": "Red Rupee (20)",
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
        "require_item": ["Bombs (Progressive)"],
        "item_override": "Whip"
    },
    "Castle Town Right Wall Chest": {
        "region_id": "castle town R wall chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x29,
        "room_id": 0,
        "require_item": ["Bombs (Progressive)"],
        "item_override": "Spirit Flute"
    },
    "Castle Town Minigame Roof": {
        "region_id": "castle town minigame roof",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x29,
        "room_id": 0,
        "require_item": ["Bombs (Progressive)", "Song of Birds"],
    },
    "Castle Town Ramp House Chest": {
        "region_id": "castle town ramp house chest",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x29,
        "room_id": 0,
        "require_item": ["Bombs (Progressive)", "Song of Birds"],
        "item_override": "Sword (Progressive)"
    },
    "Castle Town Empty House Roof Chest": {
        "region_id": "castle town empty house roof",
        "vanilla_item": "Red Rupee (20)",
        "stage_id": 0x29,
        "room_id": 0,
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
        "vanilla_item": "Small Key (ToS Tunnel)",
        "stage_id": 0x18,
        "room_id": 0,
        'dungeon': "Tunnel to ToS",
        "item_override": "Cannon"
},
    "Tunnel to ToS 2F Chest": {
        "region_id": "tower tunnel 2f chest",
        "vanilla_item": "Small Key (ToS Tunnel)",
        "stage_id": 0x18,
        "room_id": 1,
        'dungeon': "Tunnel to ToS"
    },

    # # ========== Tower of Spirits ==============

    "ToS 2F Chest": {
        "region_id": "tos 2f chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x13,
        "room_id": 1,
        'dungeon': "Tower of Spirits",
        "require_item": ["Sword (Progressive)", "Bombs (Progressive)"]
        #'set_bit': [(0x265715, 0x80)]
    },
    "ToS Forest Rail Glyph": {
        "region_id": "tos 3f rail map",
        "vanilla_item": "Forest Glyph",
        "stage_id": 0x13,
        "room_id": 2,
        "goal": True,
        "y": 0x4916,
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
    "Mayscore Whip Race 1st Reward": {
        "region_id": "mayscore whip race bomb bag",
        "vanilla_item": "Bombs (Progressive)",
        "stage_id": 0x38,
        "room_id": 2,
        "entrance_id": 1,
        "require_item": ["Whip"],
        "item_override": "Refill: Arrows"
    },
    "Mayscore Whip Race 2nd Reward": {
        "region_id": "mayscore whip race heart container",
        "vanilla_item": "Heart Container",
        "stage_id": 0x38,
        "room_id": 2,
        "entrance_id": 1,
        "require_item": ["Whip"],
    },
    "Mayscore Whip Chest": {
        "region_id": "mayscore whip chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x38,
        "room_id": 0,
        "require_item": ["Whip"],
    },

    # Forest Sanctuary
    "Forest Sanctuary Stamp Station": {
        "region_id": "fos stamp station",
        "vanilla_item": "Train: Golden Train",
        #"vanilla_item": "Forest Sanctuary Stamp",
        "stage_id": 0x30,
        "room_id": 0,
        "stamp": True,
        "require_item": ["Stamp Book"],
    },
    "Forest Sanctuary Song Statue": {
        "region_id": "fos song statue",
        "vanilla_item": "Song of Awakening",
        "stage_id": 0x30,
        "room_id": 0,
        "require_item": ["Spirit Flute"],
    },
    "Forest Sanctuary Gage Duet": {
        "region_id": "fos gage",
        "stage_id": 0x30,
        "room_id": 1,
        "vanilla_item": "Forest Temple Tracks",
        "require_item": ["Spirit Flute"],
        "duet": True,
    },
    "Forest Sanctuary Chest": {
        "region_id": "fos chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x30,
        "room_id": 0,
        "require_item": ["Whirlwind"],
    },

    # Forest Temple
    "Forest Temple Song Statue": {
        "region_id": "fot song statue",
        "vanilla_item": "Song of Healing",
        "stage_id": 0x19,
        "room_id": 0x0A,
        "dungeon": "Forest Temple",
        "require_item": ["Spirit Flute"],
    },
    "Forest Temple Stamp Station": {
        "region_id": "fot stamp station",
        "vanilla_item": "Train: Dignified Train",
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
        "dungeon": "Forest Temple",
    },
    "Forest Temple 1F Key": {
        "region_id": "fot 1f key",
        "vanilla_item": "Small Key (Forest Temple)",
        "stage_id": 0x19,
        "room_id": 0,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple 1F Switch Chest": {
        "region_id": "fot 1f switch chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 0,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple 2F Enemy Chest": {
        "region_id": "fot 2f enemy chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 1,
        "dungeon": "Forest Temple",
    },
    "Forest Temple 2F Poison Chest": {
        "region_id": "fot 2f poison chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 1,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple 3F Chestnut Chest": {
        "region_id": "fot 3f chestnut chest",
        "vanilla_item": "Small Key (Forest Temple)",
        "stage_id": 0x19,
        "room_id": 2,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple 3F SE Chest": {
        "region_id": "fot 3f se chest",
        "vanilla_item": "Treasure",
        "stage_id": 0x19,
        "room_id": 2,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple 3F Boss Key Chest": {
        "region_id": "fot 3f boss key chest",
        "vanilla_item": "Boss Key (Forest Temple)",
        "stage_id": 0x19,
        "room_id": 2,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple Boss Heart Container": {
        "region_id": "fot heart container",
        "vanilla_item": "Heart Container",
        "stage_id": 0x1E,
        "room_id": 0,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
    },
    "Forest Temple Dungeon Reward": {
        "region_id": "fot boss gem",
        "vanilla_item": "Treasure",
        "stage_id": 0x1E,
        "room_id": 0,
        "dungeon": "Forest Temple",
        "require_item": ["Whirlwind"],
        "goal": True
    },


    # "TotOK 1F Linebeck Key": {
    #     "region_id": "totok",
    #     "vanilla_item": "Small Key (Temple of the Ocean King)",
    #     "stage_id": 37,
    #     "room_id": 0,
    #     "z_min": 0xB000,
    #     "z_max": 0x11000,
    #     "x_min": -100,
    #     'set_bit': [(0x1B557D, 2)],
    #     'dungeon': "Temple of the Ocean King"
    # },
    # "TotOK 1F Empty Chest": {
    #     "region_id": "totok",
    #     "vanilla_item": "Nothing!",
    #     "stage_id": 37,
    #     "room_id": 0,
    #     "x_min": 0x4000,
    #     'dungeon': "Temple of the Ocean King"
    # },
    # "TotOK B1 Small Key": {
    #     "region_id": "totok b1 key",
    #     "vanilla_item": "Small Key (Temple of the Ocean King)",
    #     "stage_id": 37,
    #     "room_id": 1,
    #     "y": 0x1333,
    #     'dungeon': "Temple of the Ocean King"
    # },
    # "TotOK B1 Shoot Eye Chest": {
    #     "region_id": "totok b1 eye chest",
    #     "vanilla_item": "Courage Gem",
    #     "stage_id": 37,
    #     "room_id": 1,
    #     "x_min": 0xB000,
    #     "x_max": 0x10000,
    #     'dungeon': "Temple of the Ocean King"
    # },
    # "TotOK B2 Bombchu Chest": {
    #     "region_id": "totok b2 bombchu chest",
    #     "vanilla_item": "Wisdom Gem",
    #     "stage_id": 37,
    #     "room_id": 2,
    #     "x_min": 0xD800,
    #     "x_max": 0x10000,
    #     "require_item": ["Bombchus (Progressive)", "Hammer"],
    #     "delay_pickup": "TotOK B2 Small Key",
    #     'dungeon': "Temple of the Ocean King"
    # },
    # "TotOK B2 Phantom Chest": {
    #     "region_id": "totok b2 phantom chest",
    #     "vanilla_item": "Treasure",
    #     "farmable": True,
    #     "stage_id": 37,
    #     "room_id": 2,
    #     "z_min": 0x7000,
    #     "z_max": 0xF000,
    #     "delay_pickup": "TotOK B2 Small Key",
    #     'dungeon': "Temple of the Ocean King"
    # },

    # Whittleton

    # Rabbitland Rescue

    # Forest Sanctuary

    # Forest Temple

    # Trading Post

}

for i, name in enumerate(LOCATIONS_DATA):
    LOCATIONS_DATA[name]["id"] = i+1

if __name__ == "__main__":
    for location, data in LOCATIONS_DATA.items():
        print(f"{location} | {data['region_id']} | id: {data['id']} | stage: {data['stage_id']} | room: {data['room_id']}")
