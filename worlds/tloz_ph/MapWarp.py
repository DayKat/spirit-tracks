from typing import TYPE_CHECKING
from .DSZeldaClient.DSZeldaClient import read_memory_value, logger, item_count
from .data.Entrances import ENTRANCES, entrance_id_to_entrance
import logging

if TYPE_CHECKING:
    from .Client import PhantomHourglassClient
    from worlds._bizhawk.context import BizHawkClientContext


transition_lookup = {
    0x1F: "Ocean SW Cannon",
    0x20: "Ocean SE Harrow",
    0x21: "Ocean NW Uncharted",
    0x22: "Ocean NE Maze",
    0x23: "Mercay SE Boat",
    0x24: "Molida Boat",
    0x25: "Ember Boat",
    0x26: "Gust Boat",
    0x27: "Frost Boat",
    0x28: "Goron Boat",
    0x29: "Ruins Boat",
    0x2A: "Cannon Boat",
    0x2B: "Dee Ess Boat",
    0x2C: "Bannan Boat",
    0x2D: "IotD Boat",
    0x2E: "Zauz Boat",
    0x2F: "Spirit Boat",
    0x30: "Harrow Boat",
    0x31: "Maze Boat",
    0x32: "Uncharted Boat",
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
    0x2A: [0x1300],
    0x2B: [0x1B00],
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
    0x2A: [0x1300],
    0x2B: [0x1B00],
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
           "Board Ghost Ship"],
    0x22: ["Ocean NE Maze",
           "Ocean NE IotD"],
    0x2C: ["Bannan Boat",
           "Bannan West Cave",
           "Bannan West Hut"],
    0x32: ["Uncharted Boat"],
}

safe_entrances_ow = safe_entrances_common | {
    0x26: ["Gust Boat", "Gust Secret Cave", "Gust Cave West", "Gust Cave East",
           "Gust South Temple Road North", "Gust South Above Temple North"],
    0x29: ["Ruins Boat", "Ruins SW Upper Maze North", "Ruins SW Port Cliff North",
           "Ruins SW East", "Ruins SW Port Cave", "Ruins SW Cliff Cave"],
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
    if not ctx.slot_data["shuffle_ports"]:  # Entrances only exist if things are actually randomized, this solves most cases
        if not (ctx.slot_data["shuffle_caves"] and trans_value in [0x2C, 0x32]):
            return True

    visited_entrances = client.visited_entrances
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

async def map_mode(client: "PhantomHourglassClient", ctx: "BizHawkClientContext", read_list):
    # Check options
    if ctx.slot_data.get("map_warp_options", 0) == 0 and False: return

    if client.warp_to_start_flag:
        client.warp_to_start_flag = False
        logger.info(f"Canceled warp to start due to opening map warp menu")

    # read transition mode
    transition_mode = await read_memory_value(ctx, 0x1BA700, silent=True)
    if not transition_mode: return

    # Enter map mode
    if transition_mode == 6:
        client.map_mode = True
        if client.map_warp:
            client.map_warp = None
            logger.info(f"Canceled map warp")
    if not client.map_mode: return

    # Exit map mode when appropriate
    if transition_mode == 0x1E:
        client.map_mode = False
        print(f"Exiting Map Menu")
    elif client.map_warp_reselector and transition_mode in transition_lookup:
        logger.info(f"Selected map warp destination: {transition_lookup[transition_mode]}")
        print(f"bool map warp {client.map_warp} {bool(client.map_warp)}")
        client.map_warp_reselector = False

        # Setup pen mode stuff
        client.pen_mode_pointer = (await read_memory_value(ctx, 0x1CCCEC, silent=True))+26*4-0x2000000
        client.last_pen_mode = await read_memory_value(ctx, client.pen_mode_pointer)

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
            logger.info(f"You have yet to visit that island")
        elif client.current_scene in ow_er_lookup[client.map_warp.stage]:
            logger.info(f"You are already in that scene, you can't warp there")
            client.map_warp = None
        elif transition_mode in range(0x1f, 0x23) and ctx.slot_data["boat_requires_sea_chart"]:
            # If warping to sea, check sea chart reqs
            trans_mode_to_chart = {0x1F: "SW Sea Chart", 0x20: "SE Sea Chart", 0x21: "NW Sea Chart", 0x22: "NE Sea Chart"}
            if not item_count(ctx, trans_mode_to_chart[transition_mode]):
                client.map_warp = None
                logger.info(f"You do not have the correct sea chart")

    elif transition_mode == 0x17:  # Return to big map, reset selector
        client.map_warp_reselector = True
    elif client.pen_mode_pointer: # Do fun stuff with the pen and eraser buttons
        current_pen_mode = await read_memory_value(ctx, client.pen_mode_pointer)
        print(f"Current pen mode")
        if current_pen_mode in [0x18, 0x19] and current_pen_mode != client.last_pen_mode:
            print(f"Changed Pen Mode")
            if current_pen_mode == 0x19:
                logger.info(f"Currently visited entrances")
                for i in client.visited_entrances:
                    logger.info(f"\t{entrance_id_to_entrance[i].name}")

            client.last_pen_mode = current_pen_mode
