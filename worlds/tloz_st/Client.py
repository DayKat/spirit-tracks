
from .DSZeldaClient.DSZeldaClient import *
from .DSZeldaClient.subclasses import AddrFromPointer, storage_key
from .data.Addresses import STAddr
from .data.Items import ITEMS
from .data.DynamicEntrances import DYNAMIC_ENTRANCES_BY_SCENE
from .data.Entrances import ENTRANCES
from settings import get_settings
from typing import Literal

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext, BizHawkClientCommandProcessor
    from . import SpiritTracksSettings

# gMapManager -> mCourse -> mSmallKeys
SMALL_KEY_OFFSET = 0x260
STAGE_FLAGS_OFFSET = 176
TRAIN_SPEED_OFFSET = 0x94
TRAIN_GEAR_OFFSET = 0x27c
TRAIN_QUICK_STATION_OFFSET = 0x80
default_train_speed = (-143, 0, 115, 193)

train_speed_addresses = [STAddr.train_speed_reverse, STAddr.train_speed_stop, STAddr.train_speed_med, STAddr.train_speed_fast]

# Addresses to read each cycle
read_keys_always = [STAddr.game_state, STAddr.received_item_index, STAddr.stage, STAddr.room, STAddr.entrance, STAddr.slot_id, STAddr.menu,
                    STAddr.loading_room, STAddr.mid_load, STAddr.saving]
read_keys_land = [STAddr.getting_location, STAddr.getting_train_part]
read_keys_train = [STAddr.train_gear]

rabbit_storage_key = "rabbit_locs"
saved_scene_key = "last_saved_scene"
checked_entrances_key = "st_checked_entrances"

def count_bits(n):
    count = 0
    while n:
        n &= n-1
        count += 1
    return count

def get_client_as_command_processor(self: "BizHawkClientCommandProcessor"):
    ctx = self.ctx
    from worlds._bizhawk.context import BizHawkClientContext
    assert isinstance(ctx, BizHawkClientContext)
    client = ctx.client_handler
    assert isinstance(client, SpiritTracksClient)
    return client

def cmd_train_option(self: "BizHawkClientCommandProcessor",
                     option: Literal["snap_speed", "quick_station", "speed", "options"] = "options",
                     *args: str):
    """
    Change various train options. Currently implemented:
      - speed <speed: int | "default" | "reset" | "list"> <gear>
      - snap_speed (True): instantly switch to new speeds on changing gear. Never active for stopping gear
      - quick_station (True): enter stations at any speed if gear is on stop
      - options: lists current option values
    """
    # Thanks to Silvris's mm2 implementation for help with bizhawk command processing
    valid_options = ["snap_speed", "quick_station", "speed", "options"]
    option = option.lower()
    if option not in valid_options:
        self.output(f"  \"{option}\" is not a valid option! {valid_options}")
        return False

    if option == "speed":
        return cmd_train_speed(self, *args)

    client = get_client_as_command_processor(self)
    if option == "options":
        self.output(f"  Current train options:")
        self.output(f"    speed: {client.train_speed}")
        self.output(f"    snap_speed: {client.train_snap_speed}")
        self.output(f"    quick_station: {client.train_quick_station}")
        return True

    value = args[0].lower() if args else "true"
    valid_bool_values = {"0": False, "1": True, "false": False, "true": True, "default": True, "reset": True}
    value_bool = valid_bool_values.get(value, None)
    if value_bool is None:
        self.output(f"  \"{value}\" is not a valid boolean!")
        return False

    setattr(client, f"train_{option}", value_bool)
    host_settings: SpiritTracksSettings = get_settings().get('tloz_st_options')
    host_settings.update({f"train_{option}": value_bool})
    self.output(f"  Set option {option} to {value_bool}")
    return True

def cmd_train_speed(self: "BizHawkClientCommandProcessor",
                    speed: int or str = "list",
                    gear: str = "2"):

    def set_speed(speed_list):
        client.train_speed = list(speed_list)
        client.update_train_speed = True
        self.output(f"  Setting train speeds: {speed_list}")
        host_settings: SpiritTracksSettings = get_settings().get('tloz_st_options')
        host_settings.update({f"train_speed": speed_list})

    client = get_client_as_command_processor(self)
    special_speeds = ["list", "default", "reset"]
    if speed in special_speeds:
        if speed == "list":
            self.output(f"  Current train speeds: {client.train_speed}")
            return True
        elif speed in ["default", "reset"]:
            set_speed(default_train_speed)
            return True

    valid_gears = {"reverse": 0, "stop": 1, "slow": 2, "fast": 3,
                   "back": 0, "backwards": 0, "pause": 1, "neutral": 1, "mid": 2, "max": 2,
                   "-1": 0, "0": 1, "1": 2, "2": 3}
    if gear.lower() in valid_gears:
        gear_int = valid_gears[gear]
    else:
        self.output(f"  \"{gear}\" is not a valid gear! {[s for s in valid_gears]}")
        return False

    try:
        speed = min(int(speed), 9999)
        speed = max(speed, -9999)  # soft cap of 9999
    except ValueError:
        self.output(f"  \"{speed}\" is not a valid speed, must be an int or in {special_speeds}")
        return False

    client.train_speed[gear_int] = speed
    set_speed(client.train_speed)
    return True

class SpiritTracksClient(DSZeldaClient):
    game = "The Legend of Zelda - Spirit Tracks"
    system = "NDS"
    train_speed_addr: "Address"
    train_speed_pointer: "Address"
    train_gear_addr: "Address"

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

        self.visited_entrances = set()
        self.event_reads = []
        self.sent_event = False
        self.event_data = []
        self.entrances = ENTRANCES

        # Train speed stuff
        self.reset_cycles = 0
        self.last_train_gear = 2
        self.reload_on_item = False
        self.train_snap_speed = True
        self.train_quick_station = True
        self.update_train_speed: bool = False
        self.train_speed = [-143, 0, 115, 193]

    async def get_small_key_address(self, ctx) -> int:
        return STAddr.small_keys

    async def check_game_version(self, ctx: "BizHawkClientContext") -> bool:
        rom_name_bytes = await STAddr.game_identifier.read_bytes(ctx)
        rom_name = bytes([byte for byte in rom_name_bytes[0] if byte != 0]).decode("ascii")
        print(f"Rom Name: {rom_name}")
        if rom_name == "SPIRITTRACKSBKIP":  # EU

            # Set commands
            if "train_speed" not in ctx.command_processor.commands:
                ctx.command_processor.commands["train"] = cmd_train_option
            return True
        return False

    async def set_special_starting_flags(self, ctx: "BizHawkClientContext") -> list[tuple[int, list, str]]:
        res = []
        if ctx.slot_data.get("endgame_scope", 0) > 0:
            res += STAddr.adv_flags_57.get_write_list(0x91)
        return res

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

    async def has_special_dynamic_requirements(self, ctx: "BizHawkClientContext", data) -> bool:
        def check_dungeon_reqs():
            if "dungeons" in data:
                if ctx.slot_data["dark_realm_access"] != 1:
                    return data["dungeons"]  # Case where dungeons are not required for dark realm
                dungeon_locs = {self.location_name_to_id[i] for i in ctx.slot_data["required_dungeons"]}
                has_locs = sum([1 for loc in ctx.checked_locations if loc in dungeon_locs])
                comp = has_locs >= ctx.slot_data["dungeons_required"]
                print(f"Checking dungeons: {has_locs} >= {ctx.slot_data['dungeons_required']} for comp {data['dungeons']}")
                return comp == data["dungeons"]
            return True

        if not check_dungeon_reqs():
            print(f"\t{data['name']} does not have dungeon requirements")
            return False
        return True


    async def full_heal(self, ctx, bonus=0):
        hearts = (self.item_count(ctx, "Heart Container") + 3)*4
        await STAddr.health.overwrite(ctx, hearts+bonus)

    async def watched_intro_cs(self, ctx):
        return await STAddr.watched_intro.read(ctx) & 1

    async def update_main_read_list(self, ctx: "BizHawkClientContext", stage: int, in_game=True):
        read_keys = read_keys_always
        read_keys += read_keys_land  # TODO: don't bother reading on train
        # read_keys += read_keys_train
        if stage in range(4, 8):
            self.train_speed_pointer = (await STAddr.train_speed_pointer.read(ctx)) - 0x2000000
            self.train_gear_addr = AddrFromPointer(self.train_speed_pointer+TRAIN_GEAR_OFFSET)
            read_keys.append(self.train_gear_addr)

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
        getting_location = read_result[STAddr.getting_location] and not read_result[STAddr.saving]
        self.getting_location = getting_location or self.reset_cycles

        if getting_location:  # add extra time after receiving items cause finding a good flag is hard
            self.reset_cycles = 3

        if self.reset_cycles > 0 and not getting_location:
            self.reset_cycles -= 1


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

        # print(f"Goal check {ctx.slot_data['goal']} last {self.last_stage} current {hex(self.current_stage)}")
        if ctx.slot_data["goal"] == -1 and self.last_stage == 0x27 and self.current_stage == 0x25:
            self.has_goal_location = True
            await self.store_event(ctx, "GOAL: Defeat Malladus")

    async def store_event(self, ctx, event_name):
        entr = self.entrances[event_name]
        await self.store_visited_entrances(ctx, entr, entr.vanilla_reciprocal)

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

        if self.reload_on_item:
            self.reload_on_item = False
            await self._set_dynamic_entrances(ctx, self.current_scene)
            await self._set_dynamic_flags(ctx, self.current_scene)

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
        await self.detect_ut_event(ctx, self.current_scene)
        await self.process_train_speed(ctx, read_result)


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
                await self.store_event(ctx, "GOAL: Reach ToS 3F")
                self.has_goal_location = True
            if goal == 1 and location.get("region_id") == "tos 7f rail map":
                await self.store_event(ctx, "GOAL: Reach ToS 7F")
                self.has_goal_location = True
            if goal == 2 and location.get("region_id") == "wt stagnox":
                await self.store_event(ctx, "GOAL: Defeat Stagnox")
                self.has_goal_location = True
            if goal == 3 and location.get("region_id") == "bt fraaz":
                await self.store_event(ctx, "GOAL: Defeat Fraaz")
                self.has_goal_location = True

        if "rabbit" in location and "address" in location:
            await self.store_rabbit(ctx, location)

        # Connect event
        if "ut_connect" in location:
            event_name = location["ut_connect"]
            await self.store_event(ctx, event_name)

        if location["name"] in ["Outset Bee Tree", "Outset Clear Rocks"]:
            self.reload_on_item = True

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

        # Get train settings from host.yaml
        host_settings: SpiritTracksSettings = get_settings().get('tloz_st_options')
        print(f"SETTINGS: {host_settings.get('train_speed', self.train_speed)}")
        self.train_speed = host_settings.get("train_speed", self.train_speed)
        self.train_snap_speed = host_settings.get("train_snap_speed", self.train_snap_speed)
        self.train_quick_station = host_settings.get("train_quick_station", self.train_quick_station)


    async def process_deathlink(self, ctx: "BizHawkClientContext", is_dead, stage, read_result):
        pass

    async def process_post_receive(self, ctx):
        if not self.delay_pickup or self.delay_reset:
            await self.update_treasure_tracker(ctx)  # always update treasure tracker, lots of random treasures on ground!

    async def set_stage_flags(self, ctx, stage):
        if stage in STAGE_FLAGS:
            stage_address = await STAddr.stage_flag_pointer.read(ctx)
            stage_flag_address = AddrFromPointer(stage_address + STAGE_FLAGS_OFFSET - 0x2000000, size=4)
            print(f"Setting stage flags for stage {hex(stage)} at {stage_flag_address}: {[hex(i) for i in STAGE_FLAGS[stage]]}")
            await stage_flag_address.set_bits(ctx, STAGE_FLAGS[stage])

    async def process_in_menu(self, ctx, read_result):
        await self.get_saved_scene(ctx, saved_scene_key)

    # UT store entrances to defer
    async def store_visited_entrances(self, ctx: "BizHawkClientContext", detect_data, exit_data,
                                      interaction="traverse"):
        self.visited_entrances |= set(get_stored_data(ctx, checked_entrances_key, set()))
        new_data = {detect_data.id, exit_data.id} if not ctx.slot_data.get(
            "decouple_entrances", False) and detect_data.two_way else {detect_data.id}
        print(f"New Storage Data: {new_data}")

        if new_data:
            key = storage_key(ctx, checked_entrances_key)
            await self.store_data(ctx, key, new_data)

    async def detect_ut_event(self, ctx, scene):
        """
        Send UT event locations on certain flags being set in certain scenes.
        """
        if scene in UT_EVENT_DATA and not self.sent_event:
            if not self.event_reads:
                data = UT_EVENT_DATA[scene].copy()
                data = [data] if isinstance(data, dict) else data
                self.event_data = data
                for i, event in enumerate(data):
                    address = AddrFromPointer(self.stage_flag_address + event.get("offset", 0), size=event.get("size", 1)) if event["address"] == "stage_flags" else event["address"]
                    print(f"event data {self.event_data}")
                    self.event_data[i]["address"] = address
                    print(f"event data {self.event_data}")
                    self.event_reads.append(address)

            read_results = await read_multiple(ctx, self.event_reads)
            for event, res in zip(self.event_data, read_results.values()):
                if event["value"] & res:
                    if "entrance" in event:
                        print(f"Event detection Success!, {event['entrance']}")
                        entrance = self.entrances[event["entrance"]]
                        await self.store_visited_entrances(ctx, entrance, entrance.vanilla_reciprocal)
                    # elif "event" in event:  # not implemented yet
                    #     print(f"Event detection Success!, {event['event']}")
                    #     key = storage_key(ctx, ut_events_key)
                    #     await self.store_data(ctx, key, [event["event"]])

                    self.event_reads.remove(event["address"])
                    self.event_data.remove(event)
            if not self.event_data:
                print(f"All events sent!")
                self.sent_event = True

        else:
            self.sent_event = True

    async def process_hard_coded_rooms(self, ctx, current_scene):
        if self.current_stage in range(4, 8):
            await write_multiple(ctx, train_speed_addresses, self.train_speed)
            self.last_train_gear = -1  # force a quick speed increase
            self.train_speed_pointer = (await STAddr.train_speed_pointer.read(ctx)) - 0x2000000
            self.train_speed_addr = AddrFromPointer(self.train_speed_pointer+TRAIN_SPEED_OFFSET, size=4)

    async def process_train_speed(self, ctx, read_result):
        if self.current_stage in range(4, 8):
            instant_switch = False
            if self.update_train_speed:
                await write_multiple(ctx, train_speed_addresses, self.train_speed)
                self.update_train_speed = False
                instant_switch = True

            current_gear = read_result[self.train_gear_addr]
            if current_gear != self.last_train_gear or instant_switch:
                self.last_train_gear = current_gear

                if self.train_quick_station and current_gear == 1:
                    train_action_addr = AddrFromPointer(self.train_speed_pointer+TRAIN_QUICK_STATION_OFFSET)
                    await train_action_addr.overwrite(ctx, 0x5c, silent=True)  # instant-enter station
                # Instant-set train speed
                if self.train_snap_speed and current_gear != 1:
                    await self.train_speed_addr.overwrite(ctx, self.train_speed[current_gear]*0x10, silent=True)

