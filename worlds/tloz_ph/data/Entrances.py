from enum import IntEnum

class EntranceGroups(IntEnum):
    NONE = 0
    # Directions
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    INSIDE = 5
    OUTSIDE = 6
    # Areas
    HOUSE = 1 << 3
    CAVE = 2 << 3
    ISLAND = 3 << 3
    OVERWORLD = 4 << 3
    DUNGEON_ENTRANCE = 5 << 3
    BOSS = 6 << 3
    DUNGEON_ROOM = 7 << 3
    WARP_PORTAL = 8 << 3
    STAIRS = 9 << 3
    HOLES = 10 << 3
    # Bitmasks
    DIRECTION_MASK = HOUSE - 1
    AREA_MASK = ~0 << 3


OPPOSITE_ENTRANCE_GROUPS = {
    EntranceGroups.RIGHT: EntranceGroups.LEFT,
    EntranceGroups.LEFT: EntranceGroups.RIGHT,
    EntranceGroups.UP: EntranceGroups.DOWN,
    EntranceGroups.DOWN: EntranceGroups.UP,
    0: 0,
    EntranceGroups.NONE: EntranceGroups.NONE,
    EntranceGroups.INSIDE: EntranceGroups.OUTSIDE,
    EntranceGroups.OUTSIDE: EntranceGroups.INSIDE
}

ENTRANCE_DATA = {
    # "Name": {
    #   "return_name": str. what to call the vanilla connecting entrance that generates automatically
    #   "entrance": tuple[int, int, int], stage room entrance. If you come from entrance
    #   "exit": tuple[int, int, int], stage room entrance. What the vanilla game sends you on entering
    #   "entrance_region": str. logic region that the entrance is in
    #   "exit_region": str. logic region it leads to in
    #   "coords": tuple[int, int, int]. x, y, z. Where to place link on a continuous transition. y value is also used
    #       to differentiate transitions at different heights
    #   "extra_data": dict[str: int]. additional coordinate data for continuous boundaries, like "x_max" etc.
    #   "type": EntranceGroup. Entrance group entrance type (house, cave, sea etc)
    #   "direction": EntranceGroup. Entrance group direction
    #   "two_way": bool=True. generates a reciprocal entrance, also used for ER generation
    # }

    "Mercay SW Oshus": {
        "return_name": "Oshus House",
        "entrance": (0xB, 0, 2),
        "exit": (0xB, 0xA, 1),
        "entrance_region": "mercay sw",
        "exit_region": "mercay oshus",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "two_way": True
    },
    "Mercay SW Apricot": {
        "return_name": "Apricot House",
        "entrance": (0xB, 0x0, 3),
        "exit": (0xB, 0xB, 1),
        "entrance_region": "mercay sw",
        "exit_region": "mercay apricot",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "two_way": True
    },
    "Mercay SW Sword Cave": {
        "return_name": "Inside Sword Cave",
        "entrance": (0xB, 0x0, 4),
        "exit": (0xB, 0x13, 1),
        "entrance_region": "mercay sw",
        "exit_region": "mercay sword cave",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
    },
    "Mercay SW North": {
        "return_name": "Mercay NW South",
        "entrance": (0xB, 0x0, 0xFC),
        "exit": (0xB, 0x1, 0xFB),
        "coords": (-164000, -164, 16000),  # The coord that doesn't matter doesn't matter. Y level diferentiates exit
        "entrance_region": "mercay sw",
        "exit_region": "mercay nw",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Mercay SW East": {
        "return_name": "Mercay SE West",
        "entrance": (0xB, 0x0, 0xFD),
        "exit": (0xB, 0x3, 0xFE),
        "coords": (4780, -164, 53300),
        "entrance_region": "mercay sw bridge",
        "exit_region": "mercay se",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Mercay SE Milk Bar": {
        "return_name": "Inside Milk Bar",
        "entrance": (0xB, 0x3, 0x3),
        "exit": (0xB, 0xC, 0x0),
        "entrance_region": "mercay se",
        "exit_region": "mercay milk bar",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Mercay SE Shipyard": {
        "return_name": "Inside Shipyard",
        "entrance": (0xB, 0x3, 0x4),
        "exit": (0xB, 0xD, 0x0),
        "entrance_region": "mercay se",
        "exit_region": "mercay shipyard",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Mercay SE Tuzi": {
        "return_name": "Tuzi House",
        "entrance": (0xB, 0x3, 0x5),
        "exit": (0xB, 0xE, 0x0),
        "entrance_region": "mercay se",
        "exit_region": "mercay tuzi",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Mercay SE Treasure Teller": {
        "return_name": "Treasure Teller House",
        "entrance": (0xB, 0x3, 0x6),
        "exit": (0xB, 0xF, 0x0),
        "entrance_region": "mercay se",
        "exit_region": "mercay treasure teller",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Mercay SE Shop": {
        "return_name": "Inside Mercay Shop",
        "entrance": (0xB, 0x3, 0x7),
        "exit": (0xB, 0x11, 0x1),
        "entrance_region": "mercay se",
        "exit_region": "mercay shop",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },

    # =========== TotOK ==============
    "Mercay NW TotOK": {
        "return_name": "TotOK Lobby Entrance",
        "entrance": (0xB, 0x1, 0x2),
        "exit": (0x26, 0x00, 0x1),
        "entrance_region": "mercay island",
        "exit_region": "totok",
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "direction": EntranceGroups.UP,
    },

    # =========== Ember Island ================
    "Ember Port House": {
        "return_name": "Inside Ember Port House",
        "entrance": (0xD, 0x0, 0x2),
        "exit": (0xD, 0xB, 0x0),
        "entrance_region": "ember port",
        "exit_region": "ember port house",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Ember Astrid House": {
        "return_name": "Inside Astrid House",
        "entrance": (0xD, 0x0, 0x1),
        "exit": (0xD, 0xA, 0x0),
        "entrance_region": "ember port",
        "exit_region": "ember astrid",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Astrid House Stairs": {
        "return_name": "Astrid Basement",
        "entrance": (0xD, 0xA, 0x1),
        "exit": (0xD, 0x14, 0x0),
        "entrance_region": "ember astrid",
        "exit_region": "ember astrid basement",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.OUTSIDE,
    },
    "Ember Kayo House": {
        "return_name": "Inside Kayo House",
        "entrance": (0xD, 0x0, 0x3),
        "exit": (0xD, 0xC, 0x0),
        "entrance_region": "ember port",
        "exit_region": "ember kayo",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Ember West Coast South": {
        "return_name": "Ember East Coast South",
        "entrance": (0xD, 0x0, 0xFD),
        "exit": (0xD, 0x1, 0xFE),
        "coords": (-4500, -164, 80000),
        "extra_data": {"z_min": 0},
        "entrance_region": "ember port",
        "exit_region": "ember coast east",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ember West Coast North": {
        "return_name": "Ember East Coast North",
        "entrance": (0xD, 0x0, 0xFD),
        "exit": (0xD, 0x1, 0xFE),
        "coords": (-4500, -164, -85000),
        "extra_data": {"z_max": 0},
        "entrance_region": "ember coast north",
        "exit_region": "ember coast east",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ember West Climb North": {
        "return_name": "Ember East Climb North",
        "entrance": (0xD, 0x0, 0xFD),
        "exit": (0xD, 0x1, 0xFE),
        "coords": (-4500, 4751, -65000),
        "extra_data": {"z_max": 0},
        "entrance_region": "ember port",
        "exit_region": "ember climb east",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ember West Climb South": {
        "return_name": "Ember East Climb South",
        "entrance": (0xD, 0x0, 0xFD),
        "exit": (0xD, 0x1, 0xFE),
        "coords": (-4500, 4751, 50000),
        "extra_data": {"z_min": 0},
        "entrance_region": "ember climb west",
        "exit_region": "ember coast east",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ember West Heights North": {
        "return_name": "Ember East Heights North",
        "entrance": (0xD, 0x0, 0xFD),
        "exit": (0xD, 0x1, 0xFE),
        "coords": (-4500, 9666, -50000),
        "extra_data": {"z_max": 0},
        "entrance_region": "ember climb west",
        "exit_region": "ember outside tof",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ember West Heights South": {
        "return_name": "Ember East Heights South",
        "entrance": (0xD, 0x0, 0xFD),
        "exit": (0xD, 0x1, 0xFE),
        "coords": (-4500, 9666, 25000),
        "extra_data": {"z_min": 0},
        "entrance_region": "ember summit west",
        "exit_region": "ember outside tof",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ember West Summit North": {
        "return_name": "Ember East Summit North",
        "entrance": (0xD, 0x0, 0xFD),
        "exit": (0xD, 0x1, 0xFE),
        "coords": (-4500, 14582, -35000),
        "extra_data": {"z_max": 0},
        "entrance_region": "ember summit west",
        "exit_region": "ember summit north",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ember West Summit South": {
        "return_name": "Ember East Summit South",
        "entrance": (0xD, 0x0, 0xFD),
        "exit": (0xD, 0x1, 0xFE),
        "coords": (-4500, 14582, 8000),
        "extra_data": {"z_min": 0},
        "entrance_region": "ember summit west",
        "exit_region": "ember summit east",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },

    # ========== Temple of Fire ============
    "Ember Enter Temple": {
        "return_name": "ToF Entrance",
        "entrance": (0xD, 0x1, 0x0),
        "exit": (0x1C, 0x0, 0x0),
        "entrance_region": "ember outside tof",
        "exit_region": "tof 1f",
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "direction": EntranceGroups.UP,
        },
    "ToF Blaaz Warp": {
        "entrance": (0x2B, 0x0, 0x0),
        "exit": (0xD, 0x1, 0x0),
        "entrance_region": "tof blaaz",
        "exit_region": "ember outside tof",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.NONE,
        "two_way": False
    },
    # ========== Gust ============

    "Fake temp": {
        "return_name": "Temp Fake",
        "entrance": (0x40, 0x1, 0x0),
        "exit": (0x40, 0x0, 0x0),
        "entrance_region": "nope",
        "exit_region": "epon",
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.NONE,
        },


        # ========== Temple of Wind ============
    "Gust Enter Temple": {
        "return_name": "ToW Entrance",
        "entrance": (0xE, 0x1, 0x0),
        "exit": (0x1D, 0x0, 0x0),
        "entrance_region": "gust dig",
        "exit_region": "tow",
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "direction": EntranceGroups.UP,
        },
    "ToW Cyclok Warp": {
        "entrance": (0x2A, 0x0, 0x0),
        "exit": (0xE, 0x1, 0x0),
        "entrance_region": "tow cyclok",
        "exit_region": "gust dig",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.NONE,
        "two_way": False
    },
    # ========== Molida ============
    "Molida Port House": {
        "return_name": "Molida Inside Port House",
        "entrance": (0xC, 0x0, 0x4),
        "exit": (0xC, 0xC, 0x1),
        "entrance_region": "molida island",
        "exit_region": "molida port house",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },

        # ========== Temple of Courage ============
    "Molida Enter Temple": {
        "return_name": "ToC Entrance",
        "entrance": (0xC, 0x1, 0x3),
        "exit": (0x1E, 0x0, 0x0),
        "entrance_region": "toc gates",
        "exit_region": "toc",
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "direction": EntranceGroups.UP,
    },
    "ToC Crayk Warp": {
        "entrance": (0x2C, 0x0, 0x0),
        "exit": (0xC, 0x1, 0x4),
        "entrance_region": "toc crayk",
        "exit_region": "toc gates",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.NONE,
        "two_way": False
    },

    # ========== Goron ============
    "Goron Port House": {
        "return_name": "Goron Inside Port House",
        "entrance": (0x10, 0x2, 0x1),
        "exit": (0x10, 0xB, 0x0),
        "entrance_region": "goron",
        "exit_region": "goron port house",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },

    # ========== Goron Temple ============
    "Goron Enter Temple": {
        "return_name": "GT Entrance",
        "entrance": (0x10, 0x0, 0x0),
        "exit": (0x20, 0x0, 0x0),
        "entrance_region": "goron outside temple",
        "exit_region": "gt",
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "direction": EntranceGroups.UP,
    },
    "GT Dongo Warp": {
        "entrance": (0x20, 0xA, 0x0),
        "exit": (0x10, 0x0, 0x1),
        "entrance_region": "gt dongo",
        "exit_region": "goron outside temple",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.NONE,
        "two_way": False
    },
    # ========== Frost ============
    "Frost Smart House": {
        "return_name": "Frost Inside Smart House",
        "entrance": (0xF, 0x0, 0x2),
        "exit": (0xF, 0xB, 0x0),
        "entrance_region": "iof",
        "exit_region": "iof smart house",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },


    # ========== Temple of Ice ============
    "Frost Enter Temple": {
        "return_name": "ToI Entrance",
        "entrance": (0xF, 0x1, 0x0),
        "exit": (0x1F, 0x0, 0x0),
        "entrance_region": "iof yook",
        "exit_region": "toi",
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "direction": EntranceGroups.UP,
    },
    "ToI Gleeok Warp": {
        "entrance": (0x1f, 0x6, 0x0),
        "exit": (0xF, 0x1, 0x0),
        "entrance_region": "toi gleeok",
        "exit_region": "iof yook",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.NONE,
        "two_way": False
    },
    # ========== Ruins ============
    "Ruins Port Cave": {
        "return_name": "Ruins Geozard Cave East Exit",
        "entrance": (0x11, 0x0, 0x2),
        "exit": (0x11, 0xA, 0x1),
        "entrance_region": "ruins port",
        "exit_region": "ruins geozard cave east",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
    },


    # ========== Mutoh's Temple ============
    "Ruins Enter Temple": {
        "return_name": "MT Entrance",
        "entrance": (0x12, 0x2, 0x2),
        "exit": (0x21, 0x0, 0x1),
        "entrance_region": "ruins water",
        "exit_region": "mutoh",
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "direction": EntranceGroups.UP,
    },
    "MT Eox Warp": {
        "entrance": (0x21, 0x6, 0x0),
        "exit": (0x12, 0x2, 0x2),
        "entrance_region": "mutoh eox",
        "exit_region": "ruins water",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.NONE,
        "two_way": False
    },

    # ============= SW Ocean ==================

    "Ocean SW Mercay": {
        "return_name": "Mercay SE Boat",
        "entrance": (0x0, 0x0, 0x2),
        "exit": (0xB, 0x3, 0x2),
        "entrance_region": "mercay boat",
        "exit_region": "mercay se",
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean SW Cannon": {
        "return_name": "Cannon Boat",
        "entrance_region": "cannon boat",
        "exit_region": "cannon island",
        "entrance": (0x0, 0x0, 0x4),
        "exit": (0x13, 0x0, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean SW Ember": {
        "return_name": "Ember Boat",
        "entrance_region": "ember boat",
        "exit_region": "ember port",
        "entrance": (0x0, 0x0, 0x3),
        "exit": (0xD, 0x0, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean SW Molida": {
        "return_name": "Molida Boat",
        "entrance_region": "molida boat",
        "exit_region": "molida island",
        "entrance": (0x0, 0x0, 0x1),
        "exit": (0xC, 0x0, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean SW Spirit": {
        "return_name": "Spirit Boat",
        "entrance_region": "spirit boat",
        "exit_region": "spirit island",
        "entrance": (0x0, 0x0, 0x5),
        "exit": (0x17, 0x0, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },

    # ============= NW Ocean ==================

    "Ocean NW Gust": {
        "return_name": "Gust Boat",
        "entrance_region": "gust boat",
        "exit_region": "gust",
        "entrance": (0x0, 0x1, 0x0),
        "exit": (0xE, 0x0, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean NW Bannan": {
        "return_name": "Bannan Boat",
        "entrance_region": "bannan boat",
        "exit_region": "bannan",
        "entrance": (0x0, 0x1, 0x3),
        "exit": (0x14, 0x0, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean NW Zauz": {
        "return_name": "Zauz Boat",
        "entrance_region": "zauz boat",
        "exit_region": "zauz island",
        "entrance": (0x0, 0x1, 0x4),
        "exit": (0x16, 0x0, 0x1),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean NW Uncharted": {
        "return_name": "Uncharted Boat",
        "entrance_region": "uncharted boat",
        "exit_region": "uncharted",
        "entrance": (0x0, 0x1, 0x7),
        "exit": (0x1A, 0x0, 0x1),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },

    # ============= SE Ocean ==================

    "Ocean SE Goron": {
        "return_name": "Goron Boat",
        "entrance_region": "goron boat",
        "exit_region": "goron",
        "entrance": (0x0, 0x2, 0x2),
        "exit": (0x10, 0x2, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean SE Harrow": {
        "return_name": "Harrow Boat",
        "entrance_region": "harrow boat",
        "exit_region": "harrow",
        "entrance": (0x0, 0x2, 0x4),
        "exit": (0x18, 0x0, 0x1),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean SE Dee Ess": {
        "return_name": "Dee Ess Boat",
        "entrance_region": "ds boat",
        "exit_region": "ds",
        "entrance": (0x0, 0x2, 0x5),
        "exit": (0x1B, 0x0, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean SE Frost": {
        "return_name": "Frost Boat",
        "entrance_region": "frost boat",
        "exit_region": "iof",
        "entrance": (0x0, 0x2, 0x3),
        "exit": (0xF, 0x0, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },

    # ============= NE Ocean ==================

    "Ocean NE Dead": {
        "return_name": "Dead Boat",
        "entrance_region": "dead boat",
        "exit_region": "iotd",
        "entrance": (0x0, 0x3, 0x1),
        "exit": (0x15, 0x0, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean NE Ruins": {
        "return_name": "Ruins Boat",
        "entrance_region": "ruins boat",
        "exit_region": "ruins port",
        "entrance": (0x0, 0x3, 0x2),
        "exit": (0x11, 0x0, 0x0),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },
    "Ocean NE Maze": {
        "return_name": "Maze Boat",
        "entrance_region": "maze boat",
        "exit_region": "maze",
        "entrance": (0x0, 0x3, 0x3),
        "exit": (0x19, 0x0, 0x1),
        "extra_data": {"conditional": ["need_sea_chart"]},
        "type": EntranceGroups.ISLAND,
        "direction": EntranceGroups.INSIDE,
    },

    # More ruins
    "Ruins Port Cliff Cave": {
        "return_name": "Ruins Geozard Cave Exit West",
        "entrance_region": "ruins sw maze upper",
        "exit_region": "ruins geozard cave west",
        "entrance": (0x11, 0x0, 0x3),
        "exit": (0x11, 0xA, 0x2),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
    },
    "Ruins SW Maze Lower North": {
        "return_name": "Ruins NW Maze Chest South",
        "entrance_region": "ruins sw maze lower",
        "exit_region": "ruins nw maze lower chest",
        "entrance": (0x12, 0x0, 0xFC),
        "exit": (0x12, 0x1, 0xFB),
        "coords": (-63750, -164, -4815),
        "extra_data": {"conditional": ["ruins_water"]},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Ruins SW Lower Maze Exit": {
        "return_name": "Ruins NW Lower Maze Exit",
        "entrance_region": "ruins sw maze lower exit",
        "exit_region": "ruins nw maze lower exit",
        "entrance": (0x11, 0x0, 0xFC),
        "exit": (0x11, 0x1, 0xFB),
        "coords": (-194200, 9666, -4815),
        "extra_data": {"x_max": -150000},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Ruins SW Port Cliff North": {
        "return_name": "Ruins NW Port Cliff South",
        "entrance_region": "ruins sw port cliff",
        "exit_region": "ruins nw port cliff",
        "entrance": (0x11, 0x0, 0xFC),
        "exit": (0x11, 0x1, 0xFB),
        "coords": (-46050, 4751, -4815),
        "extra_data": {"x_min": -70000},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Ruins SW Upper Maze Exit": {
        "return_name": "Ruins NW Upper Maze Exit",
        "entrance_region": "ruins sw maze upper",
        "exit_region": "ruins nw maze upper exit",
        "entrance": (0x11, 0x0, 0xFC),
        "exit": (0x11, 0x1, 0xFB),
        "coords": (-174425, 4751, -4815),
        "extra_data": {"x_max": -70000},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Ruins NW Pyramid": {
        "return_name": "Bremeur Exit",
        "entrance_region": "ruins nw boulders",
        "exit_region": "bremeur",
        "entrance": (0x11, 0x1, 0x1),
        "exit": (0x24, 0x0, 0x1),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Ruins NW Cave": {
        "return_name": "Ruins Cave Exit",
        "entrance_region": "ruins nw across bridge",
        "exit_region": "ruins nw cave",
        "entrance": (0x12, 0x1, 0x2),
        "exit": (0x12, 0xB, 0x1),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
    },
    "Ruins NW Across Bridge East": {
        "return_name": "Ruins NE Doylan Bridge One-Way West",
        "entrance_region": "ruins nw across bridge",
        "exit_region": "ruins ne enter upper",
        "entrance": (0x11, 0x1, 0xFD),
        "exit": (0x11, 0x2, 0xFE),
        "coords": (4784, 9666, -62640),
        "extra_data": {"z_min": -110000},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ruins NE East Pyramid": {
        "return_name": "Doylan's Exit",
        "entrance_region": "ruins ne doylan bridge",
        "exit_region": "doylan temple",
        "entrance": (0x11, 0x2, 0x1),
        "exit": (0x22, 0x0, 0x1),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Doylan's Staircase": {
        "return_name": "Doylan's Chamber Exit",
        "entrance_region": "doylan temple",
        "exit_region": "doylan chamber",
        "entrance": (0x22, 0x0, 0x2),
        "exit": (0x22, 0x1, 0x1),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Ruins SE Coast North": {
        "return_name": "Ruins NE Coast South",
        "entrance_region": "ruins se coast",
        "exit_region": "ruins ne behind temple",
        "entrance": (0x12, 0x3, 0xFC),
        "exit": (0x12, 0x2, 0xFB),
        "coords": (213590, -164, 4784),
        "extra_data": {"x_min": 144990,
                       "conditional": ["ruins_water"]},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Ruins NW Upper One-Way East": {
        "return_name": "Ruins NE Doylan's Bridge Exit West",
        "entrance_region": "ruins nw return",
        "exit_region": "ruins ne doylan bridge",
        "entrance": (0x11, 0x1, 0xFD),
        "exit": (0x11, 0x2, 0xFE),
        "coords": (4784, 9666, -150700),
        "extra_data": {"z_max": -110000},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ruins NW Alcove East": {
        "return_name": "Ruins NE Lower East South",
        "entrance_region": "ruins nw alcove",
        "exit_region": "ruins ne lower",
        "entrance": (0x12, 0x1, 0xFD),
        "exit": (0x12, 0x2, 0xFE),
        "coords": (8192, -164, -43675),
        "extra_data": {"z_min": -80000,
                       "conditional": ["ruins_water"]},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ruins NW Lower East": {
        "return_name": "Ruins NE Lower East North",
        "entrance_region": "ruins nw lower",
        "exit_region": "ruins ne lower",
        "entrance": (0x12, 0x1, 0xFD),
        "exit": (0x12, 0x2, 0xFE),
        "coords": (4784, -164, -120000),
        "extra_data": {"z_max": -80000,
                       "conditional": ["ruins_water"]},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ruins SE North West": {
        "return_name": "Ruins NE South",
        "entrance_region": "ruins se lower",
        "exit_region": "ruins ne lower",
        "entrance": (0x12, 0x3, 0xFC),
        "exit": (0x12, 0x2, 0xFB),
        "coords": (13000, -164, 4784),
        "extra_data": {"x_max": 70000,
                       "conditional": ["ruins_water"]},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Ruins SE North Secret": {
        "return_name": "Ruins NE Secret Chest South",
        "entrance_region": "ruins se lower",
        "exit_region": "ruins ne secret chest",
        "entrance": (0x12, 0x3, 0xFC),
        "exit": (0x12, 0x2, 0xFB),
        "coords": (100700, -164, 4784),
        "extra_data": {"x_min": 70000,
                       "x_max": 101000,
                       "conditional": ["ruins_water"]},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Ruins SW East": {
        "return_name": "Ruins SE Shortcut Bridge",
        "entrance_region": "ruins sw port cliff",
        "exit_region": "ruins se return bridge west",
        "entrance": (0x11, 0x0, 0xFD),
        "exit": (0x11, 0x3, 0xFE),
        "coords": (4784, 9666, 51500),
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Ruins SE Pyramid": {
        "return_name": "Max's Exit",
        "entrance_region": "ruins se outside max",
        "exit_region": "max",
        "entrance": (0x12, 0x3, 0x1),
        "exit": (0x23, 0x0, 0x1),
        "extra_data": {"conditional": ["ruins_water"]},
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Ruins SE Path to Temple North": {
        "return_name": "Ruins NE Path to Temple South",
        "entrance_region": "ruins se path to temple",
        "exit_region": "ruins ne geozards",
        "entrance": (0x12, 0x3, 0xFC),
        "exit": (0x12, 0x2, 0xFB),
        "coords": (123000, -164, 4784),
        "extra_data": {"x_max": 140000,
                       "x_min": 101000,
                       "conditional": ["ruins_water"]},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },

# ===== Gust =====
    "Gust West Coast North": {
        "return_name": "Gust West Coast South",
        "entrance_region": "gust west ledge",
        "exit_region": "gust nw",
        "entrance": (0xE, 0x0, 0xFC),
        "exit": (0xE, 0x1, 0xFB),
        "coords": (-76000, 9666, -8192),
        "extra_data": {"x_max": -67000},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Gust West Inland North": {
        "return_name": "Gust West Inland South",
        "entrance_region": "gust west",
        "exit_region": "gust above temple",
        "entrance": (0xE, 0x0, 0xFC),
        "exit": (0xE, 0x1, 0xFB),
        "coords": (-48500, 9666, -8192),
        "extra_data": {"x_min": -56000,
                       "x_max": -40000},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Gust Above Temple North": {
        "return_name": "Gust Above Temple South",
        "entrance_region": "gust cliffs",
        "exit_region": "gust above temple",
        "entrance": (0xE, 0x0, 0xFC),
        "exit": (0xE, 0x1, 0xFB),
        "coords": (-17000, 9666, -8192),
        "extra_data": {"x_min": -25000},
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Gust Temple Road North": {
        "return_name": "Gust Temple Road South",
        "entrance_region": "gust cliffs",
        "exit_region": "gust temple road",
        "entrance": (0xE, 0x0, 0xFC),
        "exit": (0xE, 0x1, 0xFB),
        "coords": (4452, 4751, -8192),
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Gust Cave East": {
        "return_name": "Gust Miblin Cave Exit East",
        "entrance_region": "gust cliffs",
        "exit_region": "gust cave",
        "entrance": (0xE, 0x0, 0x4),
        "exit": (0xE, 0xB, 0x2),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.INSIDE,
    },
    "Gust Cave West": {
        "return_name": "Gust Miblin Cave Exit West",
        "entrance_region": "gust south",
        "exit_region": "gust cave",
        "entrance": (0xE, 0x0, 0x3),
        "exit": (0xE, 0xB, 0x1),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.INSIDE,
    },
    "Gust Hideout Cave": {
        "return_name": "Gust Hideout Exit",
        "entrance_region": "gust south",
        "exit_region": "gust hideout",
        "entrance": (0xE, 0x0, 0x2),
        "exit": (0xE, 0xA, 0x1),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.INSIDE,
    },

}

OPPOSITES = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}

class PhantomHourglassEntrance(object):

    def __init__(self, name, data):
        self.data = data

        self.name: str = name
        self.id: int | None = data.get("id", None)
        self.entrance: tuple = data["entrance"]
        self.exit: tuple = data["exit"]
        self.entrance_region: str = data["entrance_region"]
        self.exit_region: str = data["exit_region"]
        self.two_way: bool = data.get("two_way", True)
        self.category_group = data["type"]
        self.direction = data["direction"]
        self.coords: tuple | None = data.get("coords", None)
        self.extra_data: dict = data.get("extra_data", {})

        self.stage, self.room, _ = self.entrance
        self.scene: int = self.get_scene()
        self.exit_scene: int = self.get_exit_scene()
        self.exit_stage = self.exit[0]
        self.y = self.coords[1] if self.coords else None

        self.vanilla_reciprocal = None  # Paired location

        self.copy_number = 0

    def get_scene(self):
        return self.stage * 0x100 + self.room

    def get_exit_scene(self):
        return self.exit[0] * 0x100 + self.exit[1]

    def is_pairing(self, r1, r2) -> bool:
        return r1 == self.entrance_region and r2 == self.exit_region

    def get_y(self):
        return self.coords[1] if self.coords else None

    def detect_exit_simple(self, stage, room, entrance):
        return self.exit == (stage, room, entrance)

    def detect_exit_scene(self, scene, entrance):
        return self.exit_scene == scene and entrance == self.exit[2]

    def detect_exit(self, scene, entrance, coords, y_offest):
        if self.detect_exit_scene(scene, entrance):
            if entrance < 0xF0:
                return True
            # Continuous entrance check
            x_max = self.extra_data.get("x_max", 0x8FFFFFFF)
            x_min = self.extra_data.get("x_min", -0x8FFFFFFF)
            z_max = self.extra_data.get("z_max", 0x8FFFFFFF)
            z_min = self.extra_data.get("z_min", -0x8FFFFFFF)
            y = self.coords[1] if self.coords else coords["y"] - y_offest
            if coords["y"] - y_offest == y and x_max > coords["x"] > x_min and z_max > coords["z"] > z_min:
                return True
        return False

    def set_stage(self, new_stage):
        self.stage = new_stage
        self.scene = self.get_scene()
        self.entrance = tuple([new_stage] + list(self.entrance[1:]))

    def set_exit_stage(self, new_stage):
        self.exit = tuple([new_stage] + list(self.exit[1:]))
        self.exit_scene = self.get_exit_scene()
        self.exit_stage = self.exit[0]

    def copy(self):
        res = PhantomHourglassEntrance(f"{self.name}{self.copy_number+1}", self.data)
        res.copy_number = self.copy_number + 1
        return res

    def __str__(self):
        return self.name

    def debug_print(self):
        print(f"Debug print for entrance {self.name}")
        print(f"\tentrance {self.entrance}")
        print(f"\texit {self.exit}")
        print(f"\tcoords {self.coords}")
        print(f"\textra_data {self.extra_data}")




ENTRANCES: dict[str, "PhantomHourglassEntrance"] = {}
counter = {}
i = 0
for name, data in ENTRANCE_DATA.items():
    ENTRANCES[name] = PhantomHourglassEntrance(name, data)
    ENTRANCES[name].id = i
    # print(f"{i} {ENTRANCES[name]['entrance_region']} -> {ENTRANCES[name]['exit_region']}")
    i += 1
    point = data["entrance_region"] + "<=>" + data["exit_region"]
    counter.setdefault(point, 0)
    counter[point] += 1

    if data.get("two_way", True):
        reverse_name = data.get("return_name", f"Unnamed Entrance {i}")
        reverse_data = {
            "entrance_region": data.get("reverse_exit_region", data["exit_region"]),
            "exit_region": data.get("reverse_entrance_region", data["entrance_region"]),
            "id": i,
            "entrance": data["exit"],
            "exit": data["entrance"],
            "two_way": True,
            "type": data["type"],
            "direction": OPPOSITE_ENTRANCE_GROUPS[data["direction"]],
            "coords": data.get("coords", None),
        }
        if "extra_data" in data:
            reverse_data["extra_data"] = data["extra_data"]
        if reverse_name in ENTRANCES:
            print(f"DUPLICATE ENTRANCE!!! {reverse_name}")
        ENTRANCES[reverse_name] = PhantomHourglassEntrance(reverse_name, reverse_data)

        ENTRANCES[name].vanilla_reciprocal = ENTRANCES[reverse_name]
        ENTRANCES[reverse_name].vanilla_reciprocal = ENTRANCES[name]

        # print(f"{i} {ENTRANCES[reverse_name]['entrance_region']} -> {ENTRANCES[reverse_name]['exit_region']}")
        i += 1
        point = reverse_data["entrance_region"] + "<=>" + reverse_data["exit_region"]
        counter.setdefault(point, 0)
        counter[point] += 1


entrance_id_to_region = {d.id: d.entrance_region for d in ENTRANCES.values()}

# print({key: value for key, value in counter.items() if value != 1})



if __name__ == "__main__":
    for name, data in ENTRANCES.items():
        print(f"{name}:", "{")
        for k, v in data.items():
            print(f"\t{k}: {v}")
        print("},")
