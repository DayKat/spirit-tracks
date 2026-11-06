from dataclasses import dataclass

from ..DSZeldaClient.subclasses import Address, AddressLoader ,DoubleAddressLoader, load_multi, MultiAddressLoader

addr_null = Address(0)


async def load_adv_flags(ctx):
    print(f"Loading adventure flags")
    await STAddr.adv_flags_0.load(ctx)
    for i in range(1, 0x5c):
        getattr(STAddr, f"adv_flags_{hex(i)[2:]}").set_addr(STAddr.adv_flags_0 + i)

    #     print(f"{getattr(STAddr, f'adv_flags_{hex(i)[2:]}')}")
    # print(f"{STAddr.adv_flags_30}")

    STAddr.sources.set_addr(STAddr.adv_flags_0.addr)
    STAddr.restorations.set_addr(STAddr.adv_flags_1.addr)
    STAddr.glyphs.set_addr(STAddr.adv_flags_2.addr)
    STAddr.activate_portals.set_addr(STAddr.adv_flags_30.addr)

    STAddr.watched_intro.set_addr(STAddr.adv_flags_12.addr)

    STAddr.received_item_index.set_addr(STAddr.adv_flags_0 + 0x6C)
    STAddr.slot_id.set_addr(STAddr.adv_flags_0 + 0x6E)

    STAddr.key_storage_0.set_addr(STAddr.adv_flags_0 + 0x70)
    STAddr.key_storage_tos.set_addr(STAddr.adv_flags_0 + 0x71)
    STAddr.key_storage_2.set_addr(STAddr.adv_flags_0 + 0x72)

    STAddr.received_item_index = Address(STAddr.adv_flags_0 + 0x6C, size=2)
    STAddr.slot_id = Address(STAddr.adv_flags_0 + 0x6E, size=2)

async def load_on_connect(ctx):
    pass

async def load_on_enter_game(ctx):
    # Room data
    await STAddr.stage.load(ctx)  # TODO: add double loader support to load_multi()
    room_handler = await STAddr.gStageData.read(ctx)
    STAddr.room.set_addr(STAddr.stage.addr + 10)
    STAddr.entrance.set_addr(STAddr.stage.addr + 11)

    STAddr.respawn_stage.set_addr(room_handler+0x14)
    STAddr.respawn_room.set_addr(room_handler + 0x1E)
    STAddr.respawn_entrance.set_addr(room_handler + 0x1F)
    print(f"Loaded stage: {STAddr.stage}")

    # Load all single stage loaders in bulk
    await load_multi(ctx, [
        STAddr.menu,
        STAddr.health,
        STAddr.passenger_tag_0,
        STAddr.cargo_0,
        STAddr.stage_flag_pointer,
        STAddr.item_model_table,
        STAddr.getting_location,
        STAddr.saving,
        STAddr.selected_station
    ])

    STAddr.mid_load.set_addr(STAddr.stage_flag_pointer+44)

    # Item manager assignments
    STAddr.heart_count.set_addr(STAddr.health+1)
    item_manager = AddressLoader(STAddr.health+0x2C)
    await item_manager.load(ctx)

    STAddr.equipped_item.set_addr(item_manager)
    STAddr.items_0.set_addr(item_manager.addr+0x8)
    STAddr.items_2.set_addr(item_manager.addr + 0xA)
    STAddr.arrow_capacity.set_addr(item_manager.addr + 4 * 6 + 0)
    STAddr.bomb_capacity.set_addr(item_manager.addr + 4 * 6 + 1)
    STAddr.arrow_count.set_addr(item_manager.addr + 4*6 + 2)
    STAddr.bomb_count.set_addr(item_manager.addr + 4 * 6 + 3)
    STAddr.item_restrictions.set_addr(item_manager.addr + 4 * 5)

    STAddr.rupees.set_addr(item_manager.addr + 0x10)
    STAddr.tears_of_light.set_addr(item_manager.addr + 0x16)
    STAddr.small_keys.set_addr(item_manager.addr + 0x17)

    STAddr.potion_0.set_addr(item_manager.addr + 0x1C)
    STAddr.potion_1.set_addr(item_manager.addr + 0x1D)
    STAddr.all_potions.set_addr(item_manager.addr + 0x1C)

    # Rails
    rail_manager = AddressLoader(STAddr.health.addr+0x34, 1, 0x38)
    await rail_manager.load(ctx)
    STAddr.rail_restorations.set_addr(rail_manager+0)
    STAddr.tracks_0.set_addr(rail_manager+4)
    STAddr.tracks_1.set_addr(rail_manager+5)
    STAddr.tracks_2.set_addr(rail_manager+6)

    # Train Parts
    train_part_manager = rail_manager - 4*10
    STAddr.train_parts.set_addr(rail_manager-8)
    STAddr.equipped_engine.set_addr(train_part_manager+0)
    STAddr.equipped_cannon.set_addr(train_part_manager+4)
    STAddr.equipped_car.set_addr(train_part_manager + 8)
    STAddr.equipped_cart.set_addr(train_part_manager + 0xC)
    STAddr.train_health.set_addr(STAddr.health+0x1E4)

    # Passengers
    STAddr.has_passenger_0.set_addr(STAddr.passenger_tag_0 + 0x4)
    STAddr.has_passenger_1.set_addr(STAddr.passenger_tag_0 + 0x18)
    STAddr.passenger_tag_1.set_addr(STAddr.passenger_tag_0 + 0x14)
    STAddr.passenger_goal.set_addr(STAddr.passenger_tag_0 + 0x8)

    # Cargo
    STAddr.cargo_1.set_addr(STAddr.cargo_0+0xC)
    STAddr.cargo_count_0.set_addr(STAddr.cargo_0+0x4)
    STAddr.cargo_count_1.set_addr(STAddr.cargo_0 + 0x10)

    # Misc Adventure setup
    await STAddr.gpMiscAdvManager.load(ctx)

    STAddr.songs.set_addr(STAddr.gpMiscAdvManager+0x8C)
    STAddr.postcard_count.set_addr(STAddr.gpMiscAdvManager + 0x7E)
    STAddr.stamp_ids.set_addr(STAddr.gpMiscAdvManager + 0x68)
    STAddr.stamp_coords.set_addr(STAddr.gpMiscAdvManager + 0x2C)

    # Rabbits
    await STAddr.rabbits.load(ctx)
    print(f"Rabbit manager: {STAddr.rabbits}")
    STAddr.rabbits_0.set_addr(STAddr.rabbits + 0)
    STAddr.rabbits_1.set_addr(STAddr.rabbits + 1)
    STAddr.rabbits_2.set_addr(STAddr.rabbits + 2)
    STAddr.rabbits_3.set_addr(STAddr.rabbits + 3)
    STAddr.rabbits_4.set_addr(STAddr.rabbits + 4)
    STAddr.rabbits_5.set_addr(STAddr.rabbits + 5)
    STAddr.rabbits_6.set_addr(STAddr.rabbits + 6)

    # Treausure
    await STAddr.all_treasure_count.load(ctx)
    print(f"Treasure manager: {STAddr.all_treasure_count}")
    STAddr.demon_fossil_count.set_addr(STAddr.all_treasure_count + 0)
    STAddr.stalfos_skull_count.set_addr(STAddr.all_treasure_count + 2)
    STAddr.star_fragment_count.set_addr(STAddr.all_treasure_count + 4)
    STAddr.bee_larvae_count.set_addr(STAddr.all_treasure_count + 6)
    STAddr.wood_heart_count.set_addr(STAddr.all_treasure_count + 8)
    STAddr.dark_pearl_loop_count.set_addr(STAddr.all_treasure_count + 10)
    STAddr.white_pearl_loop_count.set_addr(STAddr.all_treasure_count + 12)
    STAddr.ruto_crown_count.set_addr(STAddr.all_treasure_count + 14)
    STAddr.dragon_scale_count.set_addr(STAddr.all_treasure_count + 16)
    STAddr.pirates_necklace_count.set_addr(STAddr.all_treasure_count + 18)
    STAddr.palace_dish_count.set_addr(STAddr.all_treasure_count + 20)
    STAddr.goron_amber_count.set_addr(STAddr.all_treasure_count + 22)
    STAddr.mystic_jade_count.set_addr(STAddr.all_treasure_count + 24)
    STAddr.ancient_coin_count.set_addr(STAddr.all_treasure_count + 26)
    STAddr.priceless_stone_count.set_addr(STAddr.all_treasure_count + 28)
    STAddr.regal_ring_count.set_addr(STAddr.all_treasure_count + 30)

    # Other
    await STAddr.entrance_animation.load(ctx)
    STAddr.quick_pen_coords.set_addr(STAddr.menu + 17*4)
    STAddr.last_x.set_addr(STAddr.quick_pen_coords + 4)
    STAddr.exiting_map.set_addr(STAddr.last_x + 0xA4)


async def load_on_train(ctx):
    await load_multi(ctx, [
        STAddr.train_speed_reverse
    ])
    # Train Speed Presets
    STAddr.train_speed_stop.set_addr(STAddr.train_speed_reverse + 8)
    STAddr.train_speed_med.set_addr(STAddr.train_speed_reverse + 16)
    STAddr.train_speed_fast.set_addr(STAddr.train_speed_reverse + 24)
    STAddr.train_speed_pointer.set_addr(STAddr.train_speed_reverse + 0x958C)

@dataclass
class STAddr:
    # print(f"Initializing STAddr")
    null = addr_null
    
    # Rom identification
    game_identifier = Address(0, 0, 16, "ROM")
    game_version = Address(0x1E, 0x1E, 1, "ROM")

    # DTCM stuff
    gAdventureFlags = Address(0x09b8, size=3, domain="Data TCM")
    gMapObjectManager = Address(0x0CE8, size=3, domain="Data TCM")
    gActorManager = Address(0x0ce4, size=3, domain="Data TCM")
    gItemManager = Address.pointer(0x0fb4)
    gPlayerManager = Address.pointer(0x0fbc)
    gPlayer = Address.pointer(0x0fec)
    gMapManager = Address.pointer(0x0e60)
    gpPassengerManager = Address.pointer(0x0CFC)
    gpCargoManager = Address.pointer(0x0D04)

    gStageData = Address.pointer(0x09a4)
    gpCurrentGameModeMgr = Address.pointer(0x0994)
    gSaveManager = Address.pointer(0x0CE0)
    gMiscPointer = Address.pointer(0x01F0)
    gTrainManager = Address.pointer(0x0640)
    gpMiscAdvManager = MultiAddressLoader(gMiscPointer, 1, [0x1BA08, 0, 0])
    gStageFlagManager = Address.pointer(0x0CD8)

    # No idea what these actually are, the stuff i want is on huge offsets
    entranceAnimationManager = Address.pointer(0x9c4)
    modelTableManager = Address.pointer(0x09D4)
    itemGetManager = Address.pointer(0x14b8)
    saveManager = Address.pointer(0x1530)

    # Version safe loaders
    map_object_table = DoubleAddressLoader(gMapObjectManager, 3)
    actor_table = DoubleAddressLoader(gActorManager, 3)
    adv_flags_0 = AddressLoader(gAdventureFlags, size=1, load_offset=0x14, name="adv_flags_0")

    # Fundamentals
    # rabbit_blocker = Address(0x260867)
    # loading_room = Address(0x0c2FF0)
    loading_room = Address(0x394B, size=1, domain="Data TCM")
    mid_load = Address(0x265190)

    received_item_index = Address(0x265780, size=2)
    slot_id = Address(0x265782, size=2)
    
    stage = DoubleAddressLoader(gStageData, 1, 0x58, 0x8C)
    floor = Address(0x1B2E98)
    room = Address(0x2690EA)
    entrance = Address(0x2690EB)

    respawn_stage = Address(0x262074)
    respawn_room = Address(0x26207e)
    respawn_entrance = Address(0x26207f)

    getting_location = AddressLoader(itemGetManager, 1, 0x212) # 0x0x04B114
    saving = AddressLoader(saveManager, 1, 0x58) # (0x049BD8)
    getting_tear_safety = Address(0x327B8C)
    getting_item_safety = Address(0x264648)
    entering_shop = Address(0x260A44)

    # drinking_potion = Address(0x317ED0)  # 39 normal, 3b drinking
    drinking_potion_pointer = Address(0x265338, size=4)
    
    link_x = Address.pointer(0x05CC)  # Not actually pointers, but the object does all the settings right
    link_y = Address.pointer(0x05D0)
    link_z = Address.pointer(0x05D4)
    
    menu = AddressLoader(gpCurrentGameModeMgr, 1, 0xF8, name="menu")
    equipped_item = Address(0x265318, size=4)
    flip_clog = Address(0x04C3DC)
    
    health = AddressLoader(gSaveManager, 1, 0)
    heart_count = AddressLoader(gSaveManager, 1, 1)
    rabbits = MultiAddressLoader(gMiscPointer, 7, [0x2a10, 0, 0xb98])
    rabbits_0 = Address(0x262030, name="rabbits_0")
    rabbits_1 = Address(0x262031, name="rabbits_1")
    rabbits_2 = Address(0x262032, name="rabbits_2")
    rabbits_3 = Address(0x262033, name="rabbits_3")
    rabbits_4 = Address(0x262034, name="rabbits_4")
    rabbits_5 = Address(0x262035, name="rabbits_5")
    rabbits_6 = Address(0x262036, name="rabbits_6")

    stage_flag_pointer = AddressLoader(gStageFlagManager, 4, 4)
    watched_intro = Address(0) # Address(0x265726)

    train_speed_fast = Address(0x136004, size=4)  # 0xc1 193
    train_speed_med = Address(0x135FFC, size=4)   # 0x73 115
    train_speed_stop = Address(0x135FF4, size=4)  # 0
    train_speed_reverse = AddressLoader(gTrainManager, 4, 0x9A4) # -143
    train_speed_pointer = Address(0x13F578, size=3)  # + 0x94 to get actual train speed

    train_health = Address(0x2653a0)

    train_trans_x = Address(0x262090, size=4)
    train_trans_y = Address(0x262094, size=4)
    train_trans_z = Address(0x262098, size=4)

    train_x = Address(0x264628, size=4)
    train_y = Address(0x26462C, size=4)
    train_z = Address(0x264630, size=4)
    train_coords = (train_x, train_y, train_z)

    # Inventory
    items_0 = Address(0x265320, name="items_0")
    items_2 = Address(0x265322, name="items_2")
    songs = Address(0x268FB0, name="songs")
    arrow_capacity = Address(0x265330)
    bomb_capacity = Address(0x265331)
    arrow_count = Address(0x265332, name="arrow_count")
    bomb_count = Address(0x265333, name="bomb_count")
    postcard_count = Address(0x268FA2, name="postcard_count")

    item_restrictions = Address(0x26532C, size=2)
    
    rupees = Address(0x265328, size=2)
    tears_of_light = Address(0x26532E)
    small_keys = Address(0x26532F)
    
    potion_0 = Address(0x265334)
    potion_1 = Address(0x265335)
    all_potions = Address(0x265334, size=2)
    
    rail_restorations = Address(0x2653B0, name="rail_restorations")
    tracks_0 = Address(0x2653B4, name="tracks_0")
    tracks_1 = Address(0x2653B5, name="tracks_1")
    tracks_2 = Address(0x2653B6, name="tracks_2")
    source_rails = Address(0x2653B8, name="source_rails")
    key_storage_0 = Address(0x265784)
    key_storage_tos = Address(0x265785)
    key_storage_2 = set_starting_train = Address(0x265786)

    train_parts = Address(0x2653A8, size=4)
    equipped_engine = Address(0x265388, size=4)
    equipped_cannon = Address(0x26538C, size=4)
    equipped_car = Address(0x265390, size=4)
    equipped_cart = Address(0x265394, size=4)
    train_part_array = [equipped_engine, equipped_cannon, equipped_car, equipped_cart]

    map_open = Address(0x34B4, domain="Data TCM")
    selected_station = AddressLoader(entranceAnimationManager, 1, 0x5380)  # Address(0x260A2C)
    exiting_map = Address(0x260A44)
    last_x = Address(0x2609A0, size=2)
    # map_level = Address(0x260A44)  # 8 for big map, 2 for small, FF for tween
    quick_pen_coords = Address(0x26099C, size=3)  # there's one in menu too

    # Passenger data
    has_passenger_0 = Address(0x265598, size=4)  # passenger happiness
    has_passenger_1 = Address(0x2655AC, size=4)  # passenger happiness on respawn
    passenger_tag_0 = AddressLoader(gpPassengerManager, size=4)  # passenger id
    passenger_tag_1 = Address(0x2655A8, size=4)  # passenger id on respawn
    passenger_goal = Address(0x26559C, size=4)  # goal station stage

    # Cargo Data
    cargo_0 = AddressLoader(gpCargoManager, size=4)
    cargo_1 = Address(0x2655e4, size=4)
    cargo_count_0 = Address(0x2655dc)
    cargo_count_1 = Address(0x2655e8)

    # Special events
    heatoise_pre_pointer = Address.pointer(0x580)
    mtt_b1_heatoise_trigger_x = MultiAddressLoader(heatoise_pre_pointer, 4, [0x10654, 1384])# Address(0x1231B4, size=3)
    snurglar_pre_pointer = Address.pointer(0x204)
    snurglar_flags = MultiAddressLoader(snurglar_pre_pointer, 1, [0x3B34, 0xC0])
    snurglar_pointer = Address(0x0499F4, size=3)
    snurglin_keys = Address(0x2e986c)
    # mountain_gate = Address(0x2e3640)

    # Stamps
    stamp_ids = Address(0x268f8c, size=20)
    stamp_coords = Address(0x268F50, size=40)

    # Zelda
    zelda_pointer = Address(0x0D34, size=3, domain="Data TCM")

    # Adventure Flags
    # adv_flags_0: "Address"
    adv_flags_1: "Address" = Address(0, name="adv_flags_1")
    adv_flags_2: "Address" = Address(0x265716, name="adv_flags_2")
    adv_flags_3: "Address" = Address(0x265717, name="adv_flags_3")
    adv_flags_4: "Address" = Address(0x265718, name="adv_flags_4")
    adv_flags_5: "Address" = Address(0x265719, name="adv_flags_5")
    adv_flags_6: "Address" = Address(0x26571a, name="adv_flags_6")
    adv_flags_7: "Address" = Address(0x26571b, name="adv_flags_7")
    adv_flags_8: "Address" = Address(0x26571c, name="adv_flags_8")
    adv_flags_9: "Address" = Address(0x26571d, name="adv_flags_9")
    adv_flags_a: "Address" = Address(0x26571e, name="adv_flags_a")
    adv_flags_b: "Address" = Address(0x26571f, name="adv_flags_b")
    adv_flags_c: "Address" = Address(0x265720, name="adv_flags_c")
    adv_flags_d: "Address" = Address(0x265721, name="adv_flags_d")
    adv_flags_e: "Address" = Address(0x265722, name="adv_flags_e")
    adv_flags_f: "Address" = Address(0x265723, name="adv_flags_f")
    adv_flags_10: "Address" = Address(0x265724, name="adv_flags_10")
    adv_flags_11: "Address" = Address(0x265725, name="adv_flags_11")
    adv_flags_12: "Address" = Address(0x265726, name="adv_flags_12")
    adv_flags_13: "Address" = Address(0x265727, name="adv_flags_13")
    adv_flags_14: "Address" = Address(0x265728, name="adv_flags_14")
    adv_flags_15: "Address" = Address(0x265729, name="adv_flags_15")
    adv_flags_16: "Address" = Address(0x26572a, name="adv_flags_16")
    adv_flags_17: "Address" = Address(0x26572b, name="adv_flags_17")
    adv_flags_18: "Address" = Address(0x26572c, name="adv_flags_18")
    adv_flags_19: "Address" = Address(0x26572d, name="adv_flags_19")
    adv_flags_1a: "Address" = Address(0x26572e, name="adv_flags_1a")
    adv_flags_1b: "Address" = Address(0x26572f, name="adv_flags_1b")
    adv_flags_1c: "Address" = Address(0x265730, name="adv_flags_1c")
    adv_flags_1d: "Address" = Address(0x265731, name="adv_flags_1d")
    adv_flags_1e: "Address" = Address(0x265732, name="adv_flags_1e")
    adv_flags_1f: "Address" = Address(0x265733, name="adv_flags_1f")
    adv_flags_20: "Address" = Address(0x265734, name="adv_flags_20")
    adv_flags_21: "Address" = Address(0x265735, name="adv_flags_21")
    adv_flags_22: "Address" = Address(0x265736, name="adv_flags_22")
    adv_flags_23: "Address" = Address(0x265737, name="adv_flags_23")
    adv_flags_24: "Address" = Address(0x265738, name="adv_flags_24")
    adv_flags_25: "Address" = Address(0x265739, name="adv_flags_25")
    adv_flags_26: "Address" = Address(0x26573a, name="adv_flags_26")
    adv_flags_27: "Address" = Address(0x26573b, name="adv_flags_27")
    adv_flags_28: "Address" = Address(0x26573c, name="adv_flags_28")
    adv_flags_29: "Address" = Address(0x26573d, name="adv_flags_29")
    adv_flags_2a: "Address" = Address(0x26573e, name="adv_flags_2a")
    adv_flags_2b: "Address" = Address(0x26573f, name="adv_flags_2b")
    adv_flags_2c: "Address" = Address(0x265740, name="adv_flags_2c")
    adv_flags_2d: "Address" = Address(0x265741, name="adv_flags_2d")
    adv_flags_2e: "Address" = Address(0x265742, name="adv_flags_2e")
    adv_flags_2f: "Address" = Address(0x265743, name="adv_flags_2f")
    adv_flags_30: "Address" = Address(0x265744, name="adv_flags_30")
    adv_flags_31: "Address" = Address(0x265745, name="adv_flags_31")
    adv_flags_32: "Address" = Address(0x265746, name="adv_flags_32")
    adv_flags_33: "Address" = Address(0x265747, name="adv_flags_33")
    adv_flags_34: "Address" = Address(0x265748, name="adv_flags_34")
    adv_flags_35: "Address" = Address(0x265749, name="adv_flags_35")
    adv_flags_36: "Address" = Address(0x26574a, name="adv_flags_36")
    adv_flags_37: "Address" = Address(0x26574b, name="adv_flags_37")
    adv_flags_38: "Address" = Address(0x26574c, name="adv_flags_38")
    adv_flags_39: "Address" = Address(0x26574d, name="adv_flags_39")
    adv_flags_3a: "Address" = Address(0x26574e, name="adv_flags_3a")
    adv_flags_3b: "Address" = Address(0x26574f, name="adv_flags_3b")
    adv_flags_3c: "Address" = Address(0x265750, name="adv_flags_3c")
    adv_flags_3d: "Address" = Address(0x265751, name="adv_flags_3d")
    adv_flags_3e: "Address" = Address(0x265752, name="adv_flags_3e")
    adv_flags_3f: "Address" = Address(0x265753, name="adv_flags_3f")
    adv_flags_40: "Address" = Address(0x265754, name="adv_flags_40")
    adv_flags_41: "Address" = Address(0x265755, name="adv_flags_41")
    adv_flags_42: "Address" = Address(0x265756, name="adv_flags_42")
    adv_flags_43: "Address" = Address(0x265757, name="adv_flags_43")
    adv_flags_44: "Address" = Address(0x265758, name="adv_flags_44")
    adv_flags_45: "Address" = Address(0x265759, name="adv_flags_45")
    adv_flags_46: "Address" = Address(0x26575a, name="adv_flags_46")
    adv_flags_47: "Address" = Address(0x26575b, name="adv_flags_47")
    adv_flags_48: "Address" = Address(0x26575c, name="adv_flags_48")
    adv_flags_49: "Address" = Address(0x26575d, name="adv_flags_49")
    adv_flags_4a: "Address" = Address(0x26575e, name="adv_flags_4a")
    adv_flags_4b: "Address" = Address(0x26575f, name="adv_flags_4b")
    adv_flags_4c: "Address" = Address(0x265760, name="adv_flags_4c")
    adv_flags_4d: "Address" = Address(0x265761, name="adv_flags_4d")
    adv_flags_4e: "Address" = Address(0x265762, name="adv_flags_4e")
    adv_flags_4f: "Address" = Address(0x265763, name="adv_flags_4f")
    adv_flags_50: "Address" = Address(0x265764, name="adv_flags_50")
    adv_flags_51: "Address" = Address(0x265765, name="adv_flags_51")
    adv_flags_52: "Address" = Address(0x265766, name="adv_flags_52")
    adv_flags_53: "Address" = Address(0x265767, name="adv_flags_53")
    adv_flags_54: "Address" = Address(0x265768, name="adv_flags_54")
    adv_flags_55: "Address" = Address(0x265769, name="adv_flags_55")
    adv_flags_56: "Address" = Address(0x26576a, name="adv_flags_56")
    adv_flags_57: "Address" = Address(0x26576b, name="adv_flags_57")
    adv_flags_58: "Address" = Address(0x26576c, name="adv_flags_58")
    adv_flags_59: "Address" = Address(0x26576d, name="adv_flags_59")
    adv_flags_5a: "Address" = Address(0x26576e, name="adv_flags_5a")
    adv_flags_5b: "Address" = Address(0x26576f, name="adv_flags_5b")

    sources: "Address" = Address(0, name="sources")
    glyphs: "Address" = Address(0, name="glyphs")
    restorations: "Address" = Address(0, name="restorations")
    activate_portals: "Address" = Address(0, name="activate_portals")
    
    # Treasure
    all_treasure_count = MultiAddressLoader(gMiscPointer, 32, [0x1ba10, 0, 0x3c])
    demon_fossil_count = Address(0x269000, size=2)
    stalfos_skull_count = Address(0x269002, size=2)
    star_fragment_count = Address(0x269004, size=2)
    bee_larvae_count = Address(0x269006, size=2)
    wood_heart_count = Address(0x269008, size=2)
    dark_pearl_loop_count = Address(0x26900a, size=2)
    white_pearl_loop_count = Address(0x26900c, size=2)
    ruto_crown_count = Address(0x26900e, size=2)
    dragon_scale_count = Address(0x269010, size=2)
    pirates_necklace_count = Address(0x269012, size=2)
    palace_dish_count = Address(0x269014, size=2)
    goron_amber_count = Address(0x269016, size=2)
    mystic_jade_count = Address(0x269018, size=2)
    ancient_coin_count = Address(0x26901a, size=2)
    priceless_stone_count = Address(0x26901c, size=2)
    regal_ring_count = Address(0x26901e, size=2)

    item_model_table = AddressLoader(modelTableManager, 1, 0x30E4C)  # size=big, 0x0af590 (actually starts with a blank 1 byte earlier, but don't think the game uses it)

    entrance_animation = MultiAddressLoader(entranceAnimationManager, 1, [0x1234, 0x144])  # 0x269108 | 17 to prevent blue warps working immediately
    # 9 is the slow culprit

    fade_timer = Address(0x0b5164, size=2)  # used for entrance warp from intro



#  = Address()
#  = Address()
#  = Address()
#  = Address()
#  = Address()
#  = Address()
#  = Address()
#  = Address()
#  = Address()
#  = Address()