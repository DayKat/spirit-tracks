from BaseClasses import MultiWorld, Item
from .data import LOCATIONS_DATA
from .data.LogicPredicates import *
from .Options import SpiritTracksOptions


def make_overworld_logic(player: int, origin_name: str, options: SpiritTracksOptions):
    overworld_logic = [

        # ====== Outset Village ==============

        #[region 1, region 2, two-directional, logic requirements],
        ["outset village", "outset village stamp book", False, lambda state: st_has_glyph(state, player, "Forest") and st_has_glyph(state, player, "Snow") and st_has_cannon(state, player)],
        ["outset village", "outset village stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["outset village", "outset village trees", False, lambda state: st_has_discovery_song(state, player)],
        ["outset village", "forest realm", False, lambda state: st_has_glyph(state, player, "Forest") and st_has_cannon(state, player)],

        # ========= Forest Realm ==========

        ["forest realm", "forest realm se portal track", False, lambda state: st_has_misc_tracks(state, player, "Forest Realm SE Portal")],
        ["forest realm", "forest realm rabbits", False, lambda state: st_has_net(state, player)],

        ["forest realm rabbits", "forest ocean shortcut rabbit", False, lambda state: st_has_misc_tracks(state, player, "Forest Realm Ocean Shortcut")],
        ["forest realm rabbits", "e mayscore rabbits", False, lambda state: st_has_misc_tracks(state, player, "E Mayscore Bridge")],
        ["forest realm se portal track", "sw trading post rabbit", False, lambda state: st_has_net(state, player)],
        ["forest realm rabbits", "wt rabbit", False, lambda state: st_has_temple_tracks(state, player, "Wooded")],
        ["forest realm rabbits", "s rabbit haven rabbits", False, lambda state: st_has_misc_tracks(state, player, "W Forest Realm") and (st_has_temple_tracks(state, player, "Wooded Temple") or st_has_glyph(state, player,"Snow"))],
        ["snow realm rabbits", "nr rabbit haven rabbit", False, None],

        # # ======== Castle Town =========

        ["forest realm", "castle town", True, None],
        ["castle town wall", "castle town stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["castle town", "castle town wall", False, lambda state: (st_has_bombs(state, player))],
        ["castle town wall", "castle town cuccos", False, lambda state: st_castle_town_cuccos(state, player)],

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
        ["fos", "fos chest", False, lambda state: st_has_whirlwind(state, player) or st_has_birds_song(state, player)],

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
        ["trading post", "trading post chest", False,
         lambda state: st_has_bombs(state, player)
                       and (st_has_boomerang(state, player) or st_has_bow(state, player))
                       and st_has_discovery_song(state, player)
                       and (st_has_light_song(state, player) or st_option_hard_logic(state, player))],
        ["trading post", "trading post stamp station", False, lambda state: st_has_bombs(state, player) and st_has_stamp_book(state, player)],

        # # ========== Rabbit Haven ========

        ["snow realm", "rabbit haven", True, lambda state: st_has_glyph(state, player, "Snow")],
        ["rabbit haven", "rabbit haven 5 rabbits", False, lambda state: st_has_total_rabbits(state, player, 5)],
        ["rabbit haven", "rabbit haven 10 forest rabbits", False, lambda state: st_has_rabbit_items(state, player, "Forest")],
        ["rabbit haven", "rabbit haven 10 snow rabbits", False, lambda state: st_has_rabbit_items(state, player, "Snow")],

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # # ============ Snow Realm ===============

        ["forest realm", "snow realm", False, lambda state: st_has_glyph(state, player, "Snow")],
        ["snow realm", "blizzard temple tracks", False, lambda state: st_has_temple_tracks(state, player, "Blizzard")],
        ["snow realm", "snow realm rabbits", False, lambda state: st_has_net(state, player)],
        ["blizzard temple tracks", "blizzard temple tracks rabbits", False, lambda state: st_has_net(state, player)],
        ["blizzard temple tracks rabbits", "snow realm blizzard rabbits", False, lambda state: st_has_source(state, player, "Snow")],
        ["blizzard temple tracks rabbits", "snow realm early blizzard rabbits", False, lambda state: st_has_source(state, player, "Snow") or st_option_hard_logic(state, player)],

        ["blizzard temple tracks rabbits", "snowdrift station rabbit", False, lambda state: st_has_misc_tracks(state, player, "Snowdrift Station")],
        ["blizzard temple tracks rabbits", "icyspring rabbits", False, lambda state: st_has_misc_tracks(state, player, "N Icy Spring")],

        ["forest realm se portal track", "blizzard temple tracks", True, lambda state: st_has_misc_tracks(state, player, "Forest Realm SE Portal") and st_has_temple_tracks(state, player, "Blizzard")],
        ["forest realm", "snow realm source", True, lambda state: st_has_source(state, player, "Snow")],
        ["snow realm source", "blizzard temple tracks", True, lambda state: st_has_source(state, player, "Snow") and st_has_temple_tracks(state, player, "Blizzard")],

        # ======== Anouki Village ========

        ["snow realm", "anouki village", False, None],
        ["anouki village", "anouki village stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["anouki village", "anouki village song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["anouki village", "anouki village bomb cave chest", False, lambda state: st_has_bombs(state, player)],
        ["anouki village", "anouki village lake chest", False, lambda state: st_has_boomerang(state, player)],

        # =========== Snow Sanctuary ==========

        ["anouki village", "ss", False, None],
        ["ss", "ss stamp station", False, lambda state: st_has_stamp_book(state, player)],

        ## ========== Blizzard Temple =========

        ["snow realm source", "bt", True, lambda state: st_has_source(state, player, 'Snow')],
        ["blizzard temple tracks", "bt", True, lambda state: st_has_temple_tracks(state, player, "Blizzard")],
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

        ["blizzard temple tracks", "icyspring", True, lambda state: st_has_temple_tracks(state, player, "Blizzard")],
        ["icyspring", "icyspring stamp station", False, lambda state: st_has_stamp_book(state, player) and st_has_boomerang(state, player)],
        ["icyspring", "icyspring whip chest", False, lambda state: st_has_whip(state, player)],

        # ============ Snowdrift Station =========

        ["blizzard temple tracks", "snowdrift", True, lambda state: st_has_misc_tracks(state, player, "Snowdrift Station")],
        ["snowdrift", "snowdrift reward", False, lambda state: st_has_boomerang(state, player) and st_has_shield(state, player)],

        # ========== Slippery Station ==========
        ["blizzard temple tracks", "slippery", True,
         lambda state: st_has_misc_tracks(state, player, "Slippery Station")
                       and (st_has_source(state, player, 'Snow') or st_has_misc_tracks(state, player, "N Icy Spring"))],
        ["slippery", "slippery amateur", False, None],
        ["slippery", "slippery pro", False, None],
        ["slippery", "slippery champion", False, None],

        # ========== Bridge Worker's Home =======
        ["snow realm source", "bridge workers", True, lambda state: st_has_source(state, player, "Snow")],
        ["bridge workers", "bridge workers chest", False, lambda state: st_has_discovery_song(state, player)],

    ]

    # Generate rabbit total items
    if options.rabbitsanity == "on_total":
        # overworld_logic += [  silly lambda instancing
        #     [f"{realm.lower()} realm rabbits", f"{realm} Rabbit Count {i}", False,
        #      lambda state: st_caught_rabbits(state, player, realm, i)] for i in range(1, 11)
        #     for realm in ["Forest", "Snow"]
        # ]
        overworld_logic += [
            ["forest realm rabbits", "Forest Rabbit Count 1", False,
             lambda state: st_caught_rabbits(state, player, "Forest", 1)],
            ["forest realm rabbits", "Forest Rabbit Count 2", False,
             lambda state: st_caught_rabbits(state, player, "Forest", 2)],
            ["forest realm rabbits", "Forest Rabbit Count 3", False,
             lambda state: st_caught_rabbits(state, player, "Forest", 3)],
            ["forest realm rabbits", "Forest Rabbit Count 4", False,
             lambda state: st_caught_rabbits(state, player, "Forest", 4)],
            ["forest realm rabbits", "Forest Rabbit Count 5", False,
             lambda state: st_caught_rabbits(state, player, "Forest", 5)],
            ["forest realm rabbits", "Forest Rabbit Count 6", False,
             lambda state: st_caught_rabbits(state, player, "Forest", 6)],
            ["forest realm rabbits", "Forest Rabbit Count 7", False,
             lambda state: st_caught_rabbits(state, player, "Forest", 7)],
            ["forest realm rabbits", "Forest Rabbit Count 8", False,
             lambda state: st_caught_rabbits(state, player, "Forest", 8)],
            ["forest realm rabbits", "Forest Rabbit Count 9", False,
             lambda state: st_caught_rabbits(state, player, "Forest", 9)],
            ["forest realm rabbits", "Forest Rabbit Count 10", False,
             lambda state: st_caught_rabbits(state, player, "Forest", 10)],
            ["snow realm rabbits", "Snow Rabbit Count 1", False,
             lambda state: st_caught_rabbits(state, player, "Snow", 1)],
            ["snow realm rabbits", "Snow Rabbit Count 2", False,
             lambda state: st_caught_rabbits(state, player, "Snow", 2)],
            ["snow realm rabbits", "Snow Rabbit Count 3", False,
             lambda state: st_caught_rabbits(state, player, "Snow", 3)],
            ["snow realm rabbits", "Snow Rabbit Count 4", False,
             lambda state: st_caught_rabbits(state, player, "Snow", 4)],
            ["snow realm rabbits", "Snow Rabbit Count 5", False,
             lambda state: st_caught_rabbits(state, player, "Snow", 5)],
            ["snow realm rabbits", "Snow Rabbit Count 6", False,
             lambda state: st_caught_rabbits(state, player, "Snow", 6)],
            ["snow realm rabbits", "Snow Rabbit Count 7", False,
             lambda state: st_caught_rabbits(state, player, "Snow", 7)],
            ["snow realm rabbits", "Snow Rabbit Count 8", False,
             lambda state: st_caught_rabbits(state, player, "Snow", 8)],
            ["snow realm rabbits", "Snow Rabbit Count 9", False,
             lambda state: st_caught_rabbits(state, player, "Snow", 9)],
            ["snow realm rabbits", "Snow Rabbit Count 10", False,
             lambda state: st_caught_rabbits(state, player, "Snow", 10)],
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
