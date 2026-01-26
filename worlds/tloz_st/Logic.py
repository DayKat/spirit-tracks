from BaseClasses import MultiWorld, Item
from .data import LOCATIONS_DATA
from .data.LogicPredicates import *
from .Options import SpiritTracksOptions


def make_overworld_logic(player: int, origin_name: str, options: SpiritTracksOptions):
    overworld_logic = [

        # ====== Outset Village ==============

        #[region 1, region 2, two-directional, logic requirements],
        ["outset village", "outset village rocks", False, None],
        ["outset village", "outset village stamp book", False, lambda state: st_has_glyph(state, player, "Forest") and st_has_glyph(state, player, "Snow") and st_has_cannon(state, player)],
        ["outset village", "outset village stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["outset village", "outset village bees", False, None],
        ["outset village", "outset village right tree", False, lambda state: st_has_spirit_flute(state, player) and st_has_discovery_song(state, player)],
        ["outset village", "outset village left tree", False, lambda state: st_has_spirit_flute(state, player) and st_has_discovery_song(state, player)],
        ["outset village", "forest realm", False, lambda state: st_has_glyph(state, player, "Forest") and st_has_cannon(state, player)],

        # ========= Forest Realm ==========

        ["forest realm", "forest realm se portal track", False, lambda state: st_has_glyph(state, player, "Snow") and st_has_misc_tracks(state, player, "Forest Realm SE Portal")],
        ["forest realm", "w castle town rabbit", False, lambda state: st_has_net(state, player)],
        ["forest realm", "forest ocean shortcut rabbit", False, lambda state: st_has_net(state, player) and st_has_misc_tracks(state, player, "Forest Realm Ocean Shortcut")],
        ["forest realm", "e mayscore rabbit", False, lambda state: st_has_misc_tracks(state, player, "E Mayscore Bridge") and st_has_net(state, player)],
        ["forest realm", "sw trading post rabbit", False, lambda state: st_has_misc_tracks(state, player, "Forest Realm SE Portal Tracks") and st_has_net(state, player)],
        ["forest realm", "e outset rabbit", False, lambda state: st_has_net(state, player)],
        ["forest realm", "sw rabbit haven rabbit", False, lambda state: st_has_misc_tracks(state, player, "W Forest Realm Tracks") and (st_has_temple_tracks(state, player, "Wooded Temple") or st_has_glyph(state, player, "Snow")) and st_has_net(state, player)],
        ["forest realm", "wt rabbit", False, lambda state: st_has_temple_tracks(state, player, "Wooded") and  st_has_net(state, player)],
        ["forest realm", "nr rabbit haven rabbit", False, lambda state: st_has_glyph(state, player, "Snow") and st_has_net(state, player)],
        ["forest realm", "forest after bridge rabbit", False, lambda state: st_has_misc_tracks(state, player, "E Mayscore Bridge") and st_has_net(state, player)],
        ["forest realm", "s rabbit haven rabbit", False, lambda state: st_has_misc_tracks(state, player, "W Forest Realm Tracks") and (st_has_temple_tracks(state, player, "Wooded Temple") or st_has_glyph(state, player,"Snow")) and st_has_net(state, player)],

        # # ======== Castle Town =========

        ["forest realm", "castle town", False, None],
        ["castle town", "castle town stamp station", False, lambda state: (st_has_stamp_book(state, player) and st_has_bombs(state, player))],
        ["castle town", "castle town L wall chest", False, lambda state: (st_has_bombs(state, player))],
        ["castle town", "castle town R wall chest", False, lambda state: (st_has_bombs(state, player))],
        ["castle town", "castle town minigame roof", False, lambda state: st_castle_town_cuccos(state, player)],
        ["castle town", "castle town ramp house chest", False, lambda state: st_castle_town_cuccos(state, player)],
        ["castle town", "castle town empty house roof", False, lambda state: st_castle_town_cuccos(state, player)],

        # # ======== Hyrule Castle =========

        ["castle town", "hyrule castle", False, None],
        ["hyrule castle", "hyrule castle nw chest", False, None],
        ["hyrule castle", "hyrule castle 2f indoors chest", False, None],
        ["hyrule castle", "hyrule castle 1f back chest", False, None],

        # # ======== ToS Tunnel =========

        ["hyrule castle", "tower tunnel", False, None],
        ["tower tunnel", "tower tunnel block chest", False, lambda state: (st_has_damage(state, player) or st_option_hard_logic(state, player))],
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
        ["tos", "tos section 2", False, lambda state: (st_has_source(state, player, "Forest"))],
        ["tos section 2", "tos 4f central chest", False, None],
        ["tos section 2", "tos 5f island chest", False, lambda state: st_has_sword(state, player) and st_has_whirlwind(state, player)],
        ["tos 5f island chest", "tos 5f spinnit key", False, lambda state: st_has_whirlwind(state, player)],
        ["tos 5f spinnit key", "tos 5f secret chest", False, lambda state: st_has_bombs(state, player) and st_has_boomerang(state, player)],
        ["tos 5f spinnit key", "tos 4f ne chest", False, lambda state: st_has_bombs(state, player) and st_has_boomerang(state, player)],
        ["tos 5f spinnit key", "tos 6f ne chest 1", False, lambda state: st_has_boomerang(state, player)],
        ["tos 5f spinnit key", "tos 6f ne chest 2", False, lambda state: st_has_boomerang(state, player)],
        ["tos 5f spinnit key", "tos 6f ne chest 3", False, lambda state: st_has_boomerang(state, player)],
        ["tos 5f spinnit key", "tos 6f ne big chest", False, lambda state: st_has_boomerang(state, player)],
        ["tos 5f spinnit key", "tos 6f key", False, lambda state: st_has_small_keys(state, player, "ToS", 1)],
        ["tos 6f key", "tos 7f rail map", False, lambda state: st_has_small_keys(state, player, "ToS", 2)],
        ["tos 7f rail map", "goal_snow_glyph", False, None],

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

        # # ======== Wooded Temple =========

        ["forest realm", "wt", False, lambda state: st_has_temple_tracks(state, player, "Wooded") or st_has_source(state, player, "Forest")],
        ["wt", "wt stamp station", False, lambda state: st_has_stamp_book(state, player) and (st_has_whirlwind(state, player) or st_option_hard_logic(state, player))],
        ["wt", "wt song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["wt", "wt 1f enemy chest", False, lambda state: st_has_damage(state, player)],
        ["wt 1f enemy chest", "wt 1f key", False, lambda state: st_has_whirlwind(state, player)],
        ["wt 1f enemy chest", "wt 2f enemy chest", False, None],
        ["wt 1f enemy chest", "wt 2f poison chest", False, lambda state: st_has_whirlwind(state, player) or st_option_hard_logic(state, player)],
        ["wt", "wt 1f switch chest", False, lambda state: st_has_whirlwind(state, player) or st_option_hard_logic(state, player)],
        ["wt", "wt 3f chestnut chest", False, lambda state: st_can_kill_bubble(state, player) and st_has_range(state, player) and st_has_small_keys(state, player, "Wooded Temple", 1)],
        ["wt", "wt 3f se chest", False, lambda state: st_has_whirlwind(state, player) and st_can_kill_bubble(state, player) and st_has_small_keys(state, player,"Wooded Temple", 2)],
       #["wt", "wt 3f boss key chest", False, lambda state: st_has_damage(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Wooded Temple",2)],
        #["wt", "wt heart container", False, lambda state: st_has_sword(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Wooded Temple",2)],
        ["wt", "wt stagnox", False, lambda state: st_has_sword(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Wooded Temple",2)],
        ["wt stagnox", "goal_stagnox", False, None],

        # # ============ Trading Post =============

        ["forest realm", "trading post", False, lambda state: st_has_glyph(state, player, "Ocean") and st_has_cannon(state, player)],
        #["trading post", "trading post discovery song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["trading post", "trading post light song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["trading post", "trading post chest", False, lambda state: st_has_bombs(state, player) and (st_has_boomerang(state, player) or st_has_bow(state, player)) and st_has_discovery_song(state, player) and st_has_light_song(state, player) and st_has_spirit_flute(state, player)],
        ["trading post", "trading post stamp station", False, lambda state: st_has_bombs(state, player) and st_has_stamp_book(state, player)],

        # # ========== Rabbit Haven ========

        ["forest realm", "rabbit haven", False, lambda state: st_has_glyph(state, player, "Snow")],
        ["rabbit haven", "rabbit haven chest", False, None],
        ["rabbit haven", "rabbit haven net", False, None],
        ["rabbit haven", "rabbit haven 5 rabbits", False, lambda state: st_has_total_rabbits(state, player, 5)],
        ["rabbit haven", "rabbit haven 10 forest rabbits", False, lambda state: st_has_forest_rabbits(state, player, 10)],
        ["rabbit haven", "rabbit haven 10 snow rabbits", False, lambda state: st_has_snow_rabbits(state, player, 10)],

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # # ============ Snow Realm ===============

        ["forest realm", "snow realm", False, lambda state: st_has_glyph(state, player, "Snow")],
        ["snow realm", "snow realm post song", False, lambda state: st_has_temple_tracks(state, player, "Blizzard")],
        ["snow realm post song", "ne blizzard rabbit", False, lambda state: st_has_net(state, player)],
        ["snow realm post song", "se blizzard rabbit", False, lambda state: st_has_net(state, player)],
        ["snow realm", "w anouki village rabbit", False, lambda state: st_has_net(state, player)],
        ["snow realm post song", "sw blizzard rabbit", False, lambda state: st_has_net(state, player)],
        ["snow realm", "e anouki village rabbit", False, lambda state: st_has_net(state, player)],
        ["snow realm post song", "snowdrift station rabbit", False, lambda state: st_has_misc_tracks(state, player, "Snowdrift Station") and st_has_net(state, player)],
        ["snow realm post song", "w icyspring rabbit", False, lambda state: st_has_misc_tracks(state, player, "N Icy Spring") and st_has_net(state, player)],
        ["snow realm post song", "n icyspring rabbit", False, lambda state: st_has_misc_tracks(state, player, "N Icy Spring") and st_has_net(state, player)],
        ["snow realm post song", "nw blizzard rabbit", False, lambda state: st_has_net(state, player)],
        ["snow realm post song", "central blizzard rabbit", False, lambda state: st_has_net(state, player)],

        # ======== Anouki Village ========

        ["snow realm", "anouki village", False, None],
        ["anouki village", "anouki village stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["anouki village", "anouki village discovery song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["anouki village", "anouki village song statue chest", False, lambda state: st_has_spirit_flute(state, player)],
        ["anouki village", "anouki village bomb cave chest", False, lambda state: st_has_bombs(state, player)],
        ["anouki village", "anouki village lake chest", False, lambda state: st_has_boomerang(state, player)],

        # =========== Snow Sanctuary ==========

        ["anouki village", "ss", False, None],
        ["ss", "ss stamp station", False, lambda state: st_has_stamp_book(state, player)],

        ## ========== Blizzard Temple =========

        ["snow realm", "bt", False, lambda state: st_has_temple_tracks(state, player, 'Blizzard') or st_has_source(state, player, 'Snow')],
        ["bt", "bt b1 se chest", False, lambda state: st_can_ring_bell(state, player) and st_has_whirlwind(state, player) and (st_has_range(state, player) or st_has_whip(state, player) or st_has_bombs(state, player))],
        ["bt b1 se chest", "bt b1 e enemy chest", False, None],
        ["bt b1 se chest", "bt b1 ne enemy chest", False, lambda state: st_can_kill_bubble(state, player)],
        ["bt b1 se chest", "bt 1f ne chest", False, lambda state: st_has_boomerang(state, player) or (st_has_whip(state, player) and st_has_whirlwind(state, player))],
        ["bt 1f ne chest", "bt b1 sw chest", False, lambda state: st_has_boomerang(state, player)],
        ["bt 1f ne chest", "bt stamp station", False, lambda state: st_has_stamp_book(state, player) and st_has_small_keys(state, player, "Blizzard Temple", 1)],
        ["bt 1f ne chest", "bt b1 nw enemy chest", False, lambda state: st_has_small_keys(state, player, "Blizzard Temple", 1)],
        ["bt b1 nw enemy chest", "bt 1f nw chest", False, None],
        ["bt b1 nw enemy chest", "bt 1f torch chest", False, None],
        ["bt b1 nw enemy chest", "bt heart container", False, lambda state: st_has_sword(state, player)],
        ["bt b1 nw enemy chest", "bt fraaz", False, lambda state: st_has_sword(state, player)],
        ["bt fraaz", "goal_fraaz", False, None],

        # ========== Icy Spring ==========

        ["snow realm post song", "icyspring", False, None],
        ["icyspring", "icyspring stamp station", False, lambda state: st_has_stamp_book(state, player) and st_has_boomerang(state, player)],
        ["icyspring", "icyspring whip chest", False, lambda state: st_has_whip(state, player)],

        # ============ Snowdrift Station =========

        ["snow realm post song", "snowdrift", False, lambda state: st_has_misc_tracks(state, player, "Snowdrift Station") and st_has_source(state, player, 'Snow')],
        ["snowdrift", "snowdrift reward", False, lambda state: st_has_boomerang(state, player) and st_has_shield(state, player)],

        # ========== Slippery Station ==========
        ["snow realm post song", "slippery", False, lambda state: st_has_misc_tracks(state, player, "Slippery Station") and (st_has_source(state, player, 'Snow') or st_has_misc_tracks(state, player, "N Icy Spring"))],
        ["slippery", "slippery amateur", False, None],
        ["slippery", "slippery pro", False, None],
        ["slippery", "slippery champion", False, lambda state: st_option_hard_logic(state, player)],

        # ========== Bridge Worker's Home =======
        ["snow realm", "bridge workers", False, lambda state: st_has_source(state, player, 'Snow')],
        ["bridge workers", "bridge workers chest", False, lambda state: st_has_spirit_flute(state, player) and st_has_discovery_song(state, player)],

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
