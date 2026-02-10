from .DSZeldaClient.subclasses import DSTransition
from .DSZeldaClient.ItemClass import DSItem, receive_normal
from enum import IntEnum


async def remove_treasure(client, ctx, item, rii):
    addr = item.address
    value = client.treasure_tracker[addr]
    print(f"Removing treasure {item}")
    return addr.get_write_list(value)

async def dummy(*args):
    print(f"Receiving dummy item")
    return []

class STItem(DSItem):

    def __init__(self, name, data, all_items):
        super().__init__(name, data, all_items)

    def get_receive_function(self):
        res = super().get_receive_function()
        if res is None:
            return dummy
        return res

    def get_remove_vanilla_function(self):
        if "treasure" in self.tags:
            return remove_treasure
        return super().get_remove_vanilla_function()

class EntranceGroups(IntEnum):
    NONE = 0
    # Directions
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    INSIDE = 5
    OUTSIDE = 6
    # Types
    HOUSE = 1 << 3
    CAVE = 2 << 3
    STATION = 3 << 3
    OVERWORLD = 4 << 3
    DUNGEON_ENTRANCE = 5 << 3
    BOSS = 6 << 3
    DUNGEON_ROOM = 7 << 3
    WARP_PORTAL = 8 << 3
    TRAIN_PORTAL = 9 << 3
    EVENT = 10 << 3

OPPOSITE_ENTRANCE_GROUPS = {
    EntranceGroups.RIGHT: EntranceGroups.LEFT,
    EntranceGroups.LEFT: EntranceGroups.RIGHT,
    EntranceGroups.UP: EntranceGroups.DOWN,
    EntranceGroups.DOWN: EntranceGroups.UP,
    0: 0,
    EntranceGroups.NONE: EntranceGroups.NONE,
    EntranceGroups.INSIDE: EntranceGroups.OUTSIDE,
    EntranceGroups.OUTSIDE: EntranceGroups.INSIDE
}

# Entrance data format
class STTransition(DSTransition):
    entrance_groups = EntranceGroups
    opposite_entrance_groups = OPPOSITE_ENTRANCE_GROUPS