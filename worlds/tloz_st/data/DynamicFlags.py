from .Addresses import STAddr

DYNAMIC_FLAGS = {
    "Outset Rei": {
        "on_scenes": [0x2F00],
        "not_has_locations": ["Outset Clear Rocks"],
        "unset_if_true": [(STAddr.adv_flags_0, 0x04), (STAddr.adv_flags_1, 0x80)],
        "reset_flags": ["RESET forest glyph"]
    },
    "Outset Bee Boy": {
        "on_scenes": [0x2F00],
        "not_has_locations": ["Outset Bee Tree"],
        "unset_if_true": [(STAddr.adv_flags_0, 0x44), (STAddr.adv_flags_1, 0x80)],
        "reset_flags": ["RESET forest glyph", "RESET Remove Ocean source"]
    },
    "Allow leaving Outset": {
        "on_scenes": [0x2F00],
        "has_locations": ["Outset Clear Rocks", "Outset Bee Tree"],
        "has_items": [["Forest Glyph", 1]],
        "set_if_true": [(STAddr.adv_flags_0, 0x04), (STAddr.adv_flags_1, 0x80)]
    },
    "RESET forest glyph": {
        "has_items": [["Forest Glyph", 1]],
        "set_if_true": [(STAddr.adv_flags_1, 0x80), (STAddr.adv_flags_0, 0x04)]
    },
    "Safety forest glyph on forest glyph map": {
        "on_scenes": [0x400],
        "has_items": [["Forest Glyph", 1]],
        "set_if_true": [(STAddr.adv_flags_1, 0x81), (STAddr.adv_flags_0, 0x04)]  # also prevents tree maze to fs
    },
    "Allow learning awakening song": {
        "on_scenes": [0x3000],
        "not_has_locations": ["Forest Sanctuary Song Statue"],
        "unset_if_true": [(STAddr.songs, 0x01)],
        "reset_flags": ["RESET fs statue"]
    },
    "RESET fs statue": {
        #"has_locations": ["Forest Sanctuary Song Statue"],
        "has_items": [["Song of Awakening", 1]],
        "set_if_true": [(STAddr.songs, 0x01)],
    },
    "Allow learning healing song": {
        "on_scenes": [0x190A],
        "not_has_locations": ["Wooded Temple Song Statue"],
        "unset_if_true": [(STAddr.songs, 0x02)],
        "reset_flags": ["RESET wt statue"]
    },
    "Allow learning healing song oct": {
        "on_scenes": [0x1b0a],
        "not_has_locations": ["Marine Temple Song Statue"],
        "unset_if_true": [(STAddr.songs, 0x02)],
        "reset_flags": ["RESET wt statue"]
    },
    "RESET wt statue": {
        "has_items": [["Song of Healing", 1]],
        "set_if_true": [(STAddr.songs, 0x02)],
    },
    "Allow learning light song": {
        "on_scenes": [0x3700],
        "not_has_locations": ["Trading Post Song of Light Statue"],
        "unset_if_true": [(STAddr.songs, 0x08)],
        "reset_flags": ["RESET trading post statue"]
    },
    "RESET trading post statue": {
        #"has_locations": ["Trading Post Song of Light Statue"],
        "has_items": [["Song of Light", 1]],
        "set_if_true": [(STAddr.songs, 0x08)],
    },
    "Allow learning discovery song": {
        "on_scenes": [0x2B00],
        "not_has_locations": ["Anouki Village Song Statue"],
        "unset_if_true": [(STAddr.songs, 0x10)],
        "reset_flags": ["RESET av statue"]
    },
    "RESET av statue": {
        # "has_locations": ["Anouki Village Song Statue"],
        "has_items": [["Song of Discovery", 1]],
        "set_if_true": [(STAddr.songs, 0x10)],
    },
    "Stagnox location": {
        "on_scenes": [0x1E00], #TODO seems this can also be 0x1900 instead? or maybe not taking away source fast enough?
        "not_has_locations": ["Wooded Temple Dungeon Reward"],
        "unset_if_true": [(STAddr.adv_flags_0, 0x10)],
        "reset_flags": ["RESET stagnox reward"]
    },
    "Cactops location": {
        "on_scenes": [0x2000],
        "not_has_locations": ["Marine Temple Dungeon Reward"],
        "unset_if_true": [(STAddr.adv_flags_0, 0x40)],
        "reset_flags": ["RESET Add Ocean Source"]
    },
    "Skeldritch location": {
        "on_scenes": [0x2200],
        "not_has_locations": ["Desert Temple Dungeon Reward"],
        "unset_if_true": [(STAddr.adv_flags_1a, 0x01)],
        "reset_flags": ["RESET Add Sand Source", "RESET Remove Sand Source"]
    },
    "RESET Add Sand Source": {
        "has_items": [["Sand Source", 1]],
        "set_if_true": [(STAddr.adv_flags_1a, 0x01)]
    },
    "RESET Remove Sand Source": {
        "has_items": [["Sand Source", 0]],
        "unset_if_true": [(STAddr.adv_flags_1a, 0x01)]
    },
    "RESET stagnox reward": {
        "has_items": [["Forest Source", 1]],
        "set_if_true": [(STAddr.adv_flags_0, 0x10)]
    },
    "Remove Bow of light in desert temple": {
        "on_scenes": [0x1d05],
        "unset_if_true": [(STAddr.adv_flags_16, 1)],
        "reset_flags": ["RESET Bow of Light"]
    },
    "Remove Forest Source": {
        "on_scenes": [0x1E03, 0x1E0A],
        "has_locations": ["Wooded Temple Dungeon Reward"],
        "has_items": [["Forest Source", 0]], #doesn't have item
        "unset_if_true": [(STAddr.adv_flags_0, 0x10)],
    },
    "Allow Rabbit Net Read": {
        "on_scenes": [0x3E00],
        "not_has_locations": ["Rabbit Haven Net Gift"],
        "unset_if_true": [(STAddr.adv_flags_1a, 0x40)],
    },
    "Skip intro Rabbit Net dialogue": {
        "on_scenes": [0x3E00],
        "has_locations": ["Rabbit Haven Net Gift"],
        "set_if_true": [(STAddr.adv_flags_1a, 0x40)],
    },
    "Allow rabbit catching": {
        "on_scenes": [0x0400],
        "has_items": [["Rabbit Net", 1]],
        "set_if_true": [(STAddr.adv_flags_1a, 0x40)],
    },
    "Disallow rabbit catching": {
        "on_scenes": [0x0400],
        "has_items": [["Rabbit Net", 0]],
        "unset_if_true": [(STAddr.adv_flags_1a, 0x40)],
    },
    "Move Alfonso to castle town station": {
        "on_scenes": [0x2900],
        "not_has_locations": ["Outset Receive Stamp Book"],
        "has_items": [["Snow Glyph", 1]],
        "set_if_true": [(STAddr.adv_flags_11, 0x20)],
        "check_bits": [(STAddr.adv_flags_11, 0x40, "not")],
        "has_slot_data": [("randomize_passengers", [1, 2, 3])],
        "reset_flags": ["RESET Alfonso"]
    },
    "RESET Alfonso": {
        "on_scenes": [0x2F00],
        "has_locations": ["Outset Receive Stamp Book"],
        "unset_if_true": [(STAddr.adv_flags_11, 0x60)],
        "set_if_true": [(STAddr.adv_flags_1b, 0x02)],
    },
    "Allow Stamp Book check": {
        "on_scenes": [0x2F0A],
        "not_has_locations": ["Outset Receive Stamp Book"],
        "has_slot_data": [("randomize_passengers", 1)],
        "unset_if_true": [(STAddr.adv_flags_25, 0x02), (STAddr.adv_flags_0, 0x20)],
        "reset_flags": ["RESET Stamp Book Check", "RESET Add Snow Source"]
    },
    "Allow Stamp Book check alfonzo item": {
        "on_scenes": [0x2F0A],
        "not_has_locations": ["Outset Receive Stamp Book"],
        "has_items": [("Passenger: Alfonzo", 1)],
        "has_slot_data": [("randomize_passengers", [2, 3])],
        "unset_if_true": [(STAddr.adv_flags_25, 0x02), (STAddr.adv_flags_0, 0x20)],
        "set_if_true": [(STAddr.adv_flags_11, 0x40)],
        "reset_flags": ["RESET Stamp Book Check", "RESET Add Snow Source"]
    },
    "Allow Stamp Book check no passengers": {
        "on_scenes": [0x2F0A],
        "not_has_locations": ["Outset Receive Stamp Book"],
        "has_slot_data": [("randomize_passengers", 0)],
        "has_items": [["Snow Glyph", 1]],
        "unset_if_true": [(STAddr.adv_flags_25, 0x02), (STAddr.adv_flags_0, 0x20)],
        "set_if_true": [(STAddr.adv_flags_11, 0x40)],
        "reset_flags": ["RESET Stamp Book Check", "RESET Add Snow Source"]
    },
    "RESET Stamp Book Check": {
        "has_items": [["Stamp Book", 1]],
        "set_if_true": [(STAddr.adv_flags_25, 0x02)],
    },
    "Allow stamp rewards": {
        "on_scenes": [0x2F0A],
        "has_locations": ["Outset Receive Stamp Book"],
        "set_if_true": [(STAddr.adv_flags_0, 0x20)],
        "reset_flags": ["RESET Remove Snow source"]
    },

    "Fraaz location": {
        "on_scenes": [0x1F00],
        "not_has_locations": ["Blizzard Temple Dungeon Reward"],
        "unset_if_true": [(STAddr.adv_flags_0, 0x20)],
        "reset_flags": ["RESET Add Snow Source", "RESET fraaz don't have source"]
    },
    "RESET fraaz don't have source": {
        "has_items": [["Snow Source", 0]],
        "unset_if_true": [(STAddr.adv_flags_0, 0x20)]
    },
    "Remove Snow Source": {
        "on_scenes": [0x1F03, 0x1F04], #TODO check
        "has_locations": ["Blizzard Temple Dungeon Reward"],
        "has_items": [["Snow Source", 0]],
        "unset_if_true": [(STAddr.adv_flags_0, 0x20)],
    },
    "Anjean kick out after ocean glyph fix": {
        "on_scenes": [0x1401],
        "has_items": [["Ocean Glyph", 1]],
        "set_if_true": [(STAddr.adv_flags_17, 0x20)]
    },
    "Snow realm crashes with snow source and no blizzard tracks": {
        "on_scenes": [0x500],
        "has_items": [["Snow Source", 1], ["Blizzard Temple Tracks", 0]],
        "unset_if_true": [(STAddr.adv_flags_0, 0x20)],
        "reset_flags": ["RESET Add Snow Source"]
    },
    "Snow realm crashes fire glyph and no blizzard tracks": {
        "on_scenes": [0x500],
        "has_items": [["Fire Glyph", 1], ["Blizzard Temple Tracks", 0]],
        "unset_if_true": [(STAddr.adv_flags_2, 0x04)],
        "reset_flags": ["RESET fire glyph"]
    },
    "Forest realm crashes fire glyph and no ocean glyph": {
        "on_scenes": [0x400],
        "has_items": [["Fire Glyph", 1], ["Ocean Glyph", 0]],
        "unset_if_true": [(STAddr.adv_flags_2, 0x04)],
        "reset_flags": ["RESET fire glyph"]
    },
    "RESET fire glyph": {
        "set_if_true": [(STAddr.adv_flags_2, 0x04)],
        "has_items": [["Fire Glyph", 1]],
    },
    # "Forest Sanctuary reset duet":{ #TODO wrong flag?
    #     "on_scenes": [0x3001],
    #     "not_has_locations": ["Forest Sanctuary Gage Duet"],
    #     "unset_if_true": [(0x265715, 0x01)]
    # },
    # "Assume duet done outside room":{
    #     "on_scenes": [0x3000],
    #     "not_has_locations": ["Forest Sanctuary Gage Duet"],
    #     "set_if_true": [(0x265715, 0x01)]
    # },

    # Portals
    "Allow Portal near castle town always open": {
        "on_scenes": [0x0400],
        "has_items": [["Snow Glyph", 1]],
        "has_slot_data": [("portal_behavior", 1)],
        "set_if_true": [(STAddr.adv_flags_30, 0x08)]  # activates portal to sw snow realm
    },
    "Allow Portal near castle town item": {
        "on_scenes": [0x0400],
        "has_items": [["Snow Glyph", 1],
                      ["Portal Unlock: Hyrule Castle to Anouki Village", 1]],
        "has_slot_data": [("portal_behavior", 2)],
        "set_if_true": [(STAddr.adv_flags_30, 0x08)]  # activates portal to sw snow realm
    },
    "Keep portal loc open anouki village": {
        "on_scenes": [0x0500],
        "has_slot_data": [["portal_checks", 1]],
        "not_has_locations": ["Snow Realm Shoot SW Portal"],
        "unset_if_true": [(STAddr.adv_flags_30, 0x08)]  # activates portal to sw snow realm
    },
    "Open anouki portal no cannon": {
        "on_scenes": [0x0500],
        "has_slot_data": [["portal_checks", 0]],
        "set_if_true": [(STAddr.adv_flags_30, 0x08)]
    },
    "Close Castle town portal no item": {
        "on_scenes": [0x0400],
        "has_slot_data": [("portal_behavior", 2)],
        "has_items": [["Portal Unlock: Hyrule Castle to Anouki Village", 0]],
        "unset_if_true": [(STAddr.adv_flags_30, 0x08)]  # activates portal to sw snow realm
    },

    "Allow portal snow realm E to Forest S always open": {
        "on_scenes": [0x500],
        "has_items": [["Forest Realm SE Portal Tracks", 1]],
        "has_slot_data": [("portal_behavior", 1)],
        "set_if_true": [(STAddr.adv_flags_30, 0x20)]
    },
    "Allow portal snow realm E to Forest S item": {
        "on_scenes": [0x500],
        "has_items": [["Forest Realm SE Portal Tracks", 1],
                      ["Portal Unlock: Trading Post to E Snow Realm", 1]],
        "has_slot_data": [("portal_behavior", 2)],
        "set_if_true": [(STAddr.adv_flags_30, 0x20)]
    },
    "Keep portal loc open s trading post": {
        "on_scenes": [0x400],
        "not_has_locations": ["Forest Realm Shoot SE Portal"],
        "has_slot_data": [["portal_checks", 1]],
        "unset_if_true": [(STAddr.adv_flags_30, 0x20)]
    },
    "open portal s trading post no cannon": {
        "on_scenes": [0x400],
        "has_items": [("Blizzard Temple Tracks", 1)],
        "has_slot_data": [["portal_checks", 0]],
        "set_if_true": [(STAddr.adv_flags_30, 0x20)]
    },
    "Close portal e snow realm items": {
        "on_scenes": [0x500],
        "has_items": [["Portal Unlock: Trading Post to E Snow Realm", 0]],
        "has_slot_data": [("portal_behavior", 2)],
        "unset_if_true": [(STAddr.adv_flags_30, 0x20)]
    },

    "Dark realm restart for dynamic entrances": {
        "on_scenes": [0x400],
        "unset_if_true": [(STAddr.adv_flags_57, 0x30)]
    },
    "Dark realm spawn demon train quick": {
        "on_scenes": [0x1000, 0x10FF],
        "set_if_true": [(STAddr.adv_flags_57, 0x30)]
    },

    "Allow Portal near marine temple always open": {
        "on_scenes": [0x600],
        "has_items": [["Sand to Fire Connection Tracks", 1]],
        "has_slot_data": [("portal_behavior", 1)],
        "set_if_true": [(STAddr.adv_flags_30, 0x80)]
    },
    "Allow Portal near marine temple item": {
        "on_scenes": [0x600],
        "has_items": [["Sand to Fire Connection Tracks", 1],
                      ["Portal Unlock: Fire Sand Connection to Marine Temple", 1]],
        "has_slot_data": [("portal_behavior", 2)],
        "set_if_true": [(STAddr.adv_flags_30, 0x80)]
    },
    "Allow Portal sand connection cannonless": {
        "on_scenes": [0x700],
        "has_items": [["Marine Temple Tracks", 1]],
        "has_slot_data": [("portal_checks", 0)],
        "set_if_true": [(STAddr.adv_flags_30, 0x80)]
    },
    "Prevent Portal sand connection to marine location": {
        "on_scenes": [0x700],
        "not_has_locations": ["Fire Realm Shoot Sand Portal"],
        "has_slot_data": [("portal_checks", 1)],
        "unset_if_true": [(STAddr.adv_flags_30, 0x80)]
    },

    "Allow Portal sand temple shortcut always open": {
        "on_scenes": [0x600],
        "has_items": [["Desert Temple Tracks", 1], ["Sand Realm Tracks", 1]],
        "has_slot_data": [("portal_behavior", 1)],
        "set_if_true": [(STAddr.adv_flags_31, 0x01)],
        "not_on_entrance": [0x7, 0xB, 0xFB],
    },
    "Allow Portal sand temple shortcut with item": {
        "on_scenes": [0x600],
        "has_items": [["Desert Temple Tracks", 1], ["Sand Realm Tracks", 1],
                      ("Portal Unlock: Fire Sand Connection to Marine Temple", 1)],
        "has_slot_data": [("portal_behavior", 2)],
        "set_if_true": [(STAddr.adv_flags_31, 0x01)],
        "not_on_entrance": [0x7, 0xB, 0xFB],
    },
    "Close Portal sand temple shortcut always open right": {
        "on_scenes": [0x600],
        "has_slot_data": [("portal_checks", 1)],
        "not_has_locations": ["Sand Realm Shoot Temple Portal"],
        "on_entrance": [0x7, 0xB, 0xFB],  # will also close if coming from north, but you can reload at sand sanc
        "unset_if_true": [(STAddr.adv_flags_31, 0x01)]
    },

    "Keep portal loc open icy spring": {
        "on_scenes": [0x0500],
        "has_slot_data": [["portal_checks", 1]],
        "not_has_locations": ["Snow Realm Shoot N Portal"],
        "unset_if_true": [(STAddr.adv_flags_31, 0x02)]  # activates portal to sw snow realm
    },
    "Open portal for free icy spring": {
        "on_scenes": [0x0500],
        "has_slot_data": [["portal_checks", 0]],
        "has_items": [["Mountain Temple Tracks", 1]],
        "set_if_true": [(STAddr.adv_flags_31, 0x02)]  # activates portal to sw snow realm
    },
    "Allow Portal mountain always open": {
        "on_scenes": [0x700],
        "has_items": [["N Icy Spring Tracks", 1]],
        "has_slot_data": [("portal_behavior", 1)],
        "set_if_true": [(STAddr.adv_flags_31, 0x02)],
    },
    "Allow Portal mountain with item": {
        "on_scenes": [0x700],
        "has_items": [["N Icy Spring Tracks", 1],
                      ("Portal Unlock: Icy Spring to Mountain Temple", 1)],
        "has_slot_data": [("portal_behavior", 2)],
        "set_if_true": [(STAddr.adv_flags_31, 0x02)]
    },

    "Allow Portal goron village": {
        "on_scenes": [0x0700],
        "has_items": [["Forest Realm SW Cave Tracks", 1]],
        "has_slot_data": [("portal_behavior", 1)],
        "set_if_true": [(STAddr.activate_portals, 0x20)]
    },
    "Allow Portal goron village item": {
        "on_scenes": [0x0700],
        "has_items": [["Forest Realm SW Cave Tracks", 1],
                      ["Portal Unlock: Forest Cave to Goron Village", 1]],
        "has_slot_data": [("portal_behavior", 2)],
        "set_if_true": [(STAddr.activate_portals, 0x20)]
    },
    "Open cave portal no cannon": {
        "on_scenes": [0x0400],
        "has_items": [["Fire Glyph", 1]],
        "has_slot_data": [["portal_checks", 0]],
        "set_if_true": [(STAddr.activate_portals, 0x20)]
    },
    "Keep portal loc open cave": {
        "on_scenes": [0x0400],
        "has_slot_data": [["portal_checks", 1]],
        "has_items": [["Cannon", 1]],
        "not_has_locations": ["Forest Realm Shoot SE Portal"],
        "unset_if_true": [(STAddr.activate_portals, 0x20)]
    },
    "Open portal cannonless": {
        "on_scenes": [0x0400],
        "has_slot_data": [["portal_checks", 1], ("portal_behavior", 1)],
        "has_items": [["Fire Glyph", 1], ["Cannon", 0]],
        "not_has_locations": ["Forest Realm Shoot SE Portal"],
        "set_if_true": [(STAddr.activate_portals, 0x20)]
    },

    # Sanctuaries
    "Gage don't have spirit flute": {
        "on_scenes": [0x3001],
        "has_items": [("Spirit Flute", 0)],
        "set_if_true": [(STAddr.adv_flags_1, 1)]
    },
    "Gage can play duet": {
        "on_scenes": [0x3001],
        "has_items": [("Spirit Flute", 1)],
        "not_has_locations": ["Forest Sanctuary Song of Restoration"],
        "unset_if_true": [(STAddr.adv_flags_1, 1)]
    },
    "Gage Reset flags": {
        "on_scenes": [0x3001],
        "unset_if_true": [(STAddr.rail_restorations, 0x2)],
        "reset_flags": ["FoS Reset FTT", "FoS Reset FTT not has"]
    },
    "FoS Reset FTT not has": {
        "has_items": [("Wooded Temple Tracks", 0)],
        "unset_if_true": [(STAddr.rail_restorations, 0x2)]
    },
    "FoS Reset FTT": {
        "has_items": [("Wooded Temple Tracks", 1)],
        "set_if_true": [(STAddr.rail_restorations, 0x2)]
    },
    "Steem don't have spirit flute": {
        "on_scenes": [0x3102],
        "has_items": [("Spirit Flute", 0)],
        "set_if_true": [(STAddr.adv_flags_1, 6)]  # ocean restoration removes him
    },
    "Steem can play duet": {
        "on_scenes": [0x3102],
        "has_items": [("Spirit Flute", 1)],
        "not_has_locations": ["Snowfall Sanctuary Song of Restoration"],
        "unset_if_true": [(STAddr.adv_flags_1, 6)]
    },
    "Snow sanc remove vessel": {
        "on_scenes": [0x3102],
        "has_locations": ["Snowfall Sanctuary Deliver Vessel"],
        "not_has_locations": ["Snowfall Sanctuary Song of Restoration"],
        "unset_if_true": [(STAddr.adv_flags_40, 0x20), (STAddr.adv_flags_e, 0x10)],
        "reset_flags": ["RESET snow sanc vessel"]
    },
    "RESET snow sanc vessel": {
        "set_if_true": [(STAddr.adv_flags_40, 0x20), (STAddr.adv_flags_e, 0x10)],
    },
    "Always remove btt in snow sanc room": {
        "on_scenes": [0x3102],
        "unset_if_true": [(STAddr.rail_restorations, 0x4)],
        "reset_flags": ["Snow sanc Reset BTT not has", "Snow sanc Reset BTT"]
    },
    "Snow sanc Reset BTT not has": {
        "has_items": [("Blizzard Temple Tracks", 0)],
        "unset_if_true": [(STAddr.rail_restorations, 0x4), (STAddr.adv_flags_1, 2)]
    },
    "Snow sanc Reset BTT": {
        "has_items": [("Blizzard Temple Tracks", 1)],
        "set_if_true": [(STAddr.rail_restorations, 0x4), (STAddr.adv_flags_1, 2)]
    },
    "ToS Summit maladus cs": {
        "on_scenes": [0x1500],
        "set_if_true": [(STAddr.adv_flags_20, 0x4)]
    },
    "Rael don't have spirit flute": {
        "on_scenes": [0x3502],
        "has_items": [("Spirit Flute", 0)],
        "set_if_true": [(STAddr.adv_flags_19, 0x8)]
    },
    "Rael can play duet": {
        "on_scenes": [0x3502],
        "has_items": [("Spirit Flute", 1)],
        "not_has_locations": ["Sand Sanctuary Song of Restoration"],
        "unset_if_true": [(STAddr.adv_flags_19, 0x8)]
    },
    "Rael Always remove dtt ": {
        "on_scenes": [0x3502],
        "unset_if_true": [(STAddr.rail_restorations, 0x20)],
        "reset_flags": ["Sand Sanc Reset DTT not has", "Sand Sanc Reset DTT"]
    },
    "Sand Sanc Reset DTT not has": {
        "has_items": [("Desert Temple Tracks", 0)],
        "unset_if_true": [(STAddr.rail_restorations, 0x20)]
    },
    "Sand Sanc Reset DTT": {
        "has_items": [("Desert Temple Tracks", 1)],
        "set_if_true": [(STAddr.rail_restorations, 0x20)]
    },
    "Sand sanc get cuccos no cargo rando": {
        "on_scenes": [0x3500],
        "has_slot_data": [("randomize_cargo", 0)],
        "set_if_true": [(STAddr.adv_flags_44, 0x8), (STAddr.adv_flags_d, 0x8)]
    },
    # ToS climb flags
    "ToS open sections": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 0]],
        "set_if_true": [(STAddr.adv_flags_0, 0xF0)],
        "reset_flags": ["RESET Remove Forest source", "RESET Remove Snow source",
                        "RESET Remove Ocean source", "RESET Remove Fire source"]
    },
    "ToS Snow source sections": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 1]],
        "has_items": [("Snow Source", 1)],
        "set_if_true": [(STAddr.adv_flags_0, 0x20)],
    },
    "ToS progressive sections 0": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 0]],
        "has_items": [("Progressive ToS Section", 0)],
        "unset_if_true": [(STAddr.adv_flags_0, 0xF0)],
        "reset_flags": ["RESET Add Forest source", "RESET Add Snow Source",
                        "RESET Add Ocean source", "RESET Add Fire source"]
    },
    "ToS progressive sections 1": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 0]],
        "has_items": [("Progressive ToS Section", 1, "has_exact")],
        "set_if_true": [(STAddr.adv_flags_0, 0x10)],
        "unset_if_true": [(STAddr.adv_flags_0, 0xE0)],
        "reset_flags": ["RESET Remove Forest source", "RESET Add Snow Source",
                        "RESET Add Ocean source", "RESET Add Fire source"]
    },
    "ToS progressive sections 2": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 0]],
        "has_items": [("Progressive ToS Section", 2, "has_exact")],
        "set_if_true": [(STAddr.adv_flags_0, 0x30)],
        "unset_if_true": [(STAddr.adv_flags_0, 0xC0)],
        "reset_flags": ["RESET Remove Forest source", "RESET Remove Snow source",
                        "RESET Add Ocean source", "RESET Add Fire source"]
    },
    "ToS progressive sections 3": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 0]],
        "has_items": [("Progressive ToS Section", 3, "has_exact")],
        "set_if_true": [(STAddr.adv_flags_0, 0x70)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x80)],
        "reset_flags": ["RESET Remove Forest source", "RESET Remove Snow source",
                        "RESET Remove Ocean source", "RESET Add Fire source"]
    },
    "ToS progressive sections 4": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 0]],
        "has_items": [("Progressive ToS Section", 4)],
        "set_if_true": [(STAddr.adv_flags_0, 0xF0)],
        "reset_flags": ["RESET Remove Forest source", "RESET Remove Snow source",
                        "RESET Remove Ocean source", "RESET Remove Fire source"]
    },
    "ToS progressive sections 0 base": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 1]],
        "has_items": [("Progressive ToS Section", 1, "has_exact")],
        "unset_if_true": [(STAddr.adv_flags_0, 0xF0)],
        "reset_flags": ["RESET Add Forest source", "RESET Add Snow Source",
                        "RESET Add Ocean source", "RESET Add Fire source"]
    },
    "ToS progressive sections 1 base": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 1]],
        "has_items": [("Progressive ToS Section", 2, "has_exact")],
        "set_if_true": [(STAddr.adv_flags_0, 0x10)],
        "unset_if_true": [(STAddr.adv_flags_0, 0xE0)],
        "reset_flags": ["RESET Remove Forest source", "RESET Add Snow Source",
                        "RESET Add Ocean source", "RESET Add Fire source"]
    },
    "ToS progressive sections 2 base": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 1]],
        "has_items": [("Progressive ToS Section", 3, "has_exact")],
        "set_if_true": [(STAddr.adv_flags_0, 0x30)],
        "unset_if_true": [(STAddr.adv_flags_0, 0xC0)],
        "reset_flags": ["RESET Remove Forest source", "RESET Remove Snow source",
                        "RESET Add Ocean source", "RESET Add Fire source"]
    },
    "ToS progressive sections 3 base": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 1]],
        "has_items": [("Progressive ToS Section", 4, "has_exact")],
        "set_if_true": [(STAddr.adv_flags_0, 0x70)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x80)],
        "reset_flags": ["RESET Remove Forest source", "RESET Remove Snow source",
                        "RESET Remove Ocean source", "RESET Add Fire source"]
    },
    "ToS progressive sections 5": {
        "on_scenes": [0x1700],
        "has_slot_data": [["tos_section_unlocks", 2], ["tos_unlock_base_item", 1]],
        "has_items": [("Progressive ToS Section", 5)],
        "set_if_true": [(STAddr.adv_flags_0, 0xF0)],
        "reset_flags": ["RESET Remove Forest source", "RESET Remove Snow source",
                        "RESET Remove Ocean source", "RESET Remove Fire source"]
    },

    "RESET Remove Forest source": {
        "has_items": [("Forest Source", 0)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x10)],
    },
    "RESET Remove Snow source": {
        "has_items": [("Snow Source", 0)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x20)],
    },
    "RESET Remove Ocean source": {
        "has_items": [("Ocean Source", 0)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x40)],
    },
    "RESET Remove Fire source": {
        "has_items": [("Fire Source", 0)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x80)],
    },
    "RESET Add Forest source": {
        "has_items": [("Forest Source", 1)],
        "set_if_true": [(STAddr.adv_flags_0, 0x10)],
    },
    "RESET Add Snow Source": {
        "has_items": [("Snow Source", 1)],
        "set_if_true": [(STAddr.adv_flags_0, 0x20)],
    },
    "RESET Add Ocean source": {
        "has_items": [("Ocean Source", 1)],
        "set_if_true": [(STAddr.adv_flags_0, 0x40)],
    },
    "RESET Add Fire source": {
        "has_items": [("Fire Source", 1)],
        "set_if_true": [(STAddr.adv_flags_0, 0x80)],
    },

    # Shop stuff
    "Remove beedle bomb flag": {
        "on_scenes": [0x4503],
        "not_has_locations": ["Beedle Buy Bomb Bag"],
        "has_slot_data": [("shopsanity", "uniques")],
        "unset_if_true": [(STAddr.adv_flags_22, 0x02), (STAddr.bomb_capacity, 2)],
        "reset_flags": ["RESET beedle bomb bag flag"]
    },
    "RESET beedle bomb bag flag": {
        "has_items": [("Bombs (Progressive)", 1)],
        "set_if_true": [(STAddr.adv_flags_22, 0x02)],
        "overwrite_if_true": [(STAddr.bomb_capacity, "Bombs (Progressive)", -1)]
    },
    "Add beedle bomb flag": {
        "on_scenes": [0x4503],
        "has_slot_data": [("shopsanity", "uniques", "not")],
        "set_if_true": [(STAddr.adv_flags_22, 0x02)],
    },
    # Whip Race
    "Skip whip race HC": {
        "on_scenes": [0x3800],
        "has_slot_data": [("randomize_minigames", [0, 1])],
        "set_if_true": [(STAddr.adv_flags_26, 0x02)],
    },
    "Skip whip race bomb bag": {
        "on_scenes": [0x3800],
        "has_slot_data": [("randomize_minigames", [0, 2])],
        "set_if_true": [(STAddr.adv_flags_26, 0x01)],
    },

    # Linebeck Trade
    "Has Regal Ring for Linebeck": {
        "on_scenes": [0x3700],
        "has_slot_data": [("randomize_passengers", 0)],
        "has_items": [("Treasure: Regal Ring", 1)],
        "check_bits": [(STAddr.adv_flags_24, 0x10, "not")],  # does not set flag after giving ring
        "set_if_true": [(STAddr.adv_flags_3e, 0x10)]
    },
    "Reset linebeck regal ring stuff in cave": {
        "on_scenes": [0x3702],
        "not_has_locations": ["Trading Post Chest"],
        "unset_if_true": [(STAddr.adv_flags_3e, 0x10)]
    },
    "Bring Kenzo to TP": {
        "on_scenes": [0x3700],
        "has_items": [("Passenger: Kenzo", 1)],
        "has_slot_data": [("randomize_passengers", [2, 3])],
        "check_bits": [(STAddr.adv_flags_18, 0x40, "not")],
        "set_if_true": [(STAddr.adv_flags_18, 0x20)],
        "overwrite_if_true": [(STAddr.passenger_goal, 0x37),
                              (STAddr.passenger_tag_0, 0x43524654),
                              (STAddr.has_passenger_0, 0)],
    },
    "Has Kenzo and Ring": {
        "on_scenes": [0x3700],
        "has_items": [("Treasure: Regal Ring", 1)],
        "has_locations": ["Bring Kenzo to Trading Post"],
        "has_slot_data": [("randomize_passengers", [1, 2, 3])],
        "check_bits": [(STAddr.adv_flags_24, 0x10, "not")],  # does not set flag after giving ring
        "set_if_true": [(STAddr.adv_flags_3e, 0x10)]
    },
    "Prevent Linebeck ring passengers": {
        "on_scenes": [0x3700],
        "unset_if_true": [(STAddr.adv_flags_3e, 0x10)],
        "has_slot_data": [("randomize_passengers", [1, 2, 3])],
        "not_has_locations": ["Bring Kenzo to Trading Post"],
    },
    "Prevent Linebeck ring item": {
        "on_scenes": [0x3700],
        "unset_if_true": [(STAddr.adv_flags_3e, 0x10)],
        "has_items": [("Treasure: Regal Ring", 0)],
    },
    "Remove Ocean Source for Kenzo Dialogue": {
        "on_scenes": [0x3700],
        "not_has_locations": ["Bring Kenzo to Trading Post"],
        "has_slot_data": [("randomize_passengers", [1, 2, 3])],
        "unset_if_true": [(STAddr.adv_flags_0, 0x40), (STAddr.adv_flags_18, 0x82), (STAddr.adv_flags_c, 0x20)],
        "reset_flags": ["RESET Add Ocean source"]
    },
    "Allow Kenzo to leave for AV": {
        "on_scenes": [0x3700],
        "check_bits": [(STAddr.adv_flags_24, 0x10)],
        "set_if_true": [(STAddr.adv_flags_3d, 2)],
        "has_items": [("Snow Glyph", 1)],
        "has_slot_data": [("randomize_passengers", [1, 3])],
    },
    "Prevent Kenzo from leaving TP": {
        "on_scenes": [0x3700],
        "has_slot_data": [("randomize_passengers", [0, 2])],
        "unset_if_true": [(STAddr.adv_flags_3d, 2)],
    },
    "Prevent Kenzo from leaving TP snow glyph": {
        "on_scenes": [0x3700],
        "has_items": [("Snow Glyph", 0)],
        "unset_if_true": [(STAddr.adv_flags_3d, 2)],
    },
    "Prep for TP kenzo loc": {
        "on_scenes": [0x3700],
        "not_has_locations": ["Trading Post Pick Up Kenzo"],
        "has_slot_data": [("randomize_passengers", 3)],
        "unset_if_true": [(STAddr.adv_flags_3c, 0x10)],
    },
    # Anouki chief location
    "Enter Anouki Chief house": {
        "on_scenes": [0x2b01],
        "not_has_locations": ["Anouki Village Pair Villagers"],
        "set_if_true": [(STAddr.adv_flags_b, 0x2), # Started Quest
                     (STAddr.adv_flags_18, 0x10), # Talked to all anouki
                     ],
        "unset_if_true": [(STAddr.adv_flags_b, 0x10),  # Remove finished quest flag
                        (STAddr.adv_flags_0, 0x20),  # Remove snow source
                        (STAddr.adv_flags_1, 0x02),  # Remove btt
                        (STAddr.adv_flags_c, 0x08),  # Don't advance dialogue after btt
                        (STAddr.adv_flags_4, 0x02)], # Remove Wagon, he gives ice hint
        "reset_flags": ["Snow sanc Reset BTT", "RESET Add Snow Source", "RESET Wagon"]
    },
    "Anouki village remove icons": {
        "on_scenes": [0x2b00],
        "set_if_true": [(STAddr.adv_flags_b, 0x10)],
    },
    "RESET Wagon": {
        "has_items": [("Wagon", 1)],
        "set_if_true": [(STAddr.adv_flags_4, 0x02)],
    },
    "Lock Snow Realm Rocktite Cave": {
        "on_scenes": [0x500],
        "has_items": [("Snowfall Sanctuary Cave Key", 0), ("Blizzard Temple Tracks", 0)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x20), (STAddr.adv_flags_b, 0x10)],
        "reset_flags": ["RESET Add Snow Source"]
    },
    "Unlock Snow Sanc Cave": {
        "on_scenes": [0x500],
        "has_items": [("Snowfall Sanctuary Cave Key", 1)],
        "set_if_true": [(STAddr.adv_flags_b, 0x10)],
    },
    "Anouki shop skip HC": {
        "on_scenes": [0x3103],
        "has_slot_data": [("shopsanity", "uniques", "not")],
        "set_if_true": [(STAddr.adv_flags_21, 0x40)],
    },
    "Remove shield from shield shops": {
        "on_scenes": [0x2a05, 0x290a, 0x3103, 0x370a],
        "unset_if_true": [(STAddr.items_2, 1)],
        "has_slot_data": [("shopsanity", "shields")],
        "reset_flags": ["RESET add shield"]
    },
    "Remove prize postcards in shops": {
        "on_scenes": [0x2a05, 0x290a, 0x3103, 0x2c02],
        "unset_if_true": [(STAddr.postcard_count, 0xFF)],
        "has_slot_data": [("shopsanity", "postcards")],
    },
    "RESET add shield": {
        "has_items": [("Shield", 1)],
        "set_if_true": [(STAddr.items_2, 1)],
    },
    # Take em all on stuff
    "TEAO Unlock 1": {
        "on_scenes": [0x290B],
        "has_items": [("Ocean Source", 1)],
        "has_slot_data": [("randomize_minigames", [2, 3, 4])],
        "set_if_true": [(STAddr.adv_flags_2a, 0x4)],
        "on_entrance": [0],
        "reset_flags": ["RESET TEAO 1"]
    },
    "TEAO Unlock 2": {
        "on_scenes": [0x290B],
        "has_items": [("Sand Source", 1)],
        "has_slot_data": [("randomize_minigames", [4])],
        "set_if_true": [(STAddr.adv_flags_2a, 0xC)],
        "on_entrance": [0],
        "reset_flags": ["RESET TEAO 1", "RESET TEAO 2"]
    },
    "RESET TEAO 1": {
        "not_has_locations": ["Castle Town Take 'em All On Level 1"],
        "unset_if_true": [(STAddr.adv_flags_2a, 0x4)],
    },
    "RESET TEAO 2": {
        "not_has_locations": ["Castle Town Take 'em All On Level 2"],
        "unset_if_true": [(STAddr.adv_flags_2a, 0x8)],
    },
    "TEAO remove bow of light": {
        "on_scenes": [0x290B],
        "unset_if_true": [(STAddr.adv_flags_16, 0x1)],
        "has_items": [("Sand Source", 0)],
        "reset_flags": ["RESET Bow of Light",
                        "RESET Bow of Light prog", "RESET Bow of Light big prog",
                        "RESET Bow of Light global", "RESET Bow of Light big global"]
    },
    "TEAO give bow of light": {
        "on_scenes": [0x290B],
        "set_if_true": [(STAddr.adv_flags_16, 0x1)],
        "has_items": [("Sand Source", 1)],
        "reset_flags": ["RESET remove Bow of Light"]
    },
    "RESET Bow of Light": {
        "has_items": [("Bow of Light", 1)],
        "set_if_true": [(STAddr.adv_flags_16, 0x1)],
    },
    "RESET Bow of Light prog": {
        "has_items": [("Tear of Light (Progressive)", 16)],
        "has_slot_data": [("spirit_weapons", 1)],
        "set_if_true": [(STAddr.adv_flags_16, 0x1)],
    },
    "RESET Bow of Light big prog": {
        "has_items": [("Big Tear of Light (Progressive)", 6)],
        "has_slot_data": [("spirit_weapons", 1)],
        "set_if_true": [(STAddr.adv_flags_16, 0x1)],
    },
    "RESET Bow of Light big global": {
        "has_items": [("Big Tear of Light (All Sections)", 2)],
        "has_slot_data": [("spirit_weapons", 1)],
        "set_if_true": [(STAddr.adv_flags_16, 0x1)],
    },
    "RESET Bow of Light global": {
        "has_items": [("Tear of Light (All Sections)", 4)],
        "has_slot_data": [("spirit_weapons", 1)],
        "set_if_true": [(STAddr.adv_flags_16, 0x1)],
    },
    "RESET remove Bow of Light": {
        "has_items": [("Bow of Light", 0)],
        "unset_if_true": [(STAddr.adv_flags_16, 0x1)],
    },
    # "TEAO test remove all blockers": {
    #     "on_scenes": [0x4B00],
    #     "overwrite_if_true": [(STAddr.item_restrictions, 0)]
    # }
    "Add trading post bridge": {
        "on_scenes": [0x400],
        "has_items": [("Repair Trading Post Bridge", 1)],
        "set_if_true": [(STAddr.adv_flags_17, 0x10)]
    },
    "Remove trading post bridge": {
        "on_scenes": [0x400],
        "has_items": [("Repair Trading Post Bridge", 0)],
        "unset_if_true": [(STAddr.adv_flags_17, 0x10)]
    },
    # Passenger States
    "Can pick up Kenzo": {
        "on_scenes": [0x3601],
        "has_items": [("Ocean Glyph", 1)],
        "has_slot_data": [("randomize_passengers", [1, 2, 3])],
        "set_if_true": [(STAddr.adv_flags_c, 0x80)],
        "reset_flags": ["RESET abstract kenzo on train"]
    },
    "Can't pick up kenzo": {
        "on_scenes": [0x3601],
        "has_items": [("Ocean Glyph", 0)],
        "has_slot_data": [("randomize_passengers", [1, 2, 3])],
        "unset_if_true": [(STAddr.adv_flags_c, 0x80)]
    },
    "No randomized kenzo": {
        "on_scenes": [0x3601],
        "has_slot_data": [("randomize_passengers", 0)],
        "unset_if_true": [(STAddr.adv_flags_c, 0x80)]
    },
    "RESET abstract kenzo on train": {
        "unset_if_true": [(STAddr.adv_flags_19, 0x20)],
        "has_slot_data": [("randomize_passengers", [2, 3])],
    },
    "Anouki Quests": {
        "on_scenes": [0x2b00],
        "set_if_true": [(STAddr.adv_flags_1, 4)],  # Ocean restoration
    },
    "AV Give snow source for quest stuff": {
        "on_scenes": [0x2b00],
        "set_if_true": [(STAddr.adv_flags_0, 0x20)],
        "reset_flags": ["RESET Remove Snow source"]
    },
    "Can pick up noko": {
        "on_scenes": [0x2b00],
        "has_slot_data": [("randomize_passengers", [1, 2, 3])],
        "has_items": [("Blizzard Temple Tracks", 1)],
        # "check_bits": [(STAddr.adv_flags_3a, 0x10, "not")],
        "not_has_locations": ["Icy Spring Noko's Force Gem"],
        "unset_if_true": [(STAddr.adv_flags_3a, 0x10)],
    },
    "Can't pick up Noko glyph": {
        "on_scenes": [0x2b00],
        "has_items": [("Blizzard Temple Tracks", 0)],
        "set_if_true": [(STAddr.adv_flags_3a, 0x10)],
    },
    "Can't pick up Noko": {
        "on_scenes": [0x2b00],
        "has_slot_data": [("randomize_passengers", 0)],
        "set_if_true": [(STAddr.adv_flags_3a, 0x10)],
    },
    "Bring Kenzo to AV": {
        "on_scenes": [0x2b00],
        "has_slot_data": [("randomize_passengers", [2, 3])],
        "has_items": [("Passenger: Kenzo", 1)],
        "check_bits": [(STAddr.adv_flags_3c, 0x40, "not")],
        "set_if_true": [(STAddr.adv_flags_3c, 0x10)],
        "overwrite_if_true": [(STAddr.passenger_goal, 0x2b),
                              (STAddr.passenger_tag_0, 0x43524654),
                              (STAddr.has_passenger_0, 0)]
    },
    "Bring Noko to Icyspring": {
        "on_scenes": [0x3500],
        "has_items": [("Passenger: Noko", 1)],
        "check_bits": [(STAddr.adv_flags_3a, 0x40, "not")],
        "set_if_true": [(STAddr.adv_flags_3a, 0x10)],
        "overwrite_if_true": [(STAddr.passenger_goal, 0x35),
                              (STAddr.passenger_tag_0, 0x594B4350),
                              (STAddr.has_passenger_0, 0)]
    },
    "No paseengers icyspring": {
        "on_scenes": [0x3500],
        "has_slot_data": [("randomize_passengers", 0)],
        "set_if_true": [(STAddr.adv_flags_3a, 0x50), (STAddr.adv_flags_3d, 0x10)],
    },
    "Can pick up Mona": {
        "on_scenes": [0x290c],
        "has_slot_data": [("randomize_passengers", [1, 2, 3])],
        "has_items": [("Snow Glyph", 1)],
        "set_if_true": [(STAddr.adv_flags_0, 0x40)],
        "reset_flags": ["RESET Remove Ocean source"]
    },
    "Mona missing glyph": {
        "on_scenes": [0x290c],
        "has_items": [("Snow Glyph", 0)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x40)],
        "reset_flags": ["RESET Add Ocean source"]
    },
    "Mona missing option": {
        "on_scenes": [0x290c],
        "has_slot_data": [("randomize_passengers", 0)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x40)],
        "reset_flags": ["RESET Add Ocean source"]
    },
    "Bring Mona to Rabbit Haven": {
        "on_scenes": [0x3E00],
        "has_items": [("Passenger: Mona", 1)],
        "check_bits": [(STAddr.adv_flags_3b, 0x80, "not")],
        "set_if_true": [(STAddr.adv_flags_3b, 0x20)],
        "overwrite_if_true": [(STAddr.passenger_goal, 0x3e),
                              (STAddr.passenger_tag_0, 0x43415742),
                              (STAddr.has_passenger_0, 0)]
    },
    "Can pick up Joe": {
        "on_scenes": [0x2F00],
        "has_slot_data": [("randomize_passengers", [1, 2, 3])],
        "has_locations": ["Outset Bee Tree"],
        "has_items": [("Snow Source", 1)],
        "set_if_true": [(STAddr.adv_flags_0, 0x40)],
        "reset_flags": ["RESET Remove Ocean source"]
    },
    "Joe missing glyph": {
        "on_scenes": [0x2F00],
        "has_items": [("Snow Source", 0)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x40)],
        "reset_flags": ["RESET Add Ocean source"]
    },
    "Joe missing option": {
        "on_scenes": [0x2F00],
        "has_slot_data": [("randomize_passengers", 0)],
        "unset_if_true": [(STAddr.adv_flags_0, 0x40)],
        "reset_flags": ["RESET Add Ocean source"]
    },
    "Bring Joe to Beedle": {
        "on_scenes": [0x4503],
        "has_items": [("Passenger: Joe", 1)],
        "check_bits": [(STAddr.adv_flags_3c, 0x8, "not")],
        "set_if_true": [(STAddr.adv_flags_3c, 0x2)],
        "overwrite_if_true": [(STAddr.passenger_goal, 0x45),
                              (STAddr.passenger_tag_0, 0x4E434341),
                              (STAddr.has_passenger_0, 0)]
    },


    # Cargo
    "AV skip fence text": {
        "on_scenes": [0x2b00],
        "set_if_true": [(STAddr.adv_flags_3d, 0x2)],
    },
    "AV has lumber": {
        "on_scenes": [0x2b00],
        "has_items": [("Cargo: Lumber", 1), ("Wagon", 1)],
        "has_slot_data": [("randomize_cargo", [2, 3])],
        "check_bits": [(STAddr.adv_flags_54, 0x04, "not")],
        "reset_flags": ["RESET Cargo"],
        "overwrite_if_true": [(STAddr.cargo_0, 1), (STAddr.cargo_count_0, 15)]
    },
    "AV fence no cargo": {
        "on_scenes": [0x2b00],
        "has_slot_data": [("randomize_cargo", 0), ("randomize_passengers", [1, 2, 3])],
        "set_if_true": [(STAddr.adv_flags_54, 0x4), (STAddr.adv_flags_3d, 0x1)]
    },
    "AV fence no passengers": {
        "on_scenes": [0x2b00],
        "has_slot_data": [("randomize_cargo", [1, 2, 3]), ("randomize_passengers", 0)],
        "set_if_true": [(STAddr.adv_flags_3c, 0x50), (STAddr.adv_flags_3d, 0x4)],
    },
    "RESET Cargo": {
        "set_if_true": [(STAddr.cargo_0, 0xFFFFFFFF),(STAddr.cargo_1, 0xFFFFFFFF)],
        "unset_if_true": [(STAddr.cargo_count_0, 0xFF), (STAddr.cargo_count_1, 0xFF)]
    },
    "Outset has Cuccos": {
        "on_scenes": [0x2f00],
        "has_items": [("Cargo: Cuccos", 1), ("Wagon", 1)],
        "has_slot_data": [("randomize_cargo", [2, 3])],
        "not_has_locations": ["Outset Deliver Cuccos"],
        "reset_flags": ["RESET Cargo"],
        "overwrite_if_true": [(STAddr.cargo_0, 4), (STAddr.cargo_count_0, 10)]
    },
    "CT has fish": {
        "on_scenes": [0x2900],
        "has_items": [("Cargo: Fish", 1), ("Wagon", 1)],
        "has_slot_data": [("randomize_cargo", [2, 3])],
        "not_has_locations": ["Castle Town Lucia Fish Force Gem"],
        "reset_flags": ["RESET Cargo"],
        "overwrite_if_true": [(STAddr.cargo_0, 3), (STAddr.cargo_count_0, 20)]
    },
    "Snow Sanc has vessel": {
        "on_scenes": [0x3100],
        "has_items": [("Cargo: Vessel", 1), ("Wagon", 1)],
        "has_slot_data": [("randomize_cargo", [2, 3])],
        "check_bits": [(STAddr.adv_flags_40, 0x20, "not")],
        "reset_flags": ["RESET Cargo"],
        "set_if_true": [(STAddr.adv_flags_1, 0x4)],  # ocean restoration moves him outside
        "overwrite_if_true": [(STAddr.cargo_0, 5), (STAddr.cargo_count_0, 1)]
    },
    "Linebeck has Ore": {
        "on_scenes": [0x370a, 0x370a],
        "has_items": [("Cargo: Dark Ore", 1), ("Wagon", 1)],
        "has_slot_data": [("randomize_cargo", [2, 3])],
        "not_has_locations": ["Trading Post Give Dark Ore to Linebeck"],
        "check_bits": [(STAddr.adv_flags_24, 0x10)],
        "reset_flags": ["RESET Cargo"],
        "overwrite_if_true": [(STAddr.cargo_0, 6), (STAddr.cargo_count_0, 20)]
    },
    "Rael has Cuccos": {
        "on_scenes": [0x3400],
        "has_items": [("Cargo: Cuccos", 1), ("Wagon", 1)],
        "has_slot_data": [("randomize_cargo", [2, 3])],
        "not_has_locations": ["Sand Sanctuary Deliver Cuccos to Rael"],
        "reset_flags": ["RESET Cargo"],
        "overwrite_if_true": [(STAddr.cargo_0, 4), (STAddr.cargo_count_0, 5)]
    },
    "Keep rael upstairs": {
        "on_scenes": [0x3400],
        "has_locations": ["Sand Sanctuary Deliver Cuccos to Rael"],
        "set_if_true": [(STAddr.adv_flags_19, 0x8)]
    },
    "Papuzia has ice": {
        "on_scenes": [0x2c00],
        "has_items": [("Cargo: Mega Ice", 1), ("Wagon", 1)],
        "has_slot_data": [("randomize_cargo", [2, 3])],
        "not_has_locations": ["Papuzia Village Deliver Ice"],
        "reset_flags": ["RESET Cargo"],
        "overwrite_if_true": [(STAddr.cargo_0, 0), (STAddr.cargo_count_0, 20)]
    },
    # Papuzia
    "Allow SoB statue": {
        "on_scenes": [0x2c00],
        "not_has_locations": ["Papuzia Village Song Statue"],
        "has_items": [("Song of Discovery", 1)],
        "unset_if_true": [(STAddr.songs, 0x4)],
        "set_if_true": [(STAddr.adv_flags_a, 0xA0)],
        "reset_flags": ["RESET SoB"]
    },
    "RESET SoB": {
        "has_items": [("Song of Birds", 1)],
        "set_if_true": [(STAddr.songs, 0x4)],
    },
    "Papuzia can buy vessel": {
        "on_scenes": [0x2c04],
        "has_items": [("Wagon", 1)],
        "set_if_true": [(STAddr.adv_flags_9, 0x50), (STAddr.adv_flags_1, 0x04)],
        "has_slot_data": [("randomize_cargo", [1, 2, 3])],
        "reset_flags": ["RESET Papuzia not got carben"]
    },
    "RESET Papuzia not got carben": {
        # "not_has_locations": ["Papuzia Pick Up Carben"],
        "unset_if_true": [(STAddr.adv_flags_9, 0x10)]
        # TODO: has some nasty interactions with vanilla passengers
    },
    "Desert Temple Prevent Earthquake": {
        "on_scenes": [0x1D00],
        "any_not_has_locations": ["Desert Temple 1F N Trap Chest", "Desert Temple 1F N Arena Chest"],
        "unset_if_true": [(STAddr.adv_flags_19, 0x8)]
    },
    "Desert Temple Cause Earthquake": {
        "on_scenes": [0x1D00],
        "has_locations": ["Desert Temple 1F N Trap Chest", "Desert Temple 1F N Arena Chest"],
        "set_if_true": [(STAddr.adv_flags_19, 0x8)]
    },
}
"""
"Dynamic Flag Name": {
    "on_scenes": list[int],
    "not_last_scenes": list[int]
    "has_items": list[tuple[str, int]],         item_name, min count (0 for not have item)
    "has_locations": list[str],
    "not_has_locations": list[str],
    "any_not_has_locations": list[str],
    "set_if_true": list[tuple[int, int]],       address, value
    "unset_if_true": list[tuple[int, int]],     address, value
    "has_slot_data": list[list[str, any]]       slot_data, ==value
    "goal_requirement": bool                    checks dungeon requirement if true
}
"""

