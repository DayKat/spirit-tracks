from BaseClasses import MultiWorld, Item
from .data import LOCATIONS_DATA
from .data.LogicPredicates import *
from .Options import SpiritTracksOptions


def make_overworld_logic(player: int, origin_name: str, options: SpiritTracksOptions):
    overworld_logic = [



        # ====== Outset Village ==============

        #[region 1, region 2, two-directional, logic requirements],
        ["outset village", "outset village rocks", False, None],
        #["outset village", "outset village stamp book", False, None],
        ["outset village", "outset village stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["outset village", "outset village bees", False, None],
        ["outset village", "forest realm", False, lambda state: st_has_glyph(state, player, "Forest")],

        # # ======== Castle Town =========

        ["forest realm", "castle town", False, None],
        ["castle town", "castle town stamp station", False, lambda state: (st_has_stamp_book(state, player) and st_has_bombs(state, player))],
        ["castle town", "castle town L wall chest", False, lambda state: (st_has_bombs(state, player))],
        ["castle town", "castle town R wall chest", False, lambda state: (st_has_bombs(state, player))],
        ["castle town", "castle town minigame roof", False, lambda state: (st_has_bombs(state, player) and st_has_birds_song(state, player))],
        ["castle town", "castle town ramp house chest", False, lambda state: (st_has_bombs(state, player) and st_has_birds_song(state, player))],
        ["castle town", "castle town empty house roof", False, lambda state: (st_has_bombs(state, player) and st_has_birds_song(state, player))],

        # # ======== Hyrule Castle =========

        ["castle town", "hyrule castle", False, None],
        ["hyrule castle", "hyrule castle nw chest", False, None],
        ["hyrule castle", "hyrule castle 2f indoors chest", False, None],
        ["hyrule castle", "hyrule castle 1f back chest", False, None],

        # # ======== ToS Tunnel =========

        ["hyrule castle", "tower tunnel", False, None],
        ["tower tunnel", "tower tunnel block chest", False, lambda state: (st_has_damage(state, player))],
        ["tower tunnel", "tower tunnel 2f chest", False, lambda state: (st_has_damage(state, player) and st_has_small_keys(state, player, "Tunnel to ToS", 1))],

        # # ========== ToS ===================

        ["forest realm", "tos", False, None],
        ["tos", "tos section 1", False, None],
        ["tos section 1", "tos 1f chest", False, lambda state: (st_has_bow(state, player) or st_has_boomerang(state, player))],
        ["tos section 1", "tos 2f raised chest", False, lambda state: (st_has_whirlwind(state, player) and st_has_sword(state, player))],
        ["tos section 1", "tos 2f whirlwind", False, lambda state: (st_has_whirlwind(state, player) and st_has_sword(state, player))],
        ["tos section 1", "tos 2f bomb wall", False, lambda state: (st_has_bombs(state, player) and st_has_sword(state, player))],
        ["tos section 1", "tos 3f rail map", False, lambda state: st_has_sword(state, player)],
        ["tos 3f rail map", "goal_forest_glyph", False, None],

        # # ============ Shops ====================

        # ["mercay island", "shop power gem", False, lambda state: st_can_buy_gem(state, player)],
        # ["mercay island", "shop quiver", False, lambda state: st_can_buy_quiver(state, player)],
        # ["mercay island", "shop bombchu bag", False, lambda state: st_can_buy_chu_bag(state, player)],
        # ["mercay island", "shop heart container", False, lambda state: st_can_buy_heart(state, player)],

        # # ======== Mayscore =========

        ["forest realm", "mayscore", False, None],
        ["mayscore", "mayscore stamp station", False, lambda state: st_has_stamp_book(state, player)],
        #["mayscore", "mayscore whip race bomb bag", False, lambda state: st_has_whip(state, player)],
        #["mayscore", "mayscore whip race heart container", False, lambda state: st_has_whip(state, player)],
        ["mayscore", "mayscore whip chest", False, lambda state: st_has_whip(state, player)],

        # # ======== Forest Sanctuary =========

        ["forest realm", "fos", False, None],
        ["fos", "fos stamp station", False, lambda state: st_has_stamp_book(state, player)],
        #["fos", "fos song statue", False, lambda state: st_has_spirit_flute(state, player)],
        #["fos", "fos gage", False, lambda state: st_has_spirit_flute(state, player)],
        ["fos", "fos chest", False, lambda state: st_has_whirlwind(state, player) or (st_has_birds_song(state, player) and st_has_spirit_flute(state, player))],

        # # ======== Forest Temple =========

        ["forest realm", "fot", False, lambda state: st_has_temple_tracks(state, player, "Forest")],
        ["fot", "fot stamp station", False, lambda state: st_has_stamp_book(state, player) and st_has_whirlwind(state, player)],
        #["fot", "fot song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["fot", "fot 1f enemy chest", False, lambda state: st_has_damage(state, player)],
        ["fot 1f enemy chest", "fot 1f key", False, lambda state: st_has_whirlwind(state, player)],
        ["fot 1f enemy chest", "fot 2f enemy chest", False, None],
        ["fot 1f enemy chest", "fot 2f poison chest", False, lambda state: st_has_whirlwind(state, player)],
        ["fot", "fot 1f switch chest", False, lambda state: st_has_whirlwind(state, player)],
        ["fot", "fot 3f chestnut chest", False, lambda state: st_has_damage(state, player) and st_has_range(state, player) and st_has_small_keys(state, player, "Forest Temple", 2)],
        ["fot", "fot 3f se chest", False, lambda state: st_has_damage(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Forest Temple", 2)],
       #["fot", "fot 3f boss key chest", False, lambda state: st_has_damage(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Forest Temple",2)],
        ["fot", "fot heart container", False, lambda state: st_has_damage(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Forest Temple",2)],
        ["fot", "fot stagnox", False, lambda state: st_has_damage(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Forest Temple",2)],
        ["fot stagnox", "goal_stagnox", False, None],

        # # ============ Trading Post =============

        ["forest realm", "trading post", False, lambda state: st_has_glyph(state, player, "Ocean")],
        #["trading post", "trading post discovery song statue", False, lambda state: st_has_spirit_flute(state, player)],
        #["trading post", "trading post light song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["trading post", "trading post chest", False, lambda state: st_has_boomerang(state, player) and st_has_discovery_song(state, player)],
        ["trading post", "trading post stamp station", False, lambda state: st_has_bombs(state, player) and st_has_stamp_book(state, player)],

        # # ========== Rabbitland Rescue ========

        ["forest realm", "rabbitland", False, lambda state: st_has_glyph(state, player, "Snow")],
        ["rabbitland", "rabbitland chest", False, None],
        ["rabbitland", "rabbitland net", False, None],

        # # ============ SW Ocean =================


        # # Goal stuff
        # ["mercay island", "beat required dungeons", False, lambda state: st_beat_required_dungeons(state, player)],
        # ["sw ocean east", "bellumbeck", False, lambda state: st_bellumbeck_quick_finish(state, player)],
        # ["bellumbeck", "beat bellumbeck", False, lambda state: st_can_beat_bellumbeck(state, player)],
        # ["beat bellumbeck", "goal", False, lambda state: st_option_goal_bellum(state, player)],
        # ["totok midway", "goal", False, lambda state: st_option_goal_midway(state, player)]

    ]

    return overworld_logic


def is_item(item: Item, player: int, item_name: str):
    return item.player == player and item.name == item_name


def create_connections(multiworld: MultiWorld, player: int, origin_name: str, options):
    all_logic = [
        make_overworld_logic(player, origin_name, options)
    ]

    # Create connections
    for logic_array in all_logic:
        for entrance_desc in logic_array:
            region_1 = multiworld.get_region(entrance_desc[0], player)
            region_2 = multiworld.get_region(entrance_desc[1], player)
            is_two_way = entrance_desc[2]
            rule = entrance_desc[3]

            region_1.connect(region_2, None, rule)
            if is_two_way:
                region_2.connect(region_1, None, rule)
