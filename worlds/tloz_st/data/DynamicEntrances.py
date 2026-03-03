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
        "has_items": [# ("Snow Glyph", 0),  # only crashes if you also remove blizzard lol
                              ("Snow Source", 0),
                              # ("Blizzard Temple Tracks", 0) # Fixed!
                              ],
        "message": "You don't have the snow source!"
    },
    "Exit ToS to ocean without source": {
        "entrance": "Tower of Spirits to Ocean Realm",
        "destination": "Tower of Spirits to Ocean Realm",
        "has_items": [("Ocean Source", 0),],
        "message": "You don't have the Ocean source!"
    },
    "Exit ToS to fire without source": {
        "entrance": "Tower of Spirits to Fire Realm",
        "destination": "Tower of Spirits to Fire Realm",
        "has_items": [("Fire Source", 0)],
        "message": "You don't have the Fire source!"
    },

    "Bounce ToS from forest without base prog": {
        "entrance": "Forest Realm to Tower of Spirits",
        "destination": "Forest Realm to Tower of Spirits",
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 1]],
        "has_items": [("Progressive ToS Section", 0)],
        "message": "You need 1 Progressive ToS Section to enter!"
    },
    "Bounce ToS from forest without base": {
        "entrance": "Forest Realm to Tower of Spirits",
        "destination": "Forest Realm to Tower of Spirits",
        "has_slot_data": [["tos_section_unlocks", [0, 1]], ["tos_unlock_base_item", 1]],
        "has_items": [("Tower of Spirits Base", 0)],
        "message": "You need the Tower of Spirits Base to enter!"
    },
    "Bounce ToS from snow without base prog": {
        "entrance": "Snow Realm to Tower of Spirits",
        "destination": "Snow Realm to Tower of Spirits",
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 1]],
        "has_items": [("Progressive ToS Section", 0)],
        "message": "You need 1 Progressive ToS Section to enter!"
    },
    "Bounce ToS from snow without base": {
        "entrance": "Snow Realm to Tower of Spirits",
        "destination": "Snow Realm to Tower of Spirits",
        "has_slot_data": [["tos_section_unlocks", [0, 1]], ["tos_unlock_base_item", 1]],
        "has_items": [("Tower of Spirits Base", 0)],
        "message": "You need the Tower of Spirits Base to enter!"
    },

    # Outset pre-glyph bounce
    "Bounce Outset without glyph and cannon": {
        "entrance": "Outset to Forest Realm",
        "destination": "Outset to Forest Realm",
        "not_has_all_items": [("Forest Glyph", 1), ("Cannon", 1)],
        "has_slot_data": [("cannon_logic", 0)],
        "message": "You need Forest Glyph and Cannon to board the train here"
    },
    "Bounce Outset without glyph": {
        "entrance": "Outset to Forest Realm",
        "destination": "Outset to Forest Realm",
        "not_has_all_items": [("Forest Glyph", 1)],
        "has_slot_data": [("cannon_logic", [1, 2, 3])],
        "message": "You need Forest Glyph to board the train here"
    },
    "Bounce Tutorial cannon": {
        "entrance": "Outset to Tutorial",
        "destination": "Outset to Tutorial",
        "not_has_all_items": [("Forest Glyph", 1), ("Cannon", 1)],
        "has_slot_data": [("cannon_logic", 0)],
        "message": "You need Forest Glyph and Cannon to board the train here"
    },
    "Bounce Tutorial cannonless": {
        "entrance": "Outset to Tutorial",
        "destination": "Outset to Tutorial",
        "not_has_all_items": [("Forest Glyph", 1)],
        "has_slot_data": [("cannon_logic", [1, 2, 3])],
        "message": "You need Forest Glyph to board the train here"
    },
    "Bounce Tutorial to rail cannon": {
        "entrance": "Outset to Tutorial",
        "destination": "Forest Realm to Outset",
        "has_slot_data": [("cannon_logic", 0)],
        "has_items": [("Forest Glyph", 1), ("Cannon", 1)],
    },
    "Bounce Tutorial to rail cannonless": {
        "entrance": "Outset to Tutorial",
        "destination": "Forest Realm to Outset",
        "has_items": [("Forest Glyph", 1)],
        "has_slot_data": [("cannon_logic", [1, 2, 3])],
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

    "Bounce sand portal sanc": {
        "entrance": "Sand Realm Sanctuary Portal",
        "destination": "Sand Realm Sanctuary Portal",
        "has_items": [("Desert Temple Tracks", 0)],
        "has_slot_data": [["portal_behavior", [0, 1]]],
        "message": "You don't have the Desert Temple Tracks!"
    },
    "Bounce sand portal sanc item": {
        "entrance": "Sand Realm Sanctuary Portal",
        "destination": "Sand Realm Sanctuary Portal",
        "not_has_all_items": [("Desert Temple Tracks", 1),
                              ("Portal Unlock: Desert Temple to Sand Realm", 1)],
        "has_slot_data": [["portal_behavior", 2]],
        "message": "You don't have access to this portal!"
    },

    "Bounce sand portal temple": {
        "entrance": "Sand Realm Temple Portal",
        "destination": "Sand Realm Temple Portal",
        "has_items": [("Sand Realm Tracks", 0)],
        "has_slot_data": [["portal_behavior", [0, 1]]],
        "message": "You don't have the Sand Realm Tracks!"
    },
    "Bounce sand portal temple item": {
        "entrance": "Sand Realm Temple Portal",
        "destination": "Sand Realm Temple Portal",
        "not_has_all_items": [("Sand Realm Tracks", 1),
                              ("Portal Unlock: Desert Temple to Sand Realm", 1)],
        "has_slot_data": [["portal_behavior", 2]],
        "message": "You don't have access to this portal!"
    },

    "Bounce sand fire portal": {
        "entrance": "Fire Realm Sand Portal",
        "destination": "Fire Realm Sand Portal",
        "has_items": [("Marine Temple Tracks", 0)],
        "has_slot_data": [["portal_behavior", [0, 1]]],
        "message": "You don't have the Marine Temple Tracks!"
    },
    "Bounce sand fire portal item": {
        "entrance": "Fire Realm Sand Portal",
        "destination": "Fire Realm Sand Portal",
        "not_has_all_items": [("Marine Temple Tracks", 1),
                              ("Portal Unlock: Fire Sand Connection to Marine Temple", 1)],
        "has_slot_data": [["portal_behavior", 2]],
        "message": "You don't have access to this portal!"
    },

    "Bounce marine temple portal": {
        "entrance": "Ocean Realm Temple Portal",
        "destination": "Ocean Realm Temple Portal",
        "has_items": [("Sand to Fire Connection Tracks", 0)],
        "has_slot_data": [["portal_behavior", [0, 1]]],
        "message": "You don't have the Sand to Fire Connection Tracks!"
    },
    "Bounce marine temple portal item": {
        "entrance": "Ocean Realm Temple Portal",
        "destination": "Ocean Realm Temple Portal",
        "not_has_all_items": [("Sand to Fire Connection Tracks", 1),
                              ("Portal Unlock: Fire Sand Connection to Marine Temple", 1)],
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

    # ToS Bounces
    "Bounce ToS Section 2": {
        "entrance": "Tower of Spirits Enter Section 2",
        "destination": "Tower of Spirits Enter Section 2",
        "has_items": [("Forest Source", 0)],
        "has_slot_data": [["tos_section_unlocks", 1]],
        "message": "You need the Forest Source to enter this section!"
    },
    "Bounce ToS Section 3": {
        "entrance": "Tower of Spirits Enter Section 3",
        "destination": "Tower of Spirits Enter Section 3",
        "has_items": [("Snow Source", 0)],
        "has_slot_data": [["tos_section_unlocks", 1]],
        "message": "You need the Snow Source to enter this section!"
    },
    "Bounce ToS Section 4": {
        "entrance": "Tower of Spirits Enter Section 4",
        "destination": "Tower of Spirits Enter Section 4",
        "has_items": [("Ocean Source", 0)],
        "has_slot_data": [["tos_section_unlocks", 1]],
        "message": "You need the Ocean Source to enter this section!"
    },
    "Bounce ToS Section 5": {
        "entrance": "Tower of Spirits Enter Section 5",
        "destination": "Tower of Spirits Enter Section 5",
        "has_items": [("Fire Source", 0)],
        "has_slot_data": [["tos_section_unlocks", 1]],
        "message": "You need the Fire Source to enter this section!"
    },

    # ToS Blue Warp shortcuts
    "Exit ToS 3F": {
        "entrance": "ToS 3F Blue Portal",
        "destination": "_connected_dungeon_entrance",
    },
    "Exit ToS 7F": {
        "entrance": "ToS 7F Blue Portal",
        "destination": "_connected_dungeon_entrance",
    },
    "Exit ToS 12F": {
        "entrance": "ToS 12F Blue Portal",
        "destination": "_connected_dungeon_entrance",
    },
    "Exit ToS 17F": {
        "entrance": "ToS 17F Blue Portal",
        "destination": "_connected_dungeon_entrance",
    },
    "Exit ToS 24F": {
        "entrance": "ToS 24F Blue Portal",
        "destination": "_connected_dungeon_entrance",
    },

    # Sanctuary Bounces  (solved with dynaflags instead)
    # "Bounce FoS": {
    #     "entrance": "Forest Sanctuary Enter Sanctuary",
    #     "destination": "Forest Sanctuary Enter Sanctuary",
    #     "has_items": [("Spirit Flute", 0)],
    #     "message": "You need the Spirit Flute to enter here"
    # },
    # "Bounce Snow Sanc": {
    #     "entrance": "Snow Sanctuary Enter Inner Sanctuary",
    #     "destination": "Snow Sanctuary Enter Inner Sanctuary",
    #     "has_items": [("Spirit Flute", 0)],
    #     "message": "You need the Spirit Flute to enter here"
    # },
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