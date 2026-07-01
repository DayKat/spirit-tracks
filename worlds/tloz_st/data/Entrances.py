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
    "Outset Board Train": {
        "return_name": "Forest Realm Outset Station",
        "exit": (0x4, 0x0, 1),
        "entrance": (0x2F, 0x0, 0),
        "exit_region": "outset station",
        "entrance_region": "outset village",
        "reverse_required_groups": ["Tracks: Forest Glyph"],
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
    "Mayscore Board Train": {
        "return_name": "Forest Realm Mayscore Station",
        "exit": (0x4, 0x0, 2),
        "entrance": (0x2A, 0x0, 0),
        "exit_region": "mayscore station",
        "entrance_region": "mayscore",
        "reverse_required_groups": ["Tracks: Forest Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Wooded Temple Lobby Board Train": {
        "return_name": "Forest Realm Wooded Temple Station",
        "exit": (0x4, 0x0, 4),
        "entrance": (0x19, 0xA, 0),
        "exit_region": "wt station",
        "entrance_region": "wt",
        "reverse_required_groups": [("Tracks: Wooded Temple Tracks", "Tracks: Forest Source")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Snow Realm Icy Spring": {
        "return_name": "Icy Spring Train",
        "entrance_region": "icyspring station",
        "exit_region": "icyspring",
        "required_groups": ["Tracks: Blizzard Temple Tracks"],
        "entrance": (0x5, 0x0, 0x3),
        "exit": (0x35, 0x0, 0x0),
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.INSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Blizzard Temple Lobby Board Train": {
        "return_name": "Snow Realm Blizzard Temple Station",
        "exit": (0x5, 0x0, 1),
        "entrance": (0x1A, 0x4, 0),
        "exit_region": "bt station",
        "entrance_region": "bt",
        "reverse_required_groups": [("Tracks: Blizzard Temple Tracks", "Tracks: Snow Source")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Papuzia Board Train": {
        "return_name": "Ocean Realm Papuzia Station",
        "exit": (0x6, 0x0, 0),
        "entrance": (0x2C, 0x0, 0),
        "exit_region": "papuzia station",
        "entrance_region": "papuzia",
        "reverse_required_groups": ["Tracks: Ocean Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Marine Temple Lobby Board Train": {
        "return_name": "Undersea Marine Temple Station",
        "exit": (0xA, 0x0, 1),
        "entrance": (0x1B, 0xA, 0),
        "exit_region": "oct station",
        "entrance_region": "oct",
        "reverse_required_groups": [("Tracks: Ocean Source", "Tracks: Marine Temple Tracks")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Marine Temple Train Exit Water Warp": {
        "exit": (0x6, 0x0, 3),
        "entrance": (0x1B, 0xA, 0),
        "exit_region": "ocean temple tracks",
        "entrance_region": "oct",
        "reverse_required_groups": [("Tracks: Ocean Source", "Tracks: Marine Temple Tracks")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Desert Temple Lobby Board Train": {
        "return_name": "Ocean Realm Desert Temple Station",
        "exit": (0x6, 0x0, 7),
        "entrance": (0x1D, 0x6, 0),
        "exit_region": "desert temple station",
        "entrance_region": "desert temple",
        "reverse_required_groups": ["Tracks: Desert Temple Tracks"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },

    "Fire Realm Goron Village Station": {
        "return_name": "Goron Village Board Train",
        "entrance_region": "goron village station",
        "exit_region": "goron village",
        "entrance": (0x7, 0x0, 0x3),
        "exit": (0x2E, 0x0, 0x0),
        "required_groups": [("Tracks: Fire Glyph", "Tracks: Fire Source")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.INSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Goron Target Range Exit": {
        "exit": (0x7, 0x0, 4),
        "entrance": (0x3c, 0x1, 1),
        "exit_region": "goron target station",
        "entrance_region": "gtr",
        "reverse_required_groups": ["Tracks: Fire Glyph"],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE,
        "two_way": False
    },
    "Mountain Temple Lobby Board Train": {
        "return_name": "Fire Realm Mountain Temple Station",
        "exit": (0x7, 0x0, 1),
        "entrance": (0x1c, 0xA, 0),
        "exit_region": "mtt station",
        "entrance_region": "mtt",
        "reverse_required_groups": [("Tracks: Mountain Temple Tracks", "Tracks: Fire Source")],
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
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
        "direction": EntranceGroups.OUTSIDE,
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
    "Ocean Realm East Ocean Shortcut": {
        "return_name": "Forest Realm West Ocean Shortcut",
        "entrance_region": "ocean shortcut east",
        "exit_region": "ocean shortcut",
        "extra_data": {"z_max": 0},
        "coords": (463671, 0, 147456),
        "entrance": (0x7, 0x0, 0xFD),
        "exit": (0x5, 0x0, 0xFE),
        "required_groups": ["Tracks: Forest Realm Ocean Shortcut"],
        "reverse_required_groups": ["Tracks: Forest Realm Ocean Shortcut"],
        "type": EntranceGroups.OVERWORLD_TRAIN,
        "direction": EntranceGroups.LEFT,
        "island": EntranceGroups.NONE
    },
    "Ocean Realm East Ocean Glyph": {
        "return_name": "Forest Realm West Ocean Glyph",
        "entrance_region": "ocean realm",
        "exit_region": "ocean realm mid",
        "extra_data": {"z_min": 0},
        "coords": (463671, 0, 147456),
        "entrance": (0x7, 0x0, 0xFD),
        "exit": (0x5, 0x0, 0xFE),
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
        "required_groups": ["Tracks: Sand Realm", "Tracks: Desert Temple Tracks"],
        "reverse_required_groups": ["Tracks: Sand Realm", "Tracks: Desert Temple Tracks"],
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
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits to Snow Realm": {
        "return_name": "Snow Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x5, 0x0, 6),
        "entrance_region": "tos",
        "exit_region": "tos snow station",
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits to Ocean Realm": {
        "return_name": "Ocean Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x6, 0x0, 4),
        "entrance_region": "tos",
        "exit_region": "tos ocean station",
        "type": EntranceGroups.STATION,
        "direction": EntranceGroups.OUTSIDE,
        "island": EntranceGroups.NONE
    },
    "Tower of Spirits to Fire Realm": {
        "return_name": "Fire Realm to Tower of Spirits",
        "entrance": (0x14, 1, 0),
        "exit": (0x7, 0x0, 2),
        "entrance_region": "tos",
        "exit_region": "tos fire station",
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
    "EVENT: Defeat Vulcano": {
        "two_way": False,
        "entrance_region": "mtt boss",
        "exit_region": "event_vulcano",
        "entrance": (0x21, 0x0, 0x0),
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
        "entrance": (0x37, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "EVENT: Bring Ice to Kagoron": {
        "two_way": False,
        "entrance_region": "goron ice",
        "exit_region": "goron ice event",
        "entrance": (0x2e, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },

    # Goals

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
    "GOAL: Defeat Cactops": {
        "two_way": False,
        "entrance_region": "oct phytops",
        "exit_region": "goal_phytops",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Vulcano": {
        "two_way": False,
        "entrance_region": "mtt boss",
        "exit_region": "goal_vulcano",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Skeldritch": {
        "two_way": False,
        "entrance_region": "skeldritch",
        "exit_region": "skeldritch goal",
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
    "GOAL: Reach ToS 12F": {
        "two_way": False,
        "entrance_region": "tos 11f",
        "exit_region": "goal_ocean_glyph",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Reach ToS 17F": {
        "two_way": False,
        "entrance_region": "tos 16f",
        "exit_region": "goal_fire_glyph",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Defeat Staven": {
        "two_way": False,
        "entrance_region": "tos staven",
        "exit_region": "goal_staven",
        "entrance": (0x29, 0x0, 0x0),
        "type": EntranceGroups.EVENT,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "GOAL: Reach ToS 24F": {
        "two_way": False,
        "entrance_region": "tos 24f",
        "exit_region": "goal_compass",
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
    "GOAL: Enter Dark Realm": {
        "two_way": False,
        "entrance_region": "dark realm trains",
        "exit_region": "dark realm event",
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

    "ToS Lobby Staircase": {
        "return_name": "ToS Staircase Exit",
        "entrance_region": "tos",
        "exit_region": "tos",
        "entrance": (0x14, 0x1, 0x1),  # Needs extra data for staircase side
        "exit": (0x17, 0x0, 0x0),
        "reverse_one_way_data": {"y": 0},
        "type": EntranceGroups.DUNGEON_ENTRANCE,
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
    # Misc entrances

    "Forest Sanctuary Enter Sanctuary": {
        "return_name": "Gage Exit",
        "entrance": (0x30, 0, 1),
        "exit": (0x30, 0x1, 0),
        "entrance_region": "woodland sanc",
        "exit_region": "woodland sanc song statue",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.INSIDE,
        "island": EntranceGroups.NONE
    },
    "Snow Sanctuary Enter Inner Sanctuary": {
        "return_name": "Steem Exit",
        "entrance": (0x31, 1, 1),
        "exit": (0x31, 0x2, 0),
        "entrance_region": "snow sanc",
        "exit_region": "snow sanc song",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.INSIDE,
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
    "Papuzia NW House": {
        "return_name": "Papuzia House",
        "entrance_region": "papuzia village",
        "exit_region": "papuzia nw house",
        "entrance": (0x2c, 0x0, 0x1),
        "exit": (0x2c, 0x1, 0x0),
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.NONE,
        "island": EntranceGroups.NONE
    },
    "Papuzia South": {
        "return_name": "South Papuzia North",
        "entrance_region": "papuzia village",
        "exit_region": "papuzia south",
        "entrance": (0x2c, 0x0, 0x5),
        "exit": (0x39, 0x0, 0x0),
        "type": EntranceGroups.OVERWORLD,
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
                         "ToS 7F Snow Rail Glyph": "EVENT: Reach ToS 7F",
                         "ToS 12F Ocean Rail Glyph": "EVENT: Reach ToS 12F",
                         "ToS 17F Fire Rail Glyph": "EVENT: Reach ToS 17F",
                         "ToS 23F Defeat Staven": "EVENT: Defeat Staven",
                         "ToS 24F Final Chest": "EVENT: Reach ToS 24F",
                         "Marine Temple Dungeon Reward": "EVENT: Defeat Cactops",
                         "Mountain Temple Dungeon Reward": "EVENT: Defeat Vulcano",
                         "Desert Temple Dungeon Reward": "EVENT: Defeat Skeldritch",
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