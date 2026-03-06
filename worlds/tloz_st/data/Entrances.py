from ..Subclasses import STTransition, EntranceGroups

# For adding entrance data. Generates an object for both directions from each entry
ENTRANCE_DATA = {
    # "Name": {
    #   "return_name": str. what to call the vanilla connecting entrance that generates automatically
    #   "entrance": tuple[int, int, int], stage room entrance. If you come from entrance
    #   "exit": tuple[int, int, int], stage room entrance. What the vanilla game sends you on entering
    #   "entrance_region": str. logic region that the entrance is in (only used for ER)
    #   "exit_region": str. logic region it leads to in (only used for ER)
    #   "coords": tuple[int, int, int]. x, y, z. Where to place link on a continuous transition. y value is also used
    #       to differentiate transitions at different heights
    #   "extra_data": dict[str: int]. additional coordinate data for continuous boundaries, like "x_max" etc.
    #  There are hooks for doing special things with extra data.
    #   "type": EntranceGroup. Entrance group entrance type (house, cave, station etc)
    #   "direction": EntranceGroup. Entrance group direction
    #   "two_way": bool=True. generates a reciprocal entrance, also used for ER generation
    # }

    # ==== Outset ====
    "Outset to Forest Realm": {
        "return_name": "Forest Realm to Outset",
        "exit": (0x4, 0x0, 1),
        "entrance": (0x2F, 0x0, 0),
        "exit_region": "forest realm",
        "entrance_region": "outset village",
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Outset to Tutorial": {
        "return_name": "Tutorial to Outset",
        "exit": (0x8, 0x0, 0),
        "entrance": (0x2F, 0x0, 0),
        "exit_region": "forest realm",
        "entrance_region": "outset village",
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },

    # ===== Tower of Spirits =====
    "Tower of Spirits to Forest Realm": {
        "return_name": "Forest Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x4, 0x0, 6),
        "entrance_region": "tos",
        "exit_region": "forest realm",
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits to Snow Realm": {
        "return_name": "Snow Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x5, 0x0, 6),
        "entrance_region": "tos",
        "exit_region": "snow realm",
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits to Ocean Realm": {
        "return_name": "Ocean Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x6, 0x0, 4),
        "entrance_region": "tos",
        "exit_region": "snow realm",
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits to Fire Realm": {
        "return_name": "Fire Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x7, 0x0, 2),
        "entrance_region": "tos",
        "exit_region": "snow realm",
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },

    # ===== Warp Portals =====
    "Forest Realm North Portal": {
        "return_name": "Snow Realm West Portal",
        "entrance": (0x4, 0, 0xA),
        "exit": (0x5, 0x0, 0xA),
        "entrance_region": "forest realm",
        "exit_region": "snow realm",
        "type": EntranceGroups.TRAIN_PORTAL,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Forest Realm South Portal": {
        "return_name": "Snow Realm East Portal",
        "entrance": (0x4, 0, 0xB),
        "exit": (0x5, 0x0, 0xC),
        "entrance_region": "forest realm",
        "exit_region": "snow realm",
        "type": EntranceGroups.TRAIN_PORTAL,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Snow Realm North Portal": {
        "return_name": "Mountain Portal",
        "entrance": (0x5, 0, 0xD),  # Random value, probably not correct
        "exit": (0x7, 0x0, 0x14),
        "entrance_region": "snow realm",
        "exit_region": "fire realm",
        "type": EntranceGroups.TRAIN_PORTAL,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Snow Realm Bridge Portal": {
        "return_name": "Ocean Realm Portal",
        "entrance": (0x5, 0, 0xB),
        "exit": (0x6, 0x0, 0x9),
        "entrance_region": "snow realm",
        "exit_region": "ocean realm",
        "type": EntranceGroups.TRAIN_PORTAL,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Forest Realm Cave Portal": {
        "return_name": "Fire Realm Portal",
        "entrance": (0x4, 0, 0xC),
        "exit": (0x7, 0x0, 0x12),
        "entrance_region": "forest cave tracks",
        "exit_region": "fire realm",
        "type": EntranceGroups.TRAIN_PORTAL,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Sand Realm Temple Portal": {
        "return_name": "Sand Realm Sanctuary Portal",
        "entrance": (0x6, 0, 0xB),
        "exit": (0x6, 0x0, 0xC),
        "entrance_region": "sand realm restoration",
        "exit_region": "sand realm",
        "type": EntranceGroups.TRAIN_PORTAL,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Fire Realm Sand Portal": {
        "return_name": "Ocean Realm Temple Portal",
        "entrance": (0x7, 0, 0x13),
        "exit": (0x6, 0x0, 0xA),
        "entrance_region": "sand connection",
        "exit_region": "ocean temple tracks",
        "type": EntranceGroups.TRAIN_PORTAL,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },

    # Dark Realm
    "Enter Dark Realm Portal": {
        "return_name": "Enter Dark Trains",
        "entrance": (0x4, 0, 0x9),
        "exit": (0xF, 0x0, 0x0),
        "entrance_region": "dark realm portal",
        "exit_region": "dark realm trains",
        "type": EntranceGroups.TRAIN_PORTAL,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Defeat Dark Trains": {
        "return_name": "Enter Demon Train",
        "entrance": (0xF, 0, 0x0),
        "exit": (0x10, 0xFF, 0x0),
        "two_way": False,
        "entrance_region": "dark realm trains",
        "exit_region": "demon train",
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Defeat Demon Train": {
        "return_name": "Enter Cole Fight",
        "entrance": (0x12, 0xFF, 0x0),
        "exit": (0x24, 0x00, 0x0),
        "two_way": False,
        "entrance_region": "demon train",
        "exit_region": "cole fight",
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Defeat Cole": {
        "return_name": "Enter Malladus 1",
        "entrance": (0x10, 0x0, 0x0),
        "exit": (0x25, 0x0, 0x0),
        "two_way": False,
        "entrance_region": "cole fight",
        "exit_region": "malladus 1",
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Defeat Malladus 1": {
        "return_name": "Enter Malladus 2",
        "entrance": (0x26, 0x0, 0x0),
        "exit": (0x27, 0x0, 0x0),
        "two_way": False,
        "entrance_region": "malladus 1",
        "exit_region": "malladus 2",
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },

    # Events
    "EVENT: Pick up Alfonzo": {
        "two_way": False,
        "entrance_region": "pick up alfonzo",
        "exit_region": "alfonzo event",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Defeat Stagnox": {
        "two_way": False,
        "entrance_region": "wt stagnox",
        "exit_region": "event_stagnox",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Defeat Fraaz": {
        "two_way": False,
        "entrance_region": "bt fraaz",
        "exit_region": "event_fraaz",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Defeat Cactops": {
        "two_way": False,
        "entrance_region": "oct phytops",
        "exit_region": "event_phytops",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Defeat Skeldritch": {
        "two_way": False,
        "entrance_region": "skeldritch",
        "exit_region": "skeldritch event",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Reach ToS 3F": {
        "two_way": False,
        "entrance_region": "tos 3f rail map",
        "exit_region": "event_3f",
        "entrance": (0x13, 0x2, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Reach ToS 7F": {
        "two_way": False,
        "entrance_region": "tos 7f rail map",
        "exit_region": "event_7f",
        "entrance": (0x13, 0x6, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Reach ToS 12F": {
        "two_way": False,
        "entrance_region": "tos 11f",
        "exit_region": "event_12f",
        "entrance": (0x13, 0xB, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Reach ToS 17F": {
        "two_way": False,
        "entrance_region": "tos 16f",
        "exit_region": "event_17f",
        "entrance": (0x13, 0xF, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Defeat Staven": {
        "two_way": False,
        "entrance_region": "tos staven",
        "exit_region": "event_staven",
        "entrance": (0x23, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Reach ToS 24F": {
        "two_way": False,
        "entrance_region": "tos 24f",
        "exit_region": "event_24f",
        "entrance": (0x13, 0x23, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },

    "GOAL: Defeat Stagnox": {
        "two_way": False,
        "entrance_region": "wt stagnox",
        "exit_region": "goal_stagnox",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Fraaz": {
        "two_way": False,
        "entrance_region": "bt fraaz",
        "exit_region": "goal_fraaz",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Reach ToS 3F": {
        "two_way": False,
        "entrance_region": "tos 3f rail map",
        "exit_region": "goal_forest_glyph",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Reach ToS 7F": {
        "two_way": False,
        "entrance_region": "tos 7f rail map",
        "exit_region": "goal_snow_glyph",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Malladus": {
        "two_way": False,
        "entrance_region": "malladus 2",
        "exit_region": "malladus event",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },

    # Order later
    "Tower of Spirits Enter Section 1": {
        "return_name": "ToS 1F Exit",
        "entrance": (0x17, 0, 1),
        "exit": (0x13, 0x0, 0),
        "entrance_region": "tos",
        "exit_region": "tos 1f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Enter Section 2": {
        "return_name": "ToS 4F Exit",
        "entrance": (0x17, 0, 2),
        "exit": (0x13, 0x3, 0),
        "entrance_region": "tos 2",
        "exit_region": "tos 4f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Enter Section 3": {
        "return_name": "ToS 8F Exit",
        "entrance": (0x17, 0, 3),
        "exit": (0x13, 0x7, 0),
        "entrance_region": "tos 3",
        "exit_region": "tos 8f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    # More ToS Entrances
    "Tower of Spirits Enter Section 4": {
        "return_name": "ToS 13F Exit",
        "entrance": (0x17, 0, 4),
        "exit": (0x13, 0xC, 0),
        "entrance_region": "tos 4",
        "exit_region": "tos 13f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Enter Section 5": {
        "return_name": "ToS 18F Exit",
        "entrance": (0x17, 0, 5),
        "exit": (0x13, 0x11, 0),
        "entrance_region": "tos 5",
        "exit_region": "tos 18f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Exit Staven": {
        "return_name": "ToS Summit Lower Exit",
        "entrance": (0x23, 0, 1),
        "exit": (0x15, 0x0, 0),
        "entrance_region": "tos staven",
        "exit_region": "tos summit lower",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Summit Enter Altar": {
        "return_name": "ToS 30F Exit",
        "entrance": (0x15, 0, 2),
        "exit": (0x13, 0x1d, 0),
        "entrance_region": "tos 6",
        "exit_region": "tos 30f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },

    "Forest Sanctuary Enter Sanctuary": {
        "return_name": "Gage Exit",
        "entrance": (0x30, 0, 1),
        "exit": (0x30, 0x1, 0),
        "entrance_region": "fos",
        "exit_region": "fos song statue",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "Snow Sanctuary Enter Inner Sanctuary": {
        "return_name": "Steem Exit",
        "entrance": (0x31, 1, 1),
        "exit": (0x31, 0x2, 0),
        "entrance_region": "ss",
        "exit_region": "ss song",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "ToS 3F Blue Portal": {
        "two_way": False,
        "entrance": (0x13, 2, 0),
        "exit": (0x14, 0x1, 3),
        "entrance_region": "tos 3f rail map",
        "exit_region": "tos",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "ToS 7F Blue Portal": {
        "two_way": False,
        "entrance": (0x13, 6, 0),
        "exit": (0x14, 0x1, 3),
        "entrance_region": "tos 7f rail map",
        "exit_region": "tos",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "ToS 12F Blue Portal": {
        "two_way": False,
        "entrance": (0x13, 0xB, 0),
        "exit": (0x14, 0x1, 3),
        "entrance_region": "tos 11f",
        "exit_region": "tos",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "ToS 17F Blue Portal": {
        "two_way": False,
        "entrance": (0x13, 0xF, 0),
        "exit": (0x14, 0x1, 3),
        "entrance_region": "tos 16f",
        "exit_region": "tos",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "ToS 24F Blue Portal": {
        "two_way": False,
        "entrance": (0x13, 0x23, 0),
        "exit": (0x14, 0x1, 1),
        "entrance_region": "tos 24f",
        "exit_region": "tos",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "ToS 23F Blue Warp Before Staven": {
        "return_name": "ToS Top of Staircase Blue Warp",
        "entrance": (0x13, 0x14, 2),
        "exit": (0x17, 0x0, 6),
        "entrance_region": "tos 22f",
        "exit_region": "tos 5",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Marine Temple 6F Boss Door Staircase": {
        "return_name": "Marine Temple 7F Exit",
        "entrance": (0x1b, 0x5, 3),
        "exit": (0x1b, 0x6, 0),
        "entrance_region": "oct 6f chest",
        "exit_region": "oct phytops",
        "type": EntranceGroups.DUNGEON_ROOM,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # Linebeck/bridge worker events
    "EVENT: Give Regal Ring to Linebeck": {
        "two_way": False,
        "entrance_region": "linebeck trading",
        "exit_region": "linebeck event",
        "entrance": (0x37, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Desert Temple Enter Boss": {
        "return_name": "Skeldritch Exit",
        "entrance_region": "dt b2",
        "exit_region": "skeltritch",
        "entrance": (0x1D, 0x4, 0x1),
        "exit": (0x22, 0x0, 0),
        "type": EntranceGroups.BOSS,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "Desert Temple Enter Post-Fight": {
        "return_name": "Skeldritch Post-Fight Exit",
        "entrance_region": "dt b2",
        "exit_region": "skeltritch",
        "entrance": (0x1D, 0x4, 0x1),
        "exit": (0x22, 0x1, 0),
        "type": EntranceGroups.BOSS,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },


}


ENTRANCES = STTransition.from_data(ENTRANCE_DATA)
entrance_id_to_entrance = {e.id: e for e in ENTRANCES.values()}
entrance_id_to_region = {e.id: e.entrance_region for e in ENTRANCES.values()}

location_event_lookup = {"Wooded Temple Dungeon Reward": "EVENT: Defeat Stagnox",
                         "Blizzard Temple Dungeon Reward": "EVENT: Defeat Fraaz",
                         "ToS 3F Forest Rail Glyph": "EVENT: Reach ToS 3F",
                         "ToS 7F Snow Rail Glyph": "EVENT: Reach ToS 7F",
                         "ToS 12F Ocean Rail Glyph": "EVENT: Reach ToS 12F",
                         "ToS 17F Fire Rail Glyph": "EVENT: Reach ToS 17F",
                         "ToS 23F Defeat Staven": "EVENT: Defeat Staven",
                         "ToS 24F Final Chest": "EVENT: Reach ToS 24F",
                         "Marine Temple Dungeon Reward": "EVENT: Defeat Cactops",
                         "Desert Temple Dungeon Reward": "EVENT: Defeat Skeldritch"}
goal_event_lookup =     {2: "GOAL: Defeat Stagnox",
                         3: "GOAL: Defeat Fraaz",
                         0: "GOAL: Reach ToS 3F",
                         1: "GOAL: Reach ToS 7F",
                         -1: "GOAL: Defeat Malladus"}