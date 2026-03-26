import unittest
from typing import ClassVar, Tuple

from ...content import content_packs, ContentPack, StardewContent, unpack_content, StardewFeatures, feature
from ...strings.building_names import Building

default_features = StardewFeatures(
    worlds.stardew_valley.content.feature.booksanity.BooksanityDisabled(),
    worlds.stardew_valley.content.feature.building_progression.BuildingProgressionVanilla(starting_buildings={Building.farm_house}),
    feature.cropsanity.CropsanityDisabled(),
    worlds.stardew_valley.content.feature.fishsanity.FishsanityNone(),
    feature.friendsanity.FriendsanityNone(),
    worlds.stardew_valley.content.feature.skill_progression.SkillProgressionVanilla(),
    worlds.stardew_valley.content.feature.tool_progression.ToolProgressionVanilla()
)


class SVContentPackTestBase(unittest.TestCase):
    vanilla_packs: ClassVar[Tuple[ContentPack]] = (content_packs.pelican_town, content_packs.the_desert, content_packs.the_farm, content_packs.the_mines)
    mods: ClassVar[Tuple[str]] = ()

    content: ClassVar[StardewContent]

    @classmethod
    def setUpClass(cls) -> None:
        packs = cls.vanilla_packs + tuple(content_packs.by_mod[mod] for mod in cls.mods)
        cls.content = unpack_content(default_features, packs)
