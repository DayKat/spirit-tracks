from BaseClasses import MultiWorld, Item, EntranceType, Entrance
from .data.Rules import *
from .data.Entrances import ENTRANCES
from .Subclasses import STTransition


def make_overworld_logic(player: int, origin_name: str, world):
    tower_section_lookup = world.tower_section_lookup
    overworld_logic = [

        # ====== Outset Village ==============

        #[region 1, region 2, two-directional, logic requirements],
        ["outset village", "outset station", False, None],
        ["outset station", "outset village", False, has_glyph("Forest")],
        ["outset station", "forest realm", True, has_train & has_glyph("Forest")],

        ["outset village", "niko's house", True, None],
        ["outset village", "mary's house", True, None],
        ["outset village", "train workshop", True, None],

        ["niko's house", "niko's stamp book", False, has_passenger("Alfonzo" ,"_picked_up_alfonzo")
         | Filtered(has_glyph("Snow"), options=[OptionFilter(SpiritTracksRandomizePassengers, 0)])],
        ["niko's stamp book", "outset 10 stamps", False, Has("Stamp", 10)],
        ["niko's stamp book", "outset 15 stamps", False, Has("Stamp", 15)],
        ["niko's stamp book", "outset 20 stamps", False, Has("Stamp", 20)],
        ["outset village", "outset village stamp station", False, has_stamp_book],
        ["outset village", "outset village trees", False, has_sod],
        ["outset village", "outset joe", False, has_source("Snow")],
        ["outset village", "outset cuccos", False, has_cargo("Cuccos", "_buy_cuccos")]
            if world.options.randomize_cargo.value in [1, 2] else
        ["outset village", "outset cuccos", False, has_wagon & (
                Has("Cargo: Cuccos (5)", 3) | (
                    Has("Cargo: Cuccos (5)", 2) & ool))],
        ["outset village", "delivered ferrus", False, has_passenger("Alfonzo", "_picked_up_alfonzo")
            & has_passenger("Ferrus", "_ferrus_1")],
        ["train workshop", "outset ferrus", None, Has("_delivered_ferrus")],

        # ========= Forest Realm ==========

        ["forest realm", "forest realm se portal track", True, has_tracks("Forest Realm SE Portal") & has_glyph("Forest")],
        ["forest realm", "wtt", True, has_temple_tracks("Wooded") & has_glyph("Forest")],
        ["forest realm", "forest source", True, has_source("Forest") & has_glyph("Forest")],
        ["forest realm", "w castle town tracks", True, has_tracks("W Castle Town") & has_glyph("Forest")],
        ["forest realm", "n castle town tracks", True, has_tracks("N Castle Town") & has_glyph("Forest")],
        ["wtt", "snow realm fr", True, has_temple_tracks("Wooded") & has_glyph("Snow")],
        ["wtt", "w castle town tracks", True, has_tracks("W Castle Town") & has_source("Forest")],
        ["forest realm", "snow realm south portal", False, has_portal("Hyrule Castle to Anouki Village", False) & has_glyph("Snow")],
        ["snow realm south", "forest realm", False, has_portal("Hyrule Castle to Anouki Village", True) & has_glyph("Forest")],
        ["snow realm south portal", "snow realm south", False, None],
        ["snow realm south portal", "snow realm", False, None],
        ["forest realm", "dark realm portal", True, has_compass & has_glyph("Forest")],

        # cave
        ["forest realm", "forest cave tracks", True, has_tracks("Forest Realm SW Cave") & has_glyph("Forest")],
        ["forest cave tracks", "forest cave portal", False, has_cannon],
        ["forest cave tracks", "w forest tracks", True, has_tracks("Forest Realm SW Cave") & has_tracks("W Forest Realm")],
        ["w forest tracks", "snow realm", True, has_glyph("Snow") & has_tracks("W Forest Realm")],
        ["w forest tracks", "wtt", True, has_temple_tracks("Wooded") & has_tracks("W Forest Realm")],

        # W Wooded temple
        ["wtt", "w wooded temple tracks", True, has_tracks("W Wooded Temple") & has_temple_tracks("Wooded")],
        ["w wooded temple tracks", "snow realm fr", True, has_tracks("W Wooded Temple") & has_glyph("Snow")],
        ["w wooded temple tracks north", "snow realm", True, has_tracks("W Wooded Temple") & has_glyph("Snow")],
        ["w wooded temple tracks north", "snow realm south", True, has_tracks("W Wooded Temple") & has_glyph("Snow")],
        ["w wooded temple tracks", "w wooded temple tracks north", False, has_tracks("W Wooded Temple")],
        ["w wooded temple tracks north", "w wooded temple tracks", False, has_glyph("Snow") & has_tracks("W Wooded Temple")],

        # Rabbits
        ["forest realm", "forest realm rabbits", False, has_net],
        ["ocean shortcut", "forest ocean shortcut rabbit", False, has_tracks("Forest Realm Ocean Shortcut")],
        ["e mayscore bridge", "e mayscore rabbits", False, has_tracks("E Mayscore Bridge")],
        ["forest realm se portal track", "sw trading post rabbit", False, has_net],
        ["forest realm rabbits", "sw trading post rabbit", False, has_glyph("Ocean") & hard_logic],
        ["wtt", "wt rabbit", False, has_net],
        ["forest source", "wt rabbit", False, has_net],
        ["w forest tracks", "s rabbit haven rabbits", False, has_net],
        ["snow realm fr", "nr rabbit haven rabbit", False, has_net],

        # Snow bridge
        ["w castle town tracks", "snow bridge south", True, has_tracks("W Castle Town") & has_tracks("Snow Realm Bridge")],
        ["n castle town tracks", "snow bridge south", True, has_tracks("N Castle Town") & has_tracks("Snow Realm Bridge")],
        ["n castle town tracks", "n castle town tracks north", True, has_tracks("N Castle Town")],
        ["n castle town tracks north", "snow realm source", True, has_tracks("N Castle Town") & has_source("Snow") & soft_cannon],
        ["snow bridge mid", "snow bridge south", True, has_tracks("Snow Realm Bridge")],
        ["snow bridge north", "snow bridge mid", True, has_tracks("Snow Realm Bridge")],
        ["wtt", "snow bridge south", True, has_temple_tracks("Wooded") & has_tracks("Snow Realm Bridge") & soft_cannon],
        ["snow bridge north", "snow realm", True, has_glyph("Snow") & has_tracks("Snow Realm Bridge")],
        ["snow bridge north", "snow realm source", True, has_source("Snow") & has_tracks("Snow Realm Bridge")],
        ["snow bridge north", "snow bridge portal", False, has_cannon],

        ["wtt", "forest ferrus", False, has_passenger("Ferrus", "_ferrus_3")],
        ["forest source", "forest ferrus", False, has_passenger("Ferrus", "_ferrus_3")],

        # # ======== Castle Town =========

        ["castle station", "castle town", False, has_glyph("Forest")],
        ["castle town", "castle station", False, None],
        ["forest realm", "castle station", True, has_glyph("Forest")],
        ["castle town", "castle town goron", False, has_passenger("City Goron", "_goron")],
        ["castle town", "pick up alfonzo", False, has_glyph("Snow")],
        ["castle town", "castle town teacher", False, has_glyph("Snow") | has_glyph("Ocean") | has_glyph("Fire")],
        ["pick up alfonzo", "alfonzo event", False, None],
        ["mona's house", "castle town mona", False, has_glyph("Snow")],
        ["castle town", "castle town fish", False, has_cargo("Fish", "_buy_fish")],

        ["castle town", "castle town wall", False, has_bombs],
        ["castle town wall", "castle town stamp station", False, has_stamp_book],
        ["castle town wall", "castle town cuccos", False, ct_cuccos],

        ["castle town", "lucia's house", True, None],
        ["castle town", "mona's house", True, None],
        ["castle town", "shitate's shop", True, None],
        ["castle town", "milo's house", True, None],
        ["castle town", "teao", True, None],

        ["teao", "teao rupees", False, has_rupees(150) | ool],
        ["teao rupees", "teao 1", False, And(
             has_sword,
             has_whirlwind,
             Or(has_source("Forest"), has_source("Ocean"), has_source("Sand")))],
        ["teao rupees", "teao 2", False, And(
            has_source("Ocean") | has_source("Sand"),
            has_sword,
            has_whirlwind,
            has_boomerang,
            has_whip)
         ],
        ["teao rupees", "teao 3", False, And(
            has_source("Sand"),
            has_sword,
            has_whirlwind,
            has_boomerang,
            has_whip,
            has_bow,
            has_sand_wand)],
        ["teao 3", "teao_event", False, None],

        # # ======== Hyrule Castle =========

        ["castle town", "hyrule castle courtyard", True, None],
        ["hyrule castle courtyard", "hyrule castle 1f", True, None],
        ["hyrule castle 1f", "hyrule castle throne room", True, None],
        ["hyrule castle 1f", "hyrule castle barracks", True, None],
        ["hyrule castle 1f", "hyrule castle infirmary", True, None],
        ["hyrule castle 1f", "hyrule castle roof left", True, None],
        ["hyrule castle 1f", "hyrule castle roof right", True, None],

        ["hyrule castle roof left", "hyrule castle roof right", True, None],
        ["hyrule castle roof right", "hyrule castle ne ledge", False, None],
        ["hyrule castle ne ledge", "hyrule castle courtyard", False, None],
        ["hyrule castle roof right", "hyrule castle 2f", True, None],

        ["hyrule castle 2f", "hyrule castle ne ledge", True, None],
        ["hyrule castle 2f", "hyrule castle nw ledge", True, None],
        ["hyrule castle throne room", "hyrule castle 2f left", True, None],
        ["hyrule castle throne room", "hyrule castle 2f", True, None],
        ["hyrule castle 2f left", "hyrule castle 2f", True, None],
        ["hyrule castle 2f", "zelda's room", True, None],
        ["hyrule castle 2f", "hyrule castle backdoor", True, None],

        ["hyrule castle barracks", "hyrule castle sword minigame", False, has_sword & has_source("Snow") & has_rupees(100)],

        # # ======== ToS Tunnel =========

        ["hyrule castle backdoor", "hyrule castle backyard", True, None],
        ["hyrule castle backyard", "tower tunnel 1f", False, None],
        ["tower tunnel 1f", "tower tunnel block chest", False, can_kill_bat_pit | has_whirlwind | hard_logic],
        ["tower tunnel 1f", "tower tunnel key door", True, has_small_keys("Tunnel to ToS", 1)],
        ["tower tunnel key door", "tower tunnel 2f", True, None],

        ["tower tunnel 2f", "tower tunnel 2f north", False, None],
        ["tower tunnel 2f north", "tower tunnel 2f", False, has_bombs],
        ["tower tunnel 2f north", "tower tunnel 2f door", False, can_kill_bat],
        ["tower tunnel 2f door", "tower tunnel 2f north", False, None],
        ["tower tunnel 2f door", "tower tunnel 3f", False, can_kill_bat],
        ["tower tunnel 3f", "tower tunnel 2f door", False, None],

        ["tower tunnel 3f", "tower tunnel 3f north", True, has_damage],
        ["tower tunnel 3f north", "tos", False, None],

        # # ========== ToS ===================

        ["forest realm", "tos forest station", True, can_enter_tos & has_glyph("Forest")],
        ["forest source", "tos forest station", True, can_enter_tos & has_source("Forest")],
        ["snow realm source", "tos snow station", True, can_enter_tos & has_source("Snow") & soft_cannon],
        ["ocean realm source", "tos ocean station", True, can_enter_tos & has_source("Ocean")],
        ["fire source", "tos fire station", True, can_enter_tos & has_source("Fire")],

        ["tos forest station", "tos", True, None],  # TODO: Figure out what unlocks exits from the inside
        ["tos snow station", "tos", True, None],
        ["tos ocean station", "tos", True, None],
        ["tos fire station", "tos", True, None],


        ["tos", "tos 1f", True, None],
        ["tos", "tos 2", False, can_enter_tos_section(2)],
        ["tos", "tos 3", False, can_enter_tos_section(3)],
        ["tos", "tos 4", False, can_enter_tos_section(4)],
        ["tos", "tos 5", False, can_enter_tos_section(5)],
        ["tos 5", "tos 23f", False, None] if world.exclude_tos_5 else None,

        ["tos 1f", "tos 1f chest", False, has_range | has_sword_beam],
        ["tos 1f", "tos 1f switch", False, can_kill_bat | can_possess_phantom(1)], # Phantom can hit switch
        ["tos 1f", "tos 2f", False, can_possess_phantom(1) | vanilla_tears],
        ["tos 2f", "tos 2f raised chests", False, has_whirlwind | glitched_logic],
        ["tos 2f", "tos 2f bomb wall", False, has_bombs],
        ["tos 2f", "tos 3f rail map", False, None],
        ["tos 3f rail map", "goal_forest_glyph", False, None],
        ["tos 3f rail map", "event_3f", False, None],

        ["tos 2", "tos 4f", True, None],
        ["tos 4f", "tos 4f whirlwind", False, has_whirlwind],
        ["tos 4f", "tos 5f phantom", False, can_possess_phantom(2) | (vanilla_tears & has_whirlwind)],
        ["tos 5f phantom", "tos 5f spinnit key", False, has_whirlwind],
        ["tos 5f spinnit key", "tos 5f alt path", False, has_boomerang],
        ["tos 5f alt path", "tos 5f secret chest", False, has_bombs],
        ["tos 5f alt path", "tos 4f ne chest", False, has_bombs], # needs whirlwind and boomerang to get here
        ["tos 5f alt path", "tos 6f chests", False, None], # geozards only need sword + phantom
        ["tos 5f spinnit key", "tos 6f key", False, has_small_keys("ToS 2", 1)], # already have whirlwind
        ["tos 6f key", "tos 7f rail map", False, has_small_keys("ToS 2", 2)],
        ["tos 7f rail map", "goal_snow_glyph", False, None],
        ["tos 7f rail map", "event_7f", False, None],

        ["tos 3", "tos 8f", True, None],
        ["tos 8f", "tos 8f bombs", False, has_bombs],
        ["tos 8f", "tos 9f phantom", False, vanilla_tears | can_possess_phantom(3)], #
        ["tos 9f phantom", "tos 9f nw", False, has_whirlwind],
        ["tos 9f phantom", "tos 11f", False, has_damage & (has_boss_key("ToS 3") | vanilla_boss_keys)],
        ["tos 11f", "event_12f", False, None],
        ["tos 11f", "goal_ocean_glyph", False, None],

        ["tos 4", "tos 13f", True, None],
        ["tos 13f", "tos 13f whip", False, has_whip],
        ["tos 13f", "tos 13f boomerang", False, has_boomerang],
        ["tos 13f", "tos 14f east", False, has_small_keys("ToS 4", 3, 1) | (vanilla_tears & has_small_keys("ToS 4", 2, 1))],
        ["tos 13f", "tos 13f phantom", False, can_possess_phantom(4)
            | (vanilla_tears & has_whip & has_small_keys("ToS 4", 2, 1))],
        ["tos 13f phantom", "tos 13f phantom whip", False, has_whip],
        ["tos 13f phantom", "tos 14f west", False, has_small_keys("ToS 4", 2, 1) ],

        ["tos 14f east", "tos 14f phantom", False, can_possess_phantom(4) | (vanilla_tears & has_whip)],
        ["tos 14f west", "tos 15f", False, has_whip],
        ["tos 15f", "tos 16f", False, tos_15f_glitched],
        ["tos 16f", "tos 16f bombs", False, has_bombs],
        ["tos 16f", "event_17f", False, None],
        ["tos 16f", "goal_fire_glyph", False, None],

        ["tos 5", "tos 18f", True, None],
        ["tos 18f", "tos 18f whip", False, has_whip],
        ["tos 18f", "tos 19f", False, has_small_keys("ToS 5", 1)],
        ["tos 18f", "tos 18f phantom", False, can_possess_phantom(5)],
        ["tos 18f phantom", "tos 19f center", False, None],

        ["tos 19f", "tos 19f south", False, has_bow & (has_boomerang | (can_possess_phantom(5) & can_rotate_repeater))],
        ["tos 19f south", "tos 20f tear", False, has_boomerang | has_sword_beam | (
            hard_logic & can_rotate_repeater & (
                can_possess_phantom(5) | has_whip))],
        ["tos 19f", "tos 19f center", False, can_possess_phantom(5) | (vanilla_tears & has_bow & has_boomerang)],
        ["tos 19f center", "tos 19f center chest", False, has_bow & (has_boomerang | has_sword_beam | has_whip)],
        ["tos 19f center", "tos 18f phantom", False, None],
        ["tos 19f center", "tos 20f", False, has_small_keys("ToS 5", 2) | (not_vanilla_tears & has_small_keys("ToS 5", 2, 1))],

        ["tos 20f", "tos 19f center 2", False, has_bow & can_rotate_repeater],
        ["tos 20f", "tos 19f center chest", False, has_bow],
        ["tos 20f", "tos 22f", False, has_bow & can_rotate_repeater & has_whip],
        ["tos 22f", "tos 21f bombs", False, has_bombs],
        ["tos 22f", "tos 23f", False, has_boss_key("ToS 5") | (vanilla_boss_keys & (has_bow | has_sword_beam))],
        ["tos 23f", "tos staven", False, has_sword],
        ["tos staven", "event_staven", False, None],
        ["tos staven", "goal_staven", False, None],

        ["tos staven", "tos summit lower", True, None],
        ["tos summit lower", "tos summit", True, None],
        ["tos summit", "tos stamp stand", False, has_stamp_book],
        ["tos summit", "tos 6", False, has_bow_of_light],
        ["tos 30f", "tos 6", True, None],

        ["tos 30f", "tos 30f bomb wall", False, has_bombs],
        ["tos 30f", "tos 29f", False, can_possess_phantom(6) & has_boomerang & has_whirlwind],
        ["tos 29f", "tos 29f sand wand", False, has_sand_wand],
        ["tos 29f sand wand", "tos 29f se", False, has_bow_of_light],

        ["tos 29f se", "tos 27f", False, has_small_keys("ToS 6", 3)],
        ["tos 27f", "tos 24f", False, has_whip],
        ["tos 29f", "tos 24f", False, glitched_logic & has_bombs & has_small_keys("ToS 6", 3, 1)],
        ["tos 24f", "event_24f", False, None],
        ["tos 24f", "goal_compass", False, None],

        # # ======== Mayscore =========

        ["forest realm", "mayscore station", True, has_glyph("Forest")],
        ["mayscore station", "mayscore", False, has_glyph("Forest")],
        ["mayscore", "mayscore station", False, None],
        ["mayscore", "mayscore north", True, None],

        ["mayscore", "uriko's shop", True, None],
        ["mayscore", "morris' house", True, None],
        ["mayscore", "dovok's house", True, None],
        ["mayscore", "wood's house", True, None],

        ["mayscore north", "mayscore stamp station", False, has_stamp_book],
        ["mayscore north", "mayscore whip chest", False, has_whip],
        ["mayscore whip chest", "mayscore whip game", False, has_rupees(200)],
        ["mayscore", "mayscore leaves", False, has_whirlwind],
        ["mayscore north", "mayscore leaves", False, has_whirlwind],

        ["dovok's house", "mayscore dovok", False, has_glyph("Ocean")],
        ["mayscore whip chest", "mayscore wood", False, has_glyph("Ocean")],
        ["mayscore", "mayscore steel", False, has_cargo("Goron Steel", "_buy_steel")],
        ["morris' house", "mayscore morris", False, has_glyph("Ocean")],
        ["mayscore", "mayscore quest", False, has_glyph("Ocean")],

        # # ======== Forest Sanctuary =========

        ["forest realm", "woodland sanc station", True, has_glyph("Forest")],
        ["woodland sanc station", "woodland sanc", False, has_glyph("Forest")],
        ["woodland sanc", "woodland sanc station", False, None],
        ["woodland sanc", "woodland sanc stamp station", False, has_stamp_book],
        ["woodland sanc", "woodland sanc song statue", False, has_spirit_flute],
        ["woodland sanc", "woodland sanc sanc", False, None],
        ["woodland sanc sanc", "woodland sanc duet", False, has_spirit_flute],
        ["woodland sanc", "woodland sanc chest", False, has_cuccos],

        # # ======== Wooded Temple =========

        ["wtt", "wt station", True, has_temple_tracks("Wooded")],
        ["forest source", "wt station", True, has_source("Forest")],
        ["wt station", "wt", False, has_temple_tracks("Wooded") | has_source("Forest")],
        ["wt", "wt station", False, None],
        ["wt", "wt stamp station", False, has_stamp_book & (has_whirlwind | hard_logic)],
        ["wt", "wt song statue", False, has_spirit_flute],
        ["wt", "wt 1f enemy chest", False, has_damage],
        ["wt 1f enemy chest", "wt 1f key", False, has_whirlwind],
        ["wt 1f enemy chest", "wt 2f enemy chest", False, None],
        ["wt 1f enemy chest", "wt 2f poison chest", False, has_whirlwind | hard_logic],
        ["wt", "wt 1f switch chest", False, has_whirlwind | hard_logic],

        ["wt", "wt 2f left", False, can_kill_bubble & has_small_keys("Wooded Temple", 1)],
        ["wt 2f left", "wt 3f chestnut chest", False, has_range_objects | has_sword_beam],
        ["wt 2f left", "wt 3f", False, has_small_keys("Wooded Temple", 2)],
        ["wt 3f", "wt 3f se chest", False, has_whirlwind | hard_logic],

        ["wt 3f", "wt 3f bk", False, has_whirlwind | (has_bombs & hard_logic)],
        ["wt 3f bk", "wt 4f", False, None]
            if world.options.randomize_boss_keys.value == 0 else
            ["wt 3f", "wt 4f", False, has_boss_key("Wooded Temple")],
        ["wt 4f", "wt stagnox", False, has_sword & has_whirlwind],
        ["wt stagnox", "goal_stagnox", False, None],
        ["wt stagnox", "event_stagnox", False, None]
    ]

    overworld_logic += [

        # # ============ Trading Post =============

        ["forest realm", "trading post tracks", True, has_glyph("Ocean") & soft_cannon & has_glyph("Forest")],
        ["trading post tracks", "trading post station", True, has_glyph("Ocean")],
        ["trading post station", "trading post", False, has_glyph("Ocean")],
        ["trading post", "trading post station", False, None],

        ["trading post", "linebeck's shop", True, None],
        ["trading post", "trading post tunnel", True, None],
        ["trading post north", "trading post tunnel", True, None],
        ["trading post north", "trading post island", True, has_range | has_sword_beam],
        ["trading post island", "trading post cave", False, has_range | has_sword_beam | has_bombs],
        ["trading post cave", "trading post island", False, None],

        ["trading post north", "trading post light song statue", False, has_spirit_flute],
        ["trading post cave", "trading post chest", False, has_sod & (has_sol | hard_logic)],
        ["trading post tunnel", "trading post stamp station", False, has_bombs & has_stamp_book],
        ["trading post north", "trading post leaves", False, has_whirlwind],

        ["trading post", "trading post bridge worker", False, has_passenger("Kenzo", "_kenzo_1")],
        ["trading post bridge worker", "linebeck trading", False, Has("Treasure: Regal Ring", player)]
            if world.options.randomize_passengers.value else
            ["trading post", "linebeck trading", False, Has("Treasure: Regal Ring")],
        ["linebeck trading", "linebeck event", False, None],
        ["trading post", "trading post pick up kenzo", False, Has("_can_sell_treasure") & has_glyph("Snow")],
        ["linebeck's shop", "linebeck dark ore", False, Has("_can_sell_treasure") & has_cargo("Dark Ore", "_buy_ore")],

        # # ========== Rabbit Haven ========

        ["snow realm fr", "rabbit haven station", True, has_glyph("Snow")],
        ["rabbit haven station", "rabbit haven", False, has_glyph("Snow")],
        ["rabbit haven", "rabbit haven station", False, None],

        ["rabbit haven", "rabbit haven 5 rabbits", False, has_total_rabbits(5)],
        ["rabbit haven", "rabbit haven 10 forest rabbits", False, has_rabbit_items("Grass", 10)],
        ["rabbit haven", "rabbit haven 10 snow rabbits", False, has_rabbit_items("Snow", 10)],
        ["rabbit haven", "rabbit haven 10 ocean rabbits", False, has_rabbit_items("Ocean", 10)],
        ["rabbit haven", "rabbit haven 10 mountain rabbits", False, has_rabbit_items("Mountain", 10)],
        ["rabbit haven", "rabbit haven 10 sand rabbits", False, has_rabbit_items("Sand", 10)],
        ["rabbit haven", "rabbit haven 50 rabbits", False, DebugRule()],
        ["rabbit haven", "rabbit haven 1 of each rabbits", False, has_all_rabbit_types],
        ["rabbit haven", "rabbit haven mona", False, has_passenger("Mona", "_mona")],

        # # ============ Snow Realm ===============

        ["snow realm south", "snow realm fr", True, has_glyph("Snow")],
        ["snow realm south", "snow realm", True, soft_cannon],
        ["snow realm south", "anouki portal", False, has_cannon],
        ["snow realm", "blizzard temple tracks", True, has_temple_tracks("Blizzard") & has_glyph("Snow")],
        ["snow realm", "snow realm rabbits", False, has_net],
        ["blizzard temple tracks", "blizzard temple tracks rabbits", False, has_net],
        ["blizzard temple tracks rabbits", "snow realm blizzard rabbits", False, has_source("Snow")],
        ["blizzard temple tracks rabbits", "snow realm early blizzard rabbits", False, has_source("Snow") | hard_logic],
        ["snow realm source", "blizzard temple tracks", True, has_source("Snow") & has_temple_tracks("Blizzard")],

        ["snowdrift tracks", "snowdrift station rabbit", False, has_net],
        ["blizzard temple tracks", "icyspring tracks", True, has_tracks("N Icy Spring") & has_temple_tracks("Blizzard")],
        ["icyspring tracks", "icyspring rabbits", False, has_net],
        ["icyspring tracks", "icyspring portal", False, has_cannon],

        ["blizzard temple tracks", "snow realm ferrus", False, 
            has_source("Snow") & has_passenger("Alfonzo", "_picked_up_alfonzo")],

        ["forest realm se portal track", "blizzard temple tracks", False, has_temple_tracks("Blizzard") & has_portal("Trading Post to E Snow Realm", True)],
        ["blizzard temple tracks", "forest realm se portal track", False, has_tracks("Forest Realm SE Portal") & has_portal("Trading Post to E Snow Realm", False)],
        ["forest realm se portal track", "trading post portal", False, has_cannon],

        # ======== Anouki Village ========

        ["snow realm", "anouki station", True, has_glyph("Snow")],
        ["anouki station", "anouki village", False, has_glyph("Snow")],
        ["anouki village", "anouki station", False, None],

        ["anouki village", "honcho's house", True, None],
        ["anouki village", "bulu's house", True, None],
        ["anouki village", "kofu's house", True, None],
        ["anouki village", "noko's house", True, None],
        ["anouki village", "yefu's house", True, None],
        ["anouki village", "yeko's house", True, None],
        ["anouki village", "ice block cave", False, has_bombs],
        ["ice block cave", "anouki village", False, None],

        ["anouki village", "anouki village stamp station", False, has_stamp_book],
        ["anouki village", "anouki village song statue", False, has_spirit_flute],
        ["anouki village", "anouki village lake chest", False, has_boomerang],

        ["anouki village", "av noko", False, has_temple_tracks("Blizzard")],
        ["anouki village", "av fence", False, (
                has_passenger("Kenzo", "_kenzo_2") | no_passengers
            ) & (
                has_cargo("Lumber", "_buy_lumber") | no_cargo)],
        ["anouki village", "av kenzo", False, (has_passenger("Kenzo", "_kenzo_2") | no_passengers)
        | (has_cargo("Lumber", "_buy_lumber") | no_cargo)],
        ["anouki village", "av goron", False, has_passenger("Snow Goron", "_goron")],
        ["honcho's house", "av kofu", False, (has_glyph("Fire") | has_source("Fire")) & Has("_av_goron")],

        # =========== Snow Sanctuary ==========

        ["snow realm", "snow sanc tracks", False, Has("Snow Sanctuary Cave Key") & has_cannon],
        ["snow sanc tracks", "snow realm", False, has_cannon],
        ["blizzard temple tracks", "snow sanc tracks", True, has_temple_tracks("Blizzard") & has_glyph("Snow")],
        ["snow sanc tracks", "snow sanc station", True, has_glyph("Snow")],
        ["snow sanc station", "snow sanc", False, has_glyph("Snow")],
        ["snow sanc", "snow sanc station", False, None],

        ["snow sanc", "snow sanc stamp station", False, has_stamp_book],
        ["snow sanc", "snow sanc cave", True, None],
        ["snow sanc", "snowfall supermarket", True, None],
        ["snow sanc cave", "snow sanc sanc", True, None],
        ["snow sanc sanc", "snow sanc song", False, has_spirit_flute],
        ["snow sanc song", "steem gift", False, has_source("Snow")]
            if world.options.randomize_minigames.value else
            ["snow sanc sanc", "steem gift", False, has_source("Snow")],
        ["snow sanc", "snow sanc vessel", False, has_cargo("Vessel", "_buy_vessel")],
        ["snow sanc vessel", "snow sanc sanc", False, ool],

        ## ========== Blizzard Temple =========

        ["snow realm source", "bt station", True, has_source('Snow') & soft_cannon],
        ["blizzard temple tracks", "bt station", True, has_temple_tracks("Blizzard")],
        ["bt station", "bt", False, has_temple_tracks("Blizzard") | has_source('Snow')],
        ["bt", "bt station", False, None],

        ["bt", "bt b1 se", False, can_ring_bell & has_whirlwind],
        ["bt b1 se", "bt b1 e enemy chest", False, None],
        ["bt b1 se", "bt b1 ne enemy chest", False, can_kill_bubble],
        ["bt b1 se", "bt 1f ne chest", False, has_short_range | has_boomerang],
        ["bt 1f ne chest", "bt b1 sw chest", False, has_boomerang],
        ["bt b1 sw chest", "bt west", False, has_small_keys("Blizzard Temple", 1) & can_kill_freezards_torch],
        ["bt west", "bt stamp station", False, has_stamp_book],
        ["bt west", "bt 3f", False, has_boss_key("Blizzard Temple") | vanilla_boss_keys],
        ["bt 3f", "bt fraaz", False, has_sword],
        ["bt fraaz", "goal_fraaz", False, None],
        ["bt fraaz", "event_fraaz", False, None],

        # ========== Icy Spring ==========

        ["blizzard temple tracks", "icyspring station", True, has_temple_tracks("Blizzard")],
        ["icyspring station", "icyspring", False, has_temple_tracks("Blizzard")],
        ["icyspring", "icyspring station", False, None],

        ["icyspring", "ferrus' trailer", True, None],
        ["icyspring", "icyspring stamp station", False, has_stamp_book & has_boomerang],
        ["icyspring", "icyspring whip chest", False, has_whip],
        ["icyspring", "icyspring noko", False, has_temple_tracks("Blizzard") & (# for ferrus logic
                has_passenger("Noko", "_noko") | no_passengers)],

        # ============ Snowdrift Station =========

        ["blizzard temple tracks", "snowdrift tracks", True, has_tracks("Snowdrift Station") & soft_cannon & has_temple_tracks("Blizzard")],
        ["snowdrift tracks", "snowdrift station", True, has_tracks("Snowdrift Station")],
        ["snowdrift station", "snowdrift", False, has_tracks("Snowdrift Station")],
        ["snowdrift", "snowdrift station", False, None],
        ["snowdrift", "snowdrift cave", True, None],
        ["snowdrift cave", "snowdrift reward", False, (has_range | (has_sword_beam & hard_logic)) & can_kill_freezards],

        ["snowdrift cave", "octive arena", True, None],
        ["snowdrift cave", "frostflame cave", True, None],
        ["snowdrift cave", "small skating", True, None],
        ["snowdrift cave", "big ice puzzle", True, None],

        # ========== Slippery Station ==========
        ["slippery tracks", "slippery station", True, has_tracks("Slippery Station")],
        ["slippery station", "slippery", False, has_tracks("Slippery Station")],
        ["slippery", "slippery station", False, None],
        ["blizzard temple tracks", "slippery tracks", True, has_tracks("Slippery Station") & has_temple_tracks("Blizzard") & soft_cannon & (has_source("Snow") | has_tracks("N Icy Spring"))],
        ["skating rink", "slippery station", True, None],
        ["skating rink", "slippery amateur", False, None],
        ["skating rink", "slippery pro", False, None],
        ["skating rink", "slippery champion", False, None],

        # ========== Bridge Worker's Home =======
        ["snow realm source", "bridge workers station", True, has_source("Snow")],
        ["bridge workers station", "bridge workers", False, has_source("Snow")],
        ["bridge workers", "bridge workers station", False, None],
        ["bridge workers", "bridge workers chest", False, has_sod],
        ["bridge workers", "kenzo's house", True, None],
        ["kenzo's house", "pick up bridge worker", False, has_glyph("Ocean")],

        # ========== Ocean Realm =============
        ["forest realm", "e mayscore bridge", True, has_tracks("E Mayscore Bridge") & has_glyph("Forest")],
        ["e mayscore bridge", "ocean realm mid", True, has_glyph("Ocean") & has_tracks("E Mayscore Bridge")],
        ["forest realm", "ocean shortcut", True, has_tracks("Forest Realm Ocean Shortcut") & has_glyph("Forest")],
        ["forest source", "ocean shortcut", True, has_tracks("Forest Realm Ocean Shortcut") & has_source("Forest")],
        ["ocean shortcut east", "pirate hideout tracks", True, has_tracks("Forest Realm Ocean Shortcut") & has_tracks("Pirate Hideout")],
        ["e mayscore bridge", "ocean shortcut", True, has_tracks("Forest Realm Ocean Shortcut") & has_tracks("E Mayscore Bridge")],
        ["ocean shortcut east", "ocean shortcut", True, has_tracks("Forest Realm Ocean Shortcut")],

        ["trading post tracks", "ocean realm mid", True, Has("Repair Trading Post Bridge") & has_glyph("Ocean")],
        ["ocean realm mid", "ocean realm", True, has_glyph("Ocean")],
        ["ocean realm", "ocean temple tracks", True, has_temple_tracks("Marine") & has_glyph("Ocean")],
        ["ocean temple tracks", "ocean realm source", True, has_source("Ocean") & has_temple_tracks("Marine")],
        ["ocean realm", "pirate hideout tracks", True, has_tracks("Pirate Hideout") & has_glyph("Ocean")],
        ["ocean realm source", "pirate hideout tracks", True, has_source("Ocean") & has_tracks("Pirate Hideout")],
        ["ocean realm source", "ocean portal tracks", True, has_source("Ocean") & has_tracks("Ocean Portal")],
        ["ocean temple tracks", "ocean portal tracks", True, has_temple_tracks("Marine") & has_tracks("Ocean Portal")],
        ["ocean portal tracks", "sand realm", False, has_tracks("Sand Realm") & has_tracks("Ocean Portal")],
        ["ocean portal tracks", "ocean portal", False, has_cannon],

        ["ocean temple tracks", "undersea entrance", True, has_temple_tracks("Marine")],
        ["ocean realm source", "undersea entrance", True, has_source("Ocean")],
        ["undersea entrance", "undersea tracks", True, has_temple_tracks("Marine") | has_source("Ocean")],
        ["undersea tracks", "oct station", True, has_temple_tracks("Marine") | has_source("Ocean")],

        # Ocean Portals
        ["trading post tracks", "ocean portal tracks", False, 
            has_tracks("Ocean Portal") & has_portal("Mayscore to Ocean Portal Tracks",False)],
        ["ocean portal tracks", "trading post tracks", False, has_glyph("Ocean")
         & has_portal("Mayscore to Ocean Portal Tracks", True)],
        ["snow bridge north", "ocean temple tracks", False, has_temple_tracks("Marine")
         & has_portal("Snow Bridge to Island Sanctuary", True)],
        ["ocean temple tracks", "snow bridge north", False, has_tracks("Snow Realm Bridge")
         & has_portal("Snow Bridge to Island Sanctuary", False)],

        # Ocean Rabbits
        ["ocean temple tracks", "ocean rabbits", False, has_net],
        ["las tracks", "las rabbit", False, has_net],
        ["ocean realm source", "ocean source rabbits", False, has_net],
        ["ocean portal tracks", "ocean portal rabbits", False, has_net],
        ["ocean shortcut east", "pirate rabbit", False, has_net],

        # ========== Island Sanctuary =============
        ["ocean realm", "island sanc station", True, has_glyph("Ocean")],
        ["island sanc station", "island sanc", False, has_glyph("Ocean")],
        ["island sanc", "island sanc station", False, None],

        ["island sanc", "island sanc peninsula", False, has_sob & has_whip & hard_logic],
        ["island sanc peninsula", "island sanc", False, None],
        ["island sanc peninsula", "island sanc north", True, None],
        ["island sanc", "island sanc S island chest", False, hard_birds],

        ["island sanc", "island sanc cave west", True, None],
        ["island sanc cave west", "island sanc cave east", False, has_boomerang],
        ["island sanc cave east", "island sanc cave west", False, has_bombs],
        ["island sanc cave west", "island sanc north", True, None],

        ["island sanc north", "island sanc nw chest", False, hard_birds],
        ["island sanc north", "island sanc stamp station", False, has_stamp_book & has_sob & has_whip],
        ["island sanc north", "island sanc sanc", False, None],
        ["island sanc sanc", "island sanc song", False, has_spirit_flute]
            if world.options.randomize_passengers == "no_passengers" else
            ["island sanc sanc", "island sanc song", False, has_spirit_flute & Has("_deliver_carben")],
        ["island sanc", "island sanc carben", False, has_passenger("Carben", "_carben")],

        # ========== Papuzia Village =============
        ["ocean realm", "papuzia village station", True, has_glyph("Ocean")],
        ["papuzia village station", "papuzia village", False, has_glyph("Ocean")],
        ["papuzia village", "papuzia village station", False, None],
        ["papuzia village", "papuzia village song statue", False, has_sod],
        ["papuzia village", "pv dovok", False, has_passenger("Dovok", "_dovok")],
        ["pv dovok", "orca's house", False, ool],
        ["pv wadatsumi", "orca's house", False, ool],

        ["papuzia village", "fuku's house", True, None],
        ["papuzia village", "wise one's house", True, None],
        ["papuzia village", "orca's house", True, None],
        ["papuzia village", "kogane's shop", True, None],

        ["papuzia village", "pv carben", False, has_sod],
        ["papuzia village", "pv wadatsumi", False, has_passenger("Wadatsumi", "_wadatsumi")],
        ["papuzia village song statue", "papuzia village south", False, hard_birds],
        ["papuzia village south", "papuzia village", False, Has("_papuzia_sob") & hard_birds],
        ["papuzia village south", "papuzia archipelago north", True, None],
        ["papuzia archipelago north", "papuzia archipelago", False, hard_birds],
        ["papuzia archipelago", "papuzia village stamp station", False, has_stamp_book & has_sob],
        # You need a warp to start to return without bird song, patched with a dynaentrance
        # I don't like that this is locked behind song statue, but flags might not let us get there earlier

        ["papuzia village", "papuzia ice", False, has_cargo("Mega Ice", "_buy_ice")]
        if world.options.randomize_cargo.value in [1, 2] else
        ["papuzia village", "papuzia ice", False, has_wagon
             & (Has("Cargo: Mega Ice", 3) | (Has("Cargo: Mega Ice", 1) & ool))],

        # ========= Marine Temple ==================
        ["oct station", "oct", False, has_temple_tracks("Marine") | has_source("Ocean")],
        ["oct", "oct station", False, None],
        ["oct", "oct song statue", False, has_spirit_flute],
        ["oct 2f", "oct whip chest", False, has_sword | (hard_logic & (has_bombs | (has_boomerang & has_damage)))],
        # you can't escape stunlock without sword, and the fight scripts you into it from the start
        ["oct", "oct whip", False, has_whip],
        ["oct", "oct 2f", None, Or(
            has_whip,
            can_kill_bat,
            hard_logic # damageboost through the boulders
        )],
        ["oct", "oct stamp station", False, has_stamp_book & has_whip & has_bombs & has_boomerang],
        ["oct whip chest", "oct 3f whip", False, has_whip],
        ["oct 3f whip", "oct 6f chest", False, has_small_keys("Marine Temple", 1)],
        ["oct 6f chest", "oct bk", False, has_small_keys("Marine Temple", 2) |
                                                        And(glitched_logic,
                                                             has_whirlwind,
                                                             has_bombs)],
        ["oct 6f chest", "oct bk loc", False, has_whirlwind & hard_logic],
        ["oct bk", "oct bk loc", False, None],
        ["oct bk", "oct phytops", False, None]
            if world.options.randomize_boss_keys == 0 else
            ["oct 6f chest", "oct phytops", False, has_boss_key("Marine Temple")],
        ["oct phytops", "event_phytops", False, None],
        ["oct phytops", "goal_phytops", False, None],

        ["oct", "oct ferrus", False, has_passenger("Ferrus", "_ferrus_2")
                       & (randomize_passengers | ool | Has("_ferrus_backup"))],
        # If you fail the train journey in vanilla, make sure you have access to icyspring for backup.

        # ========= Pirate Hideout ==============
        ["pirate hideout tracks", "pirate hideout station", True, has_tracks("Pirate Hideout")],
        ["pirate hideout station", "pirate hideout", False, has_tracks("Pirate Hideout")],
        ["pirate hideout", "pirate hideout station", False, None],
        ["pirate hideout", "pirate hideout stamp station", False, has_stamp_book & has_whip & has_sob],
        ["pirate hideout", "pirate hideout secret cave", False, has_bombs],
        ["pirate hideout secret cave", "pirate hideout", False, None],
        ["pirate hideout", "pirate hideout minigame", False, has_bow],
        # Wadatsumi able to be reached with only tracks with minigames turned off, otherwise requires bow
        ["pirate hideout", "pirate wadatsumi", False, has_glyph("Ocean")]
            if world.options.randomize_minigames.value in [0] else
            ["pirate hideout", "pirate wadatsumi", False, has_bow & has_glyph("Ocean")],
        # First hideout minigame gives you bow automatically, and then it shows in top right, even with no items, but doesn't let you use it. With an item, it doesn't show

        # ======== Lost at Sea Station ==========
        ["ocean temple tracks", "las tracks", True, has_temple_tracks("Marine") & has_tracks("Lost at Sea Station")],
        ["las tracks", "lost at sea station", True, has_tracks("Lost at Sea Station")],
        ["lost at sea station", "lost at sea", False, has_tracks("Lost at Sea Station")],
        ["lost at sea", "lost at sea station", False, None],

        ["lost at sea", "las outside chest", False, has_sod & (has_sol | hard_logic)],
        ["lost at sea", "las cliff", False, hard_birds],
        ["las cliff", "lost at sea", False, None],
        ["lost at sea", "las lobby", False, hard_logic | has_sol],
        ["las lobby", "lost at sea", False, None],
        ["las lobby", "las 1st room chest", False, has_soa],
        ["las 1st room chest", "las 2nd room chest", False, has_boomerang],
        ["las 2nd room chest", "las 3rd room chest", False, has_whirlwind],
        ["las 3rd room chest", "las 4th room chest", False, has_whip],
        ["las 4th room chest", "las 5th room", False, has_bombs | hard_logic],
        ["las 5th room", "las_event", False, None],

        # ===== Fire Realm =====
        ["gorge tracks east", "fire realm", True, has_glyph("Fire") & has_tracks("Snow Realm Gorge")],
        ["blizzard temple tracks", "gorge tracks west", True, has_tracks("Snow Realm Gorge") & has_temple_tracks("Blizzard")],
        ["gorge tracks west", "gorge tracks east", True, has_tracks("Snow Realm Gorge")],

        ["blizzard temple tracks", "fire realm west", True, has_glyph("Fire") & has_temple_tracks("Blizzard")],
        ["snow realm source", "fire realm west", True, has_glyph("Fire") & has_source("Snow")],
        ["fire realm", "fire realm west", True, has_glyph("Fire")],

        ["fire realm", "fire source", True, has_glyph("Fire") & has_source("Fire")],
        ["mountain temple tracks", "fire source", True, has_temple_tracks("Mountain") & has_source("Fire")],
        ["mountain temple tracks", "fire realm", True, has_temple_tracks("Mountain") & has_glyph("Fire")],
        ["mountain temple tracks", "ends of the earth tracks", True, has_temple_tracks("Mountain") & has_tracks("Ends of the Earth")],
        ["mountain temple tracks", "disorientation tracks", True, has_temple_tracks("Mountain") & has_tracks("Disorientation Station")],
        ["fire realm", "disorientation tracks", True, has_glyph("Fire") & has_tracks("Disorientation Station")],
        ["fire realm", "sand connection", True, has_glyph("Fire") & has_tracks("Fire Realm Sand Portal")],
        ["mountain temple tracks", "dark ore mine tracks", True, has_temple_tracks("Mountain") & has_tracks("Dark Ore Mine")],
        ["mountain temple tracks", "snurglars", True, has_cannon],
        ["fire realm", "fire realm ferrus", False, has_temple_tracks("Marine")],
        ["fire realm ferrus", "icyspring", False, ool & vanilla_passengers],

        ["fire realm", "fire realm rabbits", False, has_net],
        ["mountain temple tracks", "mountain rabbits", False, has_net],
        ["fire source", "fire source rabbits", False, has_net],
        ["disorientation tracks", "disorientation rabbits", False, has_net],
        ["fire realm", "disorientation rabbits", False, has_net],
        ["ends of the earth tracks", "eote rabbits", False, has_net],
        ["fire source", "s mountain temple rabbit", False, has_net],
        ["mountain temple tracks", "s mountain temple rabbit", False, has_net],

        ["fire realm", "forest cave tracks", False, has_tracks("Forest Realm SW Cave") & has_portal("Forest Cave to Goron Village",False)],
        ["forest cave tracks", "fire realm", False, has_glyph("Fire") & has_portal("Forest Cave to Goron Village", True)],
        ["mountain temple tracks", "icyspring tracks", False, has_tracks("N Icy Spring") & has_portal("Icy Spring to Mountain Temple",False)],
        ["icyspring tracks", "mountain temple tracks", False, has_temple_tracks("Mountain") & has_portal("Icy Spring to Mountain Temple", True)],

        # Goron Village
        ["fire realm", "goron village station", True, has_glyph("Fire")],
        ["goron village", "goron village station", False, has_glyph("Fire") | has_source("Fire")],
        ["goron village station", "goron village", False, None],
        ["fire source", "goron village station", True, has_source("Fire")],

        ["goron village", "goron whip", False, has_whip],
        ["goron whip", "goron village stamp", False, has_stamp_book],
        ["goron ice event", "valley sanc tunnel", False, has_whip],
        ["valley sanc tunnel", "valley sanc", False, has_boomerang],
        ["valley sanc", "valley sanc stamp", False, has_stamp_book],
        ["valley sanc", "valley sanc song", False, has_sol],
        ["goron ice event", "pick up gorons", False, has_glyph("Snow")],
        ["goron ice event", "gv kofu", False, has_passenger("Kofu", "_kofu")],

        ["goron village", "goron ice", False, None]
            if world.options.randomize_cargo == "no_cargo" else (
            ["goron whip", "goron ice", False, has_cargo("Mega Ice", "_buy_ice")]
                if world.options.randomize_cargo.value in [1, 2] else
                ["goron whip", "goron ice", False, has_wagon & (
                    Has("Cargo: Mega Ice", 2) | (
                        Has("Cargo: Mega Ice", 1) & ool))]
        ),

        ["goron ice", "goron ice event", False, None],
        ["goron ice event", "goron ice 2", False, None]
            if world.options.randomize_cargo.value in [0, 1, 2] else
            ["goron ice event", "goron ice 2", False, has_wagon & (
                Has("Cargo: Mega Ice", 3) | (
                    Has("Cargo: Mega Ice", 2) & ool))],

        # Goron Target Game
        ["fire realm", "goron target station", True, has_glyph("Fire")],
        ["goron target lobby", "gtr", False, has_cannon & Has("_goron_ice", player) & has_rupees(50)],
        ["goron target station", "goron target lobby", False, has_glyph("Fire")],
        ["goron target lobby", "goron target station", False, None],

        # Mountain Temple
        ["mountain temple tracks", "mountain temple door", False, None],
        ["fire source", "mountain temple door", False, None],
        ["mountain temple door", "mtt station", False, Has("Mountain Temple Snurglar Key", 3) | Has("Snurglar Keyring")],
        ["mtt station", "mtt", False, has_temple_tracks("Mountain") | has_source("Fire")],
        ["mtt", "mtt station", False, None],
        ["mtt station", "mountain temple tracks", False, has_temple_tracks("Mountain")],
        ["mtt station", "fire source", False, has_source("Fire")],

        ["mtt", "mtt song statue", False, has_spirit_flute],
        ["mtt", "mtt left", False, has_damage],
        ["mtt left", "mtt right", False, has_range | has_bombs],
        ["mtt left", "mtt 2f right", False, has_range | has_sword | has_whip],
        ["mtt", "mtt center", False, mtt_center],
        ["mtt center", "mtt heatoise", False, has_good_damage],
        ["mtt heatoise", "mtt 1f ne", False, has_bow],
        ["mtt 1f ne", "mtt b1", False, can_rotate_repeater],
        ["mtt b1", "mtt b2", False, has_whip],
        ["mtt b2", "mtt b1 arena", False, has_boomerang],
        ["mtt b1", "mtt b1 cart", False, has_small_keys("Mountain Temple", 3, 1)],
        # ["mtt b1 cart", "mtt b1 arena", False, None], # Removed!
        ["mtt b1 cart", "mtt stamp", False, has_stamp_book],
        ["mtt b1 cart", "mtt bk", False, has_whirlwind],
        ["mtt bk", "mtt boss", False, None] if world.options.randomize_boss_keys.value == 0 else
        ["mtt b1 cart", "mtt boss", False, has_boss_key("Mountain Temple")],
        ["mtt boss", "defeat vulcano", False, Or(
            has_sword,
            has_whip,
            Has("Bombs (Progressive)", 2))],
        ["defeat vulcano", "event_vulcano", False, None],
        ["defeat vulcano", "goal_vulcano", False, None],

        # Disorientation Station
        ["disorientation tracks", "disorientation station station", True, has_tracks("Disorientation Station")],
        ["disorientation station", "disorientation station station", False, None],
        ["disorientation station station", "disorientation station", False, has_tracks("Disorientation Station")],
        ["disorientation station", "disorientation bird", False, hard_birds],
        ["disorientation bird", "disorientation sod", False, has_sod],

        # Ends of the Earth
        ["ends of the earth tracks", "ends of the earth station", True, has_tracks("Ends of the Earth")],
        ["ends of the earth station", "ends of the earth", False, has_tracks("Ends of the Earth")],
        ["ends of the earth", "ends of the earth station", False, None],
        ["ends of the earth", "eote puzzles", False, None],

        # ===== Sand Realm =====
        ["ocean realm source", "sand realm", True, has_source("Ocean") & has_tracks("Sand Realm")],
        ["sand realm", "sand connection south", True, has_tracks("Sand Realm") & has_tracks("Fire Realm Sand Portal")],
        ["sand connection south", "sand connection", True, has_tracks("Sand Realm") & has_tracks("Fire Realm Sand Portal")],

        ["sand realm exit", "sand restoration rocktite", False, has_temple_tracks("Desert")],
        ["sand restoration rocktite", "sand realm exit", False, has_temple_tracks("Desert")],
        ["sand realm", "sand realm exit", True, has_temple_tracks("Desert") & has_tracks("Sand Realm")],
        ["sand restoration rocktite", "sand restoration", True,  has_temple_tracks("Desert") & (has_cannon | [OptionFilter(SpiritTracksShuffleTrainTransitions, 0, "ne")])],
        ["sand restoration", "sand restoration south", True, has_temple_tracks("Desert")],

        ["sand realm", "sand realm rabbits", False, has_net],
        ["sand restoration", "sand restoration rabbits", False, has_net],
        ["sand restoration south", "sand restoration south rabbits", False, has_net],
        ["sand connection", "sand connection rabbit", False, has_net],

        ["sand restoration south", "sand restoration portal", True, has_cannon],
        ["sand connection", "sand connection portal", True, has_cannon],
        ["sand realm", "sand realm portal", True, None],

        ["sand restoration south", "sand realm portal", False, has_portal("Desert Temple to Sand Realm", True) & has_tracks("Sand Realm")],
        ["sand realm portal", "sand restoration south", False, has_portal("Desert Temple to Sand Realm", False) & has_temple_tracks("Desert")],
        ["sand connection", "ocean temple tracks", False, has_portal("Sand Valley to Marine Temple", True) & has_temple_tracks("Marine")],
        ["ocean temple tracks", "sand connection", False, has_portal("Sand Valley to Marine Temple", False) & has_tracks("Fire Realm Sand Portal")],

        # ===== Sand Sanc =====
        ["sand realm", "sand sanc station", True, has_tracks("Sand Realm")],
        ["sand sanc station", "sand sanc", False, has_tracks("Sand Realm")],
        ["sand sanc", "sand sanc station", False, None],
        ["sand sanc", "sand sanc song", False, has_spirit_flute],
        ["sand sanc cuccos", "sand sanc stamp stand", False, has_stamp_book],
        ["sand sanc", "sand sanc sand wand", False, has_sand_wand],
    ]

    if world.options.randomize_cargo.value == 0:
        sand_sanc_logic = None
    elif world.options.randomize_cargo.value in [1, 2]:
        sand_sanc_logic = has_cargo("Cuccos", "_buy_cuccos")
    else:
        sand_sanc_logic = (has_wagon & (
                Has("Cargo: Cuccos (5)", 3) | (
                    Has("Cargo: Cuccos (5)", 1) & ool
                )
            )
        )
    overworld_logic.append(["sand sanc", "sand sanc cuccos", False, sand_sanc_logic])

        # ===== Desert Temple =====
    overworld_logic += [
        ["sand restoration", "desert temple door", False, has_cannon],
        ["desert temple door", "desert temple station", False, None],
        ["desert temple station", "sand restoration", False, has_temple_tracks("Desert")],
        ["desert temple station", "desert temple", False, has_temple_tracks("Desert")],
        ["desert temple", "desert temple station", False, None],

        ["desert temple", "dt sw", False, has_sand_wand],
        ["dt sw", "dt 1f nw", False, has_bow],
        ["desert temple", "dt 1f n", False, has_bow],

        ["dt sw", "dt 1f n earthquake", False, has_bow],

        ["desert temple", "dt 2f", False, has_small_keys("Desert Temple", 2, 1)],
        ["dt 2f", "dt 2f sw", False, has_sand_wand],
        ["dt 2f", "dt 3f", False, has_damage],

        ["dt sw", "dt b1", False, has_small_keys("Desert Temple", 2, 1)],
        ["dt b1", "dt stamp stand", False, has_stamp_book],
        ["dt b1", "dt b1 2", False, has_range | has_bombs],
        ["dt b1 2", "dt b1 damage", False, has_damage],
        ["dt b1", "dt b2", False, glitched_logic & has_bombs & has_sword],

        # ["dt b1 2", "dt b2", False, st_has_boss_key("Desert Temple")],
        ["dt b1 damage", "dt b2", False, None]
            if world.options.randomize_boss_keys.value == 0
            else ["dt b1 2", "dt b2", False, has_boss_key("Desert Temple")],
        ["dt b2", "skeldritch", False, has_good_damage],
        # Whip is not good enough damage
        ["skeldritch", "skeldritch event", False, None],
        ["skeldritch", "skeldritch goal", False, None],

        # ===== Dark ore mine =====
        ["sand restoration", "dark ore mine tracks", False, has_tracks("Dark Ore Mine") & soft_cannon],
        ["dark ore mine tracks", "sand restoration", False, has_temple_tracks("Desert") & has_cannon],
        ["dark ore mine tracks", "dark ore mine station", True, has_tracks("Dark Ore Mine")],
        ["dark ore mine station", "dark ore mine", False, has_tracks("Dark Ore Mine")],
        ["dark ore mine", "dark ore mine station", False, None],
        ["dark ore mine", "dark ore mine sod", False, has_sod],

        # ===== Dark Realm =====
        ["dark realm portal", "dark realm trains", False, has_dungeon_rewards],
        ["dark realm trains", "demon train", False, None],
        ["demon train", "cole fight", False, has_cannon],
        ["cole fight", "malladus 1", False, can_fight_malladus],
        ["malladus 1", "malladus 2", False, has_spirit_flute & has_sword],
        ["malladus 2", "malladus goal", False, can_fight_malladus],
        # ["dark realm portal", "malladus goal", False, None],
        ["malladus 2", "malladus event", False, can_fight_malladus],

        ["forest realm", "beedle", False, has_source("Snow")],
        ["snow realm source", "beedle", False, has_source("Snow")],
        ["beedle", "beedle joe", False, has_passenger("Joe", "_joe")]
    ]

    if world.options.endgame_scope.value == 5:
        overworld_logic += [
            ["dark realm trains", "malladus goal", False, None],  # enter dark realm goal
            ["dark realm trains", "dark realm event", False, None]
        ]

    required_rupees = world.get_required_rupees()

    overworld_logic += [
        # Shops
        ["snowfall supermarket", "snow sanc shop", False, has_rupees(required_rupees)],

        ["beedle", "beedle shop", False, has_rupees(required_rupees)],
        ["beedle shop", "beedle shop bombs", False, has_bombs],

        ["uriko's shop", "mayscore shop", False, has_rupees(required_rupees)],
        ["shitate's shop", "castle town shop", False, has_rupees(required_rupees)],
        ["kogane's shop", "papuzia shop", False, has_rupees(required_rupees)],
        ["papuzia shop", "papuzia shop arrows", False, has_bow],
        ["papuzia shop", "papuzia shop bombs", False, has_bombs],
        ["linebeck's shop", "trading post shield", False, has_rupees(required_rupees)],
        ["goron village", "goron shop", False, has_rupees(required_rupees)],
        ["goron shop", "goron shop bombs", False, has_bombs],
        ["goron shop", "goron shop bow", False, has_bow],

        ["castle town", "castle town buy cuccos", False, has_wagon & has_rupees(required_rupees)],
        ["mayscore", "mayscore lumber", False, has_wagon & has_rupees(required_rupees)],
        ["icyspring noko", "icyspring ice", False, has_wagon]
            if world.options.randomize_cargo in [2, 3] else
            ["icyspring noko", "icyspring ice", False, has_wagon & has_rupees(required_rupees)], #  You can bully noko for free ice
        ["papuzia village", "papuzia buy cargo", False, has_wagon & has_rupees(required_rupees)],
        ["wise one's house", "wise one buy vessel", False, has_wagon & has_rupees(required_rupees)],
        ["goron ice event", "goron steel", False, has_wagon & has_rupees(required_rupees)],
        ["dark ore mine", "dark ore mine ore", False, has_wagon & has_rupees(required_rupees)]
    ]

    # Generate rabbit total items
    if world.options.rabbitsanity in ["on_total", "both"]:
        # print(f"Creating total rabbit logic")
        overworld_logic += [
            [f"forest realm rabbits", f"{rabbit} Rabbit Count {i}", False, caught_rabbits(rabbit, i)
             ] for i in range(1, 11) for rabbit in ["Grass", "Snow", "Ocean", "Mountain", "Sand"]
        ]

    return overworld_logic


def is_item(item: Item, player: int, item_name: str):
    return item.player == player and item.name == item_name

def create_connections(world: "SpiritTracksWorld", player: int, origin_name: str, options):
    all_logic = [
        make_overworld_logic(player, origin_name, world)
    ]

    entrance_lookup = {(e.entrance_region, e.exit_region): e for e in ENTRANCES.values()}
    world.set_completion_rule(Has("_beaten_game"))

    def create_entrance(r1, r2, rule_):
        entrance_data: "STTransition" or None = entrance_lookup.get((r1.name, r2.name), None)
        name = entrance_data.name if entrance_data else None

        entrance = r1.connect(r2, name)
        if rule_ is not None:
            # print(f"Setting rule {entrance} {rule_}")
            world.set_rule(entrance, rule_)

        if entrance_data:
            # print(f"Creating connection {r1} -> {r2} | {entrance_data.name}")
            rando_type_bool = entrance_data.two_way
            entrance.randomization_type = EntranceType.TWO_WAY if rando_type_bool else EntranceType.ONE_WAY
            entrance.randomization_group = entrance_data.direction | entrance_data.category_group | entrance_data.island
            world.valid_entrances.append(entrance)

    # Create connections
    # print(f"Creating entrances: ")
    for logic_array in all_logic:
        for entr_data in logic_array:
            if entr_data is None:
                continue
            reg1, reg2, is_two_way, rule = entr_data

            region_1 = world.get_region(reg1)
            region_2 = world.get_region(reg2)

            create_entrance(region_1, region_2, rule)
            if is_two_way:
                create_entrance(region_2, region_1, rule)
