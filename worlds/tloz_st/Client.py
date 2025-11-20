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

    "stage": (0x2690E0, 4, "Main RAM"),
    "floor": (0x1B2E98, 4, "Main RAM"),  # TODO: Find floor value
    "room": (0x2690EA, 1, "Main RAM"),
    "entrance": (0x2690EB, 1, "Main RAM"),

    "loading_room": (0x0c2FF0, 1, "Main RAM"),
    "mid_load": (0x265190, 1, "Main RAM"),

    "getting_location": (0x04B9B8, 1, "Main RAM"),
    "getting_train_part": (0x11F5E4, 1, "Main RAM"),
    "menu": (0x260958, 1, "Main RAM"),

    "link_x": (0x05CC, 4, "Data TCM"),
    "link_y": (0x05D0, 4, "Data TCM"),
    "link_z": (0x05D4, 4, "Data TCM"),

    "equipped_item": (0x265318, 4, "Main RAM"),
    "train_gear": (0x2CA24C, 4, "Main RAM"),

    "health": (0x2651BC, 1, "Main RAM"),
    "heart_count": (0x2651BD, 1, "Main RAM"),
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
STAGE_FLAGS_OFFSET = 176
STAGE_FLAG_POINTER = 0x265164

# Addresses to read each cycle
read_keys_always = ["game_state", "received_item_index", "is_dead", "stage", "room", "entrance", "slot_id", "menu",
                    "loading_room", "mid_load"]
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
        self.loading_stage = False  # Used to set stage flags mid loading cause the usual time is too late

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
        await write_memory_value(ctx, RAM_ADDRS["health"][0], await read_memory_value(ctx, *RAM_ADDRS["heart_count"]), size=RAM_ADDRS["health"][1])

    async def watched_intro_cs(self, ctx):
        return await read_memory_value(ctx, 0x265726) & 1

    async def update_main_read_list(self, ctx: "BizHawkClientContext", stage: int, in_game=True):
        read_keys = read_keys_always
        read_keys += read_keys_land
        self.main_read_list = {k: v for k, v in RAM_ADDRS.items() if k in read_keys}
        print(self.main_read_list)

    def process_loading_variable(self, read_result) -> bool:
        mid_load = read_result.get("mid_load", True) == 0xFF
        if self._loading_scene and not self.loading_stage:
            print(f"### Loading scene {mid_load} {self.loading_stage}")
            if mid_load:
                print(f"### Mid load active")
                self.loading_stage = True

        if self.loading_stage:
            if not mid_load:
                print(f"### Mid load deactive")
                self.loading_stage = False
                return mid_load
        return not read_result.get("loading_room", 27)

    async def process_read_list(self, ctx: "BizHawkClientContext", read_result: dict):
        current_menu = read_result["menu"]
        self.in_stamp_stand = current_menu == 0x0E
        self.getting_location = not read_result["getting_location"]

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
            # Finished game?
            goal = ctx.slot_data.get("goal")
            if goal == 0 and location.get("region_id") == "tos 3f rail map":
                self.has_goal_location = True
            if goal == 1 and location.get("region_id") == "tos 7f rail map":
                self.has_goal_location = True
            if goal == 2 and location.get("region_id") == "wt stagnox":
                self.has_goal_location = True
            if goal == 3 and location.get("region_id") == "bt fraaz":
                self.has_goal_location = True

    # TODO needs a way of freezing value
    # async def game_watcher(self, ctx: "BizHawkClientContext"):
    #     await super().game_watcher(ctx)
    #     if self.current_scene == (0x0400 or 0x0500 or 0x0600 or 0x0700):
    #         current_gear = await read_memory_value(ctx, 0x2CA24C, 4)
    #         if current_gear == 0xC1:
    #             await write_memory_value(ctx, 0x2CA250, 0xFFFFFFFF)
    #             print(await read_memory_value(ctx, 0x2CA250, 4))

    async def process_game_completion(self, ctx: "BizHawkClientContext"):
        if self.has_goal_location:
            return True
        return False


    async def process_deathlink(self, ctx: "BizHawkClientContext", is_dead, stage, read_result):
        pass

    async def set_stage_flags(self, ctx, stage):
        if stage in STAGE_FLAGS:
            stage_address = await read_memory_value(ctx, STAGE_FLAG_POINTER, size=4)
            stage_flag_address = stage_address + STAGE_FLAGS_OFFSET - 0x2000000
            print(f"Setting stage flags for stage {hex(stage)} at address {hex(stage_flag_address)}: {[hex(i) for i in STAGE_FLAGS[stage]]}")
            await write_memory_values(ctx, stage_flag_address, STAGE_FLAGS[stage], size=4)

