from BaseClasses import MultiWorld, Item, EntranceType
from typing import TYPE_CHECKING
from .data.LogicPredicates import *
from .Options import SpiritTracksOptions
from .data.Entrances import ENTRANCES

if TYPE_CHECKING:
    from . import SpiritTracksWorld
    from .Subclasses import STTransition


def make_overworld_logic(player: int, origin_name: str, options: SpiritTracksOptions):
        # # ========== Rabbit Haven ========
    overworld_logic = [

        # ====== Outset Village ==============

        #[region 1, region 2, two-directional, logic requirements],
        ["outset village", "outset village stamp book", False, lambda state:
            state.has("_picked_up_alfonzo", player) or
            state.has("Passenger: Alfonzo", player) or
            (st_has_glyph(state, player, "Snow") and not options.randomize_passengers)],
        ["outset village", "outset village stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["outset village", "outset village trees", False, lambda state: st_has_discovery_song(state, player)],
        ["outset village", "forest realm", False, lambda state: st_has_train(state, player)],
        ["outset village", "outset joe", False, lambda state: st_has_source(state, player, "Snow")],
        ["outset village", "outset cuccos", False, lambda state: state.has("Cargo: Cuccos", player) or state.has("_buy_cuccos", player)],

        # ========= Forest Realm ==========

        ["forest realm", "forest realm se portal track", False, lambda state: st_has_misc_tracks(state, player, "Forest Realm SE Portal")],
        ["forest realm", "forest realm rabbits", False, lambda state: st_has_net(state, player)],
        ["forest realm", "wtt", False, lambda state: st_has_temple_tracks(state, player, "Wooded")],
        ["forest realm", "forest source", False, lambda state: st_has_source(state, player, "Forest")],
        ["forest realm", "w castle town tracks", False, lambda state: st_has_misc_tracks(state, player, "W Castle Town")],
        ["forest realm", "n castle town tracks", False, lambda state: st_has_misc_tracks(state, player, "N Castle Town")],
        ["wtt", "snow realm fr", True, lambda state: st_has_temple_tracks(state, player, "Wooded") and st_has_glyph(state, player, "Snow") and st_has_cannon(state, player)],
        ["forest realm", "snow realm fr", False, lambda state: st_has_portal(state, player, "Hyrule Castle to Anouki Village", False) and st_has_glyph(state, player, "Snow")],
        ["forest realm", "dark realm portal", True, lambda state: st_has_compass_of_light(state, player)],

        # cave
        ["forest realm", "forest cave tracks", True, lambda state: st_has_misc_tracks(state, player, "Forest Realm SW Cave")],
        ["forest cave tracks", "forest cave portal", False, lambda state: st_has_cannon(state, player)],
        ["forest cave tracks", "w forest tracks", True, lambda state: st_has_misc_tracks(state, player, "Forest Realm SW Cave") and st_has_misc_tracks(state, player,"W Forest Realm") and st_soft_cannon(state, player)],
        ["w forest tracks", "snow realm fr", True, lambda state: st_has_glyph(state, player, "Snow") and st_has_misc_tracks(state, player, "W Forest Realm")],
        ["w forest tracks", "wtt", True, lambda state: st_has_temple_tracks(state, player, "Wooded") and st_has_misc_tracks(state, player, "W Forest Realm")],

        # W Wooded temple
        ["wtt", "w wooded temple tracks", True, lambda state: st_has_misc_tracks(state, player, "W Wooded Temple")],
        ["w wooded temple tracks", "snow realm fr", True, lambda state: st_has_misc_tracks(state, player, "W Wooded Temple") and st_has_glyph(state, player, "Snow")],
        ["w wooded temple tracks", "snow realm", True,
         lambda state: st_has_misc_tracks(state, player, "W Wooded Temple") and st_has_glyph(state, player, "Snow")],

        # Rabbits
        ["forest realm rabbits", "forest ocean shortcut rabbit", False, lambda state: st_has_misc_tracks(state, player, "Forest Realm Ocean Shortcut")],
        ["forest realm rabbits", "e mayscore rabbits", False, lambda state: st_has_misc_tracks(state, player, "E Mayscore Bridge")],
        ["forest realm se portal track", "sw trading post rabbit", False, lambda state: st_has_net(state, player)],
        ["forest realm rabbits", "sw trading post rabbit", False, lambda state: st_has_glyph(state, player, "Ocean") and st_option_hard_logic(state, player)],
        ["wtt", "wt rabbit", False, lambda state: st_has_net(state, player)],
        ["forest source", "wt rabbit", False, lambda state: st_has_net(state, player)],
        ["w forest tracks", "s rabbit haven rabbits", False, lambda state: st_has_net(state, player)],
        ["snow realm rabbits", "nr rabbit haven rabbit", False, None],

        # Snow bridge
        ["w castle town tracks", "snow bridge", True, lambda state: st_has_misc_tracks(state, player, "W Castle Town") and st_has_misc_tracks(state, player, "Snow Realm Bridge") and st_soft_cannon(state, player)],
        ["n castle town tracks", "snow bridge", True, lambda state: st_has_misc_tracks(state, player, "N Castle Town") and st_has_misc_tracks(state, player, "Snow Realm Bridge") and st_soft_cannon(state, player)],
        ["n castle town tracks", "snow realm source", True, lambda state: st_has_misc_tracks(state, player, "N Castle Town") and st_has_source(state, player, "Snow") and st_soft_cannon(state, player)],
        ["wtt", "snow bridge", True, lambda state: st_has_temple_tracks(state, player, "Wooded") and st_has_misc_tracks(state, player,"Snow Realm Bridge") and st_soft_cannon(state, player)],
        ["snow bridge", "snow realm", True, lambda state: st_has_glyph(state, player, "Snow") and st_has_misc_tracks(state, player,"Snow Realm Bridge")],
        ["snow bridge", "snow realm source", True, lambda state: st_has_source(state, player, "Snow") and st_has_misc_tracks(state, player, "Snow Realm Bridge")],
        ["snow bridge", "snow bridge portal", False, lambda state: st_has_cannon(state, player)],

        # # ======== Castle Town =========

        ["forest realm", "castle town", True, None],
        ["castle town", "pick up alfonzo", False, lambda state: st_has_glyph(state, player, "Snow")],
        ["pick up alfonzo", "alfonzo event", False, None],
        ["pick up alfonzo", "castle town mona", False, None],
        ["castle town wall", "castle town stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["castle town", "castle town wall", False, lambda state: st_has_bombs(state, player)],
        ["castle town wall", "castle town cuccos", False, lambda state: st_castle_town_cuccos(state, player)],

        ["castle town", "teao 1", False, lambda state:
            st_has_sword(state, player) and
            st_has_whirlwind(state, player) and
            any([
                st_has_source(state, player, "Forest"),
                st_has_source(state, player, "Ocean"),
                st_has_source(state, player, "Sand")])],
        ["castle town", "teao 2", False, lambda state:
            (st_has_source(state, player, "Ocean") or
             st_has_source(state, player, "Sand")) and
            st_has_sword(state, player) and
            st_has_whirlwind(state, player) and
            st_has_boomerang(state, player) and
            st_has_whip(state, player)],
        ["castle town", "teao 3", False, lambda state:
            st_has_source(state, player, "Sand") and
            st_has_bow(state, player) and
            st_has_sand_wand(state, player) and
            st_has_sword(state, player) and
            st_has_whirlwind(state, player) and
            st_has_boomerang(state, player) and
            st_has_whip(state, player)],

        # # ======== Hyrule Castle =========

        ["castle town", "hyrule castle", False, None],
        ["hyrule castle", "hyrule castle sword minigame", False, lambda state: st_has_sword(state, player) and st_has_source(state, player, "Snow")],

        # # ======== ToS Tunnel =========

        ["hyrule castle", "tower tunnel", False, None],
        ["tower tunnel", "tower tunnel block chest", False, lambda state: (st_can_kill_bat(state, player) or st_has_whirlwind(state, player) or st_option_hard_logic(state, player))],
        ["tower tunnel", "tower tunnel 2f chest", False, lambda state: st_has_small_keys(state, player, "Tunnel to ToS", 1)],

        # # ========== ToS ===================

        ["forest realm", "tos", True, lambda state: st_can_enter_tos(state, player)],
        ["snow realm source", "tos", True, lambda state: st_can_enter_tos(state, player) and st_has_source(state, player, "Snow") and st_soft_cannon(state, player)],

        ["tos", "tos 1f", True, None],
        ["tos", "tos 2", False, lambda state: st_can_enter_tos_section(state, player, 2)],
        ["tos", "tos 3", False, lambda state: st_can_enter_tos_section(state, player,3)],
        ["tos", "tos 4", False, lambda state: st_can_enter_tos_section(state, player,4)],
        ["tos", "tos 5", False, lambda state: st_can_enter_tos_section(state, player,5)],


        ["tos 1f", "tos 1f chest", False, lambda state: (st_has_bow(state, player) or st_has_boomerang(state, player) or st_has_beam_sword(state, player))],
        ["tos 1f", "tos 1f switch", False, lambda state: st_can_kill_bat(state, player) or st_can_possess_phantoms(state, player, 1)],
        ["tos 1f", "tos 2f", False, lambda state: st_can_possess_phantoms(state, player, 1) or st_vanilla_tears(state, player)],
        ["tos 2f", "tos 2f raised chests", False, lambda state: st_has_whirlwind(state, player)],
        ["tos 2f", "tos 2f bomb wall", False, lambda state: st_has_bombs(state, player)],
        ["tos 2f", "tos 3f rail map", False, None],
        ["tos 3f rail map", "goal_forest_glyph", False, None],
        ["tos 3f rail map", "event_3f", False, None],

        ["tos 2", "tos 4f", True, None],
        ["tos 4f", "tos 4f whirlwind", False, lambda state: st_has_whirlwind(state, player)],
        ["tos 4f", "tos 5f phantom", False, lambda state: st_can_possess_phantoms(state, player, 2) or (st_vanilla_tears(state, player) and st_has_whirlwind(state, player))],
        ["tos 5f phantom", "tos 5f spinnit key", False, lambda state: st_has_whirlwind(state, player)],
        ["tos 5f spinnit key", "tos 5f alt path", False, lambda state: st_has_boomerang(state, player)],
        ["tos 5f alt path", "tos 5f secret chest", False, lambda state: st_has_bombs(state, player)],
        ["tos 5f alt path", "tos 4f ne chest", False, lambda state: st_has_bombs(state, player)],
        ["tos 5f alt path", "tos 6f chests", False, None],
        ["tos 5f spinnit key", "tos 6f key", False, lambda state: st_has_small_keys(state, player, "ToS 2", 1)],
        ["tos 6f key", "tos 7f rail map", False, lambda state: st_has_small_keys(state, player, "ToS 2", 2)],
        ["tos 7f rail map", "goal_snow_glyph", False, None],
        ["tos 7f rail map", "event_7f", False, None],

        ["tos 3", "tos 8f", True, None],
        ["tos 8f", "tos 8f bombs", False, lambda state: st_has_bombs(state, player)],
        ["tos 8f", "tos 9f phantom", False, lambda state: st_can_possess_phantoms(state, player, 3) or st_vanilla_tears(state, player)],
        ["tos 9f phantom", "tos 9f nw", False, lambda state: st_has_whirlwind(state, player)],
        ["tos 9f phantom", "tos 11f", False, lambda state: st_has_damage(state, player)],
        ["tos 11f", "event_12f", False, None],

        ["tos 4", "tos 13f", True, None],
        ["tos 13f", "tos 13f whip", False, lambda state: st_has_whip(state, player)],
        ["tos 13f", "tos 13f boomerang", False, lambda state: st_has_boomerang(state, player)],
        ["tos 13f", "tos 14f east", False, lambda state: st_has_small_keys(state, player, "ToS 4", 3) | (st_vanilla_tears(state, player) & st_has_small_keys(state, player, "ToS 4", 2))],
        ["tos 13f", "tos 13f phantom", False, lambda state: any([
            st_can_possess_phantoms(state, player, 4), all([
                st_vanilla_tears(state, player),
                st_has_whip(state, player),
                st_has_small_keys(state, player, "ToS 4", 2)])])],
        ["tos 13f phantom", "tos 13f phantom whip", False, lambda state: st_has_whip(state, player)],
        ["tos 13f phantom", "tos 14f west", False, lambda state: st_has_small_keys(state, player, "ToS 4", 4)],

        ["tos 14f east", "tos 14f phantom", False, lambda state:
         st_can_possess_phantoms(state, player, 4) | (st_vanilla_tears(state, player) & st_has_whip(state, player))],
        ["tos 14f east", "tos 15f", False, None],
        ["tos 15f", "tos 16f", False, lambda state: (st_has_range(state, player) | st_has_beam_sword(state, player)) & st_has_whirlwind(state, player) & st_has_small_keys(state, player, "ToS 4", 3)],
        ["tos 16f", "event_17f", False, None],
        ["tos 16f", "tos 16f bombs", False, lambda state: st_has_bombs(state, player)],

        ["tos 5", "tos 18f", True, None],
        ["tos 18f", "tos 18f whip", False, lambda state: st_has_whip(state, player)],
        ["tos 18f", "tos 19f", False, lambda state: st_has_small_keys(state, player, "ToS 5", 1)],
        ["tos 18f", "tos 18f phantom", False, lambda state: st_can_possess_phantoms(state, player, 5)],

        ["tos 19f", "tos 19f south", False, lambda state:
         st_has_bow(state, player) & (st_has_boomerang(state, player) | (st_can_possess_phantoms(state, player, 5) & st_can_rotate_repeater(state, player)))],
        ["tos 19f south", "tos 20f tear", False,  lambda state: st_has_boomerang(state, player) | st_has_beam_sword(state, player)],
        ["tos 19f", "tos 19f center", False, lambda state:
         st_can_possess_phantoms(state, player, 5) | (st_vanilla_tears(state, player) & st_has_bow(state, player) & st_has_boomerang(state, player))],
        ["tos 19f center", "tos 19f center chest", False, lambda state: st_has_bow(state, player) & (st_has_boomerang(state, player) | st_has_beam_sword(state, player))],
        ["tos 19f center", "tos 18f phantom", False, None],
        ["tos 19f center", "tos 20f", False, lambda state: st_has_small_keys(state, player, "ToS 5", 2)],

        ["tos 20f", "tos 19f center 2", False, lambda state: st_has_bow(state, player) & st_can_rotate_repeater(state, player)],
        ["tos 20f", "tos 22f", False, lambda state: st_has_bow(state, player) & st_can_rotate_repeater(state, player) & st_has_whip(state, player)],
        ["tos 22f", "tos staven", False, lambda state: st_has_sword(state, player)],
        ["tos staven", "event_staven", False, None],

        ["tos staven", "tos summit lower", True, None],
        ["tos summit lower", "tos summit", True, None],
        ["tos summit", "tos stamp stand", False, lambda state: st_has_stamp_book(state, player)],
        ["tos summit", "tos 6", False, lambda state: st_has_bow_of_light(state, player)],
        ["tos 30f", "tos 6", True, None],

        ["tos 30f", "tos 30f bomb wall", False, lambda state: st_has_bombs(state, player)],
        ["tos 30f", "tos 29f", False, lambda state: st_can_possess_phantoms(state, player, 6) & st_has_boomerang(state, player) & st_has_whirlwind(state, player)],
        ["tos 29f", "tos 29f sand wand", False, lambda state: st_has_sand_wand(state, player)],
        ["tos 29f sand wand", "tos 29f se", False, lambda state: st_has_bow_of_light(state, player)],

        ["tos 29f se", "tos 27f", False, lambda state: st_has_small_keys(state, player, "ToS 6", 3)],
        ["tos 27f", "tos 24f", False, lambda state: st_has_whip(state, player)],
        ["tos 24f", "event_24f", False, None],


        # # ======== Mayscore =========

        ["forest realm", "mayscore", False, None],
        ["mayscore", "mayscore stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["mayscore", "mayscore whip chest", False, lambda state: st_has_whip(state, player)],
        ["mayscore", "mayscore leaves", False, lambda state: st_has_whirlwind(state, player)],

        # # ======== Forest Sanctuary =========

        ["forest realm", "fos", False, None],
        ["fos", "fos stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["fos", "fos song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["fos", "fos chest", False, lambda state: st_has_whirlwind(state, player) or st_has_birds_song(state, player)],

        # # ======== Wooded Temple =========

        ["wtt", "wt", False, None],
        ["forest source", "wt", False, None],
        ["wt", "wt stamp station", False, lambda state: st_has_stamp_book(state, player) and (st_has_whirlwind(state, player) or st_option_hard_logic(state, player))],
        ["wt", "wt song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["wt", "wt 1f enemy chest", False, lambda state: st_has_damage(state, player)],
        ["wt 1f enemy chest", "wt 1f key", False, lambda state: st_has_whirlwind(state, player)],
        ["wt 1f enemy chest", "wt 2f enemy chest", False, None],
        ["wt 1f enemy chest", "wt 2f poison chest", False, lambda state: st_has_whirlwind(state, player) or st_option_hard_logic(state, player)],
        ["wt", "wt 1f switch chest", False, lambda state: st_has_whirlwind(state, player) or st_option_hard_logic(state, player)],
        ["wt", "wt 2f left", False, lambda state: st_can_kill_bubble(state, player) and st_has_small_keys(state, player, "Wooded Temple", 1)],
        ["wt 2f left", "wt 3f chestnut chest", False, lambda state: st_has_range(state, player) or st_has_beam_sword(state, player) or st_has_whirlwind(state, player)],
        ["wt 2f left", "wt 3f", False, lambda state: st_has_small_keys(state, player, "Wooded Temple", 2)],
        ["wt 3f", "wt 3f se chest", False, lambda state: st_has_whirlwind(state, player) or st_option_hard_logic(state, player)],
        ["wt 3f", "wt stagnox", False, lambda state: st_has_sword(state, player) and st_has_whirlwind(state, player)],
        ["wt stagnox", "goal_stagnox", False, None],
        ["wt stagnox", "event_stagnox", False, None],

        # # ============ Trading Post =============

        ["forest realm", "trading post tracks", False, lambda state: st_has_glyph(state, player, "Ocean") and st_soft_cannon(state, player)],
        ["trading post tracks", "trading post", False, None],
        ["trading post", "trading post light song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["trading post", "trading post chest", False,
         lambda state: (st_has_range(state, player) or st_has_beam_sword(state, player))
                       and st_has_discovery_song(state, player)
                       and (st_has_light_song(state, player) or st_option_hard_logic(state, player))],
        ["trading post", "trading post stamp station", False, lambda state: st_has_bombs(state, player) and st_has_stamp_book(state, player)],
        ["trading post", "trading post bridge worker", False, lambda state: state.has("Passenger: Kenzo", player) or state.has("_kenzo_1", player)],
        ["trading post bridge worker", "linebeck trading", False, lambda state: state.has("Treasure: Regal Ring", player)],
        ["trading post", "linebeck trading", False, lambda state: state.has("Treasure: Regal Ring", player) and options.randomize_passengers.value == 0],
        ["trading post", "trading post leaves", False, lambda state: st_has_whirlwind(state, player)],
        ["linebeck trading", "trading post pick up kenzo", False, lambda state: st_has_glyph(state, player, "Snow")],
    ]
    overworld_logic += [
        ["snow realm fr", "rabbit haven", True, lambda state: st_has_glyph(state, player, "Snow")],
        ["rabbit haven", "rabbit haven 5 rabbits", False, lambda state: st_has_total_rabbits(state, player, 5)],
        ["rabbit haven", "rabbit haven 10 forest rabbits", False, lambda state: st_has_rabbit_items(state, player, "Grass")],
        ["rabbit haven", "rabbit haven 10 snow rabbits", False, lambda state: st_has_rabbit_items(state, player, "Snow")],
        ["rabbit haven", "rabbit haven mona", False, lambda state: state.has("Passenger: Mona", player) or state.has("_mona", player)],

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # # ============ Snow Realm ===============

        ["snow realm fr", "snow realm", True, lambda state: st_soft_cannon(state, player)],
        ["snow realm fr", "anouki portal", False, lambda state: st_has_cannon(state, player)],
        ["snow realm", "blizzard temple tracks", True, lambda state: st_has_temple_tracks(state, player, "Blizzard") and st_has_glyph(state, player, "Snow")],
        ["snow realm", "snow realm rabbits", False, lambda state: st_has_net(state, player)],
        ["blizzard temple tracks", "blizzard temple tracks rabbits", False, lambda state: st_has_net(state, player)],
        ["blizzard temple tracks rabbits", "snow realm blizzard rabbits", False, lambda state: st_has_source(state, player, "Snow")],
        ["blizzard temple tracks rabbits", "snow realm early blizzard rabbits", False, lambda state: st_has_source(state, player, "Snow") or st_option_hard_logic(state, player)],

        ["blizzard temple tracks rabbits", "snowdrift station rabbit", False, lambda state: st_has_misc_tracks(state, player, "Snowdrift Station")],
        ["blizzard temple tracks", "icyspring tracks", True, lambda state: st_has_misc_tracks(state, player, "N Icy Spring")],
        ["icyspring tracks", "icyspring rabbits", False, lambda state: st_has_net(state, player)],
        ["icyspring tracks", "icyspring portal", False, lambda state: st_has_cannon(state, player)],

        ["forest realm se portal track", "blizzard temple tracks", False,
         lambda state: st_has_temple_tracks(state, player, "Blizzard")
                       and st_has_portal(state, player, "Trading Post to E Snow Realm", True)],
        ["blizzard temple tracks", "forest realm se portal track", False,
         lambda state: st_has_misc_tracks(state, player, "Forest Realm SE Portal")
                       and st_has_portal(state, player, "Trading Post to E Snow Realm", False)],
        ["forest realm se portal track", "trading post portal", False, lambda state: st_has_cannon(state, player)],
        ["snow realm source", "blizzard temple tracks", True, lambda state: st_has_source(state, player, "Snow") and st_has_temple_tracks(state, player, "Blizzard")],

        # ======== Anouki Village ========

        ["snow realm", "anouki village", False, None],
        ["anouki village", "anouki village stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["anouki village", "anouki village song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["anouki village", "anouki village bomb cave chest", False, lambda state: st_has_bombs(state, player)],
        ["anouki village", "anouki village lake chest", False, lambda state: st_has_boomerang(state, player)],
        ["anouki village", "av noko", False, lambda state: st_has_temple_tracks(state, player, "Blizzard")],
        ["anouki village", "av fence", False, lambda state:
            (state.has("Passenger: Kenzo", player) or state.has("_kenzo_2", player) or options.randomize_passengers == "no_passengers")
            and (state.has("Cargo: Lumber", player) or state.has("_buy_lumber", player) or options.randomize_cargo == "no_cargo")],
        ["anouki village", "av kenzo", False, lambda state:
            (state.has("Passenger: Kenzo", player) or state.has("_kenzo_2",  player) or options.randomize_passengers == "no_passengers")
            or (state.has("Cargo: Lumber", player) or state.has("_buy_lumber", player) or options.randomize_cargo == "no_cargo")],

        # =========== Snow Sanctuary ==========

        ["snow realm", "ss", False, lambda state: st_has_temple_tracks(state, player, "Blizzard") or (state.has("Snow Sanctuary Cave Key", player) and st_has_cannon(state, player))],
        ["ss", "ss stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["ss", "ss song", False, lambda state: st_has_spirit_flute(state, player)],

        ## ========== Blizzard Temple =========

        ["snow realm source", "bt", True, lambda state: st_has_source(state, player, 'Snow') and st_soft_cannon(state, player)],
        ["blizzard temple tracks", "bt", True, lambda state: st_has_temple_tracks(state, player, "Blizzard")],
        ["bt", "bt b1 se", False, lambda state: st_can_ring_bell(state, player) and st_has_whirlwind(state, player)],
        ["bt b1 se", "bt b1 e enemy chest", False, None],
        ["bt b1 se", "bt b1 ne enemy chest", False, lambda state: st_can_kill_bubble(state, player)],
        ["bt b1 se", "bt 1f ne chest", False, lambda state: st_has_mid_range(state, player) or st_has_bombs(state, player)],
        ["bt 1f ne chest", "bt b1 sw chest", False, lambda state: st_has_boomerang(state, player)],
        ["bt b1 sw chest", "bt b1 nw enemy chest", False, lambda state: st_has_small_keys(state, player, "Blizzard Temple", 1) and st_can_kill_freezards_torch(state, player)],
        ["bt b1 nw enemy chest", "bt stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["bt b1 nw enemy chest", "bt 1f nw chest", False, None],
        ["bt b1 nw enemy chest", "bt 1f torch chest", False, None],
        ["bt b1 nw enemy chest", "bt fraaz", False, lambda state: st_has_sword(state, player)],
        ["bt fraaz", "goal_fraaz", False, None],
        ["bt fraaz", "event_fraaz", False, None],

        # ========== Icy Spring ==========

        ["blizzard temple tracks", "icyspring", True, lambda state: st_has_temple_tracks(state, player, "Blizzard")],
        ["icyspring", "icyspring stamp station", False, lambda state: st_has_stamp_book(state, player) and st_has_boomerang(state, player)],
        ["icyspring", "icyspring whip chest", False, lambda state: st_has_whip(state, player)],
        ["icyspring", "icyspring noko", False, lambda state: state.has("Passenger: Noko", player) or state.has("_noko", player) or options.randomize_passengers == "no_passengers"],

        # ============ Snowdrift Station =========

        ["blizzard temple tracks", "snowdrift", True, lambda state: st_has_misc_tracks(state, player, "Snowdrift Station") and st_soft_cannon(state, player)],
        ["snowdrift", "snowdrift reward", False, lambda state: st_can_kill_freezards(state, player) and (
            st_has_range(state, player) or (st_has_beam_sword(state, player) and st_option_hard_logic(state, player)))],

        # ========== Slippery Station ==========
        ["blizzard temple tracks", "slippery", True,
         lambda state: st_has_misc_tracks(state, player, "Slippery Station") and st_soft_cannon(state, player)
                       and (st_has_source(state, player, 'Snow') or st_has_misc_tracks(state, player, "N Icy Spring"))],
        ["slippery", "slippery amateur", False, None],
        ["slippery", "slippery pro", False, None],
        ["slippery", "slippery champion", False, None],

        # ========== Bridge Worker's Home =======
        ["snow realm source", "bridge workers", True, lambda state: st_has_source(state, player, "Snow")],
        ["bridge workers", "bridge workers chest", False, lambda state: st_has_discovery_song(state, player)],
        ["bridge workers", "pick up bridge worker", False, lambda state: st_has_glyph(state, player, "Ocean")],

        ["forest realm", "ocean realm", False, lambda state: st_has_glyph(state, player, "Ocean") and st_has_misc_tracks(state, player, "E Mayscore Bridge")],
        ["trading post tracks", "ocean realm", True, lambda state: state.has("Repair Trading Post Bridge", player)],

        # ========== Ocean Sanctuary =============
        # ["forest realm", "ocean realm", True, lambda state: st_has_glyph(state, player, "Ocean")],
        ["ocean realm", "ocean temple tracks", True, lambda state: st_has_temple_tracks(state, player, "Ocean")
                                                                   and st_has_glyph(state, player, "Ocean")],
        ["ocean temple tracks", "ocean realm source", True, lambda state: st_has_source(state, player, "Ocean")
                                                                          and st_has_temple_tracks(state, player, "Ocean")],
        ["ocean realm", "ocean realm source", True, lambda state: st_has_source(state, player, "Ocean")
                                                                  and st_has_glyph(state, player, "Ocean")],
        ["ocean realm", "pirate hideout tracks", True, lambda state: st_has_misc_tracks(state, player, "Pirate Hideout")],
        ["ocean realm source", "pirate hideout tracks", True, lambda state: st_has_source(state, player, "Ocean")
                                                                            and st_has_misc_tracks(state, player, "Pirate Hideout")],
        ["ocean temple tracks", "oct", True, lambda state: st_has_temple_tracks(state, player, "Marine")],
        # ["ocean temple tracks", "las tracks", True, lambda state: st_has_temple_tracks(state, player, "Ocean")
        #                                                              and st_has_misc_tracks(state, player, "Lost at Sea Station")],



        # ========== Ocean Sanctuary =============
        ["ocean realm", "ocs", False, None],
        ["ocs", "ocs north", False, lambda state: st_has_boomerang(state, player)], # Spreadsheet shows Whirlwind needed too,
                                                                                  # but not sure why looking at walkthrough
                                                                                  # probably wants you to whirlwind a bomb in the cave, but you can make the throw.
        ["ocs north", "ocs stamp station", False, lambda state: st_has_stamp_book(state, player)
                                                         and st_has_birds_song(state, player) and st_has_whip(state, player)],

        ["ocs", "ocs S island chest", False, lambda state: st_has_whip(state, player)],
        ["ocs north", "ocs nw chest", False, lambda state: st_has_whip(state, player)],
        ["ocs", "ocs song", False, lambda state: st_has_spirit_flute(state, player)],

        # ========== Papuchia Village =============
        ["ocean realm", "papuchia village", False, None],
        ["papuchia village", "papuchia village song statue", False, lambda state: st_has_discovery_song(state, player)],
        ["papuchia village south", "papuchia village stamp station", False, lambda state: st_has_stamp_book(state, player)],
        ["papuchia village", "papuchia village south", False, lambda state: st_has_whip(state, player)],

        # ========= Ocean Temple ==================
        ["ocean realm source", "oct", False, lambda state: st_has_source(state, player, "Ocean")
                                                          and st_has_temple_tracks(state, player, "Marine")],
        ["oct", "oct song statue", False, lambda state: st_has_spirit_flute(state, player)],
        ["oct 2f", "oct whip chest", False, lambda state: st_has_sword(state, player)], # you can't escape stunlock without sword, and the fight scripts you into it from the start
        ["oct", "oct whip", False, lambda state: st_has_whip(state, player)],
        ["oct", "oct 2f", None, lambda state: any([
            st_has_whip(state, player),
            st_can_hit_switches(state, player),
            st_option_hard_logic(state, player)  # damageboost through the boulders
        ])],
        ["oct", "oct stamp station", False, lambda state: st_has_stamp_book(state, player) and st_has_whip(state, player) and st_has_bombs(state, player) and st_has_boomerang(state, player)],
        ["oct whip chest", "oct 3f whip", False, lambda state: st_has_whip(state, player)],
        ["oct 3f whip", "oct 6f chest", False, lambda state: st_has_small_keys(state, player, "Marine Temple", 1)],
        ["oct 6f chest", "oct phytops", False, lambda state: st_has_small_keys(state, player, "Marine Temple", 2)],

        # ========= Pirate Hideout ==============
        ["pirate hideout tracks", "pirate hideout", False, None],
        ["pirate hideout", "pirate hideout stamp station", False, lambda state: st_has_stamp_book(state, player)
                                                                                and st_has_whip(state, player) and st_has_birds_song(state, player)],
        ["pirate hideout", "pirate hideout secret cave", False, lambda state: st_has_bombs(state, player)],
    #   ["pirate hideout", "pirate hideout minigame 1st reward", False, lambda state: st_has_bow(state, player)],
    #   ["pirate hideout", "pirate hideout minigame 2nd reward", False, lambda state: st_has_bow(state, player)],

        # ======== Lost at Sea Station ==========
        #["ocean temple tracks", "las tracks", True, lambda state: st_has_temple_tracks(state, player, "Ocean")
        #                                                          and st_has_misc_tracks(state, player, "Lost at Sea Station")],
        ["ocean temple tracks", "las tracks", True, lambda state: st_has_temple_tracks(state, player, "Marine")
                                                    and st_has_misc_tracks(state, player,"Lost at Sea Station")],
        ["las tracks", "lost at sea", True, lambda state: st_has_misc_tracks(state, player, "Lost at Sea Station")],
        ["lost at sea", "las outside chest", False, lambda state: st_has_discovery_song(state, player) and (st_has_light_song(state, player) or st_option_hard_logic(state, player))],
        ["lost at sea", "las 1st room chest", False, lambda state: st_has_awakening_song(state, player) and st_has_whip(state, player)],
        ["las 1st room chest", "las 2nd room chest", False, lambda state: st_has_boomerang(state, player)],
        ["las 2nd room chest", "las 3rd room chest", False, lambda state: st_has_whirlwind(state, player)],
        ["las 3rd room chest", "las 4th room chest", False, lambda state: st_has_whip(state, player)],
        ["las 4th room chest", "las 5th room", False, lambda state: st_has_bombs(state, player) or st_option_hard_logic(state, player)],


        # ===== Dark Realm =====
        ["dark realm portal", "dark realm trains", False, lambda state: st_has_dungeon_rewards(state, player)],
        ["dark realm trains", "demon train", False, None],
        ["demon train", "cole fight", False, lambda state: st_has_cannon(state, player)],
        ["cole fight", "malladus 1", False, lambda state: st_can_fight_malladus(state, player)],
        ["malladus 1", "malladus 2", False, lambda state: st_has_spirit_flute(state, player) and st_has_sword(state, player)],
        ["malladus 2", "malladus goal", False, lambda state: st_can_fight_malladus(state, player)],

        ["malladus 2", "malladus event", False, lambda state: st_can_fight_malladus(state, player)],

        ["forest realm", "beedle", False, lambda state: st_has_source(state, player, "Snow")],
        ["beedle", "beedle joe", False, lambda state: state.has("Passenger: Joe", player) or state.has("_joe", player)],
    ]

    required_rupees = 0
    if "uniques" in options.shopsanity.value: required_rupees += 2500
    if "treasure" in options.shopsanity.value: required_rupees += 2400
    if "potions" in options.shopsanity.value: required_rupees += 700
    if "shields" in options.shopsanity.value: required_rupees += 410
    if "postcards" in options.shopsanity.value: required_rupees += 300
    if options.randomize_cargo == "vanilla": required_rupees += 200
    elif options.randomize_cargo: required_rupees += 150

    overworld_logic += [
        # Shops
        ["ss", "snow sanc shop", False, lambda state: st_has_rupees(state, player, required_rupees)],

        ["beedle", "beedle bomb bag", False, lambda state: st_has_rupees(state, player, required_rupees)],
        ["beedle", "beedle uncommon treasure", False, lambda state: st_has_rupees(state, player, required_rupees)],
        ["beedle", "beedle rare treasure", False, lambda state: st_has_rupees(state, player, required_rupees)],
        ["beedle", "beedle potion", False, lambda state: st_has_rupees(state, player, required_rupees)],

        ["mayscore", "mayscore shop", False, lambda state: st_has_rupees(state, player, required_rupees)],
        ["castle town", "castle town shop", False, lambda state: st_has_rupees(state, player, required_rupees)],
        ["trading post", "trading post shield", False, lambda state: st_has_rupees(state, player, required_rupees)],

        ["castle town", "castle town buy cuccos", False, lambda state: state.has("Wagon", player) and st_has_rupees(state, player, required_rupees)],
        ["mayscore", "mayscore lumber", False, lambda state: state.has("Wagon", player) and st_has_rupees(state, player, required_rupees)],
        ["icyspring noko", "icyspring ice", False, lambda state: state.has("Wagon", player) and st_has_rupees(state, player, required_rupees)],
    ]

    # Generate rabbit total items
    if options.rabbitsanity in ["on_total", "both"]:
        print(f"Creating total rabbit logic")
        # overworld_logic += [  silly lambda instancing
        #     [f"{realm.lower()} realm rabbits", f"{realm} Rabbit Count {i}", False,
        #      lambda state: st_caught_rabbits(state, player, realm, i)] for i in range(1, 11)
        #     for realm in ["Forest", "Snow"]
        # ]
        overworld_logic += [
            ["forest realm rabbits", "Grass Rabbit Count 1", False,
             lambda state: st_caught_rabbits(state, player, "Grass", 1)],
            ["forest realm rabbits", "Grass Rabbit Count 2", False,
             lambda state: st_caught_rabbits(state, player, "Grass", 2)],
            ["forest realm rabbits", "Grass Rabbit Count 3", False,
             lambda state: st_caught_rabbits(state, player, "Grass", 3)],
            ["forest realm rabbits", "Grass Rabbit Count 4", False,
             lambda state: st_caught_rabbits(state, player, "Grass", 4)],
            ["forest realm rabbits", "Grass Rabbit Count 5", False,
             lambda state: st_caught_rabbits(state, player, "Grass", 5)],
            ["forest realm rabbits", "Grass Rabbit Count 6", False,
             lambda state: st_caught_rabbits(state, player, "Grass", 6)],
            ["forest realm rabbits", "Grass Rabbit Count 7", False,
             lambda state: st_caught_rabbits(state, player, "Grass", 7)],
            ["forest realm rabbits", "Grass Rabbit Count 8", False,
             lambda state: st_caught_rabbits(state, player, "Grass", 8)],
            ["forest realm rabbits", "Grass Rabbit Count 9", False,
             lambda state: st_caught_rabbits(state, player, "Grass", 9)],
            ["forest realm rabbits", "Grass Rabbit Count 10", False,
             lambda state: st_caught_rabbits(state, player, "Grass", 10)],
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

def create_connections(world: "SpiritTracksWorld", player: int, origin_name: str, options):
    all_logic = [
        make_overworld_logic(player, origin_name, options)
    ]
    entrance_lookup = {(e.entrance_region, e.exit_region): e for e in ENTRANCES.values()}
    world.multiworld.completion_condition[player] = lambda state: state.has("_beaten_game", player)

    def create_entrance(r1, r2, rule_):
        entrance_data: "STTransition" or None = entrance_lookup.get((r1.name, r2.name), None)
        name = entrance_data.name if entrance_data else None

        entrance = r1.connect(r2, name)
        if rule_ is not None:
            # print(f"Setting rule {rule_}")
            world.set_rule(entrance, rule_)

        if entrance_data:
            # print(f"Creating connection {r1} -> {r2} | {entrance_data.name}")
            rando_type_bool = entrance_data.two_way
            entrance.randomization_type = EntranceType.TWO_WAY if rando_type_bool else EntranceType.ONE_WAY
            entrance.randomization_group = entrance_data.direction | entrance_data.category_group | entrance_data.island
            world.valid_entrances.append(entrance)

    # Create connections
    for logic_array in all_logic:
        for reg1, reg2, is_two_way, rule in logic_array:
            region_1 = world.get_region(reg1)
            region_2 = world.get_region(reg2)

            create_entrance(region_1, region_2, rule)
            if is_two_way:
                create_entrance(region_2, region_1, rule)
