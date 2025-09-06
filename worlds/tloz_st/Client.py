import random
from .DSZeldaClient.DSZeldaClient import *

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext


ROM_ADDRS = {
    "game_identifier": (0x00000000, 16, "ROM"),
    "slot_name": (0xFFFC0, 64, "ROM"),
}

RAM_ADDRS = {
    "game_state": (0x060C48, 1, "Main RAM"), 
    "is_dead": (0xC2EE, 1, "ARM7 System Bus"),

    "received_item_index": (0x265780, 2, "Main RAM"),
    "slot_id": (0x265782, 2, "Main RAM"),

    "stage": (0x260A2C, 4, "Main RAM"),
    "floor": (0x1B2E98, 4, "Main RAM"),  # TODO: Find floor value
    "room": (0x2690EA, 1, "Main RAM"),
    "entrance": (0x2690EB, 1, "Main RAM"),

    "loading_room": (0x0c2FF0, 1, "Main RAM"),

    "getting_location": (0x04B114, 1, "Main RAM"),
    "getting_train_part": (0x11F5E4, 1, "Main RAM"),
    "menu": (0x260958, 1, "Main RAM"),

    "link_x": (0x05CC, 4, "Data TCM"),
    "link_y": (0x05D0, 4, "Data TCM"),
    "link_z": (0x05D4, 4, "Data TCM"),

    "equipped_item": (0x265318, 4, "Main RAM")
}

POINTERS = {
    "ADDR_gItemManager": 0x0fb4,
    "ADDR_gPlayerManager": 0x0fbc,
    "ADDR_gAdventureFlags": 0x0f74,
    "ADDR_gPlayer": 0x0fec,
    "ADDR_gOverlayManager_mLoadedOverlays_4": 0x0910,
    "ADDR_gMapManager": 0x0e60
}

# gMapManager -> mCourse -> mSmallKeys
SMALL_KEY_OFFSET = 0x260
STAGE_FLAGS_OFFSET = 0x268

# Addresses to read each cycle
read_keys_always = ["game_state", "received_item_index", "is_dead", "stage", "room", "slot_id", "menu", "loading_room"]
read_keys_land = ["getting_location", "getting_train_part"]


class SpiritTracksClient(DSZeldaClient):
    game = "The Legend of Zelda - Spirit Tracks"
    system = "NDS"

    def __init__(self) -> None:
        super().__init__()

        # Required variables from inherit
        self.starting_flags = STARTING_FLAGS
        self.dungeon_key_data = DUNGEON_KEY_DATA
        self.slot_id_addr = RAM_ADDRS["slot_id"][0]
        self.received_item_index_addr = RAM_ADDRS["received_item_index"][0]
        self.starting_entrance = (0x2F, 0, 1)  # stage, room, entrance
        self.scene_addr = (RAM_ADDRS["stage"][0], RAM_ADDRS["room"][0], RAM_ADDRS["floor"][0], RAM_ADDRS["entrance"][0])  # Stage, room, floor, entrance
        self.exit_coords_addr = ()  # TODO: x, y, z. what coords to spawn link at when entering a
        # continuous transition
        self.er_y_offest = 164  # In ph i use coords who's y is 164 off the entrance y
        self.ADDR_gMapManager = POINTERS["ADDR_gMapManager"]
        self.stage_flag_offset = STAGE_FLAGS_OFFSET

        self.in_stamp_stand = False
        self.scene_to_stamp = build_scene_to_stamp()
        self.goal_locations = build_location_to_goal()
        self.has_goal_location = False

    async def get_small_key_address(self, ctx) -> int:
        return 0x26532F

    async def check_game_version(self, ctx: "BizHawkClientContext") -> bool:
        rom_name_bytes = (await bizhawk.read(ctx.bizhawk_ctx, [ROM_ADDRS["game_identifier"]]))[0]
        rom_name = bytes([byte for byte in rom_name_bytes if byte != 0]).decode("ascii")
        print(f"Rom Name: {rom_name}")
        if rom_name == "SPIRITTRACKSBKIP":  # EU
            return True
        return False

    def get_coord_address(self, at_sea=None, multi=False) -> dict[str, tuple[int, int, str]]:
        return {k: v for k, v in RAM_ADDRS.items() if k in ["link_x", "link_y", "link_z"]}

    async def get_coords(self, ctx, multi=False):
        coords = await read_memory_values(ctx, self.get_coord_address(), signed=True)
        return {
            "x": coords.get("link_x", 0),
            "y": coords.get("link_y", 0),
            "z": coords.get("link_z", 0)
        }

    async def remove_special_vanilla_item(self, ctx, vanilla_item: str):
        # ignore treasure for now
        if vanilla_item == "Treasure":
            return True
        return False

    async def full_heal(self, ctx, bonus=0):
        pass

    async def watched_intro_cs(self, ctx):
        return await read_memory_value(ctx, 0x265726) & 1

    async def update_main_read_list(self, ctx: "BizHawkClientContext", stage: int, in_game=True):
        read_keys = read_keys_always
        read_keys += read_keys_land
        self.main_read_list = {k: v for k, v in RAM_ADDRS.items() if k in read_keys}
        print(self.main_read_list)

    def process_loading_variable(self, read_result) -> bool:
        return not read_result.get("loading_room", 27)

    async def process_read_list(self, ctx: "BizHawkClientContext", read_result: dict):
        current_menu = read_result["menu"]
        self.in_stamp_stand = current_menu == 0x0E

        # Fix for stamp stand not counting as getting item
        if self.in_stamp_stand and self.receiving_location:
            self.getting_location = True

    async def process_in_game(self, ctx, read_result: dict):
        # Detect stamp stand locations
        if self.in_stamp_stand and not self.receiving_location:
            self.receiving_location = True
            stamp_location = self.scene_to_stamp[self.current_scene]
            await self._process_checked_locations(ctx, stamp_location)

    def cancel_location_read(self, location) -> bool:
        if "stamp" in location:
            return True
        return False

    async def check_location_post_processing(self, ctx, location: dict):
        if location is not None and "goal" in location:
            print("it works")
        # goal = ctx.slot_data.get("goal")
        # if location.get("name") == "Tos Forest Rail Glyph" and goal == 0:
        #     break
        # elif location.get("name") == "Forest Temple Dungeon Reward" and goal == 1:
        #     continue
            # Finished game?
            goal = ctx.slot_data.get("goal")
            if goal == 0 and location.get("region_id") == "tos 3f rail map":
                self.has_goal_location = True
            if goal == 1 and location.get("region_id") == "fot stagnox":
                self.has_goal_location = True
        #await self._set_delay_pickup(self, ctx, location)

    async def process_game_completion(self, ctx: "BizHawkClientContext"):
        if self.has_goal_location:
            return True
        return False


    async def process_deathlink(self, ctx: "BizHawkClientContext", is_dead, stage, read_result):
        pass
