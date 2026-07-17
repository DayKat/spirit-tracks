from typing import TYPE_CHECKING
from ..data.Entrances import ENTRANCES
from ..data.Locations import LOCATIONS_DATA

if TYPE_CHECKING:
    from .. import SpiritTracksWorld


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
    map_coord_checks = {}

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

    print(f"hidden entrances: {entr_hidden}")
    return locs_hidden, entr_hidden