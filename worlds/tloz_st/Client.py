
from .DSZeldaClient.DSZeldaClient import *
from .DSZeldaClient.subclasses import AddrFromPointer, storage_key
from .data.Addresses import STAddr
from .data.Items import ITEMS
from .data.DynamicEntrances import DYNAMIC_ENTRANCES_BY_SCENE

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

# gMapManager -> mCourse -> mSmallKeys
SMALL_KEY_OFFSET = 0x260
STAGE_FLAGS_OFFSET = 176

# Addresses to read each cycle
read_keys_always = [STAddr.game_state, STAddr.received_item_index, STAddr.stage, STAddr.room, STAddr.entrance, STAddr.slot_id, STAddr.menu,
                    STAddr.loading_room, STAddr.mid_load, STAddr.saving]
read_keys_land = [STAddr.getting_location, STAddr.getting_train_part]

rabbit_storage_key = "rabbit_locs"
saved_scene_key = "last_saved_scene"

def count_bits(n):
    count = 0
    while n:
        n &= n-1
        count += 1
    return count

class SpiritTracksClient(DSZeldaClient):
    game = "The Legend of Zelda - Spirit Tracks"
    system = "NDS"

    def __init__(self) -> None:
        super().__init__()

        # Required variables
        self.starting_flags = STARTING_FLAGS
        self.dungeon_key_data = DUNGEON_KEY_DATA
        self.starting_entrance = (0x2F, 0, 1)  # stage, room, entrance
        self.scene_addr = (STAddr.stage, STAddr.room, STAddr.floor, STAddr.entrance)  # Stage, room, floor, entrance

        self.exit_coords_addr = ()  # TODO: x, y, z. what coords to spawn link at when entering a continuous transition
        self.er_y_offest = 0  # In ph i use coords who's y is 164 off the entrance y
        self.stage_flag_offset = STAGE_FLAGS_OFFSET

        self.in_stamp_stand: bool = False
        self.scene_to_stamp = build_scene_to_stamp()
        self.goal_locations = build_location_to_goal()
        self.has_goal_location = False
        self.loading_stage = False  # Used to set stage flags mid loading cause the usual time is too late
        self.treasure_tracker = {}
        self.item_data = ITEMS
        self.dynamic_entrances_by_scene = DYNAMIC_ENTRANCES_BY_SCENE

        # Mandatory addresses
        self.addr_game_state = STAddr.game_state
        self.addr_slot_id = STAddr.slot_id
        self.addr_stage = STAddr.stage
        self.addr_room = STAddr.room
        self.addr_entrance = STAddr.entrance
        self.addr_received_item_index = STAddr.received_item_index
        self.health_address = STAddr.health

        self.update_rabbits = False
        self.rabbit_tracker = [0]*7  # list of bytes(as ints) for found overworld rabbits
        self.rabbit_counter = []  # list of counts for each rabbit type caught in the overworld

    async def get_small_key_address(self, ctx) -> int:
        return STAddr.small_keys

    async def check_game_version(self, ctx: "BizHawkClientContext") -> bool:
        rom_name_bytes = await STAddr.game_identifier.read_bytes(ctx)
        rom_name = bytes([byte for byte in rom_name_bytes[0] if byte != 0]).decode("ascii")
        print(f"Rom Name: {rom_name}")
        if rom_name == "SPIRITTRACKSBKIP":  # EU
            return True
        return False

    def get_coord_address(self, at_sea=None, multi=False):
        return STAddr.link_x, STAddr.link_y, STAddr.link_z

    async def get_coords(self, ctx, multi=False):
        coords = await read_multiple(ctx, self.get_coord_address(multi=multi), signed=True)
        print(f"Coords: {coords}")
        return {
            "x": coords[STAddr.link_x],
            "y": coords[STAddr.link_y],
            "z": coords[STAddr.link_z]
        }

    async def full_heal(self, ctx, bonus=0):
        hearts = (self.item_count(ctx, "Heart Container") + 3)*4
        await STAddr.health.overwrite(ctx, hearts+bonus)

    async def watched_intro_cs(self, ctx):
        return await STAddr.watched_intro.read(ctx) & 1

    async def update_main_read_list(self, ctx: "BizHawkClientContext", stage: int, in_game=True):
        read_keys = read_keys_always
        read_keys += read_keys_land  # TODO: don't bother reading on train
        self.main_read_list = read_keys
        # print(self.main_read_list)

    def process_loading_variable(self, read_result) -> bool:
        mid_load = read_result.get(STAddr.mid_load, True) == 0xFF
        if self._loading_scene and not self.loading_stage:
            if mid_load:
                self.loading_stage = True

        if self.loading_stage:
            if not mid_load:
                self.loading_stage = False
                return mid_load
        return not read_result.get(STAddr.loading_room, 27)

    async def process_read_list(self, ctx: "BizHawkClientContext", read_result: dict):
        current_menu: "Address" = read_result[STAddr.menu]
        self.in_stamp_stand = current_menu == 0x0E
        self.getting_location = not read_result[STAddr.getting_location]

        # Fix for stamp stand not counting as getting item
        if self.in_stamp_stand and self.receiving_location:
            self.getting_location = True

        if read_result[STAddr.stage] == 0x79 and self.last_saved_scene:
            print(f"Overwriting weird scene: {hex(self.last_saved_scene)}")
            stage, room = (self.last_saved_scene & 0xFF00) >> 8, self.last_saved_scene & 0xFF
            self.current_scene = self.last_saved_scene
            self.current_stage = read_result[STAddr.stage] = stage
            read_result[STAddr.room] = room
            await STAddr.stage.overwrite(ctx, stage)
            await STAddr.room.overwrite(ctx, room)

    async def update_treasure_tracker(self, ctx):
        read_list = [ITEMS[name].address for name in ITEM_GROUPS["All Treasures"]]
        self.treasure_tracker = await read_multiple(ctx, read_list)
        print(f"Updated Treasure Tracker: {self.treasure_tracker}")

    async def receive_item_post_processing(self, ctx, item_name, item_data):
        if "Rabbit" in item_name:
            await self.update_rabbit_count(ctx)
        if item_name == "Stamp Book" and self.current_scene == 0x2F0A:
            await STAddr.adv_flags_25.unset_bits(ctx, 2)
        if item_name in ["Forest Glyph", "Cannon",
                         "Portal Unlock: Hyrule Castle to Anouki Village",
                         "Portal Unlock: Trading Post to E Snow Realm"]:
            await self._set_dynamic_entrances(ctx, self.current_scene)  # allow escaping without reloading!

    async def process_on_room_load(self, ctx, current_scene, read_result: dict):
        await self.update_treasure_tracker(ctx)
        await self.update_rabbit_count(ctx)

    async def process_in_game(self, ctx, read_result: dict):
        # Detect stamp stand locations
        if self.in_stamp_stand and not self.receiving_location:
            self.receiving_location = True
            stamp_location = self.scene_to_stamp[self.current_scene] #TODO error when loading into slot (in fs) after receiving stamp book offline, scene refresh fixed
            await self._process_checked_locations(ctx, stamp_location)

        await self.save_scene(ctx, read_result, STAddr.saving, saved_scene_key, range(1, 5))

    def cancel_location_read(self, location) -> bool:
        if "stamp" in location:
            return True
        if "rabbit" in location:
            return True
        return False

    async def check_location_post_processing(self, ctx, location: dict):
        print(f"Post processing loc {location}")
        if not location:
            return

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

        if "rabbit" in location and "address" in location:
            await self.store_rabbit(ctx, location)

    # fixes conflict with bizhawk_UT
    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        await super().game_watcher(ctx)

    async def process_game_completion(self, ctx: "BizHawkClientContext"):
        if self.has_goal_location:
            return True
        return False

    async def update_rabbit_count(self, ctx):
        if self.current_stage in [4, 5, 6, 7]:
            self.update_rabbit_tracker(ctx)
            rabbit_bits = self.rabbit_tracker
        else:
            realms = ["Forest", "Snow"]
            rabbit_counts = [min(sum([ITEMS[i].value*self.item_count(ctx, i) for i in ITEM_GROUPS[f"{realm} Rabbits"]]), 10) for realm in realms]
            rabbit_bits = sum([(2 ** count - 1) << 10*i for i, count in enumerate(rabbit_counts)])
            print(f"Updating rabbit bits {hex(rabbit_bits)}")
        await STAddr.rabbits.overwrite(ctx, rabbit_bits)

    async def store_rabbit(self, ctx, loc_data):
        key = storage_key(ctx, rabbit_storage_key)
        index = loc_data["address"] - STAddr.rabbits
        self.rabbit_tracker[index] |= loc_data["value"]
        self.update_rabbit_tracker(ctx)
        await self.store_data(ctx, key, self.rabbit_tracker, operation="replace")

        # Send total location
        if ctx.slot_data["rabbitsanity"] in [3, 4]:
            rabbit_type = loc_data["vanilla_item"]
            rabbit_type_lookup = ["Forest Rabbit", "Snow Rabbit", "Water Rabbit", "Mountain Rabbit", "Sand Rabbit"]
            rabbit_count = self.rabbit_counter[rabbit_type_lookup.index(rabbit_type)]
            plural = "s" if rabbit_count > 1 else ""
            total_loc = f"Catch {rabbit_count} {rabbit_type}{plural}"
            print(f"Sending rabbit total location {total_loc}")
            await self._process_checked_locations(ctx, total_loc)

    def update_rabbit_tracker(self, ctx):
        rabbit_storage = ctx.stored_data[storage_key(ctx, rabbit_storage_key)]
        rabbit_storage = [0]*7 if not rabbit_storage else rabbit_storage
        print(f"\tRabbit storage: {rabbit_storage}")
        self.rabbit_tracker = [s | c for s, c in zip(rabbit_storage, self.rabbit_tracker)]
        print(f"\trabbit tracker {self.rabbit_tracker}")
        all_rabbits = sum([r << 8*i for i, r in enumerate(self.rabbit_tracker)])
        print(f"\tall rabbits: {hex(all_rabbits)}")
        self.rabbit_counter = [count_bits(all_rabbits & (0x3FF << n*10)) for n in range(5)]
        print(f"Updating Rabbit tracker: {[hex(i) for i in self.rabbit_tracker]} {self.rabbit_counter}")

    async def on_connect(self, ctx):
        self.rabbit_tracker = [0]*7
        await ctx.send_msgs([{
                "cmd": "Get",
                "keys": [storage_key(ctx, rabbit_storage_key)],
            }])

    async def process_deathlink(self, ctx: "BizHawkClientContext", is_dead, stage, read_result):
        pass

    async def process_post_receive(self, ctx):
        await self.update_treasure_tracker(ctx)  # always update treasure tracker, lots of random treasures on ground!

    async def set_stage_flags(self, ctx, stage):
        if stage in STAGE_FLAGS:
            stage_address = await STAddr.stage_flag_pointer.read(ctx)
            stage_flag_address = AddrFromPointer(stage_address + STAGE_FLAGS_OFFSET - 0x2000000, size=4)
            print(f"Setting stage flags for stage {hex(stage)} at {stage_flag_address}: {[hex(i) for i in STAGE_FLAGS[stage]]}")
            await stage_flag_address.set_bits(ctx, STAGE_FLAGS[stage])

    async def process_in_menu(self, ctx, read_result):
        await self.get_saved_scene(ctx, saved_scene_key)