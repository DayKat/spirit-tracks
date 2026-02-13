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
        "return_name": "Fire Realm Portal",
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
        "return_name": "Fire Realm Portal 2",
        "entrance": (0x4, 0, 0xC),
        "exit": (0x7, 0x0, 0x12),
        "entrance_region": "forest cave tracks",
        "exit_region": "fire realm",
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
    "EVENT: Reach ToS 3F": {
        "two_way": False,
        "entrance_region": "tos 3f rail map",
        "exit_region": "event_3f",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Reach ToS 7F": {
        "two_way": False,
        "entrance_region": "tos 7f rail map",
        "exit_region": "event_7f",
        "entrance": (0x29, 0x0, 0x0),
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
        "exit_region": "malladus goal",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
}


ENTRANCES = STTransition.from_data(ENTRANCE_DATA)
entrance_id_to_entrance = {e.id: e for e in ENTRANCES.values()}
entrance_id_to_region = {e.id: e.entrance_region for e in ENTRANCES.values()}

location_event_lookup = {"Wooded Temple Dungeon Reward": "EVENT: Defeat Stagnox",
                         "Blizzard Temple Dungeon Reward": "EVENT: Defeat Fraaz",
                         "ToS 3F Forest Rail Glyph": "EVENT: Reach ToS 3F",
                         "ToS 7F Snow Rail Glyph": "EVENT: Reach ToS 7F"}
goal_event_lookup =     {2: "GOAL: Defeat Stagnox",
                         3: "GOAL: Defeat Fraaz",
                         0: "GOAL: Reach ToS 3F",
                         1: "GOAL: Reach ToS 7F",
                         -1: "GOAL: Defeat Malladus"}