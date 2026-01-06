from typing import TYPE_CHECKING
from ..data.Entrances import ENTRANCES, entrance_id_to_region

if TYPE_CHECKING:
    from ..__init__ import PhantomHourglassWorld

MAP_INDEX = {
    0x2b00: 2, 0x12b00: 2,
    0x3000: 3, 0x13000: 3,
    0x2c00: 4, 0x12c00: 4,
    0x2e00: 5, 0x12e00: 5,
    0x2d00: 6, 0x12d00: 6,
    0x2a00: 7, 0x12a00: 7,
    0x2f00: 8, 0x12f00: 8,
    0x2700: 9, 0x12700: 9,
    0x2701: 10, 0x12701: 10,
    0x1c00: 11, 0x11c00: 11,
    0x1c01: 12, 0x11c01: 12,
    0x1c02: 13, 0x11c02: 13,
    0x1c03: 14, 0x11c03: 14,
    0x2900: 15, 0x12900: 15,
    0x2901: 16, 0x12901: 16,
    0x2902: 17, 0x12902: 17,
    0x2903: 18, 0x12903: 18,
    0x2904: 19, 0x12904: 19,
    0x2600: 20, 0x12600: 20,
    0x2500: 21, 0x12500: 21,
    0x2501: 22, 0x12501: 22,
    0x2502: 23, 0x12502: 23,
    0x2503: 24, 0x12503: 24,
    0x2504: 25, 0x12504: 25,
    0x2505: 26, 0x12505: 26,
    0x2506: 27, 0x12506: 27,
    0x2507: 28, 0x12507: 28,
    0x2508: 29, 0x12508: 29,
    0x2509: 30, 0x12509: 30,
    0x250A: 31, 0x1250A: 31,
    0x250B: 32, 0x1250B: 32,
    0x250C: 33, 0x1250C: 33,
    0x250D: 34, 0x1250D: 34,
    0x250E: 35, 0x1250E: 35,
    0x250F: 36, 0x1250F: 36,
    0x2510: 37, 0x12510: 37,
    0x2511: 38, 0x12511: 38,
    0x2512: 39, 0x12512: 39,
    0x1e00: 40, 0x11e00: 40,
    0x1e01: 41, 0x11e01: 41,
    0x1e02: 42, 0x11e02: 42,
    0x1e03: 43, 0x11e03: 43,
    0x2000: 44, 0x12000: 44,
    0x2001: 45, 0x12001: 45,
    0x2002: 46, 0x12002: 46,
    0x2003: 47, 0x12003: 47,
    0x2004: 48, 0x12004: 48,
    0x2005: 49, 0x12005: 49,
    0x200A: 50, 0x1200A: 50,
    0x2800: 51, 0x12800: 51,
    0x1f00: 52, 0x11f00: 52,
    0x1f01: 53, 0x11f01: 53,
    0x1f02: 54, 0x11f02: 54,
    0x1f03: 55, 0x11f03: 55,
    0x1f05: 56, 0x11f05: 56,
    0x1f06: 57, 0x11f06: 57,
    0x1d00: 58, 0x11d00: 58,
    0x1d01: 59, 0x11d01: 59,
    0x1d02: 60, 0x11d02: 60,
    0x1d03: 61, 0x11d03: 61,
    0x1d04: 62, 0x11d04: 62,
    0x1d05: 63, 0x11d05: 63,
    0x2100: 64, 0x12100: 64,
    0x2101: 65, 0x12101: 65,
    0x2102: 66, 0x12102: 66,
    0x2103: 67, 0x12103: 67,
    0x2104: 68, 0x12104: 68,
    0x2105: 69, 0x12105: 69,
    0x2106: 70, 0x12106: 70,
    0x2200: 71, 0x12200: 71,
    0x2201: 72, 0x12201: 72,
    0x2300: 73, 0x12300: 73,
    0x2400: 74, 0x12400: 74,
    0xd0a: 75, 0x10d0a: 75,
    0xd14: 78, 0x10d14: 78,
    0xd0c: 77, 0x10d0c: 77,
    0xd0b: 76, 0x10d0b: 76,
    0x1401: 79, 0x11401: 79,
    0x140a: 80, 0x1140a: 80,
    0x1400: 81, 0x11400: 81,
    0xb0a: 82, 0x10b0a: 82,
    0xb0b: 83, 0x10b0b: 83,
    0xb0c: 84, 0x10b0c: 84,
    0xb0f: 85, 0x10b0f: 85,
    0xb0e: 86, 0x10b0e: 86,
    0xb0d: 87, 0x10b0d: 87,
    0xb10: 88, 0x10b10: 88,
    0xb11: 89, 0x10b11: 89,
    0xb12: 90, 0x10b12: 90,
    0xb13: 91, 0x10b13: 91,
    0x1501: 92, 0x11501: 92,
    0x1502: 93, 0x11502: 93,
    0x1503: 94, 0x11503: 94,
    0x1504: 95, 0x11504: 95,
    0x1505: 96, 0x11505: 96,
    0x1506: 97, 0x11506: 97,
    0x1507: 98, 0x11507: 98,
    0x1508: 99, 0x11508: 99,
    0x1509: 100, 0x11509: 100,
    0x150a: 101, 0x1150a: 101,
    0x1500: 102, 0x11500: 102,
    0xc0a: 103, 0x10c0a: 103,
    0xc0b: 104, 0x10c0b: 104,
    0xc0c: 105, 0x10c0c: 105,
    0xc0d: 106, 0x10c0d: 106,
    0xc0e: 107, 0x10c0e: 107,
    0xc0f: 108, 0x10c0f: 108,
    0x100a: 109, 0x1100a: 109,
    0x100b: 110, 0x1100b: 110,
    0x100c: 111, 0x1100c: 111,
    0x100d: 112, 0x1100d: 112,
    0x100f: 113, 0x1100f: 113,
    0x100e: 114, 0x1100e: 114,
    0x1014: 115, 0x11014: 115,
    0x1701: 116, 0x11701: 116,
    0x1700: 117, 0x11700: 117,
    0x1800: 118, 0x11800: 118,
    0x1900: 119, 0x11900: 119,
    0x1a0a: 120, 0x11a0a: 120,
    0x1a0b: 121, 0x11a0b: 121,
    0x1a00: 122, 0x11a00: 122,
    0x1b00: 123, 0x11b00: 123,
    0x130a: 124, 0x1130a: 124,
    0x130b: 125, 0x1130b: 125,
    0x1300: 126, 0x11300: 126,
    0xf0a: 127, 0x10f0a: 127,
    0xf0c: 128, 0x10f0c: 128,
    0xf0b: 129, 0x10f0b: 129,
    0xf0d: 130, 0x10f0d: 130,
    0xf0e: 131, 0x10f0e: 131,
    0xf0f: 132, 0x10f0f: 132,
    0xf10: 133, 0x10f10: 133,
    0xf11: 134, 0x10f11: 134,
    0xf12: 135, 0x10f12: 135,
    0xf13: 136, 0x10f13: 136,
    0xe0a: 137, 0x10e0a: 137,
    0xe0b: 138, 0x10e0b: 138,
    0x110B: 139, 0x1110B: 139,
    0x120B: 139, 0x1120B: 139,
    0x110a: 140, 0x1110a: 140,
    0x120a: 140, 0x1120a: 140,
    0x160a: 141, 0x1160a: 141,
    0x1600: 142, 0x11600: 142,
    0x800: 143, 0x10800: 143,
    0x700: 144, 0x10700: 144,
    0xa00: 145, 0x10a00: 145,
    0x900: 146, 0x10900: 146,
    0x400: 147, 0x10400: 147,
    0x500: 148, 0x10500: 148,
    0x600: 149, 0x10600: 149,
    0x10D00: 150,
    0x10D01: 151,
    0x10B00: 152,
    0x10B01: 153,
    0x10B02: 154,
    0x10b03: 155,
    0x10c00: 156,
    0x10c01: 157,
    0x11000: 158,
    0x11001: 159,
    0x11002: 160,
    0x11003: 161,
    0x10f00: 162,
    0x10f01: 163,
    0x10f02: 164,
    0x10f03: 165,
    0x10e00: 166,
    0x10e01: 167,
    0x11100: 168,
    0x11101: 169,
    0x11102: 170,
    0x11103: 171,
    0x11200: 168,
    0x11201: 169,
    0x11202: 170,
    0x11203: 171,
    0x0: 0, 0x10000: 0,
    0x1: 0, 0x10001: 0,
    0x2: 0, 0x10002: 0,
    0x3: 0, 0x10003: 0,
    0xD00: 172,
    0xD01: 172,
    0xB00: 173,
    0xB01: 173,
    0xB02: 173,
    0xb03: 173,
    0xc00: 174,
    0xc01: 174,
    0x1000: 175,
    0x1001: 175,
    0x1002: 175,
    0x1003: 175,
    0xf00: 176,
    0xf01: 176,
    0xf02: 176,
    0xf03: 176,
    0xe00: 177,
    0xe01: 177,
    0x1100: 178,
    0x1101: 178,
    0x1102: 178,
    0x1103: 178,
    0x1200: 178,
    0x1201: 178,
    0x1202: 178,
    0x1203: 178,
}

entrance_files = [
    "entrances/overworld_transitions.json",
    "entrances/bosses.json",
    "entrances/caves.json",
    "entrances/dungeons.json",
    "entrances/houses.json",
    "entrances/ports.json",]

loc_files = [
    "locations/locations.json",
    "locations/interior_checks.json",
    "locations/overview_houses.json",
    # "locations/overview_astrid_full.json", empty
    "locations/overview_astrid_houses.json",
    "locations/overview_bosses.json",
    "locations/overview_caves.json",
    "locations/overview_dungeons_full.json",
    "locations/overview_dungeons.json",]

TRACKER_WORLD = {"map_page_folder": "tracker",
                 "map_page_maps": ["maps/maps_any_er_true.json",
                                   # "maps/maps_any_er_false.json",
                                   "maps/maps_ow_er_true.json",
                                   "maps/maps_ow_er_false.json"],
                 "map_page_locations": loc_files + entrance_files,
                 "map_page_settings_key": "{slot}_{team}_UT_MAP",
                 "map_page_index": lambda i: MAP_INDEX.get(i, 0)
                 }

def get_hidden_entrances(world: "PhantomHourglassWorld"):
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

    entr_data = get_json(entrance_files)
    loc_data = get_json(loc_files)
    active_entrances = [int(i) for i in world.ut_pairings]
    # print(f"active entrances: {[i for i in active_entrances]}")
    entr_hidden: dict[str, list[str]] = {}
    locs_hidden: dict[str, list[int]] = {}
    events_hidden = {}
    map_coord_checks = {}
    # Move event data from locations to entrances
    for loc in loc_data.copy():
        event_names = [s.get("name") for s in loc.get("sections", []) if "EVENT" in s.get("name") or "GOAL" in s.get("name")]
        if event_names:
            entr_data.append(loc)
            loc_data.remove(loc)
    # Handle entrances
    for entrance in entr_data:
        entr_grouping = entrance.get("name")
        entr_names = [s.get("name") for s in entrance.get("sections", [])]
        map_locs = entrance.get("map_locations", [])
        maps = map_locs[0].get("map", "Check Overview")
        for entr_name in entr_names:
            if entr_name not in ENTRANCES:
                print(f"Wrong Entrance in tracker data: {entr_name}")
            elif ENTRANCES[entr_name].id not in active_entrances:
                entr_hidden.setdefault(maps, []).append(entr_name)
            else:
                coords = [(i["x"], i["y"]) for i in map_locs]
                map_coord_checks.setdefault(maps, []).append(coords)
    # Handle locations and coord check entrances
    for loc in loc_data:
        loc_names = [s.get("name") for s in loc.get("sections", [])]
        loc_map_locations = loc.get("map_locations")
        loc_maps = [l["map"] for l in loc_map_locations]
        loc_coords = [(l["x"], l["y"]) for l in loc_map_locations]

        for loc_map in loc_maps:
            if loc_map in map_coord_checks:
                #print(f"Testing {loc_map} coords {loc_coords} in {[i[0] for i in map_coord_checks[loc_map]]}")
                for c in loc_coords:
                    if c in [i[0] for i in map_coord_checks[loc_map]]:
                        loc_ids = []
                        for loc2 in loc_names:
                            if "EVENT" in loc2 or "GOAL" in loc2:
                                entr_hidden.setdefault(loc_map, []).append(loc2)
                            else:
                                loc_ids.append(world.location_name_to_id[loc2])
                        locs_hidden.setdefault(loc_map, [])
                        locs_hidden[loc_map] += loc_ids

    # Special Cases
    if ENTRANCES["Bannan West Hut"].id in active_entrances:
        entr_hidden.setdefault("Bannan Island", []).append("EVENT: Meet Wayfarer")
    if ENTRANCES["Astrid's Stairs"].id in active_entrances:
        locs_hidden.setdefault("Isle of Ember", []).append(87)
        locs_hidden.setdefault("Isle of Ember (West)", []).append(87)
    else:  # Astrid's Stairs is offset by default, needs a manual removal
        entr_hidden.setdefault("Isle of Ember", []).append("Astrid's Stairs")
        entr_hidden.setdefault("Isle of Ember (West)", []).append("Astrid's Stairs")
    if ENTRANCES["Ember West Astrid's House"].id in active_entrances:
        entr_hidden.setdefault("Isle of Ember", []).append("Astrid's Stairs")
        entr_hidden.setdefault("Isle of Ember (West)", []).append("Astrid's Stairs")
    # Bosses
    if ENTRANCES["ToF Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Isle of Ember", []).extend([99, 100])
        locs_hidden.setdefault("Isle of Ember (East)", []).extend([99, 100])
    if ENTRANCES["ToW Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Isle of Gusts", []).extend([156, 157, 158])
        locs_hidden.setdefault("Isle of Gusts (North)", []).extend([156, 157, 158])
    if ENTRANCES["ToC Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Molida Island", []).extend([129, 130, 131])
        locs_hidden.setdefault("Molida Island (North)", []).extend([129, 130, 131])
    if ENTRANCES["GT Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Goron Island", []).extend([204, 205, 206])
        locs_hidden.setdefault("Goron Island (NW)", []).extend([204, 205, 206])
    if ENTRANCES["ToI Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Isle of Frost", []).extend([239, 240, 241])
        locs_hidden.setdefault("Isle of Frost (NE)", []).extend([239, 240, 241])
    if ENTRANCES["MT Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Isle of Ruins", []).extend([266, 267, 268])
        locs_hidden.setdefault("Isle of Ruins NE", []).extend([266, 267, 268])

    # for i, v in entr_hidden.items():
    #     print(f"{i}: {v}")
    # for m, locs in locs_hidden.items():
    #     print(f"{m}: {[world.location_id_to_name[loc] for loc in locs]}")
    # for m, locs in events_hidden.items():
    #     print(f"{m}: {locs}")

    return locs_hidden, entr_hidden
