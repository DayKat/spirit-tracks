from typing import TYPE_CHECKING
from .DSZeldaClient.DSZeldaClient import read_memory_value, logger
from .data.Entrances import ENTRANCES
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

async def map_mode(client: "PhantomHourglassClient", ctx: "BizHawkClientContext", read_list):
    # Check options
    if ctx.slot_data.get("map_warp_options", 0) == 0 and False: return

    if client.warp_to_start_flag:
        client.warp_to_start_flag = False
        logger.info(f"Canceled warp to start due to opening map warp menu")

    # read transition mode
    transition_mode = await read_memory_value(ctx, 0x1BA700, silent=True)

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
        client.map_warp = ENTRANCES[transition_lookup[transition_mode]]
        logger.info(f"Selected map warp destination: {transition_lookup[transition_mode]}")
        print(f"bool map warp {client.map_warp} {bool(client.map_warp)}")
        client.map_warp_reselector = False
        # Do detailed warp instructions
    elif transition_mode == 0x17:
        client.map_warp_reselector = True
