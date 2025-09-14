DYNAMIC_FLAGS = {
    "Outset Rei": {
        "on_scenes": [0x2F00],
        "not_has_locations": ["Outset Clear Rocks"],
        "unset_if_true": [(0x265714, 0x04)]
    },
    "Outset Bee Boy": {
        "on_scenes": [0x2F00],
        "not_has_locations": ["Outset Bee Tree"],
        "unset_if_true": [(0x265714, 0x04)]
    },
    "Post Outset Children": {
        "on_scenes": [0x2F00],
        "has_locations": ["Outset Clear Rocks", "Outset Bee Tree"],
        "set_if_true": [(0x265714, 0x04)]
    },
    "Allow learning discovery song": {
        "on_scenes": [0x3000],
        "not_has_locations": ["Forest Sanctuary Song Statue"],
        "unset_if_true": [(0x268FB0, 0x01)],
        "reset_flags": ["RESET fs statue"]
    },
    "RESET fs statue": {
        "on_scenes": [0x3000],
        "has_locations": ["Forest Sanctuary Song Statue"],
        "has_items": [["Song of Discovery", 1]],
        "set_if_true": [(0x268FB0, 0x01)],
    },
    "Allow learning healing song": {
        "on_scenes": [0x190A],
        "not_has_locations": ["Wooded Temple Song Statue"],
        "unset_if_true": [(0x268FB0, 0x02)],
        "reset_flags": ["RESET wt statue"]
    },
    "RESET wt statue": {
        "on_scenes": [0x190A],
        "has_locations": ["Wooded Temple Song Statue"],
        "has_items": [["Song of Healing", 1]],
        "set_if_true": [(0x268FB0, 0x02)],
    },
    "Allow learning light song": {
        "on_scenes": [0x3700],
        "not_has_locations": ["Trading Post 2nd Song Statue"],
        "unset_if_true": [(0x268FB0, 0x08)],
        "reset_flags": ["RESET trading post statue"]
    },
    "RESET trading post statue": {
        "on_scenes": [0x3700],
        "has_locations": ["Trading Post 2nd Song Statue"],
        "has_items": [["Song of Light", 1]],
        "set_if_true": [(0x268FB0, 0x08)],
    },
    "Stagnox location": {
        "on_scenes": [0x1E00],
        "not_has_locations": ["Wooded Temple Dungeon Reward"],
        "unset_if_true": [(0x265714, 0x10)],
        "reset_flags": ["RESET stagnox reward"]
    },
    "RESET stagnox reward": {
        "has_locations": ["Wooded Temple Dungeon Reward"],
        "has_items": [["Forest Source", 1]],
        "set_if_true": [(0x265714, 0x10)]
    },
    "Allow Rabbit Net Read": {
        "on_scenes": [0x3E00],
        "not_has_locations": ["Rabbit Haven Net Gift"],
        "unset_if_true": [(0x26572E, 0x40)],
        "reset_flags": ["RESET Rabbit Net Read"]
    },
    "RESET Rabbit Net Read": {
        "has_locations": ["Rabbit Haven Net Gift"],
        "set_if_true": [(0x26572E, 0x40)],
    },
    "Allow rabbit catching": {
        "on_scenes": [0x0400],
        "has_items": [["Rabbit Net", 1]],
        "set_if_true": [(0x26572E, 0x40)],
    },
    "Disallow rabbit catching": {
        "on_scenes": [0x0400],
        "has_items": [["Rabbit Net", 0]],
        "unset_if_true": [(0x26572E, 0x40)],
    },
    "Move Alfonso to castle town station": {
        "on_scenes": [0x2900],
        "not_has_locations": ["Outset Receive Stamp Book"],
        "has_items": [["Snow Glyph", 1], ["Forest Glyph", 1]],
        "set_if_true": [(0x265725, 0x20)],
        "reset_flags": ["RESET Alfonso"]
    },
    "RESET Alfonso": {
        "on_scenes": [0x2F00],
        "has_locations": ["Outset Receive Stamp Book"],
        "unset_if_true": [(0x265725, 0x60)],
        "reset_flags": ["RESET Alfonso"],
        "set_if_true": [(0x26572F, 0x02)],
    },
    "Allow Stamp Book check": {
        "on_scenes": [0x2F0A],
        "not_has_locations": ["Outset Receive Stamp Book"],
        "unset_if_true": [(0x265739, 0x02)],
        "reset_flags": ["RESET Stamp Book Check"]
    },
    "RESET Stamp Book Check": {
        "on_scenes": [0x2F00],
        "has_items": [["Stamp Book", 1]],
        "set_if_true": [(0x265739, 0x02)],
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

