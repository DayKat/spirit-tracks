from ..DSZeldaClient.subclasses import Address

addr_null = Address(0, 0)

# Basic Reads
addr_game_identifier = Address(0, 0, 16, "ROM")
addr_game_state = Address(0x060C48)
addr_save_slot = Address(0x1B8124)

addr_boat_health = Address(0x1FA036, name="boat_health")
addr_salvage_health = Address(0x1F5720, name="salvage_health")

addr_received_item_index = Address(0x1BA64C, size=2)
addr_slot_id = Address(0x1BA64A, size=2)

addr_stage = Address(0x1B2E94, size=4)
addr_room = Address(0x1B2EA6)
addr_floor = Address(0x1B2E98, size=4)  # unused
addr_entrance = Address(0x1B2EA7)

addr_transition_x = Address(0x1B2EC8, size=4)
addr_transition_y = Address(0x1B2ECC, size=4)
addr_transition_z = Address(0x1B2ED0, size=4)
addr_boat_respawn = Address(0x1B2F12, size=2)

addr_link_x = Address(0x1B6FEC, size=4, name="link_x")
addr_link_y = Address(0x1B6FF0, size=4, name="link_y")
addr_link_z = Address(0x1B6FF4, size=4, name="link_z")
addr_boat_x = Address(0x1B8518, size=4, name="boat_x")
addr_boat_z = Address(0x1B8520, size=4, name="boat_y")

# Technical Reads
addr_getting_location = Address(0x1B6F44)
addr_shot_frog = Address(0x1B7038)
addr_getting_ship_part = Address(0x11F5E4)
addr_getting_salvage = Address(0x1BA654)
addr_getting_salvage_1 = Address(0x1ba655)
addr_getting_salvage_2 = Address(0x1ba656)
addr_getting_salvage_3 = Address(0x1ba657)

addr_stage_small = Address(0x1B2E94, size=1)  # Used for precision rads

addr_saving = Address(0x19B7CF)
addr_changing_map_scene = Address(0x1BA700)
addr_pen_mode_pointer = Address(0x1CCCEC, size=4)

addr_text_speed = Address(0x0EC754)  # Sus
addr_treasure_price_index = Address(0x0EC7D8, size=4)

addr_using_item = Address(0x1BA71C)
addr_drawing_sea_route = Address(0x207C4C)
addr_equipped_item = Address(0x1BA520, size=4)
addr_got_item_menu = Address(0x19A5B0)
addr_opened_clog = Address(0x0FC5BC)
addr_flipped_clog = Address(0x0FA37B)
addr_in_map = Address(0x1B2D60)
addr_using_cyclone_slate = Address(0x1B636C)

addr_loading_stage = Address(0x1B2E78)  # 0 when loading stage, some sorta pointer
addr_loading_room = Address(0x10BD6F) # 0 when not loading room
addr_in_cutscene = Address(0x1BBCF4)
addr_in_short_cs = Address(0x1B6FE8)
addr_started_save_file = Address(0x1B7FB8)  # Used to trigger precision stuff from menu

# Pointers
addr_gItemManager = Address(0x0fb4, 0x0fb4, size=4, domain="Data TCM")
addr_gPlayerManager = Address(0x0fbc, 0x0fbc, size=4, domain="Data TCM")
addr_gAdventureFlags = Address(0x0f74, 0x0f74, size=4, domain="Data TCM")
addr_ADDR_gPlayer = Address(0x0f90, 0x0f90, size=4, domain="Data TCM")
addr_gOverlayManager_mLoadedOverlays_4 = Address(0x0910, 0x0910, size=4, domain="Data TCM")
addr_gMapManager = Address(0x0e60, 0x0e60, size=4, domain="Data TCM")

# Adventure flags
addr_adv_flags = Address(0x1B557C, size=52)
addr_adv_flags_0 = Address(0x1b557c)
addr_adv_flags_1 = Address(0x1b557d)
addr_adv_flags_2 = addr_flags_fog_spirits = Address(0x1b557e)
addr_adv_flags_3 = addr_flags_bosses_0 = Address(0x1b557f)
addr_adv_flags_4 = Address(0x1b5580)
addr_adv_flags_5 = Address(0x1b5581)
addr_adv_flags_6 = addr_flags_clear_fog = addr_flags_cannon = Address(0x1b5582)
addr_adv_flags_7 = Address(0x1b5583)
addr_adv_flags_8 = Address(0x1b5584)
addr_adv_flags_9 = Address(0x1b5585)
addr_adv_flags_10 = Address(0x1b5586)
addr_adv_flags_11 = Address(0x1b5587)
addr_adv_flags_12 = Address(0x1b5588)
addr_adv_flags_13 = addr_flags_shops = Address(0x1b5589)
addr_adv_flags_14 = Address(0x1b558a)
addr_adv_flags_15 = addr_flags_metals = Address(0x1b558b)
addr_adv_flags_16 = Address(0x1b558c)
addr_adv_flags_17 = Address(0x1b558d)
addr_adv_flags_18 = Address(0x1b558e)
addr_adv_flags_19 = Address(0x1b558f)
addr_adv_flags_20 = addr_flags_trade_quest = Address(0x1b5590)
addr_adv_flags_21 = Address(0x1b5591)
addr_adv_flags_22 = Address(0x1b5592)
addr_adv_flags_23 = Address(0x1b5593)
addr_adv_flags_24 = Address(0x1b5594)
addr_adv_flags_25 = Address(0x1b5595)
addr_adv_flags_26 = Address(0x1b5596)
addr_adv_flags_27 = Address(0x1b5597)
addr_adv_flags_28 = Address(0x1b5598)
addr_adv_flags_29 = Address(0x1b5599)
addr_adv_flags_30 = Address(0x1b559a)
addr_adv_flags_31 = Address(0x1b559b)
addr_adv_flags_32 = Address(0x1b559c)
addr_adv_flags_33 = Address(0x1b559d)
addr_adv_flags_34 = Address(0x1b559e)
addr_adv_flags_35 = Address(0x1b559f)
addr_adv_flags_36 = Address(0x1b55a0)
addr_adv_flags_37 = Address(0x1b55a1)
addr_adv_flags_38 = Address(0x1b55a2)
addr_adv_flags_39 = addr_frog_glyphs = Address(0x1b55a3)
addr_adv_flags_40 = Address(0x1b55a4)
addr_adv_flags_41 = Address(0x1b55a5)
addr_adv_flags_42 = Address(0x1b55a6)
addr_adv_flags_43 = Address(0x1b55a7)
addr_adv_flags_44 = addr_watched_intro = Address(0x1b55a8)  # intro is 0x2
addr_adv_flags_45 = Address(0x1b55a9)
addr_adv_flags_46 = Address(0x1b55aa)
addr_adv_flags_47 = addr_flags_fog_done = Address(0x1b55ab)
addr_adv_flags_48 = Address(0x1b55ac)
addr_adv_flags_49 = Address(0x1b55ad)
addr_adv_flags_50 = Address(0x1b55ae)
addr_adv_flags_51 = Address(0x1b55af)



addr_small_key_storage_1 = Address(0x1BA64E)
addr_small_key_storage_2 = Address(0x1BA64F)
addr_custom_storage = Address(0x1BA661)

addr_tof_doors = Address(0x258D20)
addr_tow_doors = Address(0x24D740, size=2)
addr_toc_boss_door = Address(0x252360)
addr_gt_boss_door = Address(0x25D9B0)
addr_toi_doors = Address(0x259CA0)
addr_mt_doors = Address(0x24DED0)

addr_color_switch_toi = Address(0x20DBE0)
addr_color_switch_toc = Address(0x207CA8)

addr_wayfarer_chest = Address(0x20DAA1)

addr_cannon_bomb_blocks = Address(0x2562F0)
addr_goron_bomb_blocks = Address(0x262888)
addr_molida_bomb_blocks = Address(0x258B6C)

addr_tow_warp = Address(0x25A224)
addr_toc_warp = Address(0x25AF1C)
addr_toi_warp = Address(0x264FE4)

addr_totok_b3_state = Address(0x2572EC, size=2)
addr_totok_b3_state_1 = Address(0x2572ED)
addr_totok_b8_state = Address(0x25762C)
addr_totok_b9_state = Address(0x257694)
addr_totok_b12_state = Address(0x257834, size=2)
addr_totok_b12_state_1 = Address(0x257835)
addr_totok_b12_pedestal_left = Address(0x257EA4)
addr_totok_b12_pedestal_right = Address(0x257FE4)
addr_toc_crystal_state = Address(0x252264)
addr_global_salvage_health = Address(0x1BA390)

addr_totok_b9_elevator = Address(0x20C5F0)

# Inventory Data
addr_inventory_1 = Address(0x1ba644)
addr_inventory_2 = Address(0x1ba645)  # Just hammer and potions lol
addr_inventory_3 = addr_fairies_0 = Address(0x1ba646)  # Fairies 0
addr_inventory_4 = addr_fairies_1 = Address(0x1ba647)  # Fairies 1
addr_inventory_5 = Address(0x1ba648)
addr_inventory_6 = Address(0x1ba649)

addr_rupee_count = Address(0x1ba53e, size=2)

addr_show_ship_prices = Address(0x1BA658, size=9)
addr_show_treasure_prices = Address(0x1BA664)
addr_ship_part_counts = Address(0x1BA564, size=72)

addr_pink_coral_count = Address(0x1BA5AC)
addr_wpl_count = Address(0x1BA5AD)
addr_dpl_count = Address(0x1BA5AE)
addr_zora_scale_count = Address(0x1BA5AF)
addr_goron_amber_count = Address(0x1BA5B0)
addr_ruto_crown_count = Address(0x1BA5B1)
addr_roc_feather_count = Address(0x1BA5B2)
addr_regal_ring_count = Address(0x1BA5B3)

addr_phantom_hourglass_max = Address(0x1BA528, size=4)
addr_phantom_hourglass_current = Address(0x1E2A48, size=4)

addr_treasure_maps_0 = Address(0x1BA650)
addr_treasure_maps_1 = Address(0x1BA651)
addr_treasure_maps_2 = Address(0x1BA652)
addr_treasure_maps_3 = Address(0x1BA653)

addr_sword_count = Address(0x1ba6b8)
addr_boomerang_bit = Address(0x1BA6BC)
addr_shovel_bit = Address(0x1BA6BE)
addr_bomb_count = Address(0x1BA6C0, size=2)
addr_arrow_count = Address(0x1BA6C2, size=2)
addr_grapple_bit = Address(0x1BA6C4)
addr_chu_count = Address(0x1BA6C6, size=2)
addr_hammer_bit = Address(0x1BA6C8)

addr_bomb_upgrades = Address(0x1ba5d2)
addr_quiver_upgrades = Address(0x1ba5d0)
addr_chu_upgrades = Address(0x1ba5d4)

addr_power_gem_count = Address(0x1BA541)
addr_wisdom_gem_count = Address(0x1BA542)
addr_courage_gem_count = Address(0x1BA540)

addr_skippyjack_count = Address(0x1BA5B4)
addr_toona_count = Address(0x1BA5B5)
addr_loovar_count = Address(0x1BA5B6)
addr_rsf_count = Address(0x1BA5B7)
addr_neptoona_count = Address(0x1BA5B8)
addr_stowfish_count = Address(0x1BA5B9)

addr_heart_containers = Address(0x1ba388, size=2)
addr_beedle_points = Address(0x1B2773)

addr_potion_left = Address(0x1BA5D8)
addr_potion_right = Address(0x1BA5D9)

addr_island_visible_mercay = Address(0x1b4b8c)
addr_island_visible_molida = Address(0x1b4bb4)
addr_island_visible_ember = Address(0x1B4BDC)
addr_island_visible_cannon = Address(0x1B4C04)
addr_island_visible_spirit = Address(0x1B4C2C)
addr_island_visible_gust = Address(0x1B4C54)
addr_island_visible_bannan = Address(0x1B4C7C)
addr_island_visible_zauz = Address(0x1B4CA4)
addr_island_visible_uncharted = Address(0x1B4CCC)
addr_island_visible_goron = Address(0x1B4CF4)
addr_island_visible_frost = Address(0x1B4D1C)
addr_island_visible_harrow = Address(0x1B4D44)
addr_island_visible_ds = Address(0x1B4D6C)
addr_island_visible_ruins = Address(0x1B4D94)
addr_island_visible_iotd = Address(0x1B4DBC)
addr_island_visible_maze = Address(0x1B4DE4)

# addr_island_visible_ = Address()
# addr_island_visible_ = Address()
# addr_island_visible_ = Address()
# addr_island_visible_ = Address()
# addr_island_visible_ = Address()
# addr_island_visible_ = Address()
