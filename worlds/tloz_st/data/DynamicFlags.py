from .Addresses import STAddr

DYNAMIC_FLAGS = {
    "Outset Rei": {
        "on_scenes": [0x2F00],
        "not_has_locations": ["Outset Clear Rocks"],
        "unset_if_true": [(STAddr.adv_flags_0, 0x04)]
    },
    "Outset Bee Boy": {
        "on_scenes": [0x2F00],
        "not_has_locations": ["Outset Bee Tree"],
        "unset_if_true": [(STAddr.adv_flags_0, 0x04)]
    },
    "Allow leaving Outset": {
        "on_scenes": [0x2F00],
        "has_locations": ["Outset Clear Rocks", "Outset Bee Tree"],
        "has_items": [["Forest Glyph", 1]],
        "set_if_true": [(STAddr.adv_flags_0, 0x04)]
    },
    "Allow learning awakening song": {
        "on_scenes": [0x3000],
        "not_has_locations": ["Forest Sanctuary Song Statue"],
        "unset_if_true": [(STAddr.songs, 0x01)],
        "reset_flags": ["RESET fs statue"]
    },
    "RESET fs statue": {
        #"has_locations": ["Forest Sanctuary Song Statue"],
        "has_items": [["Song of Awakening", 1]],
        "set_if_true": [(STAddr.songs, 0x01)],
    },
    "Allow learning healing song": {
        "on_scenes": [0x190A],
        "not_has_locations": ["Wooded Temple Song Statue"],
        "unset_if_true": [(STAddr.songs, 0x02)],
        "reset_flags": ["RESET wt statue"]
    },
    "RESET wt statue": {
        #"has_locations": ["Wooded Temple Song Statue"],
        "has_items": [["Song of Healing", 1]],
        "set_if_true": [(STAddr.songs, 0x02)],
    },
    "Allow learning light song": {
        "on_scenes": [0x3700],
        "not_has_locations": ["Trading Post Song of Light Statue"],
        "unset_if_true": [(STAddr.songs, 0x08)],
        "reset_flags": ["RESET trading post statue"]
    },
    "RESET trading post statue": {
        #"has_locations": ["Trading Post Song of Light Statue"],
        "has_items": [["Song of Light", 1]],
        "set_if_true": [(STAddr.songs, 0x08)],
    },
    "Allow learning discovery song": {
        "on_scenes": [0x2B00],
        "not_has_locations": ["Anouki Village Song Statue"],
        "unset_if_true": [(STAddr.songs, 0x10)],
        "reset_flags": ["RESET av statue"]
    },
    "RESET av statue": {
        # "has_locations": ["Anouki Village Song Statue"],
        "has_items": [["Song of Discovery", 1]],
        "set_if_true": [(STAddr.songs, 0x10)],
    },
    "Stagnox location": {
        "on_scenes": [0x1E00], #TODO seems this can also be 0x1900 instead? or maybe not taking away source fast enough?
        "not_has_locations": ["Wooded Temple Dungeon Reward"],
        "unset_if_true": [(STAddr.adv_flags_0, 0x10)],
        "reset_flags": ["RESET stagnox reward"]
    },
    "RESET stagnox reward": {
        "has_items": [["Forest Source", 1]],
        "set_if_true": [(STAddr.adv_flags_0, 0x10)]
    },
    "Remove Forest Source": {
        "on_scenes": [0x1E03, 0x1E0A],
        "has_locations": ["Wooded Temple Dungeon Reward"],
        "has_items": [["Forest Source", 0]], #doesn't have item
        "unset_if_true": [(STAddr.adv_flags_0, 0x10)],
    },
    "Allow Rabbit Net Read": {
        "on_scenes": [0x3E00],
        "not_has_locations": ["Rabbit Haven Net Gift"],
        "unset_if_true": [(STAddr.adv_flags_1a, 0x40)],
    },
    "Skip intro Rabbit Net dialogue": {
        "on_scenes": [0x3E00],
        "has_locations": ["Rabbit Haven Net Gift"],
        "set_if_true": [(STAddr.adv_flags_1a, 0x40)],
    },
    "Allow rabbit catching": {
        "on_scenes": [0x0400],
        "has_items": [["Rabbit Net", 1]],
        "set_if_true": [(STAddr.adv_flags_1a, 0x40)],
    },
    "Disallow rabbit catching": {
        "on_scenes": [0x0400],
        "has_items": [["Rabbit Net", 0]],
        "unset_if_true": [(STAddr.adv_flags_1a, 0x40)],
    },
    "Move Alfonso to castle town station": {
        "on_scenes": [0x2900],
        "not_has_locations": ["Outset Receive Stamp Book"],
        "has_items": [["Snow Glyph", 1], ["Forest Glyph", 1]],
        "set_if_true": [(STAddr.adv_flags_11, 0x20)],
        "reset_flags": ["RESET Alfonso"]
    },
    "RESET Alfonso": {
        "on_scenes": [0x2F00],
        "has_locations": ["Outset Receive Stamp Book"],
        "unset_if_true": [(STAddr.adv_flags_11, 0x60)],
        "set_if_true": [(STAddr.adv_flags_1b, 0x02)],
    },
    "Allow Stamp Book check": {
        "on_scenes": [0x2F0A],
        "not_has_locations": ["Outset Receive Stamp Book"],
        "unset_if_true": [(STAddr.adv_flags_25, 0x02)],
        "reset_flags": ["RESET Stamp Book Check"]
    },
    "RESET Stamp Book Check": {
        "on_scenes": [0x2F00],
        "has_items": [["Stamp Book", 1]],
        "set_if_true": [(STAddr.adv_flags_25, 0x02)],
    },

    "Fraaz location": {
        "on_scenes": [0x1F00],
        "not_has_locations": ["Blizzard Temple Dungeon Reward"],
        "unset_if_true": [(STAddr.adv_flags_0, 0x20)],
        "reset_flags": ["RESET fraaz reward", "RESET fraaz don't have source"]
    },
    "RESET fraaz reward": {
        "has_locations": ["Blizzard Temple Dungeon Reward"],
        "has_items": [["Snow Source", 1]],
        "set_if_true": [(STAddr.adv_flags_0, 0x20)]
    },
    "RESET fraaz don't have source": {
        "has_items": [["Snow Source", 0]],
        "unset_if_true": [(STAddr.adv_flags_0, 0x20)]
    },
    "Remove Snow Source": {
        "on_scenes": [0x1F03, 0x1F04], #TODO check
        "has_locations": ["Blizzard Temple Dungeon Reward"],
        "has_items": [["Snow Source", 0]],
        "unset_if_true": [(STAddr.adv_flags_0, 0x20)],
    },
    "Anjean kick out after ocean glyph fix": {
        "on_scenes": [0x1401],
        "has_items": [["Ocean Glyph", 1]],
        "set_if_true": [(STAddr.adv_flags_17, 0x20)]
    },
    "Snow realm crashes with snow source and no blizzard tracks": {
        "on_scenes": [0x500],
        "has_items": [["Snow Source", 1], ["Blizzard Temple Tracks", 0]],
        "unset_if_true": [(STAddr.adv_flags_0, 0x20)],
        "reset_flags": ["RESET snow realm crash"]
    },
    "RESET snow realm crash": {
        "set_if_true": [(STAddr.adv_flags_0, 0x20)],
        "has_items": [["Snow Source", 1]],
    },
    # "Forest Sanctuary reset duet":{ #TODO wrong flag?
    #     "on_scenes": [0x3001],
    #     "not_has_locations": ["Forest Sanctuary Gage Duet"],
    #     "unset_if_true": [(0x265715, 0x01)]
    # },
    # "Assume duet done outside room":{
    #     "on_scenes": [0x3000],
    #     "not_has_locations": ["Forest Sanctuary Gage Duet"],
    #     "set_if_true": [(0x265715, 0x01)]
    # },

    # Portals
    "Allow Portal near castle town always open": {
        "on_scenes": [0x0400],
        "has_items": [["Snow Glyph", 1]],
        "has_slot_data": [["portal_behavior", 1]],
        "set_if_true": [(STAddr.adv_flags_30, 0x08)]  # activates portal to sw snow realm
    },
    "Allow Portal near castle town item": {
        "on_scenes": [0x0400],
        "has_items": [["Snow Glyph", 1],
                      ["Portal Unlock: Hyrule Castle to Anouki Village", 1]],
        "has_slot_data": [["portal_behavior", 2]],
        "set_if_true": [(STAddr.adv_flags_30, 0x08)]  # activates portal to sw snow realm
    },
    "Keep portal loc open anouki village": {
        "on_scenes": [0x0500],
        "has_slot_data": [["portal_checks", 1]],
        "not_has_locations": ["Snow Realm Shoot SW Portal"],
        "unset_if_true": [(STAddr.adv_flags_30, 0x08)]  # activates portal to sw snow realm
    },
    "Close Castle town portal no item": {
        "on_scenes": [0x0400],
        "has_slot_data": [["portal_behavior", 2]],
        "has_items": [["Portal Unlock: Hyrule Castle to Anouki Village", 0]],
        "unset_if_true": [(STAddr.adv_flags_30, 0x08)]  # activates portal to sw snow realm
    },

    "Allow portal snow realm E to Forest S always open": {
        "on_scenes": [0x500],
        "has_items": [["Forest Realm SE Portal Tracks", 1]],
        "has_slot_data": [["portal_behavior", 1]],
        "set_if_true": [(STAddr.adv_flags_30, 0x20)]
    },
    "Allow portal snow realm E to Forest S item": {
        "on_scenes": [0x500],
        "has_items": [["Forest Realm SE Portal Tracks", 1],
                      ["Portal Unlock: Trading Post to E Snow Realm", 1]],
        "has_slot_data": [["portal_behavior", 2]],
        "set_if_true": [(STAddr.adv_flags_30, 0x20)]
    },
    "Keep portal loc open s trading post": {
        "on_scenes": [0x400],
        "not_has_locations": ["Forest Realm Shoot SE Portal"],
        "has_slot_data": [["portal_checks", 1]],
        "unset_if_true": [(STAddr.adv_flags_30, 0x20)]
    },
    "Close portal e snow realm items": {
        "on_scenes": [0x500],
        "has_items": [["Portal Unlock: Trading Post to E Snow Realm", 0]],
        "has_slot_data": [["portal_behavior", 2]],
        "unset_if_true": [(STAddr.adv_flags_30, 0x20)]
    },
    "Dark realm restart for dynamic entrances": {
        "on_scenes": [0x400],
        "unset_if_true": [(STAddr.adv_flags_57, 0x30)]
    },
    "Dark realm spawn demon train quick": {
        "on_scenes": [0x1000, 0x10FF],
        "set_if_true": [(STAddr.adv_flags_57, 0x30)]
    }

}
"""
"Dynamic Flag Name": {
    "on_scenes": list[int],
    "not_last_scenes": list[int]
    "has_items": list[tuple[str, int]],         item_name, min count (0 for not have item)
    "has_locations": list[str],
    "not_has_locations": list[str],
    "any_not_has_locations": list[str],
    "set_if_true": list[tuple[int, int]],       address, value
    "unset_if_true": list[tuple[int, int]],     address, value
    "has_slot_data": list[list[str, any]]       slot_data, ==value
    "goal_requirement": bool                    checks dungeon requirement if true
}
"""

