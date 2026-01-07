from typing import TYPE_CHECKING
from ..data.Entrances import ENTRANCES, entrance_id_to_region

if TYPE_CHECKING:
    from ..__init__ import PhantomHourglassWorld

MAP_INDEX = {
    0x2b00: 31, 0x12b00: 31,
    0x3000: 32, 0x13000: 32,
    0x2c00: 33, 0x12c00: 33,
    0x2e00: 34, 0x12e00: 34,
    0x2d00: 35, 0x12d00: 35,
    0x2a00: 36, 0x12a00: 36,
    0x2f00: 37, 0x12f00: 37,
    0x2700: 38, 0x12700: 38,
    0x2701: 39, 0x12701: 39,
    0x1c00: 40, 0x11c00: 40,
    0x1c01: 41, 0x11c01: 41,
    0x1c02: 42, 0x11c02: 42,
    0x1c03: 43, 0x11c03: 43,
    0x2900: 44, 0x12900: 44,
    0x2901: 45, 0x12901: 45,
    0x2902: 46, 0x12902: 46,
    0x2903: 47, 0x12903: 47,
    0x2904: 48, 0x12904: 48,
    0x2600: 49, 0x12600: 49,
    0x2500: 50, 0x12500: 50,
    0x2501: 51, 0x12501: 51,
    0x2502: 52, 0x12502: 52,
    0x2503: 53, 0x12503: 53,
    0x2504: 54, 0x12504: 54,
    0x2505: 55, 0x12505: 55,
    0x2506: 56, 0x12506: 56,
    0x2507: 57, 0x12507: 57,
    0x2508: 58, 0x12508: 58,
    0x2509: 59, 0x12509: 59,
    0x250A: 60, 0x1250A: 60,
    0x250B: 61, 0x1250B: 61,
    0x250C: 62, 0x1250C: 62,
    0x250D: 63, 0x1250D: 63,
    0x250E: 64, 0x1250E: 64,
    0x250F: 65, 0x1250F: 65,
    0x2510: 66, 0x12510: 66,
    0x2511: 67, 0x12511: 67,
    0x2512: 68, 0x12512: 68,
    0x1e00: 69, 0x11e00: 69,
    0x1e01: 70, 0x11e01: 70,
    0x1e02: 71, 0x11e02: 71,
    0x1e03: 72, 0x11e03: 72,
    0x2000: 73, 0x12000: 73,
    0x2001: 74, 0x12001: 74,
    0x2002: 75, 0x12002: 75,
    0x2003: 76, 0x12003: 76,
    0x2004: 77, 0x12004: 77,
    0x2005: 78, 0x12005: 78,
    0x200A: 79, 0x1200A: 79,
    0x2800: 80, 0x12800: 80,
    0x1f00: 81, 0x11f00: 81,
    0x1f01: 82, 0x11f01: 82,
    0x1f02: 83, 0x11f02: 83,
    0x1f03: 84, 0x11f03: 84,
    0x1f05: 85, 0x11f05: 85,
    0x1f06: 86, 0x11f06: 86,
    0x1d00: 87, 0x11d00: 87,
    0x1d01: 88, 0x11d01: 88,
    0x1d02: 89, 0x11d02: 89,
    0x1d03: 90, 0x11d03: 90,
    0x1d04: 91, 0x11d04: 91,
    0x1d05: 92, 0x11d05: 92,
    0x2100: 93, 0x12100: 93,
    0x2101: 94, 0x12101: 94,
    0x2102: 95, 0x12102: 95,
    0x2103: 96, 0x12103: 96,
    0x2104: 97, 0x12104: 97,
    0x2105: 98, 0x12105: 98,
    0x2106: 99, 0x12106: 99,
    0x2200: 100, 0x12200: 100,
    0x2201: 101, 0x12201: 101,
    0x2300: 102, 0x12300: 102,
    0x2400: 103, 0x12400: 103,
    0xd0a: 104, 0x10d0a: 104,
    0xd14: 105, 0x10d14: 105,
    0xd0c: 106, 0x10d0c: 106,
    0xd0b: 107, 0x10d0b: 107,
    0x1401: 108, 0x11401: 108,
    0x140a: 109, 0x1140a: 109,
    0x1400: 110, 0x11400: 110,
    0xb0a: 111, 0x10b0a: 111,
    0xb0b: 112, 0x10b0b: 112,
    0xb0c: 113, 0x10b0c: 113,
    0xb0f: 114, 0x10b0f: 114,
    0xb0e: 115, 0x10b0e: 115,
    0xb0d: 116, 0x10b0d: 116,
    0xb10: 117, 0x10b10: 117,
    0xb11: 118, 0x10b11: 118,
    0xb12: 119, 0x10b12: 119,
    0xb13: 120, 0x10b13: 120,
    0x1501: 121, 0x11501: 121,
    0x1502: 122, 0x11502: 122,
    0x1503: 123, 0x11503: 123,
    0x1504: 124, 0x11504: 124,
    0x1505: 125, 0x11505: 125,
    0x1506: 126, 0x11506: 126,
    0x1507: 127, 0x11507: 127,
    0x1508: 128, 0x11508: 128,
    0x1509: 129, 0x11509: 129,
    0x150a: 130, 0x1150a: 130,
    0x1500: 131, 0x11500: 131,
    0xc0a: 132, 0x10c0a: 132,
    0xc0b: 133, 0x10c0b: 133,
    0xc0c: 134, 0x10c0c: 134,
    0xc0d: 135, 0x10c0d: 135,
    0xc0e: 136, 0x10c0e: 136,
    0xc0f: 137, 0x10c0f: 137,
    0x100a: 138, 0x1100a: 138,
    0x100b: 139, 0x1100b: 139,
    0x100c: 140, 0x1100c: 140,
    0x100d: 141, 0x1100d: 141,
    0x100f: 142, 0x1100f: 142,
    0x100e: 143, 0x1100e: 143,
    0x1014: 144, 0x11014: 144,
    0x1701: 145, 0x11701: 145,
    0x1700: 146, 0x11700: 146,
    0x1800: 147, 0x11800: 147,
    0x1900: 148, 0x11900: 148,
    0x1a0a: 149, 0x11a0a: 149,
    0x1a0b: 150, 0x11a0b: 150,
    0x1a00: 151, 0x11a00: 151,
    0x1b00: 152, 0x11b00: 152,
    0x130a: 153, 0x1130a: 153,
    0x130b: 154, 0x1130b: 154,
    0x1300: 155, 0x11300: 155,
    0xf0a: 156, 0x10f0a: 156,
    0xf0c: 157, 0x10f0c: 157,
    0xf0b: 158, 0x10f0b: 158,
    0xf0d: 159, 0x10f0d: 159,
    0xf0e: 160, 0x10f0e: 160,
    0xf0f: 161, 0x10f0f: 161,
    0xf10: 162, 0x10f10: 162,
    0xf11: 163, 0x10f11: 163,
    0xf12: 164, 0x10f12: 164,
    0xf13: 165, 0x10f13: 165,
    0xe0a: 166, 0x10e0a: 166,
    0xe0b: 167, 0x10e0b: 167,
    0x110B: 168, 0x1110B: 168,
    0x120B: 168, 0x1120B: 168,
    0x110a: 169, 0x1110a: 169,
    0x120a: 169, 0x1120a: 169,
    0x160a: 170, 0x1160a: 170,
    0x1600: 171, 0x11600: 171,
    0x800: 172, 0x10800: 172,
    0x700: 173, 0x10700: 173,
    0xa00: 174, 0x10a00: 174,
    0x900: 175, 0x10900: 175,
    0x400: 176, 0x10400: 176,
    0x500: 177, 0x10500: 177,
    0x600: 178, 0x10600: 178,
    0x10D00: 9,
    0x10D01: 10,
    0x10B00: 11,
    0x10B01: 12,
    0x10B02: 13,
    0x10b03: 14,
    0x10c00: 15,
    0x10c01: 16,
    0x11000: 17,
    0x11001: 18,
    0x11002: 19,
    0x11003: 20,
    0x10f00: 21,
    0x10f01: 22,
    0x10f02: 23,
    0x10f03: 24,
    0x10e00: 25,
    0x10e01: 26,
    0x11100: 27,
    0x11101: 28,
    0x11102: 29,
    0x11103: 30,
    0x11200: 27,
    0x11201: 28,
    0x11202: 29,
    0x11203: 30,
    0x0: 0, 0x10000: 0,
    0x1: 0, 0x10001: 0,
    0x2: 0, 0x10002: 0,
    0x3: 0, 0x10003: 0,
    0xD00: 2,
    0xD01: 2,
    0xB00: 3,
    0xB01: 3,
    0xB02: 3,
    0xb03: 3,
    0xc00: 4,
    0xc01: 4,
    0x1000: 5,
    0x1001: 5,
    0x1002: 5,
    0x1003: 5,
    0xf00: 6,
    0xf01: 6,
    0xf02: 6,
    0xf03: 6,
    0xe00: 7,
    0xe01: 7,
    0x1100: 8,
    0x1101: 8,
    0x1102: 8,
    0x1103: 8,
    0x1200: 8,
    0x1201: 8,
    0x1202: 8,
    0x1203: 8,
}

entrance_files = [
    "entrances/overworld_transitions.json",
    "entrances/bosses.json",
    "entrances/caves.json",
    "entrances/dungeons.json",
    "entrances/houses.json",
    "entrances/ports.json",
    "entrances/entrances_overview.json"]

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
                 "map_page_maps": [
                                   "maps/maps_ow_er_false.json",
                                    "maps/maps_ow_er_true.json",
                                    "maps/maps_any_er_true.json",
                                   # "maps/maps_any_er_false.json",
                                   ],
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
    if ENTRANCES["Ruins NW Pyramid"].id in active_entrances:
        entr_hidden.setdefault("Isle of Ruins", []).append("EVENT: Bremeur's Temple Lower Water")
        entr_hidden.setdefault("Isle of Ruins NW", []).append("EVENT: Bremeur's Temple Lower Water")
    # Bosses
    if ENTRANCES["ToF Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Isle of Ember", []).extend([99, 100])
        locs_hidden.setdefault("Isle of Ember (East)", []).extend([99, 100])
        entr_hidden.setdefault("Isle of Ember (West)", []).append("EVENT: Defeat Blaaz")
        entr_hidden.setdefault("Isle of Ember", []).append("EVENT: Defeat Blaaz")
        entr_hidden.setdefault("Temple of Fire 3F", []).append("Blaaz Boss Reward")
        entr_hidden.setdefault("Temple of Fire 3F", []).append("Blaaz Heart Container")
    if ENTRANCES["ToW Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Isle of Gusts", []).extend([156, 157, 158])
        locs_hidden.setdefault("Isle of Gusts (North)", []).extend([156, 157, 158])
        entr_hidden.setdefault("Isle of Gusts (North)", []).append("EVENT: Defeat Cyclok")
        entr_hidden.setdefault("Isle of Gusts", []).append("EVENT: Defeat Cyclok")
        entr_hidden.setdefault("Temple of Wind 1F", []).append("Cyclok Boss Reward")
        entr_hidden.setdefault("Temple of Wind 1F", []).append("Cyclok Heart Container")
        entr_hidden.setdefault("Temple of Wind 1F", []).append("Cyclok Sand of Hours")
    if ENTRANCES["ToC Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Molida Island", []).extend([129, 130, 131])
        locs_hidden.setdefault("Molida Island (North)", []).extend([129, 130, 131])
        entr_hidden.setdefault("Molida Island", []).append("EVENT: Defeat Crayk")
        entr_hidden.setdefault("Molida Island (North)", []).append("EVENT: Defeat Crayk")
        entr_hidden.setdefault("Temple of Courage 2F", []).append("Crayk Boss Reward")
        entr_hidden.setdefault("Temple of Courage 2F", []).append("Crayk Heart Container")
        entr_hidden.setdefault("Temple of Courage 2F", []).append("Crayk Sand of Hours")
    if ENTRANCES["GT Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Goron Island", []).extend([204, 205, 206])
        locs_hidden.setdefault("Goron Island (NW)", []).extend([204, 205, 206])
        entr_hidden.setdefault("Goron Island", []).append("EVENT: Defeat Dongorongo")
        entr_hidden.setdefault("Goron Island (NW)", []).append("EVENT: Defeat Dongorongo")
        entr_hidden.setdefault("Goron Temple B3", []).append("Dongorongo Boss Reward")
        entr_hidden.setdefault("Goron Temple B3", []).append("Dongorongo Heart Container")
        entr_hidden.setdefault("Goron Temple B3", []).append("Dongorongo Sand of Hours")
    if ENTRANCES["ToI Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Isle of Frost", []).extend([239, 240, 241])
        locs_hidden.setdefault("Isle of Frost (NE)", []).extend([239, 240, 241])
        entr_hidden.setdefault("Isle of Frost", []).append("EVENT: Defeat Gleeok")
        entr_hidden.setdefault("Isle of Frost (NE)", []).append("EVENT: Defeat Gleeok")
    if ENTRANCES["MT Enter Boss"].id in active_entrances:
        locs_hidden.setdefault("Isle of Ruins", []).extend([266, 267, 268])
        locs_hidden.setdefault("Isle of Ruins NE", []).extend([266, 267, 268])
        entr_hidden.setdefault("Isle of Ruins", []).append("EVENT: Defeat Eox")
        entr_hidden.setdefault("Isle of Ruins NE", []).append("EVENT: Defeat Eox")
        entr_hidden.setdefault("Mutoh's Temple B2", []).append("Eox Boss Reward")
        entr_hidden.setdefault("Mutoh's Temple B2", []).append("Eox Heart Container")
        entr_hidden.setdefault("Mutoh's Temple B2", []).append("Eox Sand of Hours")
    # Dungeon entrances & events
    if ENTRANCES["Ember Enter Temple"].id in active_entrances:
        entr_hidden.setdefault("Isle of Ember (West)", []).append("EVENT: Defeat Blaaz")
        entr_hidden.setdefault("Isle of Ember", []).append("EVENT: Defeat Blaaz")
    if ENTRANCES["Gust Enter Temple"].id in active_entrances:
        entr_hidden.setdefault("Isle of Gusts (North)", []).append("EVENT: Defeat Cyclok")
        entr_hidden.setdefault("Isle of Gusts", []).append("EVENT: Defeat Cyclok")
    if ENTRANCES["Molida North Enter Temple"].id in active_entrances:
        entr_hidden.setdefault("Molida Island", []).append("EVENT: Defeat Crayk")
        entr_hidden.setdefault("Molida Island (North)", []).append("EVENT: Defeat Crayk")
    if ENTRANCES["Goron Enter Temple"].id in active_entrances:
        entr_hidden.setdefault("Goron Island", []).append("EVENT: Defeat Dongorongo")
        entr_hidden.setdefault("Goron Island (NW)", []).append("EVENT: Defeat Dongorongo")
    if ENTRANCES["Frost NE Enter Temple"].id in active_entrances:
        entr_hidden.setdefault("Isle of Frost", []).append("EVENT: Defeat Gleeok")
        entr_hidden.setdefault("Isle of Frost (NE)", []).append("EVENT: Defeat Gleeok")
    if ENTRANCES["Ruins Enter Temple"].id in active_entrances:
        entr_hidden.setdefault("Isle of Ruins", []).append("EVENT: Defeat Eox")
        entr_hidden.setdefault("Isle of Ruins NE", []).append("EVENT: Defeat Eox")

    # for i, v in entr_hidden.items():
    #     print(f"{i}: {v}")
    # for m, locs in locs_hidden.items():
    #     print(f"{m}: {[world.location_id_to_name[loc] for loc in locs]}")
    # for m, locs in events_hidden.items():
    #     print(f"{m}: {locs}")

    return locs_hidden, entr_hidden


