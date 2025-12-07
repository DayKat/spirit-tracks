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
}


ENTRANCES = STTransition.from_data(ENTRANCE_DATA)