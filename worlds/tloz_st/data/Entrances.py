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

    # Outset
    "Outset West House": {
        "return_name": "Niko's House Exit",
        "exit": (0x2F, 0xA, 1),
        "entrance": (0x2F, 0x0, 1),
        "exit_region": "niko's house",
        "entrance_region": "outset village",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Outset East House": {
        "return_name": "Mary's House Exit",
        "exit": (0x2F, 0xC, 0),
        "entrance": (0x2F, 0x0, 3),
        "exit_region": "mary's house",
        "entrance_region": "outset village",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Outset Alfonzo's Workshop": {
        "return_name": "Alfonzo's Workshop Exit",
        "exit": (0x2F, 0xB, 0),
        "entrance": (0x2F, 0x0, 2),
        "exit_region": "train workshop",
        "entrance_region": "outset village",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # Mayscore
    "Mayscore North House": {
        "return_name": "Dovok's House Exit",
        "exit": (0x2A, 0x4, 0),
        "entrance": (0x2A, 0x0, 4),
        "exit_region": "dovok's house",
        "entrance_region": "mayscore",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Mayscore NW House": {
        "return_name": "Morris' House Exit",
        "exit": (0x2A, 0x3, 0),
        "entrance": (0x2A, 0x0, 3),
        "exit_region": "morris' house",
        "entrance_region": "mayscore",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Mayscore NE House": {
        "return_name": "Wood's House Exit",
        "exit": (0x2A, 0x2, 0),
        "entrance": (0x2A, 0x0, 2),
        "exit_region": "wood's house",
        "entrance_region": "mayscore",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Mayscore Shop": {
        "return_name": "Uriko's Shop Exit",
        "exit": (0x2A, 0x5, 0),
        "entrance": (0x2A, 0x0, 1),
        "exit_region": "uriko's shop",
        "entrance_region": "mayscore",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Mayscore North": {
        "return_name": "Mayscore Forest South",
        "exit": (0x38, 0x0, 0),
        "entrance": (0x2A, 0x0, 5),
        "exit_region": "mayscore north",
        "entrance_region": "mayscore",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # Castle Town
    "Castle Town North": {
        "return_name": "Hyrule Castle Courtyard South",
        "exit": (0x28, 0x0, 0),
        "entrance": (0x29, 0x0, 1),
        "exit_region": "hyrule castle courtyard",
        "entrance_region": "castle town",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Castle Town West House": {
        "return_name": "Mona's House Exit",
        "exit": (0x29, 0xc, 0),
        "entrance": (0x29, 0x0, 5),
        "exit_region": "mona's house",
        "entrance_region": "castle town",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Castle Town NW House": {
        "return_name": "Lucia's House Exit",
        "exit": (0x29, 0xE, 0),
        "entrance": (0x29, 0x0, 7),
        "exit_region": "lucia's house",
        "entrance_region": "castle town",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Castle Town Shop": {
        "return_name": "Shitate's Shop Exit",
        "exit": (0x29, 0xA, 0),
        "entrance": (0x29, 0x0, 3),
        "exit_region": "shitate's shop",
        "entrance_region": "castle town",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Castle Town NE House": {
        "return_name": "Milo's House Exit",
        "exit": (0x29, 0xD, 0),
        "entrance": (0x29, 0x0, 6),
        "exit_region": "milo's house",
        "entrance_region": "castle town",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Castle Town Take 'em all On": {
        "return_name": "Take 'em all On Lobby Exit",
        "exit": (0x29, 0xB, 0),
        "entrance": (0x29, 0x0, 4),
        "exit_region": "teao",
        "entrance_region": "castle town",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # Hyrule Castle
    "Hyrule Castle Courtyard Entrance": {
        "return_name": "Hyrule Castle 1F Exit",
        "exit": (0x28, 0x1, 0),
        "entrance": (0x28, 0x0, 1),
        "exit_region": "hyrule castle 1f",
        "entrance_region": "hyrule castle courtyard",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle 1F NW": {
        "return_name": "Hyrule Castle Infirmary Exit",
        "exit": (0x28, 0x3, 1),
        "entrance": (0x28, 0x1, 3),
        "exit_region": "hyrule castle infirmary",
        "entrance_region": "hyrule castle 1f",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle 1F NE": {
        "return_name": "Hyrule Castle Barracks Exit",
        "exit": (0x28, 0x7, 0),
        "entrance": (0x28, 0x1, 2),
        "exit_region": "hyrule castle barracks",
        "entrance_region": "hyrule castle 1f",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle 1F SE": {
        "return_name": "Hyrule Castle Roof SE",
        "exit": (0x28, 0x0, 2),
        "entrance": (0x28, 0x1, 4),
        "exit_region": "hyrule castle roof right",
        "entrance_region": "hyrule castle 1f",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle 1F SW": {
        "return_name": "Hyrule Castle Roof SW",
        "exit": (0x28, 0x0, 3),
        "entrance": (0x28, 0x1, 5),
        "exit_region": "hyrule castle roof left",
        "entrance_region": "hyrule castle 1f",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle 1F Main Staircase": {
        "return_name": "Hyrule Castle Throne Room Exit",
        "exit": (0x28, 0x6, 0),
        "entrance": (0x28, 0x1, 1),
        "exit_region": "hyrule castle throne room",
        "entrance_region": "hyrule castle 1f",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle Roof Central Door": {
        "return_name": "Hyrule Castle 2F Central Exit",
        "exit": (0x28, 0x2, 1),
        "entrance": (0x28, 0x0, 4),
        "exit_region": "hyrule castle 2f",
        "entrance_region": "hyrule castle roof right",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle Roof NE": {
        "return_name": "Hyrule Castle 2F NE Exit",
        "exit": (0x28, 0x2, 4),
        "entrance": (0x28, 0x0, 5),
        "exit_region": "hyrule castle 2f",
        "entrance_region": "hyrule castle ne ledge",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle Zelda's Room Exit": {
        "return_name": "Hyrule Castle 2F NE Staircase",
        "exit": (0x28, 0x2, 3),
        "entrance": (0x28, 0x5, 0),
        "exit_region": "hyrule castle 2f",
        "entrance_region": "zelda's room",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle Throne Room NE": {
        "return_name": "Hyrule Castle 2F NE Door",
        "exit": (0x28, 0x2, 7),
        "entrance": (0x28, 0x6, 2),
        "exit_region": "hyrule castle 2f",
        "entrance_region": "hyrule castle throne room",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle Roof NW": {
        "return_name": "Hyrule Castle 2F NW Exit",
        "exit": (0x28, 0x2, 5),
        "entrance": (0x28, 0x0, 6),
        "exit_region": "hyrule castle 2f",
        "entrance_region": "hyrule castle nw ledge",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle Throne Room NW": {
        "return_name": "Hyrule Castle 2F NW Door",
        "exit": (0x28, 0x2, 6),
        "entrance": (0x28, 0x6, 1),
        "exit_region": "hyrule castle 2f left",
        "entrance_region": "hyrule castle throne room",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle Back Staircase": {
        "return_name": "Hyrule Castle 2F NW Staircase",
        "exit": (0x28, 0x2, 2),
        "entrance": (0x28, 0x1, 7),
        "exit_region": "hyrule castle 2f",
        "entrance_region": "hyrule castle backdoor",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Hyrule Castle Back Exit": {
        "return_name": "Hyrule Castle Backyard Castle",
        "exit": (0x28, 0x4, 0),
        "entrance": (0x28, 0x1, 6),
        "exit_region": "hyrule castle backyard",
        "entrance_region": "hyrule castle backdoor",
        "type": EntranceGroups.CASTLE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    "Hyrule Castle Backyard Cave": {
        "return_name": "Tunnel to the Tower 1F Exit",
        "exit": (0x18, 0x0, 0),
        "entrance": (0x28, 0x4, 1),
        "exit_region": "tower tunnel 1f",
        "entrance_region": "hyrule castle backyard",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Tunnel to the Tower 1F Staircase": {
        "return_name": "Tunnel to the Tower 2F Exit",
        "exit": (0x18, 0x1, 0),
        "entrance": (0x18, 0x0, 1),
        "exit_region": "tower tunnel key door",
        "entrance_region": "tower tunnel 2f",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Tunnel to the Tower 2F Staircase": {
        "return_name": "Tunnel to the Tower 3F Exit",
        "exit": (0x18, 0x2, 0),
        "entrance": (0x18, 0x1, 1),
        "exit_region": "tower tunnel 3f",
        "entrance_region": "tower tunnel 2f door",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # FOS
    "Woodland Sanctuary Cave": {
        "return_name": "Gage's Sanctuary Exit",
        "entrance": (0x30, 0, 1),
        "exit": (0x30, 0x1, 0),
        "entrance_region": "woodland sanc door",
        "exit_region": "woodland sanc sanc",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    # Snow realm
    "Anouki Village SW House": {
        "return_name": "Yefu's House Exit",
        "entrance": (0x2B, 0, 5),
        "exit": (0x2B, 0x5, 0),
        "entrance_region": "anouki village",
        "exit_region": "yefu's house",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Anouki Village S House": {
        "return_name": "Noko's House Exit",
        "entrance": (0x2B, 0, 4),
        "exit": (0x2B, 0x4, 0),
        "entrance_region": "anouki village",
        "exit_region": "noko's house",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Anouki Village SE House": {
        "return_name": "Bulu's House Exit",
        "entrance": (0x2B, 0, 3),
        "exit": (0x2B, 0x3, 0),
        "entrance_region": "anouki village",
        "exit_region": "bulu's house",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Anouki Village NE House": {
        "return_name": "Kofu's House Exit",
        "entrance": (0x2B, 0, 2),
        "exit": (0x2B, 0x2, 0),
        "entrance_region": "anouki village",
        "exit_region": "kofu's house",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Anouki Village NW House": {
        "return_name": "Yeko's House Exit",
        "entrance": (0x2B, 0, 6),
        "exit": (0x2B, 0x6, 0),
        "entrance_region": "anouki village",
        "exit_region": "yeko's house",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Anouki Village N House": {
        "return_name": "Honcho's House Exit",
        "entrance": (0x2B, 0, 1),
        "exit": (0x2B, 0x1, 0),
        "entrance_region": "anouki village",
        "exit_region": "honcho's house",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Anouki Village Bomb Cave": {
        "return_name": "Small Ice Puzzle Cave Exit",
        "entrance": (0x2B, 0, 7),
        "exit": (0x2B, 0x7, 0),
        "entrance_region": "anouki village",
        "exit_region": "ice block cave",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # Snowfall sanc
    "Snowfall Sanctuary Cave": {
        "return_name": "Head Statue Cave Exit",
        "entrance": (0x31, 0, 1),
        "exit": (0x31, 0x1, 0),
        "entrance_region": "snow sanc",
        "exit_region": "snow sanc cave",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Head Statue Cave Door": {
        "return_name": "Steem's Sanctuary Exit",
        "entrance": (0x31, 1, 1),
        "exit": (0x31, 0x2, 0),
        "entrance_region": "snow sanc cave",
        "exit_region": "snow sanc sanc",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Snowfall Sanctuary Shop": {
        "return_name": "Snowfall Supermarket Exit",
        "entrance": (0x31, 0, 2),
        "exit": (0x31, 0x3, 0),
        "entrance_region": "snow sanc",
        "exit_region": "snowfall supermarket",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    # Small Stations
    "Icy Spring Trailer": {
        "return_name": "Ferrus' Trailer Exit",
        "entrance": (0x35, 0, 1),
        "exit": (0x35, 0x1, 0),
        "entrance_region": "icyspring",
        "exit_region": "ferrus' trailer",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Bridge Worker's House": {
        "return_name": "Kenzo's House Exit",
        "entrance": (0x36, 0, 1),
        "exit": (0x36, 0x1, 0),
        "entrance_region": "icyspring",
        "exit_region": "ferrus' trailer",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Slippery Station Cave": {
        "return_name": "Skating Rink Exit",
        "entrance": (0x3F, 0xA, 1),
        "exit": (0x3F, 0x6, 0),
        "entrance_region": "icyspring",
        "exit_region": "ferrus' trailer",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    # Snowdrift
    "Snowdrift Station Cave": {
        "return_name": "Snowdrift Cave Exit",
        "entrance": (0x3F, 0x0, 1),
        "exit": (0x3F, 0x1, 0),
        "entrance_region": "snowdrift",
        "exit_region": "snowdrift cave",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Snowdrift Cave SE": {
        "return_name": "Octive Arena Exit",
        "entrance": (0x3F, 0x1, 1),
        "exit": (0x3F, 0x2, 0),
        "entrance_region": "snowdrift cave",
        "exit_region": "octive arena",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Snowdrift Cave NE": {
        "return_name": "Frostflame Cave Exit",
        "entrance": (0x3F, 0x1, 3),
        "exit": (0x3F, 0x3, 0),
        "entrance_region": "snowdrift cave",
        "exit_region": "frostflame cave",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Snowdrift Cave SW": {
        "return_name": "Small Skating Cave Exit",
        "entrance": (0x3F, 0x1, 2),
        "exit": (0x3F, 0x4, 0),
        "entrance_region": "snowdrift cave",
        "exit_region": "small skating",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Snowdrift Cave NW": {
        "return_name": "Big Ice Puzzle Cave Exit",
        "entrance": (0x3F, 0x1, 4),
        "exit": (0x3F, 0x5, 0),
        "entrance_region": "snowdrift cave",
        "exit_region": "big ice puzzle",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },

    # Trading post
    "Trading Post Shop": {
        "return_name": "Linebeck III's Shop Exit",
        "entrance": (0x37, 0x0, 1),
        "exit": (0x37, 0xA, 0),
        "entrance_region": "trading post",
        "exit_region": "linebeck's shop",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Trading Post South Cave": {
        "return_name": "Like-Like Tunnel Exit",
        "entrance": (0x37, 0x0, 2),
        "exit": (0x37, 0x1, 0),
        "entrance_region": "trading post",
        "exit_region": "trading post tunnel",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Trading Post North Staircase": {
        "return_name": "Like-Like Tunnel Staircase",
        "entrance": (0x37, 0x0, 3),
        "exit": (0x37, 0x1, 1),
        "entrance_region": "trading post north",
        "exit_region": "trading post tunnel",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Trading Post Island Cave": {
        "return_name": "Linebeck's Treasure's Cave",
        "entrance": (0x37, 0x0, 4),
        "exit": (0x37, 0x2, 0),
        "entrance_region": "trading post island",
        "exit_region": "trading post cave",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # Papuzia
    "Papuzia NW House": {
        "return_name": "Fuku's House Exit",
        "entrance_region": "papuzia village",
        "exit_region": "fuku's house",
        "entrance": (0x2c, 0x0, 0x1),
        "exit": (0x2c, 0x1, 0x0),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Papuzia Wise One's House": {
        "return_name": "Wise One's House Exit",
        "entrance_region": "papuzia village",
        "exit_region": "wise one's house",
        "entrance": (0x2c, 0x0, 0x4),
        "exit": (0x2c, 0x4, 0x0),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Papuzia South House": {
        "return_name": "Orca's House Exit",
        "entrance_region": "papuzia village",
        "exit_region": "orca's house",
        "entrance": (0x2c, 0x0, 0x3),
        "exit": (0x2c, 0x3, 0x0),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Papuzia Shop": {
        "return_name": "Kogane's Shop Exit",
        "entrance_region": "papuzia village",
        "exit_region": "kogane's shop",
        "entrance": (0x2c, 0x0, 0x2),
        "exit": (0x2c, 0x2, 0x0),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Papuzia South": {
        "return_name": "Papuzia Archipelago North",
        "entrance_region": "papuzia village south",
        "exit_region": "papuzia archipelago north",
        "entrance": (0x2c, 0x0, 0x5),
        "exit": (0x39, 0x0, 0x0),
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },

    # Island Sanctuary
    "Island Sanctuary South Cave": {
        "return_name": "Crab Cave Exit",
        "entrance_region": "island sanc",
        "exit_region": "island sanc cave west",
        "entrance": (0x32, 0x0, 0x1),
        "exit": (0x32, 0x1, 0x0),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Island Sanctuary North Staircase": {
        "return_name": "Crab Cave Staircase",
        "entrance_region": "island sanc north",
        "exit_region": "island sanc cave east",
        "entrance": (0x32, 0x2, 0x0),
        "exit": (0x32, 0x1, 0x1),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Island Sanctuary North Cave": {
        "return_name": "Carben's Sanctuary Exit",
        "entrance_region": "island sanc north",
        "exit_region": "island sanc sanc",
        "entrance": (0x32, 0x2, 0x2),
        "exit": (0x32, 0x4, 0x0),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Island Sanctuary South Peninsula": {
        "return_name": "Island Sanctuary North South",
        "entrance_region": "island sanc peninsula",
        "exit_region": "island sanc north",
        "entrance": (0x32, 0x0, 0x2),
        "exit": (0x32, 0x2, 0x1),
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # Ocean Islands
    "Pirate Hideout Cave": {
        "return_name": "Treasure Cave Exit",
        "entrance_region": "pirate hideout",
        "exit_region": "pirate hideout secret cave",
        "entrance": (0x3A, 0x0, 0x3),
        "exit": (0x3A, 0x1, 0x0),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Lost at Sea Cave": {
        "return_name": "Lost at Sea Lobby Exit",
        "entrance_region": "lost at sea",
        "exit_region": "las lobby",
        "entrance": (0x39, 0xA, 0x1),
        "exit": (0x39, 0xB, 0x0),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Dune Sanctuary Secret Staircase": {
        "return_name": "Sandy Tunnel Right Staircase",
        "entrance_region": "sand sanc",
        "exit_region": "sand sanc tunnel",
        "entrance": (0x34, 0x0, 0x1),
        "exit": (0x34, 0x1, 0x0),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Rael's Sanctuary Exit": {
        "return_name": "Sandy Tunnel Left Entrance",
        "entrance_region": "sand sanc sanc",
        "exit_region": "sand sanc tunnel",
        "entrance": (0x34, 0x2, 0x0),
        "exit": (0x34, 0x1, 0x1),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # Fire realm

    # Goron village
    "Goron Village West": {
        "return_name": "Goron Field East",
        "entrance_region": "goron village",
        "exit_region": "goron field",
        "entrance": (0x2e, 0x0, 0x3),
        "exit": (0x2d, 0x3, 0x1),
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.LEFT,
        "island": EntranceGroups.NONE
    },
    "Goron Field North": {
        "return_name": "Mountain Altar South",
        "entrance_region": "goron field north",
        "exit_region": "mountain altar",
        "entrance": (0x2d, 0x3, 0x2),
        "exit": (0x2d, 0x2, 0x1),
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    "Goron Village Shop": {
        "return_name": "Goron Shop Exit",
        "entrance_region": "goron village",
        "exit_region": "goron village shop",
        "entrance": (0x2e, 0x0, 0x2),
        "exit": (0x2e, 0x6, 0x1),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Goron Village SW House": {
        "return_name": "Goron 3 Pots House Exit",
        "entrance_region": "goron plaza",
        "exit_region": "goron house 3 pots",
        "entrance": (0x2e, 0x0, 0xc),
        "exit": (0x2e, 0xc, 0x1),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Goron Village Center House": {
        "return_name": "Kofu's New House Exit",
        "entrance_region": "goron plaza",
        "exit_region": "kofu's new house",
        "entrance": (0x2e, 0x0, 0xD),
        "exit": (0x2e, 0xD, 0x1),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Goron Village SE House": {
        "return_name": "Goron 2 Pots House Exit",
        "entrance_region": "goron plaza",
        "exit_region": "goron neighbour's house",
        "entrance": (0x2e, 0x0, 0xE),
        "exit": (0x2e, 0xE, 0x1),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Goron Village Elder's House": {
        "return_name": "Elder Goron House Exit",
        "entrance_region": "goron plaza",
        "exit_region": "goron elder's house",
        "entrance": (0x2e, 0x0, 0xA),
        "exit": (0x2e, 0xA, 0x1),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Goron Village NW House": {
        "return_name": "Mouldy Goron House Exit",
        "entrance_region": "goron plaza",
        "exit_region": "mouldy goron house",
        "entrance": (0x2e, 0x0, 0xB),
        "exit": (0x2e, 0xB, 0x1),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Goron Village East Lava House": {
        "return_name": "Lava Goron House Exit",
        "entrance_region": "goron ice 2",
        "exit_region": "comfy goron's house",
        "entrance": (0x2e, 0x0, 0xF),
        "exit": (0x2e, 0xF, 0x1),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    "Elder Goron House Cave": {
        "return_name": "Burning Tunnel West Exit",
        "entrance_region": "goron elder's house",
        "exit_region": "valley sanc tunnel west",
        "entrance": (0x2e, 0xA, 0x2),
        "exit": (0x2e, 0x1, 0x1),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Goron Village Enclave Staircase": {
        "return_name": "Burning Tunnel East Staircase",
        "entrance_region": "goron village north",
        "exit_region": "valley sanc tunnel east",
        "entrance": (0x2e, 0x0, 0x5),
        "exit": (0x2e, 0x1, 0x2),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Goron Village Enclave North": {
        "return_name": "Valley Sanctuary South",
        "entrance_region": "goron village north",
        "exit_region": "valley sanc",
        "entrance": (0x2e, 0x0, 0x4),
        "exit": (0x33, 0x0, 0x1),
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Valley Sanctuary Cave": {
        "return_name": "Embrose's Sanctuary Exit",
        "entrance_region": "valley sanc door",
        "exit_region": "valley sanc sanc",
        "entrance": (0x33, 0x0, 0x2),
        "exit": (0x33, 0x3, 0x1),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # Dark Ore Mine
    "Dark Ore Mine Left Cave": {
        "return_name": "Dark Ore Tunnels Left Exit",
        "entrance_region": "dark ore mine",
        "exit_region": "dark ore tunnels left",
        "entrance": (0x3D, 0x0, 0x3),
        "exit": (0x3D, 0x1, 0x2),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Dark Ore Mine Cave": {
        "return_name": "Dark Ore Tunnels Center Exit",
        "entrance_region": "dark ore mine",
        "exit_region": "dark ore tunnels mid",
        "entrance": (0x3D, 0x0, 0x2),
        "exit": (0x3D, 0x1, 0x1),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Dark Ore Mine Right Cave": {
        "return_name": "Dark Ore Tunnels Right Exit",
        "entrance_region": "dark ore mine",
        "exit_region": "dark ore tunnels right",
        "entrance": (0x3D, 0x0, 0x4),
        "exit": (0x3D, 0x1, 0x3),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # Disorientation Station
    "Disorientation Station Cave": {
        "return_name": "Disorientation 5 Staircase",
        "entrance_region": "disorientation top",
        "exit_region": "d5",
        "entrance": (0x40, 0x0, 0x1),
        "exit": (0x40, 0x5, 0x5),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "D8 Up": {
        "return_name": "D2 Down",
        "entrance_region": "d8",
        "exit_region": "d2",
        "entrance": (0x40, 0x8, 0x3),
        "exit": (0x40, 0x2, 0x1),
        "type": EntranceGroups.DISORIENTATION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    }
}

ENTRANCE_DATA |= {  # Horizontal
    f"D{i+3*j} Right": {
        "return_name": f"D{i+3*j+1} Left",
        "entrance_region": f"d{i+3*j}",
        "exit_region": f"d{i+3*j+1}",
        "entrance": (0x40, i+3*j, 0x4),
        "exit": (0x40, i+3*j+1, 0x2),
        "type": EntranceGroups.DISORIENTATION,
        "direction": EntranceGroups.RIGHT,
        "island": EntranceGroups.NONE
    } for i in range(1, 4) for j in range(3)
}

ENTRANCE_DATA |= { # Horizontal looping
    f"D{3+3*j} Right": {
        "return_name": f"D{1+3*j} Left",
        "entrance_region": f"d{3+3*j}",
        "exit_region": f"d{1+3*j}",
        "entrance": (0x40, 3+3*j, 0x4),
        "exit": (0x40, 3*j+1, 0x2),
        "type": EntranceGroups.DISORIENTATION,
        "direction": EntranceGroups.RIGHT,
        "island": EntranceGroups.NONE
    } for j in range(3)
}
ENTRANCE_DATA |= { # Vertical
    f"D{i+3*j} Up": {
        "return_name": f"D{i+3*j+3} Down",
        "entrance_region": f"d{i+3*j}",
        "exit_region": f"d{i+3*j+3}",
        "entrance": (0x40, i+3*j, 0x3),
        "exit": (0x40, i+3*j+3, 0x1),
        "type": EntranceGroups.DISORIENTATION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    } for i in range(1, 4) for j in range(2)
}

ENTRANCE_DATA |= {
    # Ends of the Earth
    "Ends of the Earth Master Cave": {
        "return_name": "EotE 1 Exit",
        "entrance_region": "ends of the earth",
        "exit_region": "eote 1",
        "entrance": (0x41, 0x0, 0x2),
        "exit": (0x41, 0x1, 0x0),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Ends of the Earth Tempered Cave": {
        "return_name": "EotE 5 Exit",
        "entrance_region": "ends of the earth",
        "exit_region": "eote 5",
        "entrance": (0x41, 0x0, 0x1),
        "exit": (0x41, 0x5, 0x0),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Ends of the Earth Golden Cave": {
        "return_name": "EotE 9 Exit",
        "entrance_region": "ends of the earth",
        "exit_region": "eote 9",
        "entrance": (0x41, 0x0, 0x3),
        "exit": (0x41, 0x9, 0x0),
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    "EotE 1 Lower Entrance": {
        "return_name": "EotE 2 Exit",
        "entrance_region": "eote 1",
        "exit_region": "eote 2",
        "entrance": (0x41, 0x1, 0x1),
        "exit": (0x41, 0x2, 0x0),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "EotE 2 Door": {
        "return_name": "EotE 3 Exit",
        "entrance_region": "eote 2",
        "exit_region": "eote 3",
        "entrance": (0x41, 0x2, 0x1),
        "exit": (0x41, 0x3, 0x0),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "EotE 3 Door": {
        "return_name": "EotE 4 Exit",
        "entrance_region": "eote 3",
        "exit_region": "eote 4",
        "entrance": (0x41, 0x3, 0x1),
        "exit": (0x41, 0x4, 0x0),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "EotE 1 Upper Entrance": {
        "return_name": "EotE 4 Chest Exit",
        "entrance_region": "eote 1 chest",
        "exit_region": "eote 4 chest",
        "entrance": (0x41, 0x1, 0x2),
        "exit": (0x41, 0x4, 0x1),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    "EotE 5 Lower Entrance": {
        "return_name": "EotE 6 Exit",
        "entrance_region": "eote 5",
        "exit_region": "eote 6",
        "entrance": (0x41, 0x5, 0x1),
        "exit": (0x41, 0x6, 0x0),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "EotE 6 Door": {
        "return_name": "EotE 7 Exit",
        "entrance_region": "eote 6",
        "exit_region": "eote 7",
        "entrance": (0x41, 0x6, 0x1),
        "exit": (0x41, 0x7, 0x0),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "EotE 7 Door": {
        "return_name": "EotE 8 Exit",
        "entrance_region": "eote 7",
        "exit_region": "eote 8",
        "entrance": (0x41, 0x7, 0x1),
        "exit": (0x41, 0x8, 0x0),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "EotE 5 Upper Entrance": {
        "return_name": "EotE 8 Chest Exit",
        "entrance_region": "eote 5 chest",
        "exit_region": "eote 8 chest",
        "entrance": (0x41, 0x5, 0x2),
        "exit": (0x41, 0x8, 0x1),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    "EotE 9 Lower Entrance": {
        "return_name": "EotE A Exit",
        "entrance_region": "eote 9",
        "exit_region": "eote a",
        "entrance": (0x41, 0x9, 0x1),
        "exit": (0x41, 0xa, 0x0),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "EotE A Door": {
        "return_name": "EotE B Exit",
        "entrance_region": "eote a",
        "exit_region": "eote b",
        "entrance": (0x41, 0xa, 0x1),
        "exit": (0x41, 0xb, 0x0),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "EotE B Door": {
        "return_name": "EotE C Exit",
        "entrance_region": "eote b",
        "exit_region": "eote c",
        "entrance": (0x41, 0xb, 0x1),
        "exit": (0x41, 0xc, 0x0),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "EotE 9 Upper Entrance": {
        "return_name": "EotE C Chest Exit",
        "entrance_region": "eote 9 chest",
        "exit_region": "eote c chest",
        "entrance": (0x41, 0x9, 0x2),
        "exit": (0x41, 0xc, 0x1),
        "type": EntranceGroups.EOTE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },


    # ==== Overworld ====
    "Outset to Tutorial": {
        "return_name": "Tutorial to Outset",
        "exit": (0x8, 0x0, 0),
        "entrance": (0x2F, 0x0, 0),
        "exit_region": "forest realm",
        "entrance_region": "outset village",
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Outset Board Train": {
        "return_name": "Forest Realm Outset Station",
        "exit": (0x4, 0x0, 1),
        "entrance": (0x2F, 0x0, 0),
        "exit_region": "outset station",
        "entrance_region": "outset village",
        "reverse_required_groups": ["Tracks: Forest Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Mayscore Board Train": {
        "return_name": "Forest Realm Mayscore Station",
        "exit": (0x4, 0x0, 2),
        "entrance": (0x2A, 0x0, 0),
        "exit_region": "mayscore station",
        "entrance_region": "mayscore",
        "reverse_required_groups": ["Tracks: Forest Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Castle Town Board Train": {
        "return_name": "Forest Realm Castle Town Station",
        "exit": (0x4, 0x0, 0),
        "entrance": (0x29, 0x0, 0),
        "exit_region": "castle station",
        "entrance_region": "castle town",
        "reverse_required_groups": ["Tracks: Forest Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Woodland Sanctuary Board Train": {
        "return_name": "Forest Realm Woodland Sanctuary Station",
        "exit": (0x4, 0x0, 3),
        "entrance": (0x30, 0x0, 0),
        "exit_region": "woodland sanc station",
        "entrance_region": "woodland sanc",
        "reverse_required_groups": ["Tracks: Forest Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Wooded Temple Lobby Board Train": {
        "return_name": "Forest Realm Wooded Temple Station",
        "exit": (0x4, 0x0, 4),
        "entrance": (0x19, 0xA, 0),
        "exit_region": "wt station",
        "entrance_region": "wt lobby",
        "reverse_required_groups": [("Tracks: Wooded Temple Tracks", "Tracks: Forest Source")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Rabbit Haven Board Train": {
        "return_name": "Forest Realm Rabbit Haven Station",
        "exit": (0x4, 0x0, 8),
        "entrance": (0x3E, 0x0, 0),
        "exit_region": "rabbit haven station",
        "entrance_region": "rabbit haven",
        "reverse_required_groups": ["Tracks: Snow Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Anouki Village Board Train": {
        "return_name": "Snow Realm Anouki Village Station",
        "exit": (0x5, 0x0, 0),
        "entrance": (0x2B, 0x0, 0),
        "exit_region": "anouki station",
        "entrance_region": "anouki village",
        "reverse_required_groups": ["Tracks: Snow Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Snowfall Sanctuary Board Train": {
        "return_name": "Snow Realm Snowfall Sanctuary Station",
        "exit": (0x5, 0x0, 2),
        "entrance": (0x31, 0x0, 0),
        "exit_region": "snow sanc station",
        "entrance_region": "snow sanc",
        "reverse_required_groups": ["Tracks: Snow Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Snow Realm Icy Spring": {
        "return_name": "Icy Spring Train",
        "entrance_region": "icyspring station",
        "exit_region": "icyspring",
        "required_groups": ["Tracks: Blizzard Temple Tracks"],
        "entrance": (0x35, 0x0, 0x3),
        "exit": (0x35, 0x0, 0x0),
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Bridge Worker's Board Train": {
        "return_name": "Snow Realm Bridge Worker's Station",
        "exit": (0x5, 0x0, 5),
        "entrance": (0x36, 0x0, 0),
        "exit_region": "bridge workers station",
        "entrance_region": "bridge workers",
        "reverse_required_groups": ["Tracks: Snow Source"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Blizzard Temple Lobby Board Train": {
        "return_name": "Snow Realm Blizzard Temple Station",
        "exit": (0x5, 0x0, 1),
        "entrance": (0x1A, 0x4, 0),
        "exit_region": "bt station",
        "entrance_region": "bt lobby",
        "reverse_required_groups": [("Tracks: Blizzard Temple Tracks", "Tracks: Snow Source")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Slippery Station Board Train": {
        "return_name": "Snow Realm Slippery Station",
        "exit": (0x5, 0x0, 0xF),
        "entrance": (0x3f, 0xA, 0),
        "exit_region": "slippery station",
        "entrance_region": "slippery",
        "reverse_required_groups": ["Tracks: Slippery Station"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Snowdrift Board Train": {
        "return_name": "Snow Realm Snowdrift Station",
        "exit": (0x5, 0x0, 0xE),
        "entrance": (0x3F, 0x0, 0),
        "exit_region": "snowdrift station",
        "entrance_region": "snowdrift",
        "reverse_required_groups": ["Tracks: Snowdrift Station"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },

    "Trading Post Board Train": {
        "return_name": "Forest Realm Trading Post Station",
        "exit": (0x4, 0x0, 7),
        "entrance": (0x37, 0x0, 0),
        "exit_region": "trading post station",
        "entrance_region": "trading post",
        "reverse_required_groups": ["Tracks: Ocean Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Papuzia Board Train": {
        "return_name": "Ocean Realm Papuzia Station",
        "exit": (0x6, 0x0, 0),
        "entrance": (0x2C, 0x0, 0),
        "exit_region": "papuzia village station",
        "entrance_region": "papuzia",
        "reverse_required_groups": ["Tracks: Ocean Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Island Sanctuary Board Train": {
        "return_name": "Ocean Realm Island Sanctuary Station",
        "exit": (0x6, 0x0, 2),
        "entrance": (0x32, 0x0, 0),
        "exit_region": "island sanc station",
        "entrance_region": "island sanc",
        "reverse_required_groups": ["Tracks: Ocean Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Marine Temple Lobby Board Train": {
        "return_name": "Undersea Marine Temple Station",
        "exit": (0xA, 0x0, 1),
        "entrance": (0x1B, 0xA, 0),
        "exit_region": "oct station",
        "entrance_region": "oct lobby",
        "reverse_required_groups": [("Tracks: Ocean Source", "Tracks: Marine Temple Tracks")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Marine Temple Train Exit Water Warp": {
        "exit": (0x6, 0x0, 3),
        "entrance": (0x1B, 0xA, 0),
        "exit_region": "ocean temple tracks",
        "entrance_region": "oct lobby",
        "reverse_required_groups": [("Tracks: Ocean Source", "Tracks: Marine Temple Tracks")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE,
        "two_way": False
    },
    "Pirate Hideout Board Train": {
        "return_name": "Ocean Realm Pirate Hideout Station",
        "exit": (0x6, 0x0, 5),
        "entrance": (0x3a, 0x0, 0),
        "exit_region": "pirate hideout station",
        "entrance_region": "pirate hideout",
        "reverse_required_groups": ["Tracks: Pirate Hideout"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Lost at Sea Board Train": {
        "return_name": "Ocean Realm Lost at Sea Station",
        "exit": (0x6, 0x0, 0xE),
        "entrance": (0x39, 0xA, 0),
        "exit_region": "lost at sea station",
        "entrance_region": "lost at sea",
        "reverse_required_groups": ["Tracks: Lost at Sea Station"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Dune Sanctuary Board Train": {
        "return_name": "Ocean Realm Dune Sanctuary Station",
        "exit": (0x6, 0x0, 6),
        "entrance": (0x34, 0x0, 0),
        "exit_region": "sand sanc station",
        "entrance_region": "sand sanc",
        "reverse_required_groups": ["Tracks: Sand Realm"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Desert Temple Lobby Board Train": {
        "return_name": "Ocean Realm Desert Temple Station",
        "exit": (0x6, 0x0, 7),
        "entrance": (0x1D, 0x6, 0),
        "exit_region": "desert temple station",
        "entrance_region": "dt lobby",
        "reverse_required_groups": ["Tracks: Desert Temple Tracks"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },

    "Fire Realm Goron Village Station": {
        "return_name": "Goron Village Board Train",
        "entrance_region": "goron village station",
        "exit_region": "goron village",
        "entrance": (0x7, 0x0, 0x0),
        "exit": (0x2E, 0x0, 0x0),
        "required_groups": [("Tracks: Fire Glyph", "Tracks: Fire Source")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Goron Target Range Board Train": {
        "return_name": "Fire Realm Goron Target Range Station",
        "exit": (0x7, 0x0, 4),
        "entrance": (0x3c, 0x0, 1),
        "exit_region": "goron target station",
        "entrance_region": "goron target lobby",
        "reverse_required_groups": ["Tracks: Fire Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Goron Target Range Exit": {
        "exit": (0x7, 0x0, 4),
        "entrance": (0x3c, 0x1, 1),
        "exit_region": "goron target station",
        "entrance_region": "gtr",
        "reverse_required_groups": ["Tracks: Fire Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE,
        "two_way": False
    },
    "Mountain Temple Lobby Board Train": {
        "return_name": "Fire Realm Mountain Temple Station",
        "exit": (0x7, 0x0, 1),
        "entrance": (0x1c, 0xA, 0),
        "exit_region": "mtt station",
        "entrance_region": "mtt lobby",
        "reverse_required_groups": [("Tracks: Mountain Temple Tracks", "Tracks: Fire Source")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Disorientation Station Board Train": {
        "return_name": "Fire Realm Disorientation Station",
        "exit": (0x7, 0x0, 0x16),
        "entrance": (0x40, 0x0, 0),
        "exit_region": "disorientation station station",
        "entrance_region": "disorientation station",
        "reverse_required_groups": ["Tracks: Disorientation Station"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Ends of the Earth Board Train": {
        "return_name": "Fire Realm Ends of the Earth Station",
        "exit": (0x7, 0x0, 0x17),
        "entrance": (0x41, 0x0, 0),
        "exit_region": "ends of the earth station",
        "entrance_region": "ends of the earth",
        "reverse_required_groups": ["Tracks: Ends of the Earth"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Dark Ore Mine Board Train": {
        "return_name": "Fire Realm Dark Ore Mine Station",
        "exit": (0x7, 0x0, 5),
        "entrance": (0x3D, 0x0, 0),
        "exit_region": "dark ore mine station",
        "entrance_region": "dark ore mine",
        "reverse_required_groups": ["Tracks: Dark Ore Mine"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },

    # Train Transitions
    "Ocean Realm Dive Underwater": {
        "return_name": "Undersea Tracks Surface",
        "exit": (0xA, 0x0, 0),
        "entrance": (0x6, 0x0, 3),
        "exit_region": "undersea tracks",
        "entrance_region": "undersea entrance",
        "reverse_required_groups": [("Tracks: Ocean Source", "Tracks: Marine Temple Tracks")],
        "required_groups": [("Tracks: Ocean Source", "Tracks: Marine Temple Tracks")],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Forest Realm North Snow Glyph": {
        "return_name": "Snow Realm South Snow Glyph",
        "entrance_region": "snow realm fr",
        "exit_region": "snow realm south",
        "extra_data": {"x_max": -240000},
        "coords": (-368640, 983, -342045),
        "reverse_coords": "flip_h",
        "entrance": (0x4, 0x0, 0xFB),
        "exit": (0x5, 0x0, 0xFC),
        "required_groups": ["Tracks: Snow Glyph"],
        "reverse_required_groups": ["Tracks: Snow Glyph"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Forest Realm North W Wooded Temple": {
        "return_name": "Snow Realm South W Wooded Temple",
        "entrance_region": "w wooded temple tracks",
        "exit_region": "w wooded temple tracks north",
        "extra_data": {"x_max": -200000, "x_min": -240000},
        "coords": (-221184, 1393, -341845),
        "reverse_coords": "flip_h",
        "entrance": (0x4, 0x0, 0xFB),
        "exit": (0x5, 0x0, 0xFC),
        "required_groups": ["Tracks: W Wooded Temple"],
        "reverse_required_groups": ["Tracks: W Wooded Temple", "Tracks: Snow Glyph"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Forest Realm North Bridge Tracks": {
        "return_name": "Snow Realm South Bridge Tracks",
        "entrance_region": "snow bridge south",
        "exit_region": "snow bridge mid",
        "extra_data": {"x_min": 70000, "x_max": 80000},
        "coords": (73728, 1393, -342035),
        "reverse_coords": (73728, 1393, 334525),
        "entrance": (0x4, 0x0, 0xFB),
        "exit": (0x5, 0x0, 0xFC),
        "required_groups": ["Tracks: Snow Realm Bridge"],
        "reverse_required_groups": ["Tracks: Snow Realm Bridge"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Forest Realm North Castle Tracks": {
        "return_name": "Snow Realm South Castle Tracks",
        "entrance_region": "n castle town tracks",
        "exit_region": "n castle town tracks north",
        "extra_data": {"x_min": -200000},
        "coords": (270336, 983, -342045),
        "reverse_coords": "flip_h",
        "entrance": (0x4, 0x0, 0xFB),
        "exit": (0x5, 0x0, 0xFC),
        "required_groups": ["Tracks: N Castle Town"],
        "reverse_required_groups": ["Tracks: N Castle Town"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Fire Realm East Fire Glyph": {
        "return_name": "Snow Realm West Fire Glyph",
        "entrance_region": "fire realm",
        "exit_region": "fire realm west",
        "extra_data": {"z_min": 0},
        "coords": (463671, 0, 147456),
        "reverse_coords": "flip_h",
        "entrance": (0x7, 0x0, 0xFD),
        "exit": (0x5, 0x0, 0xFE),
        "required_groups": ["Tracks: Fire Glyph"],
        "reverse_required_groups": ["Tracks: Fire Glyph"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.LEFT,
        "island": EntranceGroups.NONE
    },
    "Fire Realm East Gorge Tracks": {
        "return_name": "Snow Realm West Gorge Tracks",
        "entrance_region": "gorge tracks east",
        "exit_region": "gorge tracks west",
        "extra_data": {"z_max": 0},
        "coords": (-464925, 901, -147456),
        "reverse_coords": "flip_h",
        "entrance": (0x7, 0x0, 0xFD),
        "exit": (0x5, 0x0, 0xFE),
        "required_groups": ["Tracks: Snow Realm Gorge"],
        "reverse_required_groups": ["Tracks: Snow Realm Gorge"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.LEFT,
        "island": EntranceGroups.NONE
    },
    "Ocean Realm West Ocean Shortcut": {
        "return_name": "Forest Realm East Ocean Shortcut",
        "entrance_region": "ocean shortcut east",
        "exit_region": "ocean shortcut",
        "extra_data": {"z_max": 10000},
        "coords": (487572, 0, 0),
        "reverse_coords": "flip_h",
        "entrance": (0x6, 0x0, 0xFD),
        "exit": (0x4, 0x0, 0xFE),
        "required_groups": ["Tracks: Forest Realm Ocean Shortcut"],
        "reverse_required_groups": ["Tracks: Forest Realm Ocean Shortcut"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.LEFT,
        "island": EntranceGroups.NONE
    },
    "Ocean Realm West Ocean Glyph": {
        "return_name": "Forest Realm East Ocean Glyph",
        "entrance_region": "ocean realm",
        "exit_region": "ocean realm mid",
        "extra_data": {"z_min": 10000},
        "coords": (-453624, 9585, 245760),
        "reverse_coords": "flip_h",
        "entrance": (0x6, 0x0, 0xFD),
        "exit": (0x4, 0x0, 0xFE),
        "required_groups": ["Tracks: Forest Realm Ocean Shortcut"],
        "reverse_required_groups": ["Tracks: Forest Realm Ocean Shortcut"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.LEFT,
        "island": EntranceGroups.NONE
    },
    "Ocean Realm North Sand Connection": {
        "return_name": "Fire Realm South Sand Connection",
        "entrance_region": "sand connection south",
        "exit_region": "sand connection",
        "extra_data": {"x_max": -300000},
        "coords": (-319488, 1393, -342045),
        "reverse_coords": "flip_v",
        "entrance": (0x6, 0x0, 0xFB),
        "exit": (0x7, 0x0, 0xFC),
        "required_groups": ["Tracks: Sand Realm", "Tracks: Fire Realm Sand Portal"],
        "reverse_required_groups": ["Tracks: Sand Realm", "Tracks: Fire Realm Sand Portal"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Ocean Realm North Rocktite Cave": {
        "return_name": "Fire Realm South Rocktite Cave",
        "entrance_region": "sand realm exit",
        "exit_region": "sand restoration rocktite",
        "extra_data": {"x_min": 20000, "x_max": 30000},
        "coords": (24576, 983, 342045),
        "reverse_coords": "flip_v",
        "entrance": (0x6, 0x0, 0xFB),
        "exit": (0x7, 0x0, 0x11),
        "required_groups": ["Tracks: Desert Temple Tracks"],
        "reverse_required_groups": ["Tracks: Desert Temple Tracks"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Ocean Realm North Rocktite Cave Fight": {
        "return_name": "Desert Rocktite Fight Entrance",
        "entrance_region": "sand realm exit",
        "exit_region": "sand restoration",
        "extra_data": {"x_min": -200000},
        "coords": (24576, 983, 342045),
        "entrance": (0x6, 0x0, 0xFB),
        "exit": (0xC, 0x0, 0x0),
        "required_groups": ["Tracks: Sand Realm", "Tracks: Desert Temple Tracks"],
        "reverse_required_groups": ["Tracks: Sand Realm", "Tracks: Desert Temple Tracks"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE,
        "two_way": False
    },
    "Desert Rocktite Fight Exit": {
        "return_name": "Fire Realm Exit Rocktite Fight",
        "entrance_region": "sand restoration rocktite",
        "exit_region": "disorientation station tracks",
        "entrance": (0xC, 0x0, 0x0),
        "exit": (0x7, 0x0, 0x6),
        "required_groups": ["Tracks: Desert Temple Tracks"],
        "reverse_required_groups": ["Tracks: Desert Temple Tracks"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE,
        "two_way": False
    },
    "Ocean Realm North Desert Temple": {
        "return_name": "Fire Realm South Desert Temple",
        "entrance_region": "sand restoration south",
        "exit_region": "sand restoration",
        "extra_data": {"x_min": 400000},
        "coords": (417792, 1695, -334526),
        "reverse_coords": (417792, 983, 342045),
        "entrance": (0x6, 0x0, 0xFB),
        "exit": (0x7, 0x0, 0xFC),
        "required_groups": ["Tracks: Desert Temple Tracks"],
        "reverse_required_groups": ["Tracks: Desert Temple Tracks"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    # ===== Tower of Spirits =====
    "Tower of Spirits to Forest Realm": {
        "return_name": "Forest Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x4, 0x0, 6),
        "entrance_region": "tos",
        "exit_region": "tos forest station",
        "reverse_required_groups": [("Tracks: Forest Glyph", "Tracks: Forest Source")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits to Snow Realm": {
        "return_name": "Snow Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x5, 0x0, 6),
        "entrance_region": "tos",
        "exit_region": "tos snow station",
        "reverse_required_groups": ["Tracks: Snow Source"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits to Ocean Realm": {
        "return_name": "Ocean Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x6, 0x0, 4),
        "entrance_region": "tos",
        "exit_region": "tos ocean station",
        "reverse_required_groups": ["Tracks: Ocean Source"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits to Fire Realm": {
        "return_name": "Fire Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x7, 0x0, 2),
        "entrance_region": "tos",
        "exit_region": "tos fire station",
        "reverse_required_groups": ["Tracks: Fire Source"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.DOWN,
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
        "return_name": "Ocean Realm South Portal",
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
        "entrance_region": "ocean portal tracks",
        "exit_region": "trading post tracks",
        "type": EntranceGroups.TRAIN_PORTAL,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Ocean Realm West Portal": {
        "return_name": "Forest Realm Mayscore Portal",
        "entrance": (0x6, 0, 0xd),
        "exit": (0x4, 0, 0xd),
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
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Defeat Stagnox": {
        "two_way": False,
        "entrance_region": "wt stagnox",
        "exit_region": "event_stagnox",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Defeat Fraaz": {
        "two_way": False,
        "entrance_region": "bt fraaz",
        "exit_region": "event_fraaz",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Defeat Cactops": {
        "two_way": False,
        "entrance_region": "oct phytops",
        "exit_region": "event_phytops",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Defeat Vulcano": {
        "two_way": False,
        "entrance_region": "mtt vulcano",
        "exit_region": "event_vulcano",
        "entrance": (0x21, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Defeat Skeldritch": {
        "two_way": False,
        "entrance_region": "dt skeldritch",
        "exit_region": "skeldritch event",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Reach ToS 3F": {
        "two_way": False,
        "entrance_region": "tos 3f rail map",
        "exit_region": "event_3f",
        "entrance": (0x13, 0x2, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Reach ToS 7F": {
        "two_way": False,
        "entrance_region": "tos 7f rail map",
        "exit_region": "event_7f",
        "entrance": (0x13, 0x6, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Reach ToS 12F": {
        "two_way": False,
        "entrance_region": "tos 11f",
        "exit_region": "event_12f",
        "entrance": (0x13, 0xB, 0xF),
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
    "EVENT: Complete Lost at Sea Dungeon": {
        "two_way": False,
        "entrance_region": "las 5th room",
        "exit_region": "las_event",
        "entrance": (0x13, 0x23, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Complete Take 'em All On 3": {
        "two_way": False,
        "entrance_region": "teao 3",
        "exit_region": "teao_event",
        "entrance": (0x13, 0x23, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Give Regal Ring to Linebeck": {
        "two_way": False,
        "entrance_region": "linebeck trading",
        "exit_region": "linebeck event",
        "entrance": (0x37, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Bring Ice to Kagoron": {
        "two_way": False,
        "entrance_region": "goron ice",
        "exit_region": "goron ice event",
        "entrance": (0x2e, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },

    # Goals

    "GOAL: Defeat Stagnox": {
        "two_way": False,
        "entrance_region": "wt stagnox",
        "exit_region": "goal_stagnox",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Fraaz": {
        "two_way": False,
        "entrance_region": "bt fraaz",
        "exit_region": "goal_fraaz",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Cactops": {
        "two_way": False,
        "entrance_region": "oct phytops",
        "exit_region": "goal_phytops",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Vulcano": {
        "two_way": False,
        "entrance_region": "mtt pre vulcano",
        "exit_region": "goal_vulcano",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Skeldritch": {
        "two_way": False,
        "entrance_region": "dt skeldritch",
        "exit_region": "skeldritch goal",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Reach ToS 3F": {
        "two_way": False,
        "entrance_region": "tos 3f rail map",
        "exit_region": "goal_forest_glyph",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Reach ToS 12F": {
        "two_way": False,
        "entrance_region": "tos 11f",
        "exit_region": "goal_ocean_glyph",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Reach ToS 17F": {
        "two_way": False,
        "entrance_region": "tos 16f",
        "exit_region": "goal_fire_glyph",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Staven": {
        "two_way": False,
        "entrance_region": "tos staven",
        "exit_region": "goal_staven",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Reach ToS 24F": {
        "two_way": False,
        "entrance_region": "tos 24f",
        "exit_region": "goal_compass",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Malladus": {
        "two_way": False,
        "entrance_region": "malladus 2",
        "exit_region": "malladus event",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Enter Dark Realm": {
        "two_way": False,
        "entrance_region": "dark realm trains",
        "exit_region": "dark realm event",
        "entrance": (0x29, 0x0, 0xF),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },

    # Order later
    "Tower of Spirits Enter Section 1": {
        "return_name": "ToS 1F Exit",
        "entrance": (0x17, 0, 1),
        "exit": (0x13, 0x0, 0),
        "entrance_region": "tos 1",
        "exit_region": "tos 1f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Enter Section 2": {
        "return_name": "ToS 4F Exit",
        "entrance": (0x17, 0, 2),
        "exit": (0x13, 0x3, 0),
        "entrance_region": "tos 2",
        "exit_region": "tos 4f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Enter Section 3": {
        "return_name": "ToS 8F Exit",
        "entrance": (0x17, 0, 3),
        "exit": (0x13, 0x7, 0),
        "entrance_region": "tos 3",
        "exit_region": "tos 8f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Enter Section 4": {
        "return_name": "ToS 13F Exit",
        "entrance": (0x17, 0, 4),
        "exit": (0x13, 0xC, 0),
        "entrance_region": "tos 4",
        "exit_region": "tos 13f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Enter Section 5": {
        "return_name": "ToS 18F Exit",
        "entrance": (0x17, 0, 5),
        "exit": (0x13, 0x11, 0),
        "entrance_region": "tos 5",
        "exit_region": "tos 18f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Exit Staven": {
        "return_name": "ToS Summit Lower Exit",
        "entrance": (0x23, 0, 1),
        "exit": (0x15, 0x0, 0),
        "entrance_region": "tos staven",
        "exit_region": "tos summit lower",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits Summit Enter Altar": {
        "return_name": "ToS 30F Exit",
        "entrance": (0x15, 0, 2),
        "exit": (0x13, 0x1d, 0),
        "entrance_region": "tos 6",
        "exit_region": "tos 30f",
        "type": EntranceGroups.TOS_SECTION,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },

    "ToS Lobby Staircase": {
        "return_name": "ToS Staircase Exit",
        "entrance_region": "tos",
        "exit_region": "tos",
        "entrance": (0x14, 0x1, 0x1),  # Needs extra data for staircase side
        "exit": (0x17, 0x0, 0x0),
        "reverse_one_way_data": {"y": 0},
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "ToS 3F Blue Portal": {
        "two_way": False,
        "entrance": (0x13, 2, 0),
        "exit": (0x14, 0x1, 3),
        "entrance_region": "tos 3f rail map",
        "exit_region": "tos",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "ToS 7F Blue Portal": {
        "two_way": False,
        "entrance": (0x13, 6, 0),
        "exit": (0x14, 0x1, 3),
        "entrance_region": "tos 7f rail map",
        "exit_region": "tos",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "ToS 12F Blue Portal": {
        "two_way": False,
        "entrance": (0x13, 0xB, 0),
        "exit": (0x14, 0x1, 3),
        "entrance_region": "tos 11f",
        "exit_region": "tos",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "ToS 17F Blue Portal": {
        "two_way": False,
        "entrance": (0x13, 0xF, 0),
        "exit": (0x14, 0x1, 3),
        "entrance_region": "tos 16f",
        "exit_region": "tos",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "ToS 24F Blue Portal": {
        "two_way": False,
        "entrance": (0x13, 0x23, 0),
        "exit": (0x14, 0x1, 1),
        "entrance_region": "tos 24f",
        "exit_region": "tos",
        "type": EntranceGroups.WARP_PORTAL,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.NONE
    },
    "ToS 23F Blue Warp Before Staven": {
        "return_name": "ToS Top of Staircase Blue Warp",
        "entrance": (0x13, 0x14, 2),
        "exit": (0x17, 0x0, 6),
        "entrance_region": "tos 22f",
        "exit_region": "tos 5",
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },

    # ===== Dungeons =====

    # wooded temple
    "Wooded Temple Lobby Enter Dungeon": {
        "return_name": "Wooded Temple 1F Exit",
        "entrance_region": "wt lobby",
        "exit_region": "wt 1f",
        "entrance": (0x19, 0xA, 1),
        "exit": (0x19, 0x0, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "island": EntranceGroups.WOODED
    },
    "Wooded Temple 1F SE Staircase": {
        "return_name": "Wooded Temple 2F SE Staircase",
        "entrance_region": "wt 1f right arena",
        "exit_region": "wt 2f",
        "entrance": (0x19, 0x0, 1),
        "exit": (0x19, 0x1, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.WOODED
    },
    "Wooded Temple 1F NW Staircase": {
        "return_name": "Wooded Temple 2F NW Staircase",
        "entrance_region": "wt 1f north",
        "exit_region": "wt 2f north",
        "entrance": (0x19, 0x0, 2),
        "exit": (0x19, 0x1, 1),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.WOODED
    },
    "Wooded Temple 1F SW Staircase": {
        "return_name": "Wooded Temple 2F SW Staircase",
        "entrance_region": "wt 1f left arena",
        "exit_region": "wt 2f left",
        "entrance": (0x19, 0x0, 3),
        "exit": (0x19, 0x1, 3),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.WOODED
    },
    "Wooded Temple 2F W Staircase": {
        "return_name": "Wooded Temple 3F W Staircase",
        "entrance_region": "wt 2f left",
        "exit_region": "wt 3f left",
        "entrance": (0x19, 0x1, 4),
        "exit": (0x19, 0x2, 2),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.WOODED
    },
    "Wooded Temple 2F Central Staircase": {
        "return_name": "Wooded Temple 3F N Staircase",
        "entrance_region": "wt 2f moth door",
        "exit_region": "wt 3f",
        "entrance": (0x19, 0x1, 2),
        "exit": (0x19, 0x2, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.WOODED
    },
    "Wooded Temple 3F S Staircase": {
        "return_name": "Wooded Temple 4F S Staircase",
        "entrance_region": "wt 3f boss door",
        "exit_region": "wt 4f",
        "entrance": (0x19, 0x2, 1),
        "exit": (0x19, 0x3, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.WOODED
    },
    "Wooded Temple 4F N Staircase": {
        "return_name": "Stagnox Exit",
        "entrance_region": "wt 4f",
        "exit_region": "wt pre stagnox",
        "entrance": (0x19, 0x3, 1),
        "exit": (0x1E, 0x0, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.BOSS,
        "island": EntranceGroups.WOODED
    },
    "Wooded Temple 4F Blue Warp": {
        "return_name": "Wooded Temple Lobby Blue Warp",
        "entrance_region": "wt 4f",
        "exit_region": "wt blue warp",
        "entrance": (0x19, 0x3, 2),
        "exit": (0x19, 0xA, 2),
        "direction": EntranceGroups.DOWN,
        "type": EntranceGroups.WARP_PORTAL,
        "island": EntranceGroups.WOODED
    },

    # Blizzard Temple
    "Blizzard Temple Lobby Enter Dungeon": {
        "return_name": "Blizzard Temple 1F South Exit",
        "entrance_region": "bt lobby",
        "exit_region": "bt 1f exit",
        "entrance": (0x1a, 0x4, 1),
        "exit": (0x1a, 0x5, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 1F South Entrance": {
        "return_name": "Blizzard Temple 1F Main South",
        "entrance_region": "bt 1f s",
        "exit_region": "bt 1f",
        "entrance": (0x1a, 0x5, 5),
        "exit": (0x1a, 0x0, 7),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 1F Main East": {
        "return_name": "Blizzard Temple 1F SE Entrance",
        "entrance_region": "bt 1f e",
        "exit_region": "bt 1f se",
        "entrance": (0x1a, 0x0, 8),
        "exit": (0x1a, 0x5, 6),
        "direction": EntranceGroups.DOWN,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 1F SE Staircase": {
        "return_name": "Blizzard Temple B1 SE Staircase",
        "entrance_region": "bt 1f se door",
        "exit_region": "bt b1 se",
        "entrance": (0x1a, 0x5, 1),
        "exit": (0x1a, 0x1, 1),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 1F NE Staircase": {
        "return_name": "Blizzard Temple B1 NE Staircase",
        "entrance_region": "bt 1f ne",
        "exit_region": "bt b1 ne door",
        "entrance": (0x1a, 0x0, 2),
        "exit": (0x1a, 0x1, 2),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 1F Main SW": {
        "return_name": "Blizzard Temple 1F SW Entrance",
        "entrance_region": "bt 1f",
        "exit_region": "bt 1f sw",
        "entrance": (0x1a, 0x0, 6),
        "exit": (0x1a, 0x5, 4),
        "direction": EntranceGroups.DOWN,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 1F SW Staircase": {
        "return_name": "Blizzard Temple B1 SW Staircase",
        "entrance_region": "bt 1f sw door",
        "exit_region": "bt b1 sw",
        "entrance": (0x1a, 0x5, 3),
        "exit": (0x1a, 0x1, 3),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 1F NW Staircase": {
        "return_name": "Blizzard Temple B1 NW Staircase",
        "entrance_region": "bt 1f nw",
        "exit_region": "bt b1 nw",
        "entrance": (0x1a, 0x0, 4),
        "exit": (0x1a, 0x1, 4),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 1F NW Entrance": {
        "return_name": "Blizzard Temple 1F West Entrance",
        "entrance_region": "bt 1f nw",
        "exit_region": "bt 1f w",
        "entrance": (0x1a, 0x0, 9),
        "exit": (0x1a, 0x5, 7),
        "direction": EntranceGroups.DOWN,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 1F North Staircase": {
        "return_name": "Blizzard Temple 2F North Staircase",
        "entrance_region": "bt 1f n",
        "exit_region": "bt 2f",
        "entrance": (0x1a, 0x0, 5),
        "exit": (0x1a, 0x2, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 2F South Staircase": {
        "return_name": "Blizzard Temple 3F South Staircase",
        "entrance_region": "bt 2f boss door",
        "exit_region": "bt 3f",
        "entrance": (0x1a, 0x2, 1),
        "exit": (0x1a, 0x3, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 3F North Staircase": {
        "return_name": "Fraaz Exit",
        "entrance_region": "bt 3f",
        "exit_region": "bt pre fraaz",
        "entrance": (0x1a, 0x3, 1),
        "exit": (0x1F, 0x0, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.BOSS,
        "island": EntranceGroups.BLIZZARD
    },
    "Blizzard Temple 3F Blue Warp": {
        "return_name": "Blizzard Temple Lobby Blue Warp",
        "entrance_region": "bt 3f",
        "exit_region": "bt blue warp",
        "entrance": (0x1a, 0x3, 2),
        "exit": (0x1a, 0x4, 3),
        "direction": EntranceGroups.DOWN,
        "type": EntranceGroups.WARP_PORTAL,
        "island": EntranceGroups.BLIZZARD
    },

    # Marine Temple
    "Marine Temple Lobby Enter Dungeon": {
        "return_name": "Marine Temple 1F Exit",
        "entrance_region": "oct lobby",
        "exit_region": "oct 1f",
        "entrance": (0x1b, 0xA, 1),
        "exit": (0x1b, 0x0, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 1F North Staircase": {
        "return_name": "Marine Temple 2F North Staircase",
        "entrance_region": "oct 1f",
        "exit_region": "oct 2f",
        "entrance": (0x1b, 0x0, 1),
        "exit": (0x1b, 0x1, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 2F Left Bomb Cave": {
        "return_name": "Marine Temple Stamp Room Exit",
        "entrance_region": "oct 2f",
        "exit_region": "oct stamp room",
        "entrance": (0x1b, 0x1, 3),
        "exit": (0x1b, 0x7, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 2F Right Bomb Cave": {
        "return_name": "Marine Temple Switch Room Exit",
        "entrance_region": "oct 2f",
        "exit_region": "oct boomerang room",
        "entrance": (0x1b, 0x1, 4),
        "exit": (0x1b, 0x7, 1),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 1F East Staircase": {
        "return_name": "Marine Temple 2F NE Staircase",
        "entrance_region": "oct 1f right",
        "exit_region": "oct 2f right",
        "entrance": (0x1b, 0x0, 2),
        "exit": (0x1b, 0x1, 2),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 2F East Staircase": {
        "return_name": "Marine Temple 3F East Staircase",
        "entrance_region": "oct 2f right",
        "exit_region": "oct 3f east",
        "entrance": (0x1b, 0x1, 1),
        "exit": (0x1b, 0x2, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 3F North Staircase": {
        "return_name": "Marine Temple 4F North Staircase",
        "entrance_region": "oct 3f ne",
        "exit_region": "oct 4f north",
        "entrance": (0x1b, 0x2, 3),
        "exit": (0x1b, 0x3, 2),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 3F West Staircase": {
        "return_name": "Marine Temple 4F West Staircase",
        "entrance_region": "oct 3f west",
        "exit_region": "oct 4f west",
        "entrance": (0x1b, 0x2, 1),
        "exit": (0x1b, 0x3, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 3F South Staircase": {
        "return_name": "Marine Temple 4F South Staircase",
        "entrance_region": "oct 3f south",
        "exit_region": "oct 4f south",
        "entrance": (0x1b, 0x2, 2),
        "exit": (0x1b, 0x3, 3),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 4F East Staircase": {
        "return_name": "Marine Temple 5F East Staircase",
        "entrance_region": "oct 4f east",
        "exit_region": "oct 5f",
        "entrance": (0x1b, 0x3, 1),
        "exit": (0x1b, 0x4, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 5F NW Staircase": {
        "return_name": "Marine Temple 6F NW Staircase",
        "entrance_region": "oct 5f nw",
        "exit_region": "oct 6f nw",
        "entrance": (0x1b, 0x4, 2),
        "exit": (0x1b, 0x5, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 5F SW Staircase": {
        "return_name": "Marine Temple 6F SW Staircase",
        "entrance_region": "oct 5f sw",
        "exit_region": "oct 6f sw",
        "entrance": (0x1b, 0x4, 1),
        "exit": (0x1b, 0x5, 1),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 5F SE Staircase": {
        "return_name": "Marine Temple 6F SE Staircase",
        "entrance_region": "oct 5f se",
        "exit_region": "oct 6f se",
        "entrance": (0x1b, 0x4, 4),
        "exit": (0x1b, 0x5, 2),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 6F Central Staircase": {
        "return_name": "Marine Temple 7F South Staircase",
        "entrance_region": "oct 6f boss door",
        "exit_region": "oct 7f south",
        "entrance": (0x1b, 0x5, 3),
        "exit": (0x1b, 0x6, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 7F North Staircase": {
        "return_name": "Cactops Exit",
        "entrance_region": "oct 7f north",
        "exit_region": "oct pre phytops",
        "entrance": (0x1b, 0x6, 1),
        "exit": (0x20, 0x0, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.BOSS,
        "island": EntranceGroups.MARINE
    },
    "Marine Temple 7F Blue Warp": {
        "return_name": "Marine Temple Lobby Blue Warp",
        "entrance_region": "oct 7f north",
        "exit_region": "oct blue warp",
        "entrance": (0x1b, 0x6, 2),
        "exit": (0x1b, 0xA, 2),
        "direction": EntranceGroups.DOWN,
        "type": EntranceGroups.WARP_PORTAL,
        "island": EntranceGroups.MARINE
    },

    # Mountain Temple
    "Mountain Temple Lobby Enter Dungeon": {
        "return_name": "Mountain Temple 1F Exit",
        "entrance_region": "mtt lobby",
        "exit_region": "mtt 1f",
        "entrance": (0x1c, 0xA, 1),
        "exit": (0x1c, 0x0, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple 1F SW Staircase": {
        "return_name": "Mountain Temple 2F SW Staircase",
        "entrance_region": "mtt 1f left",
        "exit_region": "mtt 2f left",
        "entrance": (0x1c, 0x0, 5),
        "exit": (0x1c, 0x6, 3),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple 1F SE Staircase": {
        "return_name": "Mountain Temple 2F SE Staircase",
        "entrance_region": "mtt 1f right",
        "exit_region": "mtt 2f right",
        "entrance": (0x1c, 0x0, 4),
        "exit": (0x1c, 0x6, 2),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple 1F Central Staircase": {
        "return_name": "Mountain Temple 2F Central Staircase",
        "entrance_region": "mtt 1f door",
        "exit_region": "mtt 2f arena",
        "entrance": (0x1c, 0x0, 1),
        "exit": (0x1c, 0x6, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple 1F NE Staircase": {
        "return_name": "Mountain Temple 2F NE Staircase",
        "entrance_region": "mtt 1f ne",
        "exit_region": "mtt 2f ne",
        "entrance": (0x1c, 0x0, 3),
        "exit": (0x1c, 0x6, 1),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple 1F North Staircase": {
        "return_name": "Mountain Temple B1 NE Staircase",
        "entrance_region": "mtt 1f n",
        "exit_region": "mtt b1 n",
        "entrance": (0x1c, 0x0, 2),
        "exit": (0x1c, 0x2, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple B1 North Staircase": {
        "return_name": "Mountain Temple B2 North Staircase",
        "entrance_region": "mtt b1 n",
        "exit_region": "mtt b2 n",
        "entrance": (0x1c, 0x2, 1),
        "exit": (0x1c, 0x3, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple B1 East Staircase": {
        "return_name": "Mountain Temple B2 East Staircase",
        "entrance_region": "mtt b1 arena",
        "exit_region": "mtt b2 se",
        "entrance": (0x1c, 0x2, 3),
        "exit": (0x1c, 0x3, 4),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple B1 West Staircase": {
        "return_name": "Mountain Temple B2 West Staircase",
        "entrance_region": "mtt b1 arena exit",
        "exit_region": "mtt b2 sw",
        "entrance": (0x1c, 0x2, 4),
        "exit": (0x1c, 0x3, 5),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple B1 Central Staircase": {
        "return_name": "Mountain Temple B2 Central Staircase",
        "entrance_region": "mtt b1 cart exit",
        "exit_region": "mtt b2 s",
        "entrance": (0x1c, 0x2, 2),
        "exit": (0x1c, 0x3, 2),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple B2 South Staircase": {
        "return_name": "Mountain Temple B3 South Staircase",
        "entrance_region": "mtt b2 s",
        "exit_region": "mtt b3",
        "entrance": (0x1c, 0x3, 3),
        "exit": (0x1c, 0x4, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple B3 North Staircase": {
        "return_name": "Mountain Temple B4 South Staircase",
        "entrance_region": "mtt b3 boss door",
        "exit_region": "mtt b4",
        "entrance": (0x1c, 0x4, 2),
        "exit": (0x1c, 0x5, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple B4 North Staircase": {
        "return_name": "Vulcano Exit",
        "entrance_region": "mtt b4",
        "exit_region": "mtt pre vulcano",
        "entrance": (0x1c, 0x5, 2),
        "exit": (0x21, 0x0, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.BOSS,
        "island": EntranceGroups.MOUNTAIN
    },
    "Mountain Temple Lobby Blue Warp": {
        "return_name": "Mountain Temple B4 Blue Warp",
        "entrance_region": "mtt blue warp",
        "exit_region": "mtt b4",
        "entrance": (0x1c, 0xa, 2),
        "exit": (0x1c, 0x5, 1),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.WARP_PORTAL,
        "island": EntranceGroups.MOUNTAIN
    },

    # Desert Temple
    "Desert Temple Lobby Enter Dungeon": {
        "return_name": "Desert Temple 1F Exit",
        "entrance_region": "dt lobby",
        "exit_region": "dt",
        "entrance": (0x1d, 0x6, 1),
        "exit": (0x1d, 0x0, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.DUNGEON_ENTRANCE,
        "island": EntranceGroups.DESERT
    },
    "Desert Temple 1F Lower Staircase": {
        "return_name": "Desert Temple B1 Left Staircase",
        "entrance_region": "dt",
        "exit_region": "dt b1 stairs",
        "entrance": (0x1d, 0x0, 2),
        "exit": (0x1d, 0x3, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.DESERT
    },
    "Desert Temple 1F Upper Staircase": {
        "return_name": "Desert Temple 2F Left Staircase",
        "entrance_region": "dt",
        "exit_region": "dt 2f west",
        "entrance": (0x1d, 0x0, 1),
        "exit": (0x1d, 0x1, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.DESERT
    },
    "Desert Temple 3F Staircase": {
        "return_name": "Desert Temple 2F Right Staircase",
        "entrance_region": "dt 3f",
        "exit_region": "dt 2f",
        "entrance": (0x1d, 0x2, 0),
        "exit": (0x1d, 0x1, 1),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.DESERT
    },
    "Desert Temple B1 Boss Door Staircase": {
        "return_name": "Desert Temple B2 South Staircase",
        "entrance_region": "dt b1 boss door",
        "exit_region": "dt b2 s",
        "entrance": (0x1d, 0x3, 1),
        "exit": (0x1d, 0x4, 0),
        "direction": EntranceGroups.NONE,
        "type": EntranceGroups.DUNGEON_ROOM,
        "island": EntranceGroups.DESERT
    },
    "Desert Temple B2 North Entrance": {
        "return_name": "Capbone Exit",
        "entrance_region": "dt b2 n",
        "exit_region": "dt pre skeldritch",
        "entrance": (0x1d, 0x4, 1),
        "exit": (0x22, 0x0, 0),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.BOSS,
        "island": EntranceGroups.DESERT
    },
    "Desert Temple Lobby Blue Warp": {
        "return_name": "Desert Temple B2 Blue Warp",
        "entrance_region": "dt blue warp",
        "exit_region": "dt b2 n",
        "entrance": (0x1d, 0x6, 3),
        "exit": (0x1d, 0x4, 2),
        "direction": EntranceGroups.UP,
        "type": EntranceGroups.WARP_PORTAL,
        "island": EntranceGroups.DESERT
    },

    # Misc entrances
    "Desert Temple Enter Post-Fight": {
        "return_name": "Skeldritch Post-Fight Exit",
        "entrance_region": "dt b2",
        "exit_region": "skeldritch",
        "entrance": (0x1D, 0x4, 0x1),
        "exit": (0x22, 0x1, 0),
        "type": EntranceGroups.BOSS,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.DESERT
    },
    "Stagnox Blue Warp": {
        "return_name": "Wooded Temple Lobby Boss Warp",
        "entrance_region": "wt stagnox",
        "exit_region": "wt lobby",
        "entrance": (0x1E, 0x0, 5),
        "exit": (0x19, 0xA, 1),
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.WOODED,
        "two_way": False
    },
    "Fraaz Blue Warp": {
        "return_name": "Blizzard Temple Lobby Boss Warp",
        "entrance_region": "bt fraaz",
        "exit_region": "bt lobby",
        "entrance": (0x1F, 0x0, 5),
        "exit": (0x1A, 0x4, 2),
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.BLIZZARD,
        "two_way": False
    },
    "Cactops Blue Warp": {
        "return_name": "Marine Temple Lobby Boss Warp",
        "entrance_region": "oct phytops",
        "exit_region": "oct lobby",
        "entrance": (0x20, 0x0, 5),
        "exit": (0x1B, 0xC, 1),
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.MARINE,
        "two_way": False
    },
    "Vulcano Blue Warp": {
        "return_name": "Mountain Temple Lobby Boss Warp",
        "entrance_region": "mtt vulcano",
        "exit_region": "mtt lobby",
        "entrance": (0x21, 0x0, 5),
        "exit": (0x1C, 0xC, 1),
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.MOUNTAIN,
        "two_way": False
    },
    "Desert Temple Bow of Light Room Blue Warp": {
        "return_name": "Desert Temple Lobby Boss Warp",
        "entrance_region": "dt skeldritch",
        "exit_region": "dt lobby",
        "entrance": (0x1d, 0x5, 1),
        "exit": (0x1D, 0x6, 1),
        "type": EntranceGroups.NONE,
        "direction": EntranceGroups.UP,
        "island": EntranceGroups.DESERT,
        "two_way": False
    },
}


ENTRANCES: dict[str, STTransition] = STTransition.from_data(ENTRANCE_DATA)
entrance_id_to_entrance = {e.id: e for e in ENTRANCES.values()}
entrance_id_to_region = {e.id: e.entrance_region for e in ENTRANCES.values()}
entrance_tuple_to_entrance: dict[tuple[int, int, int], STTransition] = {e.entrance: e for e in ENTRANCES.values()}

location_event_lookup = {"Stagnox Boss Reward": "EVENT: Defeat Stagnox",
                         "Fraaz Boss Reward": "EVENT: Defeat Fraaz",
                         "ToS 3F Forest Rail Glyph": "EVENT: Reach ToS 3F",
                         "ToS 7F Snow Rail Glyph": "EVENT: Reach ToS 7F",
                         "ToS 12F Ocean Rail Glyph": "EVENT: Reach ToS 12F",
                         "ToS 17F Fire Rail Glyph": "EVENT: Reach ToS 17F",
                         "ToS 23F Defeat Staven": "EVENT: Defeat Staven",
                         "ToS 24F Final Chest": "EVENT: Reach ToS 24F",
                         "Cactops Boss Reward": "EVENT: Defeat Cactops",
                         "Vulcano Boss Reward": "EVENT: Defeat Vulcano",
                         "Capbone Boss Reward": "EVENT: Defeat Skeldritch",
                         "Castle Town Take 'em All On Level 3": "EVENT: Complete Take 'em All On 3",
                         "Lost at Sea Final Chest": "EVENT: Complete Lost at Sea Dungeon"}
boss_events = set(location_event_lookup.values())
goal_event_lookup =     {0: "GOAL: Defeat Stagnox",
                         1: "GOAL: Defeat Fraaz",
                         2: "GOAL: Defeat Cactops",
                         3: "GOAL: Defeat Vulcano",
                         4: "GOAL: Defeat Skeldritch",
                         5: "GOAL: Reach ToS 3F",
                         6: "GOAL: Reach ToS 7F",
                         7: "GOAL: Reach ToS 12F",
                         8: "GOAL: Reach ToS 17F",
                         9: "GOAL: Defeat Staven",
                         10: "GOAL: Reach ToS 24F",
                         -1: "GOAL: Defeat Malladus"}