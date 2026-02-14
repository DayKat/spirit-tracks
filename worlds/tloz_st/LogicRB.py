from BaseClasses import MultiWorld, Item
from .data.Rules import *
from .data.Entrances import ENTRANCES


def make_overworld_logic(player: int, origin_name: str, options: SpiritTracksOptions):
    overworld_logic = [

        # ====== Outset Village ==============

        #[region 1, region 2, two-directional, logic requirements],
        ["outset village", "outset village stamp book", False, Has("_picked_up_alfonzo")],
        ["outset village", "outset village stamp station", False, has_stamp_book],
        ["outset village", "outset village trees", False, has_sod],
        ["outset village", "forest realm", False, has_train],

        # ========= Forest Realm ==========

        ["forest realm", "forest realm se portal track", False, Has("Forest Realm SE Portal Tracks")],
        ["forest realm", "forest realm rabbits", False, has_net],
        ["forest realm", "wtt", False, has_temple_tracks("Wooded")],
        ["forest realm", "forest source", False, has_source("Forest")],
        ["forest realm", "w castle town tracks", False, Has("W Castle Town Tracks")],
        ["forest realm", "n castle town tracks", False, Has("N Castle Town Tracks")],
        ["wtt", "snow realm", True, has_temple_tracks("Wooded") & has_glyph("Snow")],
        ["forest realm", "snow realm", False, has_portal("Hyrule Castle to Anouki Village", False) & has_glyph("Snow")],
        ["forest realm", "dark realm portal", True, has_compass],

        # cave
        ["forest realm", "forest cave tracks", True, Has("Forest Realm SW Cave Tracks")],
        ["forest cave tracks", "w forest tracks", True, Has("Forest Realm SW Cave Tracks") & Has("W Forest Realm Tracks")],
        ["w forest tracks", "snow realm", True, has_glyph("Snow") & Has("W Forest Realm Tracks")],
        ["w forest tracks", "wtt", True, has_temple_tracks("Wooded") & Has("W Forest Realm Tracks")],

        # Rabbits
        ["forest realm rabbits", "forest ocean shortcut rabbit", False, Has("Forest Realm Ocean Shortcut Tracks")],
        ["forest realm rabbits", "e mayscore rabbits", False, Has("E Mayscore Bridge Tracks")],
        ["forest realm se portal track", "sw trading post rabbit", False, has_net],
        ["forest realm rabbits", "sw trading post rabbit", False, has_glyph("Ocean")],
        ["wtt", "wt rabbit", False, has_net],
        ["forest source", "wt rabbit", False, has_net],
        ["w forest tracks", "s rabbit haven rabbits", False, has_net],
        ["snow realm rabbits", "nr rabbit haven rabbit", False, None],

        # Snow bridge
        ["w castle town tracks", "snow bridge", True, Has("W Castle Town Tracks") & Has("Snow Realm Bridge Tracks")],
        ["n castle town tracks", "snow bridge", True, Has("N Castle Town Tracks") & Has("Snow Realm Bridge Tracks")],
        ["wtt", "snow bridge", True, has_temple_tracks("Wooded") & Has("Snow Realm Bridge Tracks")],
        ["snow bridge", "snow realm", True, has_glyph("Snow") & Has("Snow Realm Bridge Tracks")],
        ["snow bridge", "snow realm source", True, has_source("Snow") & Has("Snow Realm Bridge Tracks")],

        # # ======== Castle Town =========

        ["forest realm", "castle town", True, None],
        ["castle town", "castle town wall", False, has_bombs],
        ["castle town", "pick up alfonzo", False, has_glyph("Snow")],
        ["pick up alfonzo", "alfonzo event", False, None],
        ["castle town wall", "castle town stamp station", False, has_stamp_book],
        ["castle town wall", "castle town cuccos", False, ct_cuccos],

        # # ======== Hyrule Castle =========

        ["castle town", "hyrule castle", False, None],
        ["hyrule castle", "hyrule castle nw chest", False, None],
        ["hyrule castle", "hyrule castle 2f indoors chest", False, None],
        ["hyrule castle", "hyrule castle 1f back chest", False, None],

        # # ======== ToS Tunnel =========

        ["hyrule castle", "tower tunnel", False, None],
        ["tower tunnel", "tower tunnel block chest", False, has_damage | hard_logic],
        ["tower tunnel", "tower tunnel 2f chest", False, has_small_keys("Tunnel to ToS", 1)],

        # # ========== ToS ===================

        ["forest realm", "tos", False, None],
        ["tos", "tos 1f", False, None],
        ["tos 1f", "tos 1f chest", False, has_range],
        ["tos 1f", "tos 2f", False, has_sword | has_bow_of_light],
        ["tos 2f", "tos 2f raised chests", False, has_whirlwind],
        ["tos 2f", "tos 2f bomb wall", False, has_bombs],
        ["tos 2f", "tos 3f rail map", False, None],
        ["tos 3f rail map", "goal_forest_glyph", False, None],
        ["tos 3f rail map", "event_3f", False, None],

        ["tos", "tos 4f", False, has_source("Forest")],
        ["tos 4f", "tos 5f island chest", False, has_sword & (has_whirlwind | has_bow_of_light)],
        ["tos 5f island chest", "tos 5f spinnit key", False, has_whirlwind],
        ["tos 5f spinnit key", "tos 5f alt path", False, has_boomerang],
        ["tos 5f alt path", "tos 5f secret chest", False, has_bombs],
        ["tos 5f alt path", "tos 4f ne chest", False, has_bombs],  # needs whirlwind and boomerang to get here
        ["tos 5f alt path", "tos 6f chests", False, None],  # geozards only need sword + phantom
        ["tos 5f spinnit key", "tos 6f key", False, has_small_keys("ToS", 1)],  # already have whirlwind
        ["tos 6f key", "tos 7f rail map", False, has_small_keys("ToS", 2)],
        ["tos 7f rail map", "goal_snow_glyph", False, None],
        ["tos 7f rail map", "event_7f", False, None],

        # # ============ Shops ====================

        # # ======== Mayscore =========

        ["forest realm", "mayscore", False, None],
        ["mayscore", "mayscore stamp station", False, has_stamp_book],
        # ["mayscore", "mayscore whip race bomb bag", False, lambda state: st_has_whip(state, player)],
        # ["mayscore", "mayscore whip race heart container", False, lambda state: st_has_whip(state, player)],
        ["mayscore", "mayscore whip chest", False, has_whip],

        # # ======== Forest Sanctuary =========

        ["forest realm", "fos", False, None],
        ["fos", "fos stamp station", False, has_stamp_book],
        ["fos", "fos song statue", False, has_spirit_flute],
        # ["fos", "fos gage", False, lambda state: st_has_spirit_flute(state, player)],
        ["fos", "fos chest", False, has_cuccos],

        # # ======== Wooded Temple =========

        ["wtt", "wt", False, None],
        ["forest source", "wt", False, None],
        ["wt", "wt stamp station", False, has_stamp_book & (has_whirlwind | hard_logic)],
        ["wt", "wt song statue", False, has_spirit_flute],
        ["wt", "wt 1f enemy chest", False, has_damage],
        ["wt 1f enemy chest", "wt 1f key", False, has_whirlwind],
        ["wt 1f enemy chest", "wt 2f enemy chest", False, None],
        ["wt 1f enemy chest", "wt 2f poison chest", False, has_whirlwind | hard_logic],
        ["wt", "wt 1f switch chest", False, has_whirlwind | hard_logic],
        ["wt", "wt 2f left", False, can_kill_bubble & has_small_keys("Wooded Temple", 1)],
        ["wt 2f left", "wt 3f chestnut chest", False, has_range_objects],
        ["wt 2f left", "wt 3f", False, has_small_keys("Wooded Temple", 2)],
        ["wt 3f", "wt 3f se chest", False, has_whirlwind | hard_logic],
       #["wt", "wt 3f boss key chest", False, lambda state: st_has_damage(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Wooded Temple",2)],
        #["wt", "wt heart container", False, lambda state: st_has_sword(state, player) and st_has_whirlwind(state, player) and st_has_small_keys(state, player,"Wooded Temple",2)],
        ["wt 3f", "wt stagnox", False, has_sword & has_whirlwind],
        ["wt stagnox", "goal_stagnox", False, None],
        ["wt stagnox", "event_stagnox", False, None],

        # # ============ Trading Post =============

        ["forest realm", "trading post", False, has_glyph("Ocean")],
        #["trading post", "trading post discovery song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["trading post", "trading post light song statue", False, has_spirit_flute],
        ["trading post", "trading post chest", False, has_bombs & has_range & has_sod & (has_sol | hard_logic)],
        ["trading post", "trading post stamp station", False, has_bombs & has_stamp_book],

        # # ========== Rabbit Haven ========

        ["snow realm", "rabbit haven", True, has_glyph("Snow")],
        ["rabbit haven", "rabbit haven 5 rabbits", False, has_total_rabbits(5)],
        ["rabbit haven", "rabbit haven 10 forest rabbits", False, has_rabbit_items("Forest", 10)],
        ["rabbit haven", "rabbit haven 10 snow rabbits", False, has_rabbit_items("Snow", 10)],

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # # ============ Snow Realm ===============

        ["snow realm", "blizzard temple tracks", True, has_temple_tracks("Blizzard") & has_glyph("Snow")],
        ["snow realm", "snow realm rabbits", False, has_net],
        ["blizzard temple tracks", "blizzard temple tracks rabbits", False, has_net],
        ["blizzard temple tracks rabbits", "snow realm blizzard rabbits", False, has_source("Snow")],
        ["blizzard temple tracks rabbits", "snow realm early blizzard rabbits", False, has_source("Snow") | hard_logic],

        ["blizzard temple tracks rabbits", "snowdrift station rabbit", False, Has("Snowdrift Station Tracks")],
        ["blizzard temple tracks", "icyspring tracks", True, Has("N Icy Spring Tracks")],
        ["icyspring tracks", "icyspring rabbits", False, has_net],

        ["forest realm se portal track", "blizzard temple tracks", False, has_temple_tracks("Blizzard") & has_portal("Trading Post to E Snow Realm", True)],
        ["blizzard temple tracks", "forest realm se portal track", False, Has("Forest Realm SE Portal Tracks") & has_portal("Trading Post to E Snow Realm", False)],
        ["forest realm", "snow realm source", True, has_source("Snow")],
        ["snow realm source", "blizzard temple tracks", True, has_source("Snow") & has_temple_tracks("Blizzard")],

        # ======== Anouki Village ========

        ["snow realm", "anouki village", False, None],
        ["anouki village", "anouki village stamp station", False, has_stamp_book],
        ["anouki village", "anouki village song statue", False, has_spirit_flute],
        ["anouki village", "anouki village bomb cave chest", False, has_bombs],
        ["anouki village", "anouki village lake chest", False, has_boomerang],

        # =========== Snow Sanctuary ==========

        ["anouki village", "ss", False, None],
        ["ss", "ss stamp station", False, has_stamp_book],

        ## ========== Blizzard Temple =========

        ["snow realm source", "bt", True, has_source('Snow')],
        ["blizzard temple tracks", "bt", True, has_temple_tracks("Blizzard")],
        ["bt", "bt b1 se chest", False, can_ring_bell & has_whirlwind & has_short_range],
        ["bt b1 se chest", "bt b1 e enemy chest", False, None],
        ["bt b1 se chest", "bt b1 ne enemy chest", False, can_kill_bubble],
        ["bt b1 se chest", "bt 1f ne chest", False, has_boomerang | (has_whip & has_whirlwind)],
        ["bt 1f ne chest", "bt b1 sw chest", False, has_boomerang],
        ["bt 1f ne chest", "bt b1 nw enemy chest", False, has_small_keys("Blizzard Temple", 1)],
        ["bt b1 nw enemy chest", "bt stamp station", False, has_stamp_book],
        ["bt b1 nw enemy chest", "bt 1f nw chest", False, None],
        ["bt b1 nw enemy chest", "bt 1f torch chest", False, None],
        ["bt b1 nw enemy chest", "bt fraaz", False, has_sword],
        ["bt fraaz", "goal_fraaz", False, None],
        ["bt fraaz", "event_fraaz", False, None],

        # ========== Icy Spring ==========

        ["blizzard temple tracks", "icyspring", True, has_temple_tracks("Blizzard")],
        ["icyspring", "icyspring stamp station", False, has_stamp_book & has_boomerang],
        ["icyspring", "icyspring whip chest", False, has_whip],

        # ============ Snowdrift Station =========

        ["blizzard temple tracks", "snowdrift", True, Has("Snowdrift Station Tracks")],
        ["snowdrift", "snowdrift reward", False, has_range & (has_shield | has_bow_of_light | hard_logic) & (has_sword | has_whip | has_bombs | has_bow)], # and maybe bow?

        # ========== Slippery Station ==========
        ["blizzard temple tracks", "slippery", True, Has("Slippery Station Tracks") & (has_source("Snow") | Has("N Icy Spring Tracks"))],
        ["slippery", "slippery amateur", False, None],
        ["slippery", "slippery pro", False, None],
        ["slippery", "slippery champion", False, None],

        # ========== Bridge Worker's Home =======
        ["snow realm source", "bridge workers", True, has_source("Snow")],
        ["bridge workers", "bridge workers chest", False, has_sod],

        # ===== Dark Realm =====
        ["dark realm portal", "dark realm trains", False, has_dungeon_rewards(options.dungeons_required.value)],
        ["dark realm trains", "demon train", False, None],
        ["demon train", "cole fight", False, None],
        ["cole fight", "malladus 1", False, has_bow_of_light & has_sword],
        ["malladus 1", "malladus 2", False, has_spirit_flute & has_sword],
        ["malladus 2", "malladus goal", False, has_bow_of_light & has_sword],
        ["malladus 2", "malladus event", False, has_bow_of_light & has_sword],

    ]

    # Generate rabbit total items
    if options.rabbitsanity in ["on_total", "both"]:
        print(f"Creating total rabbit logic")
        overworld_logic += [
            [f"{realm.lower()} realm rabbits", f"{realm} Rabbit Count {i}", False,
             caught_rabbits(realm, i)] for i in range(1, 11)
            for realm in ["Forest", "Snow"]
        ]
        # overworld_logic += [
        #     ["forest realm rabbits", "Forest Rabbit Count 1", False,
        #      lambda state: st_caught_rabbits(state, player, "Forest", 1)],
        #     ["forest realm rabbits", "Forest Rabbit Count 2", False,
        #      lambda state: st_caught_rabbits(state, player, "Forest", 2)],
        #     ["forest realm rabbits", "Forest Rabbit Count 3", False,
        #      lambda state: st_caught_rabbits(state, player, "Forest", 3)],
        #     ["forest realm rabbits", "Forest Rabbit Count 4", False,
        #      lambda state: st_caught_rabbits(state, player, "Forest", 4)],
        #     ["forest realm rabbits", "Forest Rabbit Count 5", False,
        #      lambda state: st_caught_rabbits(state, player, "Forest", 5)],
        #     ["forest realm rabbits", "Forest Rabbit Count 6", False,
        #      lambda state: st_caught_rabbits(state, player, "Forest", 6)],
        #     ["forest realm rabbits", "Forest Rabbit Count 7", False,
        #      lambda state: st_caught_rabbits(state, player, "Forest", 7)],
        #     ["forest realm rabbits", "Forest Rabbit Count 8", False,
        #      lambda state: st_caught_rabbits(state, player, "Forest", 8)],
        #     ["forest realm rabbits", "Forest Rabbit Count 9", False,
        #      lambda state: st_caught_rabbits(state, player, "Forest", 9)],
        #     ["forest realm rabbits", "Forest Rabbit Count 10", False,
        #      lambda state: st_caught_rabbits(state, player, "Forest", 10)],
        #     ["snow realm rabbits", "Snow Rabbit Count 1", False,
        #      lambda state: st_caught_rabbits(state, player, "Snow", 1)],
        #     ["snow realm rabbits", "Snow Rabbit Count 2", False,
        #      lambda state: st_caught_rabbits(state, player, "Snow", 2)],
        #     ["snow realm rabbits", "Snow Rabbit Count 3", False,
        #      lambda state: st_caught_rabbits(state, player, "Snow", 3)],
        #     ["snow realm rabbits", "Snow Rabbit Count 4", False,
        #      lambda state: st_caught_rabbits(state, player, "Snow", 4)],
        #     ["snow realm rabbits", "Snow Rabbit Count 5", False,
        #      lambda state: st_caught_rabbits(state, player, "Snow", 5)],
        #     ["snow realm rabbits", "Snow Rabbit Count 6", False,
        #      lambda state: st_caught_rabbits(state, player, "Snow", 6)],
        #     ["snow realm rabbits", "Snow Rabbit Count 7", False,
        #      lambda state: st_caught_rabbits(state, player, "Snow", 7)],
        #     ["snow realm rabbits", "Snow Rabbit Count 8", False,
        #      lambda state: st_caught_rabbits(state, player, "Snow", 8)],
        #     ["snow realm rabbits", "Snow Rabbit Count 9", False,
        #      lambda state: st_caught_rabbits(state, player, "Snow", 9)],
        #     ["snow realm rabbits", "Snow Rabbit Count 10", False,
        #      lambda state: st_caught_rabbits(state, player, "Snow", 10)],
        # ]

    return overworld_logic


def is_item(item: Item, player: int, item_name: str):
    return item.player == player and item.name == item_name

def create_connections(world: "SpiritTracksWorld", player: int, origin_name: str, options):
    all_logic = [
        make_overworld_logic(player, origin_name, options)
    ]

    entrance_lookup = {(e.entrance_region, e.exit_region): e.name for e in ENTRANCES.values()}
    world.set_completion_rule(Has("_beaten_game"))

    # Create connections
    for logic_array in all_logic:
        for reg1, reg2, is_two_way, rule in logic_array:
            region_1 = world.get_region(reg1)
            region_2 = world.get_region(reg2)
            name = entrance_lookup.get((reg1, reg2), None)
            # print(f"Creating connection {reg1} -> {reg2}")

            entrance = region_1.connect(region_2, name)
            if rule is not None:
                world.set_rule(entrance, rule)
            if is_two_way:
                name = entrance_lookup.get((reg2, reg1), None)
                entrance = region_2.connect(region_1, name)
                if rule is not None:
                    world.set_rule(entrance, rule)
