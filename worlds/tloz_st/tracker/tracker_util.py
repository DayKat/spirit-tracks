from typing import TYPE_CHECKING
from ..data.Entrances import ENTRANCES
from ..data.Locations import LOCATIONS_DATA

if TYPE_CHECKING:
    from .. import SpiritTracksWorld

map_lookup: dict[int, str] = {
    0: "Overview",
    1: "Forest Realm",
    2: "Snow Realm",
    3: "Ocean Realm",
    4: "Fire Realm",
    5: "Ocean Undersea",

    6: "Outset Village",
    7: "Mayscore",
    8: "Mayscore Forest",
    9: "Castle Town",
    10: "Woodland Sanctuary",
    11: "Rabbit Haven",
    12: "Trading Post",

    13: "Anouki Village",
    14: "Snowfall Sanctuary",
    15: "Bridge Worker",
    16: "Icy Spring",
    17: "Slippery Station",
    18: "Snowdrift Station",

    19: "Papuzia Village",
    20: "Papuzia Archipelago",
    21: "Island Sanctuary South",
    22: "Island Sanctuary North",
    23: "Pirate Hideout",
    24: "Lost at Sea Station",

    25: "Goron Village",
    26: "Goron Field",
    27: "Valley Sanctuary",
    28: "Goron Target Range",
    29: "Disorientation Station",
    30: "Dark Ore Mine",
    31: "Ends of the Earth Station",

    32: "Dune Sanctuary",
    33: "Tower of Spirits Lobby",
    34: "Tower of Spirits",

    35: "Wooded Temple Lobby",
    36: "Wooded Temple 1F",
    37: "Wooded Temple 2F",
    38: "Wooded Temple 3F",
    39: "Wooded Temple 4F",
    40: "Stagnox Arena",

    41: "Blizzard Temple Lobby",
    42: "Blizzard Temple 1F",
    43: "Blizzard Temple B1",
    44: "Blizzard Temple 2F",
    45: "Blizzard Temple 3F",
    46: "Fraaz Arena",

    47: "Marine Temple Lobby",
    48: "Marine Temple 1F",
    49: "Marine Temple 2F",
    50: "Marine Temple 3F",
    51: "Marine Temple 4F",
    52: "Marine Temple 5F",
    53: "Marine Temple 6F",
    54: "Marine Temple 7F",
    55: "Marine Temple 2F Secret",
    56: "Cactops Arena",

    57: "Mountain Temple Lobby",
    58: "Mountain Temple 1F",
    59: "Mountain Temple 2F",
    60: "Mountain Temple B1",
    61: "Mountain Temple B2",
    62: "Mountain Temple B3",
    63: "Mountain Temple B4",
    64: "Vulcano Arena",

    65: "Desert Temple Lobby",
    66: "Desert Temple 1F",
    67: "Desert Temple 2F",
    68: "Desert Temple 3F",
    69: "Desert Temple B1",
    70: "Desert Temple B2",
    71: "Capbone Arena",
    72: "Desert Temple B4",

    73: "Tower of Spirits 1F",
    74: "Tower of Spirits 2F",
    75: "Tower of Spirits 2F Secret",
    76: "Tower of Spirits 3F",

    77: "Tower of Spirits 4F",
    78: "Tower of Spirits 5F",
    79: "Tower of Spirits 5F Secret",
    80: "Tower of Spirits 6F",
    81: "Tower of Spirits 7F",

    82: "Tower of Spirits 8F",
    83: "Tower of Spirits 8F North Secret",
    84: "Tower of Spirits 8F South Secret",
    85: "Tower of Spirits 9F",
    86: "Tower of Spirits 9F Secret",
    87: "Tower of Spirits 10F",
    88: "Tower of Spirits 11F",
    89: "Tower of Spirits 12F",

    90: "Tower of Spirits 13F",
    91: "Tower of Spirits 14F",
    92: "Tower of Spirits 15F",
    93: "Tower of Spirits 16F",
    94: "Tower of Spirits 16F Secret",
    95: "Tower of Spirits 17F",

    96: "Tower of Spirits 18F",
    97: "Tower of Spirits 19F",
    98: "Tower of Spirits 20F",
    99: "Tower of Spirits 21F",
    100: "Tower of Spirits 21F Secret",
    101: "Tower of Spirits 22F",
    102: "Tower of Spirits 23F",
    103: "Tower of Spirits Staven Arena",

    104: "Tower of Spirits 31F",
    105: "Tower of Spirits 30F",
    106: "Tower of Spirits 29F",
    107: "Tower of Spirits 29F Secret",
    108: "Tower of Spirits 30F Secret",
    109: "Tower of Spirits 28F",
    110: "Tower of Spirits 27F",
    111: "Tower of Spirits 26F",
    112: "Tower of Spirits 25F",
    113: "Tower of Spirits 24F",

    114: "Lost at Sea Lobby",
    115: "Lost at Sea 1",
    116: "Lost at Sea 2",
    117: "Lost at Sea 3",
    118: "Lost at Sea 4",
    119: "Lost at Sea 5",
    120: "Lost at Sea 6",

    121: "Niko's House",
    122: "Alfonzo's House",
    123: "Mary's House",

    124: "Mayscore Shop",
    125: "Wood's House",
    126: "Morris' House",
    127: "Dovok's House",

    128: "Gage's Sanctuary",

    129: "Castle Town Shop",
    130: "Mona's House",
    131: "Lucia's House",
    132: "Milo's House",
    133: "Take 'em All On Lobby",

    134: "Hyrule Castle Courtyard",
    135: "Hyrule Castle 1F",
    136: "Hyrule Castle 2F",
    137: "Hyrule Castle Barracks",
    138: "Hyrule Castle Infirmary",
    139: "Hyrule Castle Throne",
    140: "Zelda's Room",
    141: "Hyrule Castle Backyard",
    142: "Tunnel to ToS 1F",
    143: "Tunnel to ToS 2F",
    144: "Tunnel to ToS 3F",

    145: "Like-Like Tunnel",
    146: "Linebeck's Shop",
    147: "Linebeck's Treasure Cave",

    148: "Small Ice Puzzle Cave",
    149: "Yefu's House",
    150: "Noko's House",
    151: "Bulu's House",
    152: "Yeko's House",
    153: "Honcho's House",
    154: "Kofu's House",

    155: "Head Statue Cave",
    156: "Steem's Sanctuary",
    157: "Snowfall Supermarket",

    158: "Kenzo's House",
    159: "Ferrus' Trailer",
    160: "Skating Rink",

    161: "Snowdrift Cave",
    162: "Octive Arena",
    163: "Small Skating Cave",
    164: "Frostflame Cave",
    165: "Big Ice Puzzle Cave",

    166: "Treasure Cave",
    167: "Papuzia Shop",
    168: "Orca's House",
    169: "Wise One's House",
    170: "Fuku's House",

    171: "Crab Cave",
    172: "Carben's Sanctuary",

    173: "Disorientation 1",
    174: "Disorientation 2",
    175: "Disorientation 3",
    176: "Disorientation 4",
    177: "Disorientation 5",
    178: "Disorientation 6",
    179: "Disorientation 7",
    180: "Disorientation 8",
    181: "Disorientation 9",

    182: "Dark Ore Tunnels",

    183: "Ends of the Earth 1",
    184: "Ends of the Earth 2",
    185: "Ends of the Earth 3",
    186: "Ends of the Earth 4",
    187: "Ends of the Earth 5",
    188: "Ends of the Earth 6",
    189: "Ends of the Earth 7",
    190: "Ends of the Earth 8",
    191: "Ends of the Earth 9",
    192: "Ends of the Earth A",
    193: "Ends of the Earth B",
    194: "Ends of the Earth C",

    195: "Mountain Altar",
    196: "Goron Shop",
    197: "Kofu's New House",
    198: "Elder Goron House",
    199: "Goron 3 Pots House",
    200: "Mouldy Goron House",
    201: "Goron 2 Pots House",
    202: "Lava Goron House",
    203: "Burning Tunnel",
    204: "Embrose's Sanctuary",

    205: "Sandy Tunnel",
    206: "Rael's Sanctuary",

    207: "Dark Realm",
    208: "Cosmic Ocean",
    209: "Disorientation Dungeon",
    210: "Pirate Hangout",
    211: "Beedle"
}

station_section_link: dict[str, str] = {
    "Overview Castle Town": "Forest Realm Castle Town Station",
    "Overview Hyrule Castle": ["Forest Realm Castle Town Station", "Castle Town North", "Hyrule Castle Courtyard Entrance"],
    "Overview Outset": "Forest Realm Outset Station",
    "Overview Mayscore": "Forest Realm Mayscore Station",
    "Overview Woodland": "Forest Realm Woodland Sanctuary Station",
    "Overview Rabbit Haven": "Forest Realm Rabbit Haven Station",
    "Overview Trading Post": "Forest Realm Trading Post Station",
    "Overview WT": ["Forest Realm Wooded Temple Station", "Wooded Temple Lobby Enter Dungeon"],

    "Overview Anouki": "Snow Realm Anouki Village Station",
    "Overview Snowfall": "Snow Realm Snowfall Sanctuary Station",
    "Overview BT": ["Snow Realm Blizzard Temple Station", "Blizzard Temple Lobby Enter Dungeon"],
    "Overview Icyspring": "Snow Realm Icy Spring Station",
    "Overview Snowdrift": "Snow Realm Snowdrift Station",
    "Overview Slippery": "Snow Realm Slippery Station",
    "Overview Kenzo": "Snow Realm Bridge Worker's Station",

    "Overview Papuzia": "Ocean Realm Papuzia Station",
    "Overview Island": "Ocean Realm Island Sanctuary Station",
    "Overview OCT": ["Undersea Marine Temple Station", "Marine Temple Lobby Enter Dungeon"],
    "Overview Pirate": "Ocean Realm Pirate Hideout Station",
    "Overview LAS": "Ocean Realm Lost at Sea Station",
    "Overview Dune": "Ocean Realm Dune Sanctuary Station",
    "Overview DT": ["Ocean Realm Desert Temple Station", "Desert Temple Lobby Enter Dungeon"],

    "Overview Disorientation": "Fire Realm Disorientation Station",
    "Overview EotE": "Fire Realm Ends of the Earth Station",
    "Overview DOM": "Fire Realm Dark Ore Mine Station",
    "Overview Goron": "Fire Realm Goron Village Station",
    "Overview Goron Field": ["Goron Village West", "Fire Realm Goron Village Station"],
    "Overview Valley": ["Fire Realm Goron Village Station", "Goron Village Enclave North", "Elder Goron House Cave", "Goron Village Elder's House"],
    "Overview GTR": "Fire Realm Goron Target Range Station",
    "Overview MTT": ["Fire Realm Mountain Temple Station", "Mountain Temple Lobby Enter Dungeon"],

    "Lost at Sea Station Cave": ["Lost at Sea Lobby Enter Dungeon"],
}

boss_event_link: dict[str, list[str]] = {
    "Overview WT Events": [
        "Forest Realm Wooded Temple Station",
        "Wooded Temple Lobby Enter Dungeon",
        "Wooded Temple 4F N Staircase"],
    "Overview BT Events": [
        "Snow Realm Blizzard Temple Station",
        "Blizzard Temple Lobby Enter Dungeon",
        "Blizzard Temple 3F North Staircase"],
    "Overview OCT Events": [
        "Ocean Realm Dive Underwater",
        "Undersea Marine Temple Station",
        "Marine Temple Lobby Enter Dungeon",
        "Marine Temple 7F North Staircase"],
    "Overview MTT Events": [
        "Fire Realm Mountain Temple Station",
        "Mountain Temple Lobby Enter Dungeon",
        "Mountain Temple B4 North Staircase"],
    "Overview DT Events": [
        "Ocean Realm Desert Temple Station",
        "Desert Temple Lobby Enter Dungeon",
        "Desert Temple B2 North Entrance"],
    "Overview OCT Undersea Events": [
        "Undersea Marine Temple Station",
        "Marine Temple Lobby Enter Dungeon",
        "Marine Temple 7F North Staircase"],

    "Ferrus Outset Event": ["Forest Realm Outset Station"],
    "Carben Island Event": ["Ocean Realm Island Sanctuary Station"],
    "Goron Anouki Event": ["Snow Realm Anouki Village Station"],
    "Disorientation Event": ["Fire Realm Disorientation Station", "Disorientation Station Cave"],

    "Mayscore Stamp Event": ["Mayscore North"],
    "Papuzia Stamp Event": ["Papuzia South"],
    "Island Sanctuary Stamp Event": ["Island Sanctuary South Peninsula"],
    "Goron Stamp Event": ["Goron Village West"],
    "Valley Sanctuary Stamp Event": ["Fire Realm Goron Village Station", "Goron Village Enclave North", "Elder Goron House Cave", "Goron Village Elder's House"]

}

def get_hidden_map_icons(world: "SpiritTracksWorld"):
    import json
    import pkgutil
    pack_name = world.__class__.__module__

    def get_json(files):
        res = []
        for f in files:
            res += json.loads(
                pkgutil.get_data(
                    pack_name,
                    f"/tracker/{f}").decode('utf-8-sig'))
        return res

    entr_data = get_json(["entrances/entrances.json"])
    loc_data = get_json(["locations/overworld.json"])
    active_entrances = [int(i) for i in world.ut_pairings]
    entr_hidden: dict[str, list[str]] = {}
    locs_hidden: dict[str, list[int]] = {}  # map_name: [loc_ids]
    events_hidden = {}
    map_coord_checks: dict[str, list[tuple[int, int]]] = {}

    # Handle entrances
    for entrance in entr_data:
        entr_section = entrance.get("name")
        entr_names = [s.get("name") for s in entrance.get("sections", [])]
        map_locs = [m for m in entrance.get("map_locations", [])]
        map_loc_names = [m["map"] for m in map_locs]

        for entr_name in entr_names:
            if entr_name not in ENTRANCES:
                print(f"Wrong Entrance in tracker data: {entr_name}")
            elif ENTRANCES[entr_name].id not in active_entrances:
                for map_loc in map_loc_names:
                    entr_hidden.setdefault(map_loc, []).append(entr_name)
            else:
                for map_loc in map_locs:
                    if world.options.randomize_stamps.value == 1 and entr_name.endswith("Stamp Station"):
                        entr_hidden.setdefault(map_loc["map"], []).append(entr_name)
                    else:
                        coords = (map_loc["x"], map_loc["y"])
                        map_coord_checks.setdefault(map_loc["map"], []).append(coords)



        # Filter out stations using station_section_link
        if entr_section in boss_event_link:
            blocking_entrances = [ENTRANCES[e].id for e in boss_event_link[entr_section]]
            for blocking_entrance in blocking_entrances:
                if blocking_entrance in active_entrances:
                    for loc_map in map_loc_names:
                        entr_hidden.setdefault(loc_map, [])
                        entr_hidden[loc_map] += entr_names

    # print(f"map_coord_checks: {map_coord_checks}")

    # Handle locations and coord check entrances
    for loc in loc_data:
        loc_section = loc["name"]
        loc_names = [s.get("name") for s in loc.get("sections", [])]
        loc_map_locations = loc.get("map_locations")
        loc_maps = [l["map"] for l in loc_map_locations]
        loc_coords = [(l["x"], l["y"]) for l in loc_map_locations]

        # Filter out stations using station_section_link
        if loc_section in station_section_link:
            _e = station_section_link[loc_section]
            _e = _e if isinstance(_e, list) else [_e]
            blocking_entrances = [ENTRANCES[i].id for i in _e]
            for blocking_entrance in blocking_entrances:
                if blocking_entrance in active_entrances:
                    for loc_map in loc_maps:
                        locs_hidden.setdefault(loc_map, [])
                        locs_hidden[loc_map] += [world.location_name_to_id[n] for n in loc_names]

        for loc_map in loc_maps:
            if loc_map in map_coord_checks:
                # print(f"Testing {loc_map} coords {loc_coords} in {[i for i in map_coord_checks[loc_map]]}")
                coords_in_map = [i for i in map_coord_checks[loc_map]]
                for c in loc_coords:
                    if c in coords_in_map:
                        loc_ids = []
                        for loc2 in loc_names:
                            if "EVENT" in loc2 or "GOAL" in loc2:
                                entr_hidden.setdefault(loc_map, []).append(loc2)
                            else:
                                loc_ids.append(world.location_name_to_id[loc2])
                        locs_hidden.setdefault(loc_map, [])
                        locs_hidden[loc_map] += loc_ids


    # Hard coded examples
    if ENTRANCES["Forest Realm Trading Post Station"].id in active_entrances:
        entr_hidden.setdefault("Overview", []).append("EVENT: Give Regal Ring to Linebeck")
        entr_hidden.setdefault("Forest Realm", []).append("EVENT: Give Regal Ring to Linebeck")
    if any([ENTRANCES[e].id in active_entrances for e in ["Fire Realm Goron Village Station",
                                                          "Goron Village West",
                                                          "Goron Field North"]]):
        entr_hidden.setdefault("Overview", []).append("EVENT: Visit Kagoron at the Mountain Altar")
        entr_hidden.setdefault("Fire Realm", []).append("EVENT: Visit Kagoron at the Mountain Altar")
    if ENTRANCES["Fire Realm Goron Village Station"].id in active_entrances:
        entr_hidden.setdefault("Overview", []).append("EVENT: Bring Ice to Kagoron")
        entr_hidden.setdefault("Fire Realm", []).append("EVENT: Bring Ice to Kagoron")

    if ENTRANCES["Ocean Realm Dive Underwater"].id in active_entrances:
        entr_hidden.setdefault("Overview", []).append("Undersea Marine Temple Station")
        entr_hidden.setdefault("Ocean Realm", []).append("Undersea Marine Temple Station")
    if ENTRANCES["Lost at Sea Cave"].id in active_entrances:
        entr_hidden.setdefault("Overview", []).append("EVENT: Complete Lost at Sea Dungeon")
        entr_hidden.setdefault("Ocean Realm", []).append("EVENT: Complete Lost at Sea Dungeon")
        entr_hidden.setdefault("Lost at Sea Station", []).append("EVENT: Complete Lost at Sea Dungeon")
    if ENTRANCES["Castle Town Take 'em all On"].id in active_entrances:
        entr_hidden.setdefault("Overview", []).append("EVENT: Complete Take 'em All On 3")
        entr_hidden.setdefault("Forest Realm", []).append("EVENT: Complete Take 'em All On 3")
    if ENTRANCES["Forest Realm Castle Town Station"].id in active_entrances:
        entr_hidden.setdefault("Castle Town", []).append("EVENT: Complete Take 'em All On 3")
        entr_hidden.setdefault("Overview", []).append("EVENT: Complete Take 'em All On 3")  # these are duplicated, is fine.
        entr_hidden.setdefault("Forest Realm", []).append("EVENT: Complete Take 'em All On 3")



    # print(f"hidden entrances: {entr_hidden}")
    return locs_hidden, entr_hidden