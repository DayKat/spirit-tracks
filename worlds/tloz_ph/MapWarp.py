from typing import TYPE_CHECKING
from .DSZeldaClient.DSZeldaClient import read_memory_value, logger, item_count, storage_key, get_stored_data, \
    write_memory_values
from .data.Entrances import ENTRANCES, entrance_id_to_entrance
import worlds._bizhawk as bizhawk
import logging

if TYPE_CHECKING:
    from .Client import PhantomHourglassClient
    from worlds._bizhawk.context import BizHawkClientContext


transition_lookup = {
    0x1F: "Ocean SW Cannon",
    0x20: "Ocean SE Harrow",
    0x21: "Ocean NW Uncharted",
    0x22: "Ocean NE Maze",
    0x23: "Mercay SE Board Ship",
    0x24: "Molida South Board Ship",
    0x25: "Ember West Board Ship",
    0x26: "Gust South Board Ship",
    0x27: "Frost SW Board Ship",
    0x28: "Goron SW Board Ship",
    0x29: "Ruins SW Board Ship",
    0x33: "Dee Ess Board Ship",
    0x2B: "Cannon Board Ship",
    0x2C: "Bannan West Board Ship",
    0x2D: "IotD Board Ship",
    0x2E: "Zauz Board Ship",
    0x2F: "Spirit Board Ship",
    0x30: "Harrow Board Ship",
    0x31: "Maze Board Ship",
    0x32: "Uncharted Board Ship",
}

warp_item_lookup = {
    0x23: "Map Warp: Mercay",
    0x24: "Map Warp: Molida",
    0x25: "Map Warp: Ember",
    0x26: "Map Warp: Gust",
    0x27: "Map Warp: Frost",
    0x28: "Map Warp: Goron",
    0x29: "Map Warp: Ruins",
    0x33: "Map Warp: Dee Ess",
    0x2B: "Map Warp: Cannon",
    0x2C: "Map Warp: Bannan",
    0x2D: "Map Warp: Isle of the Dead",
    0x2E: "Map Warp: Zauz",
    0x2F: "Map Warp: Spirit",
    0x30: "Map Warp: Harrow",
    0x31: "Map Warp: Maze",
    0x32: "Map Warp: Uncharted",
}

ut_event_lookup = {
    0x1F: "wsw",
    0x20: "wse",
    0x21: "wnw",
    0x22: "wne",
    0x23: "wmc",
    0x24: "wml",
    0x25: "we",
    0x26: "wgu",
    0x27: "wf",
    0x28: "wgo",
    0x29: "wr",
    0x33: "wds",
    0x2B: "wc",
    0x2C: "wb",
    0x2D: "wd",
    0x2E: "wz",
    0x2F: "ws",
    0x30: "wh",
    0x31: "wmz",
    0x32: "wu",
}

no_ow_er_lookup = {
    0x1F: [0],
    0x20: [2],
    0x21: [1],
    0x22: [3],
    0x23: [0xb00, 0xb02, 0xb03],
    0x24: [0xc00],
    0x25: [0xd00, 0xd01],
    0x26: [0xe00, 0xe01],
    0x27: [0xf00, 0xf02],
    0x28: [0x1000, 0x1001, 0x1002, 0x1003],
    0x29: [0x1100, 0x1101, 0x1103,
           0x1200, 0x1201, 0x1203],
    0x33: [0x1B00],
    0x2B: [0x1300],
    0x2C: [0x1400],
    0x2D: [0x1500],
    0x2E: [0x1600],
    0x2F: [0x1700],
    0x30: [0x1800],
    0x31: [0x1900],
    0x32: [0x1A00],
}

ow_er_lookup = {
    0x1F: [0],
    0x20: [2],
    0x21: [1],
    0x22: [3],
    0x23: [0xb03],
    0x24: [0xc00],
    0x25: [0xd00],
    0x26: [0xe00],
    0x27: [0xf00],
    0x28: [0x1002],
    0x29: [0x1100,
           0x1200],
    0x33: [0x1B00],
    0x2B: [0x1300],
    0x2C: [0x1400],
    0x2D: [0x1500],
    0x2E: [0x1600],
    0x2F: [0x1700],
    0x30: [0x1800],
    0x31: [0x1900],
    0x32: [0x1A00],
}

safe_entrances_common = {
    0x1F: ["Ocean SW Mercay",
           "Ocean SW Cannon",
           "Ocean SW Ember"],
    0x21: ["Ocean NW Uncharted",
           "Ocean NW Zauz",
           "Ocean NW Gust",
           "Ocean NW Bannan",
           "Ocean NW Board Ghost Ship"],
    0x22: ["Ocean NE Maze",
           "Ocean NE IotD"],
    0x2C: ["Bannan West Board Ship",
           "Bannan West Cave",
           "Bannan West Hut"],
    0x32: ["Uncharted Board Ship"],
}

safe_entrances_ow = safe_entrances_common | {
    0x26: ["Gust South Board Ship", "Gust Secret Cave", "Gust Cave West", "Gust Cave East",
           "Gust South Temple Road North", "Gust South Above Temple North"],
    0x29: ["Ruins SW Board Ship", "Ruins SW Upper Maze North", "Ruins SW Port Cliff North",
           "Ruins SW East", "Ruins SW Port Cave", "Ruins SW Cliff Cave"],
}

island_visibility_addr = {
    "Map Warp: Mercay": 0x1b4b8c,
    "Map Warp: Molida": 0x1b4bb4,
    "Map Warp: Ember": 0x1B4BDC,
    "Map Warp: Cannon": 0x1B4C04,
    "Map Warp: Spirit": 0x1B4C2C,
    "Map Warp: Gust": 0x1B4C54,
    "Map Warp: Bannan": 0x1B4C7C,
    "Map Warp: Zauz": 0x1B4CA4,
    "Map Warp: Uncharted": 0x1B4CCC,
    "Map Warp: Goron": 0x1B4CF4,
    "Map Warp: Frost": 0x1B4D1C,
    "Map Warp: Harrow": 0x1B4D44,
    "Map Warp: Dee Ess": 0x1B4D6C,
    "Map Warp: Ruins": 0x1B4D94,
    "Map Warp: Isle of the Dead": 0x1B4DBC,
    "Map Warp: Maze": 0x1B4DE4,
}

safe_entrances_no_ow = safe_entrances_common | {}

# Ruins lower does not count! check entrances for that!
# Uncharted cave exit does not count
# bannan east does not count
#

stage_lookup = {}

def check_any_er(ctx):
    return any([ctx.slot_data[i] for i in ["shuffle_dungeon_entrances",
                                           "shuffle_ports", "shuffle_caves",
                                           "shuffle_houses",
                                           "shuffle_overworld_transitions",
                                           "shuffle_bosses"]
    ])

# Check for safe entrances
def check_entrances(client: "PhantomHourglassClient", ctx: "BizHawkClientContext", trans_value, safe_entrance_map):
    if trans_value not in safe_entrance_map:
        return True
    if not ctx.slot_data["shuffle_ports"]:  # Entrances only exist if things are actually randomized, this solves most cases. actually it prevents warping to uncharted but i dont care
        if not (ctx.slot_data["shuffle_caves"] and trans_value in [0x2C, 0x32]):
            return True

    client.visited_entrances |= set(get_stored_data(ctx, "ph_traversed_entrances", []))
    visited_entrances = client.visited_entrances
    print(f"Visited entrances: {visited_entrances}")
    for entr in safe_entrance_map[trans_value]:
        entr_id = ENTRANCES[entr].id
        if entr_id in visited_entrances:
            return True
    return False

# Check if player has visited an island
def check_visited_scenes(client, ctx, transition_mode, scene_lookup, safe_entrances_lookup):
    for scene in scene_lookup[transition_mode]:
        if (scene in client.visited_scenes
                and check_entrances(client, ctx, transition_mode, safe_entrances_lookup)):
            print(f"Has visited scene {hex(scene)}. Done!")
            return ENTRANCES[transition_lookup[transition_mode]]
    return None

async def set_visibility(ctx: "BizHawkClientContext"):
    write_list = []
    for item, addr in island_visibility_addr.items():
        if item_count(ctx, item):
            write_list.append((addr, [0x1], "Main RAM"))
        else:
            write_list.append((addr, [0], "Main RAM"))
    await bizhawk.write(ctx.bizhawk_ctx, write_list)

async def map_mode(client: "PhantomHourglassClient", ctx: "BizHawkClientContext", read_list):
    # Check options
    if ctx.slot_data.get("map_warp_options", 0) == 0 and False: return

    if client.warp_to_start_flag:
        client.warp_to_start_flag = False
        logger.info(f"Canceled warp to start due to opening map warp menu")

    # read transition mode
    transition_mode = await read_memory_value(ctx, 0x1BA700, silent=True)

    client.visited_scenes |= set(get_stored_data(ctx, 'ph_visited_scenes', []))

    if client.pen_mode_pointer: # Do fun stuff with the pen and eraser buttons
        current_pen_mode = await read_memory_value(ctx, client.pen_mode_pointer, silent=True)
        if current_pen_mode in [0x18, 0x19] and current_pen_mode != client.last_pen_mode:
            if current_pen_mode == 0x19:
                def quick_entrance_log(key):
                    logger.info(f"Current storage {key}:")
                    for e in get_stored_data(ctx, key, []):
                        logger.info(f"  {entrance_id_to_entrance[e].name}")

                quick_entrance_log("ph_checked_entrances")
                quick_entrance_log("ph_disconnect_entrances")
                quick_entrance_log("ph_traversed_entrances")
                logger.info(f"local traverses: {client.visited_entrances}")

                logger.info(f"Currently stored scenes:")
                for i in set(get_stored_data(ctx, 'ph_visited_scenes', [])) | client.visited_scenes:
                    logger.info(f"  {hex(i)}")

            client.last_pen_mode = current_pen_mode


    if not transition_mode: return

    # Enter map mode
    if transition_mode == 6:
        client.map_mode = True
        if client.map_warp:
            client.map_warp = None
            logger.info(f"Canceled map warp")
        if ctx.slot_data["map_warp_options"] == 1:
            await set_visibility(ctx)
    if not client.map_mode: return

    # Exit map mode when appropriate
    if transition_mode == 0x1E:
        client.map_mode = False
        print(f"Exiting Map Menu")
    elif client.map_warp_reselector and transition_mode in transition_lookup:
        print(f"bool map warp {client.map_warp} {bool(client.map_warp)}")
        client.map_warp_reselector = False

        # Setup pen mode stuff
        pen_mode_pointer = await read_memory_value(ctx, 0x1CCCEC, silent=True, size=4)
        print(f"pen mode pointer {hex(pen_mode_pointer)}")
        client.pen_mode_pointer = pen_mode_pointer+25*4-0x2000000
        if client.pen_mode_pointer < 0xFFFFFF:
            client.last_pen_mode = await read_memory_value(ctx, client.pen_mode_pointer)
        else: client.pen_mode_pointer = None

        # Do detailed warp instructions
        if check_any_er(ctx):
            print(f"Seed has ER. Checking ER conditions")
            if not ctx.slot_data["shuffle_overworld_transitions"]:
                # No OW er: any island access allows warping
                client.map_warp = check_visited_scenes(client, ctx, transition_mode,
                                                       no_ow_er_lookup, safe_entrances_no_ow)
            else:
                # other: require port quadrant access
                client.map_warp = check_visited_scenes(client, ctx, transition_mode,
                                                       ow_er_lookup, safe_entrances_ow)
        else:
            client.map_warp = ENTRANCES[transition_lookup[transition_mode]]

        # Failure conditions
        if not client.map_warp:
            land_type = "ocean" if transition_mode in range(0x1f, 0x23) else "island's port"
            if ctx.slot_data["shuffle_caves"] and not ctx.slot_data["shuffle_ports"] and transition_mode == 0x32:
                logger.info(f"You can't warp to uncharted with these settings, cause i don't know if you have boat access.")
            else:
                logger.info(f"You have yet to visit that {land_type}")
        elif client.current_scene in ow_er_lookup[transition_mode]:
            logger.info(f"You are already in that scene, you can't warp there")
            client.map_warp = None
        elif ctx.slot_data["map_warp_options"] == 1:
            if transition_mode in warp_item_lookup and not item_count(ctx, warp_item_lookup[transition_mode]):
                client.map_warp = None
                logger.info(f"Missing warp unlock item for that island")
        elif transition_mode in range(0x1f, 0x23) and ctx.slot_data["boat_requires_sea_chart"]:
            # If warping to sea, check sea chart reqs
            trans_mode_to_chart = {0x1F: "SW Sea Chart", 0x20: "SE Sea Chart", 0x21: "NW Sea Chart", 0x22: "NE Sea Chart"}
            if not item_count(ctx, trans_mode_to_chart[transition_mode]):
                client.map_warp = None
                logger.info(f"You do not have the correct sea chart")

        # Success
        if client.map_warp:
            logger.info(f"Selected map warp destination: {transition_lookup[transition_mode]}")
            # Store connection for ut glp
            await client.store_data(ctx, storage_key(ctx, "ph_ut_events"), [ut_event_lookup[transition_mode]])

    elif transition_mode == 0x17:  # Return to big map, reset selector
        client.map_warp_reselector = True
