from typing import Dict
from .data.Locations import LOCATIONS_DATA
from .data.DynamicFlags import DYNAMIC_FLAGS
from .data.Items import ITEMS
from .data.Constants import HINTS_ON_SCENE

def build_hint_scene_to_watches() -> dict[int, list]:
    return {}

def build_entrance_id_to_data():
    return {}, {}

def build_location_room_to_watches() -> Dict[int, dict[str, dict]]:
    location_room_to_watches: Dict[int, dict[str, dict]] = {}
    for loc_name, location in LOCATIONS_DATA.items():
        room_id = location.get("stage_id", 0) * 0x100 + location.get("room_id", 0)
        if room_id not in location_room_to_watches:
            location_room_to_watches[room_id] = {}
        location_room_to_watches[room_id][loc_name] = location

        # Build Island shops
        if "island_shop" in location:
            for shop_id, shop in HINTS_ON_SCENE.items():
                if shop_id not in location_room_to_watches:
                    location_room_to_watches[shop_id] = {}
                if "island_shop" in shop:
                    location_room_to_watches[shop_id][loc_name] = location
        # Add location to multiple rooms
        if "additional_rooms" in location:
            for room in location["additional_rooms"]:
                if room not in location_room_to_watches:
                    location_room_to_watches[room] = {}
                location_room_to_watches[room][loc_name] = location
    return location_room_to_watches


def build_scene_to_dynamic_flag() -> Dict[int, list[dict]]:
    scene_to_dynamic_flag: Dict[int, list[dict]] = {}
    for flag_name, data in DYNAMIC_FLAGS.items():
        data["name"] = flag_name
        for scene in data.get("on_scenes", []):
            scene_to_dynamic_flag.setdefault(scene, [])
            scene_to_dynamic_flag[scene].append(data)
    return scene_to_dynamic_flag


def build_location_name_to_id_dict() -> Dict[str, int]:
    location_name_to_id: Dict[str, int] = {}
    for loc_name, location in LOCATIONS_DATA.items():
        # ids are for sending flags
        location_name_to_id[loc_name] = location["id"]
    return location_name_to_id

def build_rabbit_location_id_to_name_dict() -> Dict[int, str]:
    location_id_to_name: Dict[int, str] = {}
    for loc_name, location in LOCATIONS_DATA.items():
        if "rabbit" in location:
            index = location["id"]
            location_id_to_name[index] = loc_name
    return location_id_to_name


def build_item_name_to_id_dict() -> Dict[str, int]:
    item_name_to_id: Dict[str, int] = {}
    for item_name, item in ITEMS.items():
        item_name_to_id[item_name] = item.id
    return item_name_to_id


def build_item_id_to_name_dict() -> Dict[int, str]:
    item_id_to_name: Dict[int, str] = {}
    for item_name, item in ITEMS.items():
        index = item.id
        item_id_to_name[index] = item_name
    return item_id_to_name

# Making a dictionary of stamp scenes
def build_scene_to_stamp() -> Dict[int, str]:
    stamp_locations: Dict[int, str] = {}
    for loc_name, location in LOCATIONS_DATA.items():
        if location.get("stamp"):
            scene = location.get("stage_id", 0) * 0x100 + location.get("room_id", 0)
            stamp_locations[scene] = loc_name
    return stamp_locations

def build_location_to_goal():
    goal_locations = []
    for loc_name, location in LOCATIONS_DATA.items():
        if location.get("goal"):
            goal_locations.append(loc_name)
    return goal_locations

