from BaseClasses import MultiWorld, Item
from .data import LOCATIONS_DATA
from .data.LogicPredicates import *
from .Options import SpiritTracksOptions


def make_overworld_logic(player: int, origin_name: str, options: SpiritTracksOptions):
    overworld_logic = [

        # ====== Outset Village ==============

        #[region 1, region 2, two-directional, logic requirements],
        ["outset village", "outset village rocks", False, None],
        ["outset village", "outset village stamp book", False, lambda state: st_has_glyph(state, player, "Forest") and st_has_glyph(state, player, "Snow")],
        ["outset village", "outset village stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["outset village", "outset village bees", False, None],
        ["outset village", "outset village right tree", False, lambda state: st_has_spirit_flute(state, player) and st_has_discovery_song(state, player)],
        ["outset village", "outset village left tree", False, lambda state: st_has_spirit_flute(state, player) and st_has_discovery_song(state, player)],
        ["outset village", "forest realm", False, lambda state: st_has_glyph(state, player, "Forest") and st_has_cannon(state, player)],

        # # ======== Castle Town =========

        ["forest realm", "castle town", False, None],
        ["castle town", "castle town stamp station", False, lambda state: (st_has_stamp_book(state, player) and st_has_bombs(state, player))],
        ["castle town", "castle town L wall chest", False, lambda state: (st_has_bombs(state, player))],
        ["castle town", "castle town R wall chest", False, lambda state: (st_has_bombs(state, player))],
        #TODO can also use whirlwind for cucco if chased
        ["castle town", "castle town minigame roof", False, lambda state: (st_has_bombs(state, player) and st_has_birds_song(state, player) and st_has_spirit_flute(state, player))],
        ["castle town", "castle town ramp house chest", False, lambda state: (st_has_bombs(state, player) and st_has_birds_song(state, player) and st_has_spirit_flute(state, player))],
        ["castle town", "castle town empty house roof", False, lambda state: (st_has_bombs(state, player) and st_has_birds_song(state, player) and st_has_spirit_flute(state, player))],

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
        ["fos", "fos song statue", False, lambda state: st_has_spirit_flute(state, player)],
        #["fos", "fos gage", False, lambda state: st_has_spirit_flute(state, player)],
        ["fos", "fos chest", False, lambda state: st_has_whirlwind(state, player) or (st_has_birds_song(state, player) and st_has_spirit_flute(state, player))],

        # # ======== Wooded Temple ========= #TODO stamp stand + chest + poison chest + 3f se can damage boost

        ["forest realm", "wt", False, lambda state: st_has_temple_tracks(state, player, "Wooded")],
        ["wt", "wt stamp station", False, lambda state: st_has_stamp_book(state, player) and st_has_whirlwind(state, player)],
        ["wt", "wt song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["wt", "wt 1f enemy chest", False, lambda state: st_has_damage(state, player)],
        ["wt 1f enemy chest", "wt 1f key", False, lambda state: st_has_whirlwind(state, player)],
        ["wt 1f enemy chest", "wt 2f enemy chest", False, None],
        ["wt 1f enemy chest", "wt 2f poison chest", False, lambda state: st_has_whirlwind(state, player)],
        ["wt", "wt 1f switch chest", False, lambda state: st_has_whirlwind(state, player)],
        ["wt", "wt 3f chestnut chest", False, lambda state: st_can_kill_bubble(state, player) and st_has_range(state, player) and st_has_small_keys(state, player, "Wooded Temple", 1)],
        ["wt", "wt 3f se chest", False, lambda state: st_has_whirlwind(state, player) and st_can_kill_bubble(state, player) and st_has_small_keys(state, player,"Wooded Temple", 2)],
       #["wt", "wt 3f boss key chest", False, lambda state: st_has_damage(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Wooded Temple",2)],
        ["wt", "wt heart container", False, lambda state: st_has_sword(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Wooded Temple",2)],
        ["wt", "wt stagnox", False, lambda state: st_has_sword(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Wooded Temple",2)],
        ["wt stagnox", "goal_stagnox", False, None],

        # # ============ Trading Post =============

        ["forest realm", "trading post", False, lambda state: st_has_glyph(state, player, "Ocean") and st_has_cannon(state, player)],
        #["trading post", "trading post discovery song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["trading post", "trading post light song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["trading post", "trading post chest", False, lambda state: st_has_bombs(state, player) and (st_has_boomerang(state, player) or st_has_bow(state, player)) and st_has_discovery_song(state, player) and st_has_light_song(state, player) and st_has_spirit_flute(state, player)],
        ["trading post", "trading post stamp station", False, lambda state: st_has_bombs(state, player) and st_has_stamp_book(state, player)],

        # # ========== Rabbit Haven ========

        ["forest realm", "rabbit haven", False, lambda state: st_has_glyph(state, player, "Snow") and st_has_temple_tracks(state, player, "Wooded") and st_has_cannon(state, player)],
        ["rabbit haven", "rabbit haven chest", False, None],
        ["rabbit haven", "rabbit haven net", False, None],

        # # ============ SW Ocean =================


        # # Goal stuff
        # ["mercay island", "beat required dungeons", False, lambda state: st_beat_required_dungeons(state, player)],
        # ["sw ocean east", "bellumbeck", False, lambda state: st_bellumbeck_quick_finish(state, player)],
        # ["bellumbeck", "beat bellumbeck", False, lambda state: st_can_beat_bellumbeck(state, player)],
        # ["beat bellumbeck", "goal", False, lambda state: st_option_goal_bellum(state, player)],
        # ["totok midway", "goal", False, lambda state: st_option_goal_midway(state, player)]

    ]

    return overworld_logic

# TODO require cannon before non-forest glyph
# def make_item_logic(player: int, origin_name: str, options: SpiritTracksOptions):
#     item_logic = [
#         ["Cannon", ["Snow Glyph", "Ocean Glyph", "Fire Glyph"]
#     ]]
#     return item_logic

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
