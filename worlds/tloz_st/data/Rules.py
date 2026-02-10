import dataclasses

from rule_builder.rules import Filtered
from .Items import ITEMS
from .Constants import ITEM_GROUPS
from ..Options import *

from rule_builder.rules import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..__init__ import SpiritTracksWorld

has_sword = Has("Sword (Progressive)")
has_shield = Has("Shield")
has_whirlwind = Has("Whirlwind")
has_boomerang = Has("Boomerang")
has_whip = Has("Whip")
has_bow = Has("Bow (Progressive)")
has_bombs = Has("Bombs (Progressive)")
has_bow_of_light = Has("Bow of Light") & has_bow
has_sword_beam = has_sword & Has("Sword Beam Swordsman's Scroll")
has_stamp_book = Has("Stamp Book")

has_cannon = Has("Cannon")

# Songs
has_spirit_flute = Has("Spirit Flute")
has_soa = has_spirit_flute & Has("Song of Awakening")
has_soh = has_spirit_flute & Has("Song of Healing")
has_sob = has_spirit_flute & Has("Song of Birds")
has_sol = has_spirit_flute & Has("Song of Light")
has_sod = has_spirit_flute & Has("Song of Discovery")

# Keys
def has_small_keys(dungeon, count):
    return Has(f"Small Key ({dungeon})", count)

# Rabbits
has_net = Has("Rabbit Net")

def has_rabbit_items(realm, count):
    return HasRabbitItems(realm, count)

def caught_rabbits(realm, count):
    return Has(f"_caught_{realm.lower()}_rabbits", count)

rabbit_count_lookup = {r: ITEMS[r].value for r in ITEM_GROUPS["Rabbits"]}

@dataclasses.dataclass
class HasRabbitItems(Rule["SpiritTracksWorld"], game="The Legend of Zelda - Spirit Tracks"):
    realm: str
    count: int

    @override
    def _instantiate(self, world: "SpiritTracksWorld") -> Rule.Resolved:
        return self.Resolved(
            self.realm,
            self.count,
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    class Resolved(Rule.Resolved):
        realm: str
        count: int

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            rabbit_lookup = {r: ITEMS[r].value for r in ITEM_GROUPS[f"{self.realm} Rabbits"]}
            rabbit_total = 0
            for r, v in rabbit_lookup.items():
                rabbit_total += state.count(r, self.player) * v
            return rabbit_total >= self.count


@dataclasses.dataclass
class HasRabbitsTotal(Rule["SpiritTracksWorld"], game="The Legend of Zelda - Spirit Tracks"):
    count: int

    @override
    def _instantiate(self, world: "SpiritTracksWorld") -> Rule.Resolved:
        return self.Resolved(
            self.count,
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    class Resolved(Rule.Resolved):
        count: int

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            rabbit_total = 0
            for r, v in rabbit_count_lookup.items():
                rabbit_total += state.count(r, self.player) * v
            return rabbit_total >= self.count

# Tracks
has_compass = Has("Compass of Light")

def has_glyph(realm):
    return Has(f"{realm} Glyph")

def has_source(realm):
    return Has(f"{realm} Source")

def has_temple_tracks(temple):
    return Has(f"{temple} Temple Tracks")

def has_portal(portal, forward):
    option = SpiritTracksRandomizePortals
    if forward:
        return ([OptionFilter(option, 1), OptionFilter(option, 0)]
                | Has(f"Portal Unlock: {portal}", options=[OptionFilter(option, 2)]))
    return ([OptionFilter(option, 1)]
        | Has(f"Portal Unlock: {portal}", options=[OptionFilter(option, 2)]))

# Isolated options
hard_logic_filter = [OptionFilter(SpiritTracksLogic, SpiritTracksLogic.option_hard), OptionFilter(SpiritTracksLogic, SpiritTracksLogic.option_glitched)]
hard_logic = Has("_UT_Glitched_Logic") | hard_logic_filter

# Composites
has_train = has_cannon & has_glyph("Forest")
has_damage = has_bombs | has_sword | has_bow | has_whip
can_kill_bat = has_damage | has_boomerang
can_kill_bat_pit = can_kill_bat | has_whirlwind
can_kill_bubble = has_bombs | has_bow | has_whip | (has_sword & (has_boomerang | has_whirlwind))
has_range = has_bow | has_boomerang
has_range_objects = has_range | has_whirlwind  # range with
has_short_range = has_range | has_whip | has_sword_beam | has_bombs
can_ring_bell = has_sword | has_boomerang
has_cuccos = has_sob | has_whirlwind
ct_cuccos = has_sob | (has_whirlwind & hard_logic)

# Rupees
def has_rupees(count):
    return Has("Rupees", count)


class HasRequiredDungeons(Rule["SpiritTracksWorld"], game="The Legend of Zelda - Spirit Tracks"):
    @override
    def _instantiate(self, world: "SpiritTracksWorld") -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(world.options.dungeons_required.value, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        dungeons_required: int

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            # print(f"\tDungeons required: {self.dungeons_required} {state.count('_dungeon_reward', self.player)} {state.has('_dungeon_reward', self.player, count=self.dungeons_required)}")
            return state.has("_dungeon_reward", self.player, count=self.dungeons_required)


has_dungeon_rewards = [OptionFilter(SpiritTracksDarkRealmUnlock, SpiritTracksDarkRealmUnlock.option_dungeons, operator="ne")] | HasRequiredDungeons(options=[OptionFilter(SpiritTracksDarkRealmUnlock, SpiritTracksDarkRealmUnlock.option_dungeons)])

def st_has_dungeon_rewards(state, player):
    if state.multiworld.worlds[player].options.dark_realm_access != "dungeons":
        return True
    dungeon_count = state.multiworld.worlds[player].options.dungeons_required.value
    return state.has("_dungeon_reward", player, dungeon_count)
