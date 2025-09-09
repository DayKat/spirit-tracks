DYNAMIC_FLAGS = {
    "Aboda Rei": {
        "on_scenes": [0x2F00],
        "not_has_locations": ["Aboda Clear Rocks"],
        "unset_if_true": [(0x265714, 0x04)]
    },
    "Aboda Bee Boy": {
        "on_scenes": [0x2F00],
        "not_has_locations": ["Aboda Bee Tree"],
        "unset_if_true": [(0x265714, 0x04)]
    },
    "Post Aboda Children": {
        "on_scenes": [0x2F00],
        "has_locations": ["Aboda Clear Rocks", "Aboda Bee Tree"],
        "set_if_true": [(0x265714, 0x04)]
    },
    # "Forest Sanctuary Song Statue":{
    #     "on_scenes": [0x3000],
    #     "not_has_locations": ["Forest Sanctuary Song Statue"],
    #     "unset_if_true": [(0x268FB0, 0x01)]
    # },
    # "Wooded Temple Song Statue":{
    #     "on_scenes": [0x1900],
    #     "not_has_locations": ["Wooded Temple Song Statue"],
    #     "unset_if_true": [(0x268FB0, 0x02)]
    # },
    # "RESET FS statue":{
    #     "on_scenes": [0x3000],
    #     "has_locations": ["Forest Sanctuary Song Statue"],
    #     "set_if_true": [(0x268FB0, 0x01)]
    # },
    # "RESET WT statue":{
    #     "on_scenes": [0x1900],
    #     "has_locations": ["Wooded Temple Song Statue"],
    #     "set_if_true": [(0x268FB0, 0x02)]
    # },
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

