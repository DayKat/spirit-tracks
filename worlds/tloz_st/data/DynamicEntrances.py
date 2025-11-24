from .Entrances import ENTRANCES
from .Constants import LOCATION_GROUPS

# For adding entrances that change based on items, locations, slot_data etc.
# uses all the same conditions as dynamic flags
# "entrance: str name of the STTransition to enter
# "destination": str name of the STTransition to warp to if conditions are true
DYNAMIC_ENTRANCES = {
    # ToS Bounce
    "Exit ToS to snow without source": {
        "entrance": "Tower of Spirits Snow Realm",
        "destination": "Tower of Spirits Snow Realm",
        "not_has_all_items": [("Snow Glyph", 0), ("Snow Source", 0),
                              # ("Blizzard Temple Tracks", 0) # Fixed!a
                              ]
    },
    # Portal Bounces
    "Bounce forest portal north": {
        "entrance": "Forest Realm North Portal",
        "destination": "Forest Realm North Portal",
        "has_items": [("Snow Glyph", 0)]
    },
    "Bounce forest portal south": {
        "entrance": "Forest Realm South Portal",
        "destination": "Forest Realm South Portal",
        "not_has_all_items": [("Blizzard Temple Tracks", 0), ("Snow Glyph", 0)]
    },
    "Bounce snow portal east": {
        "entrance": "Snow Realm East Portal",
        "destination": "Snow Realm East Portal",
        "has_items": [("Forest Realm SE Portal Tracks", 0)]
    },
    "Bounce snow portal west": {
        "entrance": "Snow Realm West Portal",
        "destination": "Snow Realm West Portal",
        "not_has_all_items": [("Snow Glyph", 0)]
    },
    "Bounce snow portal north": {
        "entrance": "Snow Realm North Portal",
        "destination": "Snow Realm North Portal",
    },
    "Bounce snow portal bridge": {
        "entrance": "Snow Realm Bridge Portal",
        "destination": "Snow Realm Bridge Portal",
    },
}

# Reorganize above data to the form {scene: data} or something
DYNAMIC_ENTRANCES_BY_SCENE = {}
for name, data in DYNAMIC_ENTRANCES.items():
    data["name"] = name
    entrance_data = ENTRANCES[data["entrance"]]
    if data["destination"] == "_connected_dungeon_entrance":
        destination_data = None
    else:
        destination_data = ENTRANCES[data["destination"]]

    entrance_scene = entrance_data.scene

    # Save er_in_scene values in data
    data["detect_data"] = entrance_data
    data["exit_data"] = destination_data
    DYNAMIC_ENTRANCES_BY_SCENE.setdefault(entrance_scene, {})
    DYNAMIC_ENTRANCES_BY_SCENE[entrance_scene][name] = data