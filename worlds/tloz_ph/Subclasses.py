from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region
from enum import IntEnum

if TYPE_CHECKING:
    from entrance_rando import ERPlacementState

class PHEntrance(Entrance):

    def is_valid_source_transition(self, er_state: "ERPlacementState") -> bool:
        return self.can_reach(er_state.collection_state)

    def can_connect_to(self, other: Entrance, dead_end: bool, er_state: "ERPlacementState") -> bool:
        # the implementation of coupled causes issues for self-loops since the reverse entrance will be the
        # same as the forward entrance. In uncoupled they are ok.

        # Check if there are enough valid entrances to go around for the dead ends
        if not hasattr(er_state, "dead_end_counter"):
            self.make_dead_end_counter(er_state)

        if not dead_end:
            combined_groups = {}
            for i in er_state.target_group_lookup[self.randomization_group] + er_state.target_group_lookup[other.randomization_group]:
                combined_groups.setdefault(i, 0)
                combined_groups[i] += 1
            for i, c in combined_groups.items():
                if i in er_state.dead_end_counter and er_state.dead_end_counter[i] - c <=0:
                    print(f"\tTried to connect {self.name} => {other.name}")
                    return False
        return self.randomization_type == other.randomization_type and (not er_state.coupled or self.name != other.name)

    def make_dead_end_counter(self, er_state: "ERPlacementState"):
        dead_ends_in_group = {}
        for dead_end in er_state.entrance_lookup.dead_ends:
            dead_ends_in_group.setdefault(dead_end.randomization_group, 0)
            dead_ends_in_group[dead_end.randomization_group] += 1

        remaining_entrances = {}
        target_group_lookup = er_state.target_group_lookup
        for group, count in dead_ends_in_group.items():
            remaining_entrances.setdefault(group, -count)
            print(f"looking for {count} entrances targeting {decode_entrance_groups(group)}")
            for entrance in er_state.entrance_lookup.others:
                if entrance.randomization_group in target_group_lookup[group]:
                    print(f"\t{entrance.name}")
                    remaining_entrances[group] += 1


        printable = {decode_entrance_groups(g):c for g, c in dead_ends_in_group.items()}
        print(f"Dead ends by group: {printable}")
        print(f"number of connections per group: {remaining_entrances}")
        er_state.dead_end_counter = remaining_entrances

class PHRegion(Region):
    entrance_type = PHEntrance

class PHTransition:
    """
    Datastructures for dealing with Transitions on the client side.
    Not to be confused with PHEntrances, that deals with entrance objects during ER placement.
    """

    def __init__(self, name, data):
        self.data = data

        self.name: str = name
        self.id: int | None = data.get("id", None)
        self.entrance: tuple = data["entrance"]
        self.exit: tuple = data["exit"]
        self.entrance_region: str = data["entrance_region"]
        self.exit_region: str = data["exit_region"]
        self.two_way: bool = data.get("two_way", True)
        self.category_group = data["type"]
        self.direction = data["direction"]
        self.island = data.get("island", EntranceGroups.NONE)
        self.coords: tuple | None = data.get("coords", None)
        self.extra_data: dict = data.get("extra_data", {})

        self.stage, self.room, _ = self.entrance
        self.scene: int = self.get_scene()
        self.exit_scene: int = self.get_exit_scene()
        self.exit_stage = self.exit[0]
        self.y = self.coords[1] if self.coords else None

        self.vanilla_reciprocal = None  # Paired location

        self.copy_number = 0

    def get_scene(self):
        return self.stage * 0x100 + self.room

    def get_exit_scene(self):
        return self.exit[0] * 0x100 + self.exit[1]

    def is_pairing(self, r1, r2) -> bool:
        return r1 == self.entrance_region and r2 == self.exit_region

    def get_y(self):
        return self.coords[1] if self.coords else None

    def detect_exit_simple(self, stage, room, entrance):
        return self.exit == (stage, room, entrance)

    def detect_exit_scene(self, scene, entrance):
        return self.exit_scene == scene and entrance == self.exit[2]

    def detect_exit(self, scene, entrance, coords, y_offest):
        if self.detect_exit_scene(scene, entrance):
            if entrance < 0xF0:
                return True
            # Continuous entrance check
            x_max = self.extra_data.get("x_max", 0x8FFFFFFF)
            x_min = self.extra_data.get("x_min", -0x8FFFFFFF)
            z_max = self.extra_data.get("z_max", 0x8FFFFFFF)
            z_min = self.extra_data.get("z_min", -0x8FFFFFFF)
            y = self.coords[1] if self.coords else coords["y"] - y_offest
            if coords["y"] - y_offest == y and x_max > coords["x"] > x_min and z_max > coords["z"] > z_min:
                return True
        return False

    def set_stage(self, new_stage):
        self.stage = new_stage
        self.scene = self.get_scene()
        self.entrance = tuple([new_stage] + list(self.entrance[1:]))

    def set_exit_stage(self, new_stage):
        self.exit = tuple([new_stage] + list(self.exit[1:]))
        self.exit_scene = self.get_exit_scene()
        self.exit_stage = self.exit[0]

    def copy(self):
        res = PHTransition(f"{self.name}{self.copy_number+1}", self.data)
        res.copy_number = self.copy_number + 1
        return res

    def __str__(self):
        return self.name

    def debug_print(self):
        print(f"Debug print for entrance {self.name}")
        print(f"\tentrance {self.entrance}")
        print(f"\texit {self.exit}")
        print(f"\tcoords {self.coords}")
        print(f"\textra_data {self.extra_data}")

island_lookup = {
    0: "sea",
    1: "mercay",
    2: "cannon",
    3: "ember",
    4: "molida",
    5: "spirit",
    6: "gust",
    7: "bannan",
    8: "uncharted",
    9: "zauz",
    10: "ghost",
    11: "goron",
    12: "frost",
    13: "dead",
    14: "ruins"
}
direction_lookup = {
    0: "none",
    1: "left",
    2: "right",
    3: "up",
    4: "down",
    5: "enter",
    6: "exit"}
type_lookup = {
    0: "none",
    1: "house",
    2: "cave",
    3: "port",
    4: "overworld",
    5: "dungeon",
    6: "boss",
    7: "dungeon_room",
    8: "warp",
    9: "stairs",
    10: "holes",
}

# Print EntranceGroups as human readable string
def decode_entrance_groups(group):
    direction = group & EntranceGroups.DIRECTION_MASK
    area = (group & EntranceGroups.AREA_MASK) >> 3
    island = (group & EntranceGroups.ISLAND_MASK) >> 7

    return f"{direction_lookup[direction]}_{type_lookup[area]}_{island_lookup[island]}"

class EntranceGroups(IntEnum):
    NONE = 0
    # Directions
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    INSIDE = 5
    OUTSIDE = 6
    # Types
    HOUSE = 1 << 3
    CAVE = 2 << 3
    ISLAND = 3 << 3
    OVERWORLD = 4 << 3
    DUNGEON_ENTRANCE = 5 << 3
    BOSS = 6 << 3
    DUNGEON_ROOM = 7 << 3
    WARP_PORTAL = 8 << 3
    STAIRS = 9 << 3
    HOLES = 10 << 3
    # Island mask
    SEA = 0 << 7
    MERCAY = 1 << 7
    CANNON = 2 << 7
    EMBER = 3 << 7
    MOLIDA = 4 << 7
    SPIRIT = 5 << 7
    GUST = 6 << 7
    BANNAN = 7 << 7
    UNCHARTED = 8 << 7
    ZAUZ = 9 << 7
    GHOST = 10 << 7
    GORON = 11 << 7
    FROST = 12 << 7
    DEAD = 13 << 7
    RUINS = 14 << 7

    # Bitmasks
    DIRECTION_MASK = HOUSE - 1
    AREA_MASK = MERCAY - HOUSE
    ISLAND_MASK =  ~0 << 7

    def __str__(self):
        return decode_entrance_groups(self.value)

    @staticmethod
    def area_shift(area):
        return area << 3

    @staticmethod
    def area_unshift(area):
        return area >> 3

    @staticmethod
    def island_shift(island):
        return island << 7

    @staticmethod
    def island_unshift(island):
        return island >> 7

OPPOSITE_ENTRANCE_GROUPS = {
    EntranceGroups.RIGHT: EntranceGroups.LEFT,
    EntranceGroups.LEFT: EntranceGroups.RIGHT,
    EntranceGroups.UP: EntranceGroups.DOWN,
    EntranceGroups.DOWN: EntranceGroups.UP,
    0: 0,
    EntranceGroups.NONE: EntranceGroups.NONE,
    EntranceGroups.INSIDE: EntranceGroups.OUTSIDE,
    EntranceGroups.OUTSIDE: EntranceGroups.INSIDE
}