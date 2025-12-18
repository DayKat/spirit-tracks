from BaseClasses import MultiWorld, Item, Entrance, EntranceType
from .data import LOCATIONS_DATA
from .data.LogicPredicates import *
from .Options import PhantomHourglassOptions
from .data.Entrances import ENTRANCES
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Subclasses import PHRegion

def make_overworld_logic():
    overworld_logic = [

        # Randomized start
        ["Menu", "Mercay SW", False, None],

        # ====== Mercay Island ==============

        ["Mercay SW", "Mercay SW Dig Spot", False, "shovel"],
        ["Oshus' House", "Mercay Oshus Gem", False, "oshus_gem"],
        ["Oshus' House", "Mercay Oshus Phantom Blade", False, "can_make_phantom_sword"],
        ["Mercay Oshus Phantom Blade", "Mercay Oshus Gem", False, None],
        ["Mercay SW", "Mercay SW Bridge", True, None],
        ["Mercay SW", "Oshus' House", True, None],
        ["Mercay SW", "Apricot's House", True, None],
        ["Mercay SW", "Sword Cave", True, None],
        ["Mercay SW", "Mercay NW Chus", True, False],

        ["Mercay SW Bridge", "Mercay SE", True, None],
        ["Mercay SE", "Tuzi's House", True, None],
        ["Mercay SE", "Milk Bar", True, None],
        ["Mercay SE", "Mercay Shop", True, None],
        ["Mercay Shop", "Island Shop", False, None],
        ["Mercay SE", "Shipyard", False, "has", "_beat_tof"],
        ["Shipyard", "Mercay SE", False, None],
        ["Mercay SE", "Treasure Teller", False, "courage_crest"],
        ["Treasure Teller", "Mercay SE", False, None],
        ["Mercay SE", "Mercay SE Yellow Guy", False, "courage_crest"],
        ["Mercay SE", "Mercay NE", True, False],
        ["Mercay SE Ledge", "Mercay SE", False, None],

        ["Mercay NW Chus", "Mercay NW Bamboo", True, "can_cut_bamboo"],
        ["Mercay NW Temple", "Mercay Geozard Cave North", False, "explosives"],
        ["Mercay Geozard Cave North", "Mercay NW Temple", False, None],
        ["Mercay Geozard Cave North", "Mercay Geozard Cave South", False, "bow"],
        ["Mercay Geozard Cave South", "Mercay NE Ledge", True, None],
        ["Mercay NW Temple", "TotOK Lobby", True, None],

        ["Mercay NE", "Mercay Freedle Tunnel", False, "explosives"],
        ["Mercay Freedle Tunnel", "Mercay NE", False, None],
        ["Mercay Freedle Tunnel", "Mercay NW Freedle Island", True, None],
        ["Mercay NW Freedle Island", "Mercay NE", False, None],
        ["Mercay Freedle Tunnel", "Mercay Freedle Tunnel Chest", False, "range"],
        ["Mercay NW Freedle Island", "Mercay NW Freedle Gift", False, "sea_chart", "SE"],
        ["Mercay NE", "Mercay NW Temple", True, None],
        ["Mercay NE Ledge", "Mercay NE", False, None],
        ["Mercay NE Ledge", "Mercay SE Ledge", True, None],

        ["Mercay NW Temple", "Mercay NW OoB High", False, "scroll_clip"],
        ["Mercay NW OoB High", "Mercay NW Temple", False, None],
        ["Mercay NW OoB High", "Mercay NW OoB Low", False, None],
        ["Mercay NW OoB Low", "Mercay NW Chus", False, None],
        ["Mercay NW OoB Low", "Mercay NW Bamboo", False, None],
        ["Mercay NW OoB High", "Mercay NE OoB", True, None],
        ["Mercay NW OoB High", "Mercay SW OoB High", True, None],
        ["Mercay NW OoB High", "Mercay SW OoB East", True, None],
        ["Mercay NW OoB Low", "Mercay SW OoB Low", True, None],

        ["Mercay SW OoB High", "Mercay SW OoB Low", False, None],
        ["Mercay SW OoB Low", "Mercay SW", False, None],
        ["Mercay SW OoB East", "Mercay SW Bridge", False, None],
        ["Mercay SW OoB East", "Mercay SE OoB", True, None],

        ["Mercay SE OoB", "Mercay SE Ledge", False, None],
        ["Mercay SE OoB", "Mercay NE OoB", True, None],
        ["Mercay NE OoB", "Mercay NE Ledge", False, None],

        # ======== Mountain Passage =========

        ["Mercay NW Bamboo", "Mountain Passage 1", True, None],
        ["Mountain Passage 1", "Mountain Passage 2", False, "can_reach_mp2"],
        ["Mountain Passage 2 Exit", "Mountain Passage 2", False, "can_reach_mp2_top"],
        ["Mountain Passage 1", "Mountain Passage 2 Exit", False, "mp2_bypass_fore"],
        ["Mountain Passage 2 Exit", "Mountain Passage 1", False, "mp2_bypass"],
        ["Mountain Passage 2 Exit", "Mountain Passage 3", True, None],
        ["Mountain Passage 3", "Mountain Passage Rat", False, "mp_rat"],
        ["Mountain Passage 3", "Mountain Passage 4", False, "mp3"],
        ["Mountain Passage 4", "Mountain Passage 3", False, "mp3_back"],
        ["Mountain Passage 4", "Mercay SE", True, None],
        ["Mountain Passage 4", "Mountain Passage 1", False, "hard_logic"],

        # ========== TotOK ===================
        ["TotOK Lobby", "TotOK 1F", False, "totok_1f"],

        ["TotOK 1F", "TotOK 1F Chest", False, "totok_1f_chest"],
        ["TotOK 1F", "TotOK 1F Chart", False, "totok_1f_chart"],
        ["TotOK 1F", "TotOK B1", False, "totok_b1"],

        ["TotOK B1", "TotOK B1 Key", False, "totok_b1_key"],
        ["TotOK B1", "TotOK B1 Phantom", False, "totok_b1_phantom"],
        ["TotOK B1", "TotOK B1 Bow", False, "totok_b1_bow"],
        ["TotOK B1", "TotOK B2", False, "totok_b2"],

        ["TotOK B2", "TotOK B2 Key", False, "totok_b2_key"],
        ["TotOK B2", "TotOK B2 Phantom", False, "totok_b2_phantom"],
        ["TotOK B2", "TotOK B2 Chu", False, "totok_b2_chu"],
        ["TotOK B2", "TotOK B3", False, "totok_b3"],

        ["TotOK B3", "TotOK B3 NW Chest", False, "totok_b3_nw"],
        ["TotOK B3", "TotOK B3 SE Chest", False, "totok_b3_se"],
        ["TotOK B3", "TotOK B3 SW Chest", False, "totok_b3_sw"],
        ["TotOK B3", "TotOK B3 Bow", False, "totok_b3_bow"],
        ["TotOK B3", "TotOK B3 Key", False, "totok_b3_key"],
        ["TotOK B3", "TotOK B3 Phantom", False, "totok_b3_phantom"],
        ["TotOK B3", "TotOK B3.5", False, "totok_b35"],

        ["totok b3.5", "totok b4", False, "totok_b4"],
        ["totok b4", "totok b4 key", False, "totok_b4_key"],
        ["totok b4", "totok b4 eyes", False, "totok_b4_eyes"],
        ["totok b4", "totok b4 phantom", False, "totok_b4_phantom"],
        ["totok b4", "totok b5", False, "totok_b5"],
        ["totok b4", "totok b5 alt path", False, "totok_b5_alt"],

        ["totok b5", "totok b5 chest", False, "totok_b5_chest"],
        ["totok b5", "totok b6", False, "totok_b6"],
        ["totok b5 alt Path", "totok b5 alt path chest", False, "totok_b5_alt_chest"],
        ["totok b5 alt Path", "totok b6", False, "totok_b6"],

        ["totok b6", "totok b6 bow", False, "totok_b6_bow"],
        ["totok b6", "totok b6 phantom", False, "totok_b6_phantom"],
        ["totok b6", "totok b6 crest", False, "totok_b6_crest"],
        ["totok b6", "totok midway", False, "totok_b7"],
        ["totok B6 midway", "totok b7", False, "spirit", "Courage"],

        ["totok b7", "totok b7 crystal", False, "totok_b7_crystal"],
        ["totok b7", "totok b7 switch", False, "totok_b7_switch_chest"],
        ["totok b7", "totok b8", False, "totok_b8"],

        ["totok b8", "totok b8 phantom", False, "totok_b8_phantom"],
        ["totok b8", "totok b9", False, "totok_b9"],
        ["totok b8", "totok b8 2 crystals chest", False, "totok_b8_2_crystal_chest"],
        ["totok b8", "totok b7 phantom", False, "totok_b7_phantom"],
        ["totok b8", "totok b9 corner chest", False, "totok_b9_corner_chest"],

        ["totok b9", "totok b9 phantom", False, "totok_b9_phantom"],
        ["totok b9", "totok b9 wizzrobes", False, "totok_b9_ghosts"],

        ["totok b9", "totok b9.5", False, "totok_b10"],
        ["totok b9.5", "totok b10", True, None],

        ["totok b10", "totok b10 key", False, "totok_b10_key"],
        ["totok b10", "totok b10 phantom", False, "totok_b10_phantom"],
        ["totok b10", "totok b10 eyes", False, "totok_b10_eye"],
        ["totok b10", "totok b10 hammer", False, "totok_b10_hammer"],
        ["totok b10", "totok b11", False, "totok_b11"],

        ["totok b11", "totok b11 phantom", False, "totok_b11_phantom"],
        ["totok b11", "totok b11 eyes", False, "totok_b11_eyes"],
        ["totok b11", "totok b12", False, "totok_b12"],

        ["totok b12", "totok b12 nw Chest", False, "totok_b12_nw"],
        ["totok b12", "totok b12 ne Chest", False, "totok_b12_ne"],
        ["totok b12", "totok b12 phantom", False, "totok_b12_phantom"],
        ["totok b12", "totok b12 ghost", False, "totok_b12_ghost"],
        ["totok b12", "totok b12 hammer", False, "totok_b12_hammer"],
        ["totok b12", "totok b13", False, "totok_b13"],

        ["totok b13", "totok b13 chest", False, "totok_b13_chest"],
        ["totok b13", "totok before bellum", False, "b13_door"],
        ["totok lobby", "totok b14 before bellum", False, "bellum_warp"],
        # Bellum
        ["totok before bellum", "bellum 1", False, "bellum_staircase"],
        ["bellum 1", "ghost ship fight", False, "can_beat_bellum"],
        ["ghost ship fight", "bellumbeck", False, "can_beat_ghost_ship_fight"],

        # ============ Shops ====================

        ["island shop", "island shop power gem", False, "can_buy_gem"],
        ["island shop", "island shop quiver", False, "can_buy_quiver"],
        ["island shop", "island shop bombchu bag", False, "can_buy_chu_bag"],
        ["island shop", "island shop heart container", False, "can_buy_heart"],

        ["sw ocean east", "beedle", False, None],
        ["sw ocean west", "beedle", False, None],
        ["nw ocean", "beedle", False, None],
        ["se ocean", "beedle", False, None],
        ["ne ocean", "beedle", False, None],
        ["beedle", "beedle gem", False, "beedle_shop", 500],
        ["beedle", "beedle bomb bag", False, "can_buy_bomb_bag"],
        ["beedle", "masked ship gem", False, "beedle_shop", 500],
        ["beedle", "masked ship hc", False, "beedle_shop", 500],

        ["beedle", "beedle bronze", False, "can_get_beedle_bronze"],
        ["beedle", "beedle silver", False, "has_beedle_points", 20],
        ["beedle", "beedle gold", False, "has_beedle_points", 50],
        ["beedle", "beedle plat", False, "has_beedle_points", 100],
        ["beedle", "beedle vip", False, "has_beedle_points", 200],


        # ============ SW Ocean =================

        ["Mercay SE", "mercay boat", False, "boat_access"],
        ["mercay boat", "Mercay SE", False, None],
        ["mercay boat", "sw ocean east", True, "require_chart", "SW"],
        ["cannon boat", "cannon island", True, None],
        ["cannon boat", "sw ocean east", True, "require_chart", "SW"],
        ["ember boat", "ember port", True, None],
        ["ember boat", "sw ocean east", True, "require_chart", "SW"],
        ["sw ocean east", "sw ocean crest salvage", False, "salvage_courage_crest"],
        ["sw ocean east", "sw ocean west", False, "cannon"],
        ["sw ocean west", "sw ocean east", False, "cannon"],
        ["molida boat", "molida island", True, None],
        ["molida boat", "sw ocean west", True, "require_chart", "SW"],
        ["spirit boat", "spirit island", True, None],
        ["spirit boat", "sw ocean west", True, "require_chart", "SW"],
        ["sw ocean west", "sw ocean nyave", False, "nyave_fight"],
        ["sw ocean nyave", "sw ocean nyave trade", False, "guard_notebook"],
        ["sw ocean west", "sw ocean frog phi", False, "cannon"],
        ["sw ocean east", "sw ocean frog x", False, "cannon"],
        ["sw ocean west", "frog warps", False, None],
        ["sw ocean east", "frog warps", False, None],

        # ============= Frog Warps ==================
        ["frog warps", "sw ocean west", False, "frog_phi"],
        ["frog warps", "sw ocean east", False, "frog_x"],
        ["frog warps", "nw ocean", False, "frog_n"],
        ["frog warps", "ne ocean", False, "frog_square"],
        ["frog warps", "se ocean", False, "frog_se"],

        # ============ Cannon Island ===============

        ["cannon island", "Fuzo's Workshop", True, None],
        ["cannon island", "cannon island dig", False, "shovel"],
        ["cannon island", "cannon cave south", True, None],
        ["cannon cave south", "cannon cave north", False, None],
        ["cannon cave north", "cannon bomb garden", True, None],
        ["cannon bomb garden", "cannon outside eddo", False, None],
        ["cannon outside eddo", "cannon bomb garden", False, "explosives"],
        ["cannon bomb garden", "cannon island", False, None],
        ["cannon outside eddo", "cannon island", False, "glitched_logic"],
        ["cannon outside eddo", "Eddo's Workshop", True, None],
        ["Fuzo's Workshop", "Eddo's Workshop", True, "has", "_eddo_door"],
        ["Eddo's Workshop", "Eddo salvage arm", False, "courage_crest"],
        ["cannon bomb garden", "cannon bomb garden dig", False, "shovel"],

        # =============== Isle of Ember ================

        # ER
        ["ember port", "Astrid's House", True, None],
        ["Astrid's House", "Astrid's Basement", True, None],
        ["Astrid's Basement", "Astrid's Basement dig", False, "spade"],
        ["ember port", "Kayo's House", True, None],
        ["ember port", "ember port house", True, None],
        ["Astrid's House", "astrid post tof", False, "has", "_beat_tof"],

        ["ember port", "ember grapple", False, "ember_grapple"],
        ["ember grapple", "ember port", False, "grapple"],
        ["ember grapple", "ember coast north", True, "grapple"],

        ["ember coast north", "ember coast east", True, None],
        ["ember port", "ember coast east", True, None],
        ["ember climb west", "ember coast east", True, None],
        ["ember climb west", "ember outside tof", True, None],
        ["ember outside tof", "tof 1f", True, None],
        ["ember summit west", "ember outside tof", True, None],
        ["ember summit west", "ember summit east", True, None],
        ["ember outside tof", "ember outside tof dig", False, "shovel"],

        ["ember summit west", "ember climb west", False, None],
        ["ember summit east", "ember outside tof", False, None],
        ["ember climb west", "ember port", False, None],
        ["ember outside tof", "ember coast east", False, None],

        ["ember climb east", "ember coast east", True, None],
        ["ember summit north", "ember summit east", True, None],
        ["ember climb east", "ember port", True, None],
        ["ember summit north", "ember summit west", True, None],



        # =============== Temple of Fire =================

        ["tof 1f", "tof 1f keese Arena", False, "can_kill_bat"],
        ["tof 1f", "tof 1f maze", False, "tof_maze"],
        ["tof 1f maze", "tof 2f", False, "can_hit_spin_switches"],
        # 2F
        ["tof 2f", "tof 1f west", False, "short_range"],
        ["tof 1f west", "tof 1f sw", False, "can_hit_spiral_wall_switches"],
        ["tof 1f sw", "tof 2f south", False, "can_kill_bubble"],
        ["tof 2f south", "tof 3f", False, "tof_3f"],
        # 3F
        ["tof 3f", "tof 3f key drop", False, "tof_key_drop"],
        ["tof 3f", "tof 3f key door", False, "tof_3f_key_door"],
        ["tof 3f key door", "tof 3f boss key", False, "boomerang"],
        ["tof 3f key door", "tof 4F", False, "tof_bk"],  # Includes UT
        ["tof 4F", "blaaz", True, None],
        ["blaaz", "post blaaz", False, "tof_blaaz"],
        ["post blaaz", "post tof", False, "tof_blaaz"],  # Used for events

        # =========== Molida Island ===============

        ["molida island", "molida dig", False, "spade"],
        ["molida island", "molida port house", True, None],
        ["molida island", "Potato's House", True, None],
        ["molida island", "molida shop", True, None],
        ["molida shop", "island shop", False, None],
        ["molida island", "Romaros' House", True, None],
        ["Romaros' House", "Archery Game", False, "has", "_beat_toc"],
        ["molida island", "molida cave", True, None],
        ["molida island", "molida cave upper", False, "shovel"],

        ["molida cave upper", "molida cave", False, None],
        ["molida cave", "molida cave grapple", False, "grapple"],
        ["molida cave", "molida cave geozard", False, None],
        ["molida cave geozard", "molida cave geozard dig", False, "shovel"],
        ["molida cave geozard", "molida cave post geozard", False, "cave_damage"],
        ["molida cave post geozard", "Octorok Cave", True, None],
        ["molida cave", "molida cave back", False, "bombs"],
        ["molida cave back", "molida cave", False, None],
        ["molida cave back", "Octorok Cave", True, None],
        ["molida cave back", "shovel cave", True, None],
        ["shovel cave", "shovel cave dig", False, "shovel"],
        ["molida cave back", "molida cliff north", True, None],

        ["molida cliff north", "molida cliff south", True, None],
        ["molida cliff south", "molida island", False, None],
        ["molida cliff south", "molida cucco dig", False, "cuccoo_dig"],

        ["molida cave upper", "molida cave sun door", True, "sun_key"],
        ["molida north", "Molida Cave North Drop", False, "shovel"],
        ["Molida Cave North Drop", "molida cave sun door", False, None],
        ["molida cave sun door", "molida north", True, None],
        ["molida north", "molida north grapple", False, "grapple"],
        ["molida north", "Molida Outside Temple", False, "enter_toc"],
        ["Molida Outside Temple", "ToC 1F", True, None],

        # =============== Temple of Courage ================

        ["ToC 1F", "toc 1F bomb alcove", False, "boom"],
        ["ToC 1F", "toc b1", False, "toc_door_1"],
        ["ToC 1F", "toc hammer clips", False, "hammer_clip"],
        ["toc b1", "toc b1 grapple", False, "toc_grapple"],
        ["toc b1", "toc 1f west", False, "toc_1f_west"],
        ["toc b1 grapple", "toc 1f west", False, "bow"],
        ["toc hammer clips", "toc 1f west", False, None],
        ["toc 1f west", "toc 1F map room", False, "boom"],
        ["toc 1f west", "toc 2f beamos Room", False, "toc_door_2"],
        ["toc 1f west", "ToC B1 Invisible Maze", False, "shape_crystal", "Temple of Courage", "Square", "North"],
        ["toc 2f beamos Room", "ToC B1 Invisible Maze", False, "ut_pedestals_vanilla"],  # UT Crystal
        ["toc 2f beamos Room", "toc south 1f", False, "toc_beamos_ut"],  # UT Crystal South
        ["toc b1 grapple", "ToC B1 Invisible Maze", False, None],
        ["ToC B1 Invisible Maze", "toc south 1f", False, "toc_crystal_south"],

        ["toc south 1f", "toc 2f spike corridor", False, "boom"],
        ["toc 2f spike corridor", "toc 2f Moving Platform Room", False, "toc_spike_corridor"],
        ["toc hammer clips", "toc 2f spike corridor", False, None],
        ["toc south 1f", "toc 2f Moving Platform Room", False, "bow"],
        ["toc 2f spike corridor", "ToC B1 Torches Platforms", False, "boomerang"],
        ["ToC B1 Torches Platforms", "ToC B1 Torches Chest", False, "bow"],
        ["ToC B1 Torches Platforms", "ToC 1F Pols NW", False, "toc_switch_state"],
        ["ToC 1F Pols NW", "ToC 2F Scribble Platform Room", False, "toc_door_3"],
        ["ToC 2F Scribble Platform Room", "toc bk chest", False, "bow"],
        ["ToC 2F Scribble Platform Room", "toc before boss", False, "toc_boss_key"],
        ["toc bk chest", "toc before boss", False, "simple_boss_key", "Temple of Courage"],
        ["toc 3F", "toc 3F chest", False, "boom"],
        ["toc 3F", "crayk", True, None],
        ["crayk", "post crayk", False, "bow"],
        ["post crayk", "post toc", False, None],  # Used for events

        # ================ Spirit Island =====================

        ["spirit island", "spirit island gauntlet", False, "grapple"],
        ["spirit island", "spirit cave", True, None],
        ["spirit cave", "spirit power 1", False, "spirit_gems", "Power", 10],
        ["spirit cave", "spirit power 2", False, "spirit_gems",  "Power", 20],
        ["spirit cave", "spirit wisdom 1", False, "spirit_gems",  "Wisdom", 10],
        ["spirit cave", "spirit wisdom 2", False, "spirit_gems",  "Wisdom", 20],
        ["spirit cave", "spirit courage 1", False, "spirit_gems",  "Courage", 10],
        ["spirit cave", "spirit courage 2", False, "spirit_gems",  "Courage", 20],

        # ============ Ocean NW ===============
        ["sw ocean west", "nw ocean", False, "sea_chart", "NW"],
        ["nw ocean", "sw ocean west", False, "sea_chart", "SW"],
        ["nw ocean", "sw ocean east", False, "sea_chart", "SW"],
        ["nw ocean", "frog warps", False, None],
        ["nw ocean", "nw ocean frog n", False, "cannon"],
        ["gust boat", "gust south", True, None],
        ["gust boat", "nw ocean", True, "require_chart", "NW"],
        ["bannan boat", "bannan", True, None],
        ["bannan boat", "nw ocean", True, "require_chart", "NW"],
        ["zauz boat", "zauz", True, None],
        ["zauz boat", "nw ocean", True, "require_chart", "NW"],
        ["uncharted boat", "uncharted", True, None],
        ["uncharted boat", "nw ocean", True, "require_chart", "NW"],
        ["nw ocean", "ghost ship deck", False, "ghost_ship"],
        ["ghost ship deck", "nw ocean", False, None],
        ["nw ocean", "porl", False, None],
        ["porl", "porl item", False, "sword"],
        ["porl", "porl trade", False, "heroes_new_clothes"],

        # ================= Isle of Gust ====================

        ["gust south", "gust hideout", True, None],
        ["gust south", "Miniblin cave", True, None],
        ["Miniblin cave", "Miniblin cave damage", False, "cave_damage"],
        ["Miniblin cave", "gust cliffs", True, None],
        ["gust south cliffs", "gust south", False, None],
        ["gust south cliffs", "gust south cliffs dig", False, "shovel"],
        ["gust south cliffs", "gust north temple road", True, None],
        ["gust south cliffs", "gust north above temple", True, None],
        ["gust north above temple", "gust south NW", True, None],
        ["gust south NW", "gust south NW chest", False, "shovel"],
        ["gust south NW", "gust south NW ledge", False, "shovel"],
        ["gust south NW ledge", "gust south NW", False, None],
        ["gust south NW ledge", "gust north", True, None],
        ["gust north", "gust north dig", False, "shovel"],
        ["gust north", "gust north sandworms", True, "shovel"],
        ["gust north sandworms", "gust north above temple", True, "has", "_windmills"],
        ["gust north above temple", "Gust North Temple Road", False, None],
        ["gust north temple road", "gust north outside temple", False,  "has", "_windmills"],
        ["gust north outside temple", "gust north temple road", False, None],
        ["gust north outside temple", "tow 1F", True, None],

        # ================= Temple of Wind ====================

        ["tow 1F", "tow b1", False, "tow_b1"],
        ["tow b1", "tow b2", False, None],
        ["tow b2", "tow b2 dig", False, "shovel"],
        ["tow b2", "tow b2 bombs", False, "explosives"],
        ["tow b2", "tow b2 key", False, "tow_key"],
        ["tow b2", "tow 1f NE", False, "bombs"],
        ["tow 1F", "tow 2F", False, "tow_cyclok"],
        ["tow 2F", "cyclok", True, None],
        ["cyclok", "post cyclok", False, None],
        ["post cyclok", "post tow", False, None],

        # ================= Bannan Island ====================

        ["bannan Island", "bannan West grapple", False, "grapple"],
        ["bannan Island", "bannan dig", False, "shovel"],
        ["bannan Island", "Wayfarer's House", True, None],
        ["bannan Island", "bannan cave west", True, None],
        ["bannan cave west", "bannan cave east", True, "bombs"],
        ["bannan cave east", "bannan east", True, None],
        ["bannan east", "bannan east grapple", False, "grapple"],
        ["bannan east grapple", "bannan east grapple dig", False, "shovel"],
        ["bannan east", "bannan cannon game", False, "cannon"],
        ["Wayfarer's House", "Wayfarer Trade Quest", False, "bannan_scroll"],
        ["Wayfarer's House", "Wayfarer Give Loovar", False, "loovar"],
        ["Wayfarer's House", "Wayfarer Give Rusty Swordfish", False, "rsf"],
        ["Wayfarer's House", "Wayfarer Give Legendary Neptoona", False, "neptoona"],
        ["Wayfarer's House", "Wayfarer Give Stowfish", False, "stowfish"],
        ["Wayfarer's House", "Joanne Give Letter", False, "jolene_letter"],

        # ================= Zauz's Island ====================

        ["Zauz's Island", "zauz dig", False, "shovel"],
        ["Zauz's Island", "zauz's house", True, None],
        ["zauz's house", "zauz's blade", False, "has_zauz_required_metals"],
        ["zauz's house", "zauz's crest", False, "has", "_beat_ghost_ship"],

        # ================= Uncharted Island ====================

        ["uncharted island", "uncharted dig", False, "shovel"],
        ["uncharted", "uncharted outside cave", False, "sword"],
        ["uncharted outside cave", "uncharted cave", True, None],
        ["uncharted cave", "Golden Chief Cave", True, None],
        ["uncharted cave", "uncharted cave grapple", False, "grapple"],

        # ================= Ghost Ship ====================

        ["ghost ship 1F", "ghost ship B1", True, None],
        ["ghost ship B1", "ghost ship B1 barrel", False, "gs_barrel"],
        ["ghost ship B1 barrel", "ghost ship b2", False, "gs_triangle"],
        ["ghost ship b2", "ghost ship b2 chests", False, "can_hit_switches"],
        ["ghost ship b2 chests", "ghost ship b3", False, "can_kill_bat"],
        ["ghost ship b3", "cubus sisters", True, None],
        ["cubus sisters", "post cubus sisters", False, "sword"],
        ["ghost ship b2", "ghost ship tetra", False, "ghost_key"],
        ["ghost ship tetra", "spawn pirate ambush", False, None],

        # ================= SE Ocean ====================

        ["sw ocean east", "se ocean", False, "se_ocean"],
        ["se ocean", "sw ocean east", False, "sea_chart", "SW"],
        ["se ocean", "frog warps", False, None],
        ["se ocean", "se ocean frogs", False, "cannon"],
        ["se ocean", "goron boat", False, "can_pass_sea_monsters"],
        ["goron boat", "se ocean", False, "require_chart", "SE"],
        ["goron sw", "goron boat", True, None],
        ["se ocean", "se ocean trade", False, "kaleidoscope"],
        ["se ocean", "frost boat", False, "can_pass_sea_monsters"],
        ["frost boat", "se ocean", False, "require_chart", "SE"],
        ["frost boat", "frost", True, None],
        ["harrow boat", "harrow island", True, None],
        ["harrow boat", "se ocean", True, "require_chart", "SE"],
        ["ds boat", "dee ess island", True, None],
        ["ds boat", "se ocean", True, "require_chart", "SE"],
        ["se ocean", "pirate ambush", False, "beat_gs"],

        # ================= Goron Island ====================

        ["goron sw", "goron port house", True, None],
        ["goron sw", "goron shop", True, None],
        ["goron shop", "island shop", False, None],
        ["goron sw", "goron rock house", True, None],
        ["goron sw", "goron chu house", True, None],
        ["goron sw", "goron shortcut", True, None],
        ["goron sw chu ledge", "goron chus", False, "goron_chus"],
        ["goron sw chu ledge", "goron sw grapple", False, "grapple"],
        ["goron sw", "goron se", True, None],
        ["goron sw chu ledge", "goron sw", False, None],
        ["goron se", "goron SW chu ledge", True, None],
        ["goron se", "goron mountain house", True, None],
        ["goron se", "goron se house", True, None],
        ["goron se", "goron chief house", True, None],
        ["goron chief house", "goron quiz", False, "has", "_goron_chus"],
        ["goron quiz", "goron chief Post Dungeon", False, "has", "_beat_gt"],
        ["goron se", "goron ne", True, None],

        ["goron ne", "goron ne south", False, None],
        ["goron ne south", "goron ne", False, "explosives"],
        ["goron ne south", "goron ne south dead end", True, None],
        ["goron ne", "goron ne middle", False, None],
        ["goron ne", "goron ne chu chest", False, "bombchu_switches"],
        ["goron ne middle", "goron ne", False, "explosives"],
        ["goron ne middle", "goron ne coast", True, "explosives"],
        ["goron en middle", "goron nw north dead end", True, None],
        ["goron ne coast", "goron nw like like", True, None],
        ["goron nw like like", "goron nw outside temple", False, "damage"],
        ["goron nw like like", "goron ne spikes", True, None],
        ["goron ne spikes", "goron ne spike chest", False, "has", "_goron_maze_switch"],
        ["goron nw outside temple", "goron nw like like", False, "clever_bombs"],  # Hard logic

        ["goron nw shortcut", "goron nw outside temple", False, "hammer_clip"],
        ["goron nw outside temple", "goron nw shortcut", False, None],
        ["goron nw outside temple", "gt", True, None],

        # ================= Goron Temple ====================
        ["GT 1F", "GT 1F Upper", False, "goron_entrance"],
        ["GT 1F Upper", "GT 1F bow", False, "bow"],
        ["GT 1F Upper", "GT b1", False, "gt_b1"],
        ["GT b1", "GT b2", False, "bombchu_switches"],
        ["GT b2", "GT b3", False, None],
        ["GT b2", "GT b2 back", False, "gt_b2_back"],
        ["GT b2 back", "GT B2 back chest", False, "chus"],
        ["GT b2", "GT b4", False, "gt_enter_dongo"],
        ["GT before dongo", "Dongorongo", True, None],
        ["Dongorongo", "post Dongorongo", False, "gt_dongo"],
        ["post Dongorongo", "post GT", False, None],

        # ================= Harrow Island ====================

        ["harrow island", "harrow sword", False, "sword"],
        ["harrow sword", "harrow minigame", False, "shovel"],
        ["harrow minigame", "harrow minigame ne chart", False, "sea_chart", "NE"],

        # ================= Dee Ess Island ====================

        ["Dee Ess Island", "Dee Ess Dig", False, "shovel"],
        ["Dee Ess Island", "Dee Ess Eye Brutes", False, "can_kill_eye_brute"],
        ["Dee Ess Island", "Dee Ess Goron Race", False, "has", "_beat_gt"],

        # ================= Isle of Frost ====================

        ["Frost SW", "Frost SW grapple", False, "grapple"],
        ["frost SW", "frost SW dig", False, "spade"],
        ["frost SW", "Smart Anouki's House", True, None],
        ["frost SW", "Sensitive Anouki's House", True, None],
        ["frost SW", "frost chief house", True, None],
        ["frost SW", "frost estate", True, None],
        ["frost SW", "frost cave", True, None],

        ["frost NW", "Fofo's House", True, None],
        ["frost NW", "Kumu's House", True, None],
        ["frost NW", "Dobo's House", True, None],
        ["frost NW", "Gumo's House", True, None],
        ["frost NW", "Aroo's House", True, None],
        ["frost NW", "Mazo's House", True, None],
        ["frost NW", "frost NW dig", False, "shovel"],
        ["frost NW dig", "frost NW grapple dig", False, "grapple"],

        ["frost cave", "frost SE", True, None],
        ["frost SE", "frost SE exit", False, "ice_field"],
        ["frost SE", "frost SE upper east", False, "grapple"],
        ["frost SE upper east", "frost SE", False, None],
        ["frost SE upper east", "frost SE upper chests", False, "grapple"],
        ["frost SE upper east", "frost SE east ledge", False, None],
        ["frost SE upper east", "frost SE upper north", True, "grapple"],
        ["frost SE upper east", "frost SE exit", False, None],
        ["frost SE upper north", "frost SE", False, None],
        ["frost SE upper north", "frost SE exit", False, None],
        ["frost SE upper north", "frost NE above temple west", True, None],
        ["frost SE upper east", "frost NE above temple east", True, None],
        ["frost SE exit", "frost NE outside arena", True, None],

        ["frost NE above temple east", "frost NE outside arena", False, None],
        ["frost NE above temple west", "frost NE outside arena", False, None],
        ["frost NE outside arena", "frost NE arena", False, None],
        ["frost NE arena", "frost NE outside arena", False, "dark_yook"],
        ["frost NE arena", "frost NE outside temple", False, "dark_yook"],
        ["frost NE arena", "frost NE above temple west", False, "grapple"],
        ["frost NE outside temple", "frost NE arena", False, None],
        ["frost NE outside temple", "toi 1f", True, None],

        # ================= Ice Temple ====================

        ["toi 1f", "toi 1f ascent", False, "toi_2f"],
        ["toi 1f ascent", "toi 2f right", True, None],
        ["toi 3f right", "toi 2f right", True, None],
        ["toi 3f right", "toi 3f", False, "toi_3f"],
        ["toi 3f", "toi 3f right", False, "range"],
        ["toi 3f", "toi 3f key door", True, "toi_key_door_1"],  # TODO: Key logic
        ["toi 3f", "toi 3f switch state", False, "bombs"],  # TODO: Switch state logic
        ["toi 3f switch state", "toi 3f boomerang key", False, "toi_3f_boomerang"],
        ["toi 3f key door", "toi 2f arena", True, None],
        ["toi 2f arena", "toi 2f post arena", False, "dark_yook"],
        ["toi 2f arena", "toi 2f left", False, "toi_miniboss"],
        ["toi 2f left", "toi 1f beetles", True, None],
        ["toi 1f beetles", "toi 1f shortcut", False, "grapple"],
        ["toi 1f shortcut", "toi 1f beetles", False, "grapple_glitch"],
        ["toi", "toi 1f shortcut", False, "hammer_clip"],
        ["toi 1f shortcut", "toi", False, None],
        ["toi 1f shortcut", "toi 1f descent", False, "grapple"],
        ["toi 1f descent", "toi b1 ascent", True, None],

        ["toi b1 ascent", "toi b1 shore", False, None],  # TODO: Switch state logic
        ["toi b1 shore", "toi b1 ascent", False, "hammer_clip"],
        ["toi b1 shore", "toi b1 south", False, "toi_b1"],
        ["toi b1 south", "toi b1 shore", False, None],
        ["toi b1 south", "toi b1 mid", True, "explosives"],
        ["toi b1 mid", "toi b1 right", False, "grapple"],
        ["toi b1 right", "toi b1 switch", False, "hammer_clip"],
        ["toi b1 right", "toi b1 switch room", False, "toi_key_door_2"],  # TODO: Key logic, and also backwards switch logic?
        ["toi b1 switch room", "toi b1 switch", False, "toi_b1_switch"],
        ["toi b1 mid", "toi b1 boss door", False, "toi_b2"],
        ["toi b1 boss door", "toi b1 mid", False, "grapple"],  # TODO: Switch state red
        ["toi b1 boss door", "toi b1 before boss", True, "toi_boss_door"],  # TODO: do ER logic
        ["toi b1 before boss", "gleeok", True, None],
        ["gleeok", "beat gleeok", False, "grapple"],
        ["beat gleeok", "post toi", False, None],
        ["toi b1 before boss", "toi blue warp", True, None],
        ["toi", "toi blue warp", True, "has", "_toi_blue_warp"],
        ["toi b1 boss door", "toi b2", True, None],

        ["toi b2", "toi b2 north", False, "toi_b2_north"],
        ["toi b2 north", "toi b2 bk chest", False, "hammer_clip"],
        ["toi b2 north", "toi b2 east", False, None],
        ["toi b2 east", "toi b2 bow", False, "bow"],
        ["toi b2 east", "toi b2 east arena", False, "toi_key_doors", 3, 3],  # TODO: Key logic
        ["toi b2 east arena", "toi b2 bk chest", False, None],

        # ================= NE Ocean ====================

        ["se ocean", "ne ocean", False, "sea_chart", "NE"],
        ["ne ocean", "se ocean", False, "sea_chart", "SE"],
        ["ne ocean", "frog warps", False, None],
        ["ne ocean", "ne ocean frog", False, "cannon"],
        ["ne ocean", "ne ocean combat", False, "can_kill_blue_chu"],
        ["dead boat", "iotd port", True, None],
        ["dead boat", "ne ocean", True, "require_chart", "NE"],
        ["maze boat", "maze", True, None],
        ["maze boat", "ne ocean", True, "require_chart", "NE"],
        ["ne ocean inner", "ruins boat", True, "require_chart", "NE"],
        ["ruins boat", "ruins port", True, None],
        ["ne ocean", "pirate ambush", False, "beat_gs"],

        # ================= IotD ====================

        ["iotd port", "iotd cave", True, None],
        ["iotd", "iotd port", False, None],
        ["Aquanine cave", "rupoor cave", False, "bombs"],
        ["rupoor cave", "Aquanine cave", False, None],
        ["Aquanine cave", "iotd", True, None],
        ["Isle of the Dead", "Brant's temple", True, None],
        ["Isle of the Dead", "iotd tunnel", False, "shovel"],
        ["iotd tunnel", "iotd tunnel cave", False, "bombs"],
        ["iotd tunnel cave", "iotd tunnel", False, None],
        ["iotd tunnel", "iotd face", True, None],
        ["iotd face", "Isle of the Dead", False, None],
        ["Brant's temple", "iotd crown", True, None],
        ["iotd crown", "Isle of the Dead", False, None],

        # ================= Isle of Ruins ====================

        ["ruins sw port", "ruins geozard cave east", True, None],
        ["ruins geozard cave east", "ruins geozard cave west", True, "ruins_geozards"],
        ["ruins geozard cave west", "ruins sw maze upper", True, None],
        ["ruins sw maze upper", "ruins sw port", False, None],
        ["ruins sw maze upper", "ruins sw maze lower", False, "ruins_water"],
        ["ruins sw port cliff", "ruins sw maze upper", False, None],
        ["ruins sw maze lower", "ruins sw maze lower exit", True, "ruins_water"],
        ["ruins sw maze lower exit", "ruins nw maze lower exit", True, None],
        ["ruins sw maze upper", "ruins nw maze upper exit", True, None],
        ["ruins sw maze lower", "ruins nw maze lower chest", True, "ruins_water"],

        ["ruins nw maze lower exit", "ruins nw boulders", False, None],
        ["ruins nw maze upper exit", "ruins nw boulders", False, None],
        ["ruins nw boulders", "ruins nw dig", False, "shovel"],
        ["ruins nw port cliff", "ruins nw maze lower chest", False, "ruins_water"],
        ["ruins nw boulders", "ruins nw across bridge", True, None],
        ["ruins nw boulders", "Bremeur's Temple", True, None],
        ["Bremeur's Temple", "Bremeur's Temple Kings Key", False, "kings_key"],
        ["Ruins nw boulders", "ruins nw port cliff", False, None],
        ["ruins nw port cliff", "ruins sw port cliff", True, None],
        ["ruins nw port cliff", "ruins nw port cliff tree", True, "ruins_water"],
        ["ruins nw boulders", "ruins nw lower", False, "ruins_water"],
        ["ruins nw across bridge", "ruins nw cave", True, "ruins_water"],
        ["ruins nw cave", "ruins rupee cave", True, None],
        ["ruins nw across bridge", "ruins nw alcove", False, "ruins_water"],
        ["ruins nw across bridge", "ruins ne enter upper", True, None],
        ["ruins nw return", "ruins nw boulders", False, None],
        ["ruins nw across bridge", "ruins nw return",  False, "hard_logic"],
        ["ruins nw lower", "ruins ne lower", True, "ruins_water"],

        ["ruins ne enter upper", "ruins ne doylan bridge", False, None],
        ["ruins ne doylan bridge", "ruins ne lower", False, "ruins_water"],
        ["ruins ne doylan bridge", "ruins ne behind Pyramids", True, "ruins_water"],
        ["ruins ne doylan bridge", "ruins nw return", True, None],
        ["ruins ne doylan bridge", "Doylan's temple", True, None],
        ["Doylan's Temple", "Doylan's chamber", True, None],
        ["ruins ne lower", "ruins nw alcove", True, "ruins_water"],
        ["ruins ne lower", "ruins ne behind Pyramids", True, "grapple"],
        ["ruins ne lower", "ruins se lower", True, "ruins_water"],
        ["ruins ne behind Pyramids", "ruins se coast", True, "ruins_water"],
        ["ruins ne outside temple", "ruins ne behind Pyramids", False, "ruins_water"],
        ["ruins ne outside temple", "MT 1F", True, None],
        ["ruins ne outside temple", "ruins ne geozard arena", False, "ruins_water"],
        ["ruins ne geozard arena", "ruins ne outside temple", False, "damage"],

        ["ruins se lower", "ruins ne secret chest", True, "ruins_water"],
        ["ruins se lower", "ruins se return bridge east", True, "ruins_water"],
        ["ruins se return bridge west", "ruins se return bridge east", False, "hammer"],
        ["ruins se return bridge east", "ruins se return bridge west", False, None],
        ["ruins se lower", "ruins se outside Pyramid", True, "ruins_water"],
        ["ruins se return bridge west", "ruins sw port cliff", True, None],
        ["ruins se outside Pyramid", "Max's Temple", True, None],
        ["ruins se lower", "ruins se Royal Road", False, None],
        ["ruins se path to temple", "ruins ne geozards", True, "ruins_water"],

        # ================= Mutoh's Temple ====================

        ["MT 1F", "MT landing", False, "mutoh_entrance"],
        ["MT landing", "MT hammer", False, "hammer"],
        ["MT hammer", "MT lower water", False, "mutoh_water"],
        ["MT water", "MT Bk chest", False, "mutoh_bk_chest"],
        ["MT water", "MT B3", False, "mutoh_boss_door"],
        ["MT B3", "eox", True, None],
        ["eox", "post eox", False, "hammer"],

        # ================= Maze Island ====================

        ["maze Island", "maze Island Minigame", False, "sword"],
        ["maze Island Minigame", "maze Island bomb chest", False, "explosives"],
        ["maze Island Minigame", "maze Island Minigame normal", False, "bow"],
        ["maze Island Minigame normal", "maze Island Minigame expert", False, "grapple"],
        ["maze Island Minigame", "maze Island dig", False, "shovel"],

        # ========== Fishing ====================

        ["frog warps", "fishing", False, "fishing_rod"],
        ["fishing", "fishing big catch lure", False, "big_catch_lure"],
        ["fishing", "fishing rusty swordfish", False, "can_catch_rsf"],
        ["fishing", "fishing shadows", False, "swordfish_shadows"],
        ["fishing", "fishing stowfish", False, "ut_can_stowfish"],

        # ========== Salvage ==============

        ["sw ocean west", "sw ocean west salvage", False, "salvage"],
        ["sw ocean east", "sw ocean east salvage", False, "salvage"],
        ["nw ocean", "nw ocean salvage", False, "salvage"],
        ["se ocean", "se ocean salvage", False, "salvage"],
        ["ne ocean", "ne ocean salvage", False, "salvage"],
        ["ne ocean", "ne ocean inner", False, "regal_necklace"],
        ["ne ocean inner", "ne ocean", False, None],
        ["ne ocean inner", "ne ocean salvage inner", False, "salvage"],
        ["ne ocean", "nw ocean corner salvage", False, "salvage_behind_bannan"],

        ["sw ocean west salvage", "salvage 1", False, "treasure_map", 1],
        ["sw ocean east salvage", "salvage 2", False, "treasure_map", 2],
        ["nw ocean salvage", "salvage 3", False, "treasure_map", 3],
        ["nw ocean corner salvage", "salvage 4", False, "treasure_map", 4],
        ["sw ocean west salvage", "salvage 5", False, "treasure_map", 5],
        ["nw ocean salvage", "salvage 6", False, "treasure_map", 6],
        ["nw ocean salvage", "salvage 7", False, "treasure_map", 7],
        ["sw ocean east salvage", "salvage 8", False, "treasure_map", 8],
        ["sw ocean east salvage", "salvage 9", False, "treasure_map", 9],
        ["nw ocean salvage", "salvage 10", False, "treasure_map", 10],
        ["nw ocean salvage", "salvage 11", False, "treasure_map", 11],
        ["se ocean salvage", "salvage 12", False, "treasure_map", 12],
        ["se ocean salvage", "salvage 13", False, "treasure_map", 13],
        ["se ocean salvage", "salvage 14", False, "treasure_map", 14],
        ["se ocean salvage", "salvage 15", False, "treasure_map", 15],
        ["se ocean salvage", "salvage 16", False, "treasure_map", 16],
        ["se ocean salvage", "salvage 17", False, "treasure_map", 17],
        ["sw ocean east salvage", "salvage 18", False, "treasure_map", 18],
        ["nw ocean salvage", "salvage 19", False, "treasure_map", 19],
        ["nw ocean corner salvage", "salvage 20", False, "treasure_map", 20],
        ["sw ocean west salvage", "salvage 21", False, "treasure_map", 21],
        ["se ocean salvage", "salvage 22", False, "treasure_map", 22],
        ["se ocean salvage", "salvage 23", False, "treasure_map", 23],
        ["ne ocean salvage", "salvage 24", False, "treasure_map", 24],
        ["ne ocean salvage", "salvage 25", False, "treasure_map", 25],
        ["ne ocean salvage inner", "salvage 26", False, "treasure_map", 26],
        ["ne ocean salvage", "salvage 27", False, "treasure_map", 27],
        ["ne ocean salvage inner", "salvage 28", False, "treasure_map", 28],
        ["ne ocean salvage", "salvage 29", False, "treasure_map", 29],
        ["ne ocean salvage", "salvage 30", False, "treasure_map", 30],
        ["ne ocean salvage", "salvage 31", False, "treasure_map", 31],

        # Goal stuff
        ["sw ocean east", "bellumbeck", False, "bellumbeck_quick_finish"],
        ["bellumbeck", "beat bellumbeck", False, "can_beat_bellumbeck"],
        ["beat bellumbeck", "goal", False, None],
        ["totok midway", "goal", False, "goal_midway"],
        ["menu", "goal", False, "win_on_metals"],

    ]

    return overworld_logic


def is_item(item: Item, player: int, item_name: str):
    return item.player == player and item.name == item_name


def create_connections(multiworld: MultiWorld, player: int, origin_name: str, options):
    def create_entrance(r1: "PHRegion", r2: "PHRegion", *arguments):
        entrance_key = (r1.name, r2.name)
        name = None
        if entrance_key in test_entrances:
            entrance_data = test_entrances[entrance_key]
            name = entrance_data.name
        if rule_lookup:
            rule_func = RULE_DICT[rule_lookup]
            entrance = r1.connect(r2, name, lambda state: rule_func(state, player, *arguments))
        else:
            entrance = r1.connect(r2, name, None)

        if entrance_key in test_entrances:
            # Set entrance data
            entrance_data = test_entrances[entrance_key]
            rando_type_bool = entrance_data.two_way
            entrance.randomization_type = EntranceType.TWO_WAY if rando_type_bool else EntranceType.ONE_WAY
            entrance.randomization_group = entrance_data.direction | entrance_data.category_group | entrance_data.island
            entrance.name = entrance_data.name
            multiworld.worlds[player].entrances[entrance.name] = entrance
            uncreated_entrances.remove(entrance.name)

    all_logic = [
        make_overworld_logic()
    ]

    test_entrances = {(e.entrance_region, e.exit_region): e for e in ENTRANCES.values()}
    uncreated_entrances = [e.name for e in ENTRANCES.values()]

    # Create connections
    for logic_array in all_logic:
        for entrance_desc in logic_array:
            reg1, reg2, is_two_way, rule_lookup, *args = entrance_desc
            region_1 = multiworld.get_region(reg1, player)
            region_2 = multiworld.get_region(reg2, player)

            create_entrance(region_1, region_2, *args)
            if is_two_way:
                create_entrance(region_2, region_1, *args)


    # print(f"Some entrances had no logical matches: ")
    # for i in uncreated_entrances:
    #     print(f"\t{i}")

if __name__ == "__main__":
    from worlds.tloz_ph.data.Regions import REGIONS

    for reg1, reg2, *args in make_overworld_logic():
        regions_lower = [r.lower() for r in REGIONS]
        if reg1 in regions_lower:
            i = regions_lower.index(reg1)
            reg1 = REGIONS[i]

        if reg2 in regions_lower:
            i = regions_lower.index(reg2)
            reg2 = REGIONS[i]
        print(f"\t\t[{reg1}, {reg2}, {args}],")