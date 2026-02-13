from .Entrances import ENTRANCES
from .Constants import LOCATION_GROUPS

# For adding entrances that change based on items, locations, slot_data etc.
# uses all the same conditions as dynamic flags
# "entrance: str name of the STTransition to enter
# "destination": str name of the STTransition to warp to if conditions are true
DYNAMIC_ENTRANCES = {
    # ToS Bounce
    "Exit ToS to snow without source": {
        "entrance": "Tower of Spirits to Snow Realm",
        "destination": "Tower of Spirits to Snow Realm",
        "not_has_all_items": [# ("Snow Glyph", 0),  # only crashes if you also remove blizzard lol
                              ("Snow Source", 0),
                              # ("Blizzard Temple Tracks", 0) # Fixed!
                              ],
        "message": "You don't have the snow source!"
    },
    # Outset pre-glyph bounce
    "Bounce Outset without glyph": {
        "entrance": "Outset to Forest Realm",
        "destination": "Outset to Forest Realm",
        "not_has_all_items": [("Forest Glyph", 0), ("Cannon", 0)],
        "message": "You need Forest Glyph and Cannon to board the train here"
    },
    "Bounce Tutorial": {
        "entrance": "Outset to Tutorial",
        "destination": "Outset to Tutorial",
        "not_has_all_items": [("Forest Glyph", 0), ("Cannon", 0)],
        "message": "You need Forest Glyph and Cannon to board the train here"
    },
    "Bounce Tutorial missing locs": {
        "entrance": "Outset to Tutorial",
        "destination": "Outset to Tutorial",
        "has_items": [("Forest Glyph", 1), ("Cannon", 1)],
        "any_not_has_locations": ["Outset Clear Rocks", "Outset Bee Tree"],
        "message": "You need to get the bee tree and clear rocks locations before leaving"
    },
    "Bounce Tutorial to rail": {
        "entrance": "Outset to Tutorial",
        "destination": "Forest Realm to Outset",
        "has_items": [("Forest Glyph", 1), ("Cannon", 1)],
        "has_locations": ["Outset Clear Rocks", "Outset Bee Tree"],
    },

    # Portal Bounces
    "Bounce forest portal north": {
        "entrance": "Forest Realm North Portal",
        "destination": "Forest Realm North Portal",
        "has_items": [("Snow Glyph", 0)],
        "has_slot_data": [["portal_behavior", [0, 1]]],
        "message": "You don't have the Snow Glyph!"
    },
    "Bounce forest portal north item": {
        "entrance": "Forest Realm North Portal",
        "destination": "Forest Realm North Portal",
        "not_has_all_items": [("Snow Glyph", 1), ("Portal Unlock: Hyrule Castle to Anouki Village", 1)],
        "has_slot_data": [["portal_behavior", 2]],
        "message": "You don't have access to this portal!"
    },

    "Bounce forest portal south": {
        "entrance": "Forest Realm South Portal",
        "destination": "Forest Realm South Portal",
        "not_has_all_items": [("Blizzard Temple Tracks", 1)],
        "has_slot_data": [["portal_behavior", [0, 1]]],
        "message": "You don't have the Blizzard Temple Tracks!"
    },
    "Bounce forest portal south item": {
        "entrance": "Forest Realm South Portal",
        "destination": "Forest Realm South Portal",
        "not_has_all_items": [("Blizzard Temple Tracks", 1), ("Portal Unlock: Trading Post to E Snow Realm", 1)],
        "has_slot_data": [["portal_behavior", 2]],
        "message": "You don't have access to this portal!"
    },

    "Bounce snow portal east": {
        "entrance": "Snow Realm East Portal",
        "destination": "Snow Realm East Portal",
        "has_items": [("Forest Realm SE Portal Tracks", 0)],
        "has_slot_data": [["portal_behavior", [0, 1]]],
        "message": "You don't have the Forest Realm SE Portal Tracks!"
    },
    "Bounce snow portal east item": {
        "entrance": "Snow Realm East Portal",
        "destination": "Snow Realm East Portal",
        "not_has_all_items": [("Forest Realm SE Portal Tracks", 1),
                              ("Portal Unlock: Trading Post to E Snow Realm", 1)],
        "has_slot_data": [["portal_behavior", 2]],
        "message": "You don't have access to this portal!"
    },

    "Bounce snow portal west item": {  # No need for other bounce condition, unlocked with forest glyph
        "entrance": "Snow Realm West Portal",
        "destination": "Snow Realm West Portal",
        "has_slot_data": [["portal_behavior", 2]],
        "not_has_all_items": [("Portal Unlock: Hyrule Castle to Anouki Village", 1)],
        "message": "You don't have access to this portal!"
    },

    "Bounce snow portal north": {
        "entrance": "Snow Realm North Portal",
        "destination": "Snow Realm North Portal",
        "message": "You don't have access to this portal!"
    },
    "Bounce snow portal bridge": {
        "entrance": "Snow Realm Bridge Portal",
        "destination": "Snow Realm Bridge Portal",
        "message": "You don't have access to this portal!"
    },
    "Bounce forest portal cave": {
        "entrance": "Forest Realm Cave Portal",
        "destination": "Forest Realm Cave Portal",
        "message": "You don't have access to this portal!"
    },

    # Dark realm options
    "Bounce Dark realm missing endgame requirements": {
        "entrance": "Enter Dark Realm Portal",
        "destination": "Enter Dark Realm Portal",
        "message": "You are missing dark realm requirements",
        "dungeons": False
    },
    "Dark realm Skip dark trains": {
        "entrance": "Enter Dark Realm Portal",
        "destination": "Enter Demon Train",
        "has_slot_data": [["endgame_scope", 1]],
        "dungeons": True
    },
    "Dark realm Skip demon train": {
        "entrance": "Enter Dark Realm Portal",
        "destination": "Enter Cole Fight",
        "has_slot_data": [["endgame_scope", 2]],
        "dungeons": True
    },
    "Dark realm Skip Cole": {
        "entrance": "Enter Dark Realm Portal",
        "destination": "Enter Malladus 1",
        "has_slot_data": [["endgame_scope", 3]],
        "dungeons": True
    },
    "Dark realm Skip Malladus 1": {
        "entrance": "Enter Dark Realm Portal",
        "destination": "Enter Malladus 2",
        "has_slot_data": [["endgame_scope", 4]],
        "dungeons": True
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