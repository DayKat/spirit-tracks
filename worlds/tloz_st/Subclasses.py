
from .DSZeldaClient.subclasses import DSTransition
from .DSZeldaClient.ItemClass import DSItem, receive_normal
from enum import IntEnum
from typing import TYPE_CHECKING
from .data.Constants import DUNGEON_KEY_DATA
if TYPE_CHECKING:
    from .Client import SpiritTracksClient
from .data.Addresses import STAddr

async def receive_tos_key(client: "SpiritTracksClient", ctx, item: "STItem", rii):
    async def write_keys_to_storage(dungeon) -> tuple[int, list, str]:
        key_data = DUNGEON_KEY_DATA[dungeon]
        prev = await key_data["address"].read(ctx)
        bit_filter = key_data["filter"]
        new_v = prev | bit_filter if (prev & bit_filter) + key_data[
            "value"] > bit_filter else prev + key_data["value"]
        print(f"Writing {key_data['name']} key to storage: {hex(prev)} -> {hex(new_v)}")
        return key_data["address"].get_inner_write_list(new_v)

    res = []
    if client.current_stage == item.dungeon and client.current_room in item.rooms:
        print("Getting ToS key in correct section")
        if client.last_vanilla_item and client.last_vanilla_item[-1] == "Small Key (ToS)":
            client.last_vanilla_item.pop()
    else:
        dungeon_key = 0x130 + item.section
        res.append(await write_keys_to_storage(dungeon_key))
    return res

async def receive_tear_of_light(client: "SpiritTracksClient", ctx, item: "STItem", rii):
    if client.current_stage == 0x13:
        await client.set_tears(ctx)

    return []

async def remove_treasure(client, ctx, item, rii):
    addr = item.address
    value = client.treasure_tracker[addr]
    print(f"Removing treasure {item}")
    return addr.get_write_list(value)

async def remove_tear_of_light(client, ctx, item: "STItem", rii):
    for i in range(20):
        if not await STAddr.getting_tear_safety.read(ctx, silent=True):
            break
    await client.set_tears(ctx)
    return []

async def dummy(*args):
    print(f"Receiving dummy item")
    return []

class STItem(DSItem):
    rooms: list[int]
    section: int

    def __init__(self, name, data, all_items):
        super().__init__(name, data, all_items)

    def get_receive_function(self):
        res = super().get_receive_function()
        if res is None:
            return dummy
        if "Tear of Light" in self.name:
            return receive_tear_of_light
        if self.name.startswith("Small Key (ToS"):
            return receive_tos_key
        return res

    def get_remove_vanilla_function(self):
        if "treasure" in self.tags:
            return remove_treasure
        if "Tear of Light" in self.name:
            return remove_tear_of_light
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