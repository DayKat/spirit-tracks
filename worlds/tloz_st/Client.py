
from .DSZeldaClient.DSZeldaClient import *
from .DSZeldaClient.subclasses import storage_key
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
read_keys_land = [STAddr.getting_location, STAddr.getting_item_safety]
read_keys_train = []

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

def cmd_warp_to_start(self: "BizHawkClientCommandProcessor"):
    """Prime a warp to start that triggers on entering any entrance. Run again to cancel"""
    client = get_client_as_command_processor(self)
    client.warp_to_start_flag = not client.warp_to_start_flag
    if client.warp_to_start_flag:
        self.output(f"Primed a warp to start. Enter any entrance to warp to Outset")
    else:
        self.output(f"Canceled Warp to Start")
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
        self.treasure_tracker: dict = {}
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
        self.boss_warp_entrance = None

        # Train speed stuff
        self.reset_cycles = 0
        self.last_train_gear = 2
        self.reload_on_item = False
        self.train_snap_speed = True
        self.train_quick_station = True
        self.update_train_speed: bool = False
        self.train_speed = [-143, 0, 115, 193]
        self.has_set_starting_train = False
        self.key_address = STAddr.small_keys

        self.hint_data = HINT_DATA
        self.got_item_no_loc = False
        self.potion_tracker = [0, 0]
        self.save_ammo = None
        self.drinking_potion = False
        self.addr_drinking_potion = None
        self.set_train_in_overworld: bool = False

        self.boss_key_y = None
        self.boss_key_read = None

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
            if "warp_to_start" not in ctx.command_processor.commands:
                ctx.command_processor.commands["warp_to_start"] = cmd_warp_to_start
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
                print(f"{ctx.slot_data['required_dungeons']}")
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
            train_speed_thingy = (await STAddr.train_speed_pointer.read(ctx)) - 0x2000000
            print(f"Train speed thingy {hex(train_speed_thingy)}")
            if 0x400000 > train_speed_thingy > 0:
                self.train_speed_pointer = train_speed_thingy
                self.train_gear_addr = Address.from_pointer(self.train_speed_pointer+TRAIN_GEAR_OFFSET)
                read_keys.append(self.train_gear_addr)
        else:
            offset = 0xf80 if self.current_stage == 0x29 else 0xf64
            potion_addr = await STAddr.drinking_potion_pointer.read(ctx) - 0x2000000 + offset
            if 0x400000 > potion_addr > 0:
                self.addr_drinking_potion = Address.from_pointer(potion_addr, size=4)
                read_keys.append(self.addr_drinking_potion)
            print(f"Potion pointer {hex(potion_addr)}")

        self.main_read_list = read_keys
        # print(f"read keys len: {len(read_keys)}")
        # print(self.main_read_list, read_keys)
        # print(f"Slot data {ctx.slot_data}")

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

        if self.getting_location:
            self.reset_cycles = True

        if self.reset_cycles and not getting_location and not read_result[STAddr.getting_item_safety]:
            self.reset_cycles = False


        # Fix for stamp stand not counting as getting item
        if self.in_stamp_stand and self.receiving_location:
            self.getting_location = True

        if read_result[STAddr.stage] == 0x79 and self.last_saved_scene:
            stage = (self.last_saved_scene & 0xFF00) >> 8
            if stage in DUNGEON_STAGES_TO_ENTRANCE_SCENE:
                self.last_saved_scene = DUNGEON_STAGES_TO_ENTRANCE_SCENE[stage]

            print(f"Overwriting weird scene: {hex(self.last_saved_scene)}")
            stage, room = (self.last_saved_scene & 0xFF00) >> 8, self.last_saved_scene & 0xFF
            if stage in DUNGEON_STAGES_TO_ENTRANCE_SCENE:
                self.last_saved_scene = DUNGEON_STAGES_TO_ENTRANCE_SCENE[stage]

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

    async def update_potion_tracker(self, ctx, spec=""):
        reads = await read_multiple(ctx, [STAddr.potion_0, STAddr.potion_1])
        new_potions = list(reads.values())
        res = False
        if new_potions != self.potion_tracker:
            print(F"New Potions: {new_potions} {spec}")
            res = True
        self.potion_tracker = new_potions
        return res

    async def check_potion_location(self, ctx):
        """Checks for potion locations in shops if treasure tracker doesn't find a treasure on a location"""
        if self.current_scene in potion_location_lookup and "potions" in ctx.slot_data["shopsanity"]:
            empty_slots = [addr for addr, prev in zip([STAddr.potion_0, STAddr.potion_1], self.potion_tracker) if prev == 0]
            if not empty_slots:
                return
            slot = await empty_slots[0].read(ctx)
            if not slot:
                return
            location = potion_location_lookup.get(self.current_scene, {}).get(slot, None)
            if location:
                if self.location_name_to_id[location] not in ctx.checked_locations:
                    await self._process_checked_locations(ctx, location)


    async def check_ammo_shop(self, ctx):
        if self.save_ammo is None or "ammo" not in ctx.slot_data["shopsanity"]:
            return
        for addr, loc in ammo_shop_lookup.get(self.current_scene, {}).items():
            current_ammo = await addr.read(ctx)
            if current_ammo == 0:
                continue
            if self.location_name_to_id[loc] not in ctx.checked_locations:
                await self._process_checked_locations(ctx, loc)
                return
            self.save_ammo[addr] = current_ammo

    async def update_treasure_tracker(self, ctx: "BizHawkClientContext", last_loc=None):
        read_list = [ITEMS[name].address for name in ITEM_GROUPS["All Treasures"]]
        new_treasure = await read_multiple(ctx, read_list)
        print(f"Updating Treasure Tracker: {last_loc}")

        if last_loc == "no_loc":
            self.treasure_tracker = new_treasure
            self.got_item_no_loc = True
            return
        elif not (last_loc == "post_receive" and self.got_item_no_loc):
            self.treasure_tracker = new_treasure
            print(f"No special treasure")
            return

        self.got_item_no_loc = False
        diff = {t: n - o for n, o, t in
                zip(new_treasure.values(), self.treasure_tracker.values(), ITEM_GROUPS["All Treasures"]) if n - o > 0}
        if not diff:
            await self.check_potion_location(ctx)
            return

        single_item = [t for t in diff][0]
        print(f"Updated Treasure Tracker: {diff}")

        async def remove_treasure():
            reads = await read_multiple(ctx, [ITEMS[i].address for i in diff])
            await write_multiple(ctx, [a for a in reads], [v-1 for v in reads.values()])

        # Detect shop locations
        if "treasure" in ctx.slot_data["shopsanity"] and self.current_scene in SHOP_TREASURE_DATA:
            for data in SHOP_TREASURE_DATA[self.current_scene]:
                if single_item in ITEM_GROUPS[data["group"] + " Treasures"]:
                    for location in data["locations"]:
                        if self.location_name_to_id[location] not in ctx.checked_locations:
                            await remove_treasure()
                            await self._process_checked_locations(ctx, location)
                            return

        # Do stuff with excess treasure
        if ctx.slot_data["excess_random_treasure"] in [0, 2]:
            print(f"Removing {diff} from treasures")
            await remove_treasure()
            # self.last_vanilla_item.extend([t for t in diff])
        if ctx.slot_data["excess_random_treasure"] == 2:
            rupees = sum([TREASURE_PRICES[treasure]*count for treasure, count in diff.items()])
            print(f"Getting {rupees} rupees")
            await STAddr.rupees.add(ctx, rupees)


        self.treasure_tracker = new_treasure

    async def receive_item_post_processing(self, ctx, item_name, item_data):
        print(f"Post Processing {item_name}")

        if "Rabbit" in item_name:
            await self.update_rabbit_count(ctx)
        if "Treasure:" in item_name:
            await self.update_treasure_tracker(ctx, "item_process")
        if item_name == "Stamp Book" and self.current_scene == 0x2F0A:
            await STAddr.adv_flags_25.unset_bits(ctx, 2)
        if item_name == "Bombs (Progressive)" and self.current_scene == 0x4503:
            await STAddr.adv_flags_22.unset_bits(ctx, 2)
        if item_name in ["Forest Glyph", "Cannon",
                         "Portal Unlock: Hyrule Castle to Anouki Village",
                         "Portal Unlock: Trading Post to E Snow Realm"]:
            print(f"Reloading dynamic entrances")
            await self._set_dynamic_entrances(ctx, self.current_scene)  # allow escaping without reloading!

        if self.reload_on_item:
            print(f"Reloading dynamic entrances")
            self.reload_on_item = False
            await self._set_dynamic_entrances(ctx, self.current_scene)
            await self._set_dynamic_flags(ctx, self.current_scene)

        # Get spirit weapons from final tear of light
        if "Tear of Light" in item_name and ctx.slot_data["spirit_weapons"] == 1:
            if any([
                self.item_count(ctx, "Tear of Light (All Sections)") >= 6,
                self.item_count(ctx, "Tear of Light (Progressive)") >= 16,
                self.item_count(ctx, "Big Tear of Light (All Sections)") >= 2,
                self.item_count(ctx, "Big Tear of Light (Progressive)") >= 6]):
                await STAddr.adv_flags_16.set_bits(ctx, 1)
                await STAddr.items_2.set_bits(ctx, 4)
                logger.info(f"You Unlocked the Lokomo Sword and the Bow of Light!")

        if item_name in ["Cannon", "Wagon"] and ctx.slot_data["starting_train"] != -1:
            self.set_train_in_overworld = True
            await self.set_starting_train(ctx)

        if "ammo" in ctx.slot_data["shopsanity"] and self.current_scene in ammo_shop_lookup and item_name in ITEM_GROUPS["Ammo Items"]:
            addr = item_data.ammo_address if hasattr(item_data, "ammo_address") else item_data.address
            await addr.overwrite(ctx, 0)
            item_count = self.item_count(ctx, item_data.refill) if item_name in ITEM_GROUPS["Refill Items"] else self.item_count(ctx, item_name)
            self.save_ammo[addr] = item_data.give_ammo[item_count-1]

        # Open boss door if got key in that room
        if item_name.startswith("Boss Key") and self.current_scene in BOSS_KEY_DATA:
            data = BOSS_KEY_DATA[self.current_scene]
            if data["dungeon"] in item_name and (self.current_scene & 0xff00 != 0x1300 or self.location_name_to_id[data["location"]] in ctx.checked_locations):
                print(f"Opening boss door for {self.current_scene}")
                await data["door"].overwrite(ctx, 3)

    async def process_on_room_load(self, ctx, current_scene, read_result: dict):
        await self.update_treasure_tracker(ctx, "room_load")
        await self.update_potion_tracker(ctx, "room_load")
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
        await self.drink_potion(ctx, read_result)
        await self.detect_boss_key(ctx)

    async def drink_potion(self, ctx, read_results):
        drinking_potion = read_results.get(self.addr_drinking_potion, 0)
        if drinking_potion == 0x3b:
            self.drinking_potion = True
        if self.drinking_potion and drinking_potion == 0x39:
            self.drinking_potion = False
            await self.update_potion_tracker(ctx, "drunk_potion")

    def cancel_location_read(self, location) -> bool:
        if "stamp" in location:
            return True
        if "rabbit" in location:
            return True
        return False

    async def check_location_post_processing(self, ctx, location: dict):
        print(f"Post processing loc {location}")
        if not location:
            await self.update_treasure_tracker(ctx, "no_loc")
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

        if "Tear of Light" in location.get("vanilla_item", "") and ctx.slot_data["randomize_tears"] != -1:
            await STAddr.tears_of_light.overwrite(ctx, 1)  # prevent cutscene and underflow

        if self.current_scene in [0x1309, 0x1318] and location.get("vanilla_item", "").startswith("Boss Key"):
            if self.item_count(ctx, location["vanilla_item"]):
                print("Opening ToS boss door after having key and getting boss key location")
                await BOSS_KEY_DATA[self.current_scene]["door"].overwrite(ctx, 3)

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
            realms = ["Grass", "Snow", "Sand"]
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
            rabbit_type_lookup = ["Grass Rabbit", "Snow Rabbit", "Water Rabbit", "Mountain Rabbit", "Sand Rabbit"]
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
        if not self.delay_pickup:
            await self.update_treasure_tracker(ctx, "post_receive")  # always update treasure tracker, lots of random treasures on ground!

    async def set_stage_flags(self, ctx, stage):
        if stage in STAGE_FLAGS:
            stage_address = await STAddr.stage_flag_pointer.read(ctx)
            stage_flag_address = Address.from_pointer(stage_address + STAGE_FLAGS_OFFSET - 0x2000000, size=4)
            if ctx.slot_data["randomize_passengers"] == 0:
                if stage == 0x35:
                    STAGE_FLAGS[stage] = [0x16, 0x00, 0x00, 0x00]
                elif stage == 0x35:
                    STAGE_FLAGS[stage] = [0x16, 0x04, 0x00, 0x00]
            print(f"Setting stage flags for stage {hex(stage)} at {stage_flag_address}: {[hex(i) for i in STAGE_FLAGS[stage]]}")
            await stage_flag_address.set_bits(ctx, STAGE_FLAGS[stage])
        if self.set_train_in_overworld:
            await self.set_starting_train(ctx)
            self.set_train_in_overworld = False

        # Give tears of light when entering ToS
        if stage == 0x13 and ctx.slot_data["randomize_tears"] != -1:
            await self.set_tears(ctx)

    async def set_tears(self, ctx):
        set_tears = (self.item_count(ctx, "Tear of Light (All Sections)")
                     or self.item_count(ctx, "Big Tear of Light (All Sections)") * 3)
        if not set_tears:
            section = TOS_FLOOR_TO_SECTION.get(self.current_room, 0)
            if ctx.slot_data["shuffle_tos_sections"] and ctx.slot_data.get("tear_sections", 2) == 2:
                print(f"Section {section} is order {ctx.slot_data['tower_section_lookup']}!")
                section = ctx.slot_data["tower_section_lookup"][str(section)]

            if section == 6:
                return
            big_prog_sub = section - 1
            set_tears = (self.item_count(ctx, f"Tear of Light (ToS {section})")
                         or self.item_count(ctx, f"Big Tear of Light (ToS {section})") * 3
                         or max(0, (self.item_count(ctx, "Big Tear of Light (Progressive)") - big_prog_sub) * 3)
                         or max(0, self.item_count(ctx, "Tear of Light (Progressive)") - big_prog_sub * 3)
                         )
            print(f"Setting tears for section {section} tears {set_tears}")
        else:
            print(f"Setting tears {set_tears}")

        await STAddr.tears_of_light.overwrite(ctx, set_tears)

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

    async def detected_new_scene(self, ctx):
        await self.save_tos_keycount(ctx)
        self.event_reads = []
        self.sent_event = False

    async def save_scene(self, ctx, *args):
        if await super().save_scene(ctx, *args):
            await self.save_tos_keycount(ctx)

    async def save_tos_keycount(self, ctx):
        """ToS keycount is not dependent on stage, so save current count on room change or save"""
        print(f"Saving Keycount {self.last_stage} {self.last_scene}")
        if self.last_stage != 0x13 or self.last_scene is None:
            return

        current_keys = await self.key_address.read(ctx)
        current_section = TOS_FLOOR_TO_SECTION[self.last_scene & 0xFF]  # triggers after scene change
        section_key = 0x130 + current_section
        if section_key in DUNGEON_KEY_DATA:
            key_data = await STAddr.key_storage_tos.read(ctx)
            blank_data = key_data & (0xFF - DUNGEON_KEY_DATA[section_key]["filter"])
            new_data = blank_data + DUNGEON_KEY_DATA[section_key]["value"]*current_keys
            if new_data != key_data:
                print(f"Saving ToS key count: {hex(new_data)}")
                await STAddr.key_storage_tos.overwrite(ctx, new_data)

    async def enter_special_key_room(self, ctx, stage, scene_id):
        if stage == 0x13:
            section = TOS_FLOOR_TO_SECTION[self.current_room]
            key_code = 0x130 + section
            print(f"Special Keycode: {key_code} {DUNGEON_KEY_DATA.get(key_code)}")
            if key_code in DUNGEON_KEY_DATA:
                key_data = DUNGEON_KEY_DATA[key_code]
                key_storage = await STAddr.key_storage_tos.read(ctx)
                current_keys = (key_storage & key_data["filter"]) // key_data["value"]
                print(f"Current Keys = {current_keys} | {(key_storage & key_data['filter'])} / {key_data['value']}")
                await self.key_address.overwrite(ctx, current_keys)
            else:
                await self.key_address.overwrite(ctx, 0)
            return True

        return False

    async def detect_ut_event(self, ctx, scene):
        """
        Send UT event locations on certain flags being set in certain scenes.
        """
        if scene in UT_EVENT_DATA and not self.sent_event:
            if not self.event_reads:
                data = UT_EVENT_DATA[scene]
                data = [data] if isinstance(data, dict) else data
                print(f"Event Data {UT_EVENT_DATA} {data}")
                self.event_data = data
                for i, event in enumerate(data):
                    address = Address.from_pointer(self.stage_flag_address + event.get("offset", 0), size=event.get("size", 1)) if event["address"] == "stage_flags" else event["address"]
                    self.event_data[i]["address"] = address
                    self.event_reads.append(address)

            read_results = await read_multiple(ctx, self.event_reads)
            for event, res in zip(self.event_data, read_results.values()):
                # print(read_results)
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

    @staticmethod
    async def set_starting_train(ctx):
        res = []
        train = ctx.slot_data["starting_train"]
        if train == -1:  # all parts
            res += STAddr.train_parts.get_write_list(0xFFFFFFFF)
            train = 0
        else:
            res += STAddr.train_parts.get_write_list(0xF << (train*4))
        res += [a.get_inner_write_list(train) for a in [
            STAddr.equipped_engine, STAddr.equipped_cannon, STAddr.equipped_car, STAddr.equipped_cart,
        ]]
        print(f"Setting starting train {res}")
        await bizhawk.write(ctx.bizhawk_ctx, res)

    async def process_hard_coded_rooms(self, ctx, current_scene):
        if self.current_stage in range(4, 8):
            await write_multiple(ctx, train_speed_addresses, self.train_speed)
            self.last_train_gear = -1  # force a quick speed increase
            self.train_speed_pointer = (await STAddr.train_speed_pointer.read(ctx)) - 0x2000000
            self.train_speed_addr = Address.from_pointer(self.train_speed_pointer+TRAIN_SPEED_OFFSET, size=4)
        if current_scene == 0x2f00 and not self.has_set_starting_train:
            if self.location_name_to_id["Outset Bee Tree"] not in ctx.checked_locations:
                print(f"Setting starting train")
                await self.set_starting_train(ctx)
            self.has_set_starting_train = True
        # if current_scene in range(0x4b00, 0x5000):  still too early
        #     await STAddr.item_restrictions.overwrite(ctx, 0)
        if self.save_ammo:
            await write_multiple(ctx, list(self.save_ammo.keys()), list(self.save_ammo.values()))
            self.save_ammo = None

        if current_scene in ammo_shop_lookup and "ammo" in ctx.slot_data["shopsanity"]:
            ammo_addresses = [STAddr.bomb_count, STAddr.arrow_count]
            self.save_ammo = await read_multiple(ctx, ammo_addresses)
            await write_multiple(ctx, ammo_addresses, [0, 0])

        # Boss key rando stuff
        if current_scene in BOSS_KEY_DATA and ctx.slot_data.get("randomize_boss_keys", 0):
            data = BOSS_KEY_DATA[self.current_scene]
            # Set key watches
            if self.location_name_to_id[data["location"]] in ctx.checked_locations:
                print(f"Has found location {data['location']}, deleting boss key")
                await self.delete_boss_key(ctx)
            else:
                pointer = await data["pointer"].read(ctx) -0x2000000
                self.boss_key_y = data["y"]
                self.boss_key_read = Address(pointer+8, size=4)
                print(f"Loaded boss key data: {self.boss_key_read} y: {self.boss_key_y}")

            # Open door
            if self.item_count(ctx, f"Boss Key ({data['dungeon']})"):
                if current_scene & 0xff00 != 0x1300 or self.location_name_to_id[data["location"]] in ctx.checked_locations:
                    print(f"Opening boss door for {current_scene}")
                    if await data["door"].read(ctx) != 0x5:
                        await data["door"].overwrite(ctx, 3)
        else:
            self.boss_key_y, self.boss_key_read = None, None

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
                    train_action_addr = Address.from_pointer(self.train_speed_pointer+TRAIN_QUICK_STATION_OFFSET)
                    await train_action_addr.overwrite(ctx, 0x5c, silent=True)  # instant-enter station
                # Instant-set train speed
                if self.train_snap_speed and current_gear != 1:
                    await self.train_speed_addr.overwrite(ctx, self.train_speed[current_gear]*0x10, silent=True)


    def update_boss_warp(self, ctx, stage, scene_id):
        if scene_id in BOSS_WARP_SCENE_LOOKUP:  # Boss rooms
            reverse_exit = BOSS_WARP_SCENE_LOOKUP[scene_id]
            reverse_exit_id = self.entrances[reverse_exit].id
            pair = ctx.slot_data["er_pairings"].get(f"{reverse_exit_id}", self.entrances[reverse_exit].vanilla_reciprocal.id)
            if pair is None:
                print(f"Boss Entrance not Randomized")
                self.boss_warp_entrance = reverse_exit
            self.boss_warp_entrance = self.entrance_id_to_entrance[pair]
            print(f"Warp Stage: {stage}, current warp {self.boss_warp_entrance}")
            return self.boss_warp_entrance

        return None

    async def detect_boss_key(self, ctx):
        """Called each cycle while in a boss key room to detect a change in boss key position"""
        if self.boss_key_y is not None:
            if await self.boss_key_read.read(ctx, signed=True, silent=True) > self.boss_key_y + 10:
                loc = BOSS_KEY_DATA[self.current_scene]["location"]
                await self._process_checked_locations(ctx, loc)
                print(f"Found boss key location {loc}")
                await self.delete_boss_key(ctx)
                self.boss_key_y, self.boss_key_read = None, None


    async def delete_boss_key(self, ctx):
        pointer = await STAddr.boss_key_deletion_pointer.read(ctx) - 0x2000000
        print(f"Deleting boss key @ {hex(pointer)}")
        size = 12
        if self.current_stage == 0x1b:
            pointer += 44  # Ocean temple bk does not load into the first slot in memory
            await Address.from_pointer(pointer+60, 4).overwrite(ctx, 0)  # also needs this to not crash
            size = 8
        deletion_address = Address.from_pointer(pointer, size)
        # print(f"Deleting boss key @ {STAddr.boss_key_deletion}")
        await deletion_address.overwrite(ctx, 0)

