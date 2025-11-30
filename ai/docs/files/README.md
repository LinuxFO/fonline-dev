# Script Documentation

| Script | Description |
| :--- | :--- |
| [FOClassic.fos](FOClassic.fos.md) | //  FOClassic v7 Timestamp 06.03.2019  //  This file contains all exposed 'magic numbers' used in FOClassic. It should not be edited directly by game developers.  Used by engine, native extensions, and scripts.  //  FOCLASSIC_EXTENSION Enables macros, C++ syntax; cannot be used with FOCLASSIC_SCRIPT. Enables macros/values useful in C++ code only.  FOCLASSIC_SCRIPT Enables macros, AngelScript syntax; cannot be used with FOCLASSIC_EXTENSION. They're weirdly formatted currently; uncrustify cannot correctly handle "#" between "MACRO_NAME" and "()"  FOCLASSIC_BLEEDING_EDGE All values which are planned for removal/renaming in future, or related to experimental features, won't be defined.  FOCLASSIC_SKIP_PARAM Critter parameters indexes won't be defined.  FOCLASSIC_SKIP_PID Items prototypes IDs won't be defined.  // |
| [WitchLord.fos](WitchLord.fos.md) | AngelScript bugs checker  (compiles, current revision)        // pass (doesn't compile, current revision) // r[revision] -- [error] (compiles, future revision)         // r[revision] -- pass (description)                       // [what it means for us] void name(...) {...} |
| [_ai.fos](_ai.fos.md) |  FOnline: 2238 Rotators  _ai.fos  |
| [_animation.fos](_animation.fos.md) |  FOnline: 2238 Rotators  _animation.fos  |
| [_bags.fos](_bags.fos.md) |  FOnline: 2238 Rotators  _bags.fos  |
| [_basetypes.fos](_basetypes.fos.md) |  FOnline: 2238 Rotators  _basetypes.fos  |
| [_client_defines.fos](_client_defines.fos.md) |  FOnline: 2238 Rotators  _client_defines.fos  |
| [_client_maps.fos](_client_maps.fos.md) |  FOnline: 2238 Rotators  _client_maps.fos  |
| [_colors.fos](_colors.fos.md) |  FOnline: 2238 Rotators  _colors.fos  |
| [_defines.fos](_defines.fos.md) | uncomment for verbose npc_schedule*.fos #define DEBUG_SCHEDULES |
| [_dialogs.fos](_dialogs.fos.md) |  |
| [_entires.fos](_entires.fos.md) |  FOnline: 2238 Rotators  _entires.fos  |
| [_globalvars.fos](_globalvars.fos.md) |  FOnline: 2238 Rotators  _globalvars.fos  |
| [_macros.fos](_macros.fos.md) |  FOnline: 2238 Rotators  _macros.fos  |
| [_mapper_defines.fos](_mapper_defines.fos.md) |  FOnline: 2238 Rotators  _mapper_defines.fos  |
| [_mapper_macros.fos](_mapper_macros.fos.md) |  FOnline: 2238 Rotators  _mapper_macros.fos  |
| [_maps.fos](_maps.fos.md) |  |
| [_math.fos](_math.fos.md) |  FOnline: 2238 Rotators  _math.fos  |
| [_msgstr.fos](_msgstr.fos.md) |  |
| [_npc_pids.fos](_npc_pids.fos.md) |  |
| [_scripts.fos](_scripts.fos.md) |  FOnline: 2238 Rotators  _scripts.fos  |
| [_time.fos](_time.fos.md) |  FOnline: 2238 Rotators  _time.fos  |
| [_town.fos](_town.fos.md) |  FOnline: 2238 Rotators  _town.fos  |
| [_vals.fos](_vals.fos.md) |  FOnline: 2238 Rotators  _vals.fos  |
| [_vars.fos](_vars.fos.md) |  |
| [all_brahmin.fos](all_brahmin.fos.md) |  FOnline: 2238 Rotators  all_brahmin.fos  |
| [all_brahmin_herdsman.fos](all_brahmin_herdsman.fos.md) |  FOnline: 2238 Rotators  all_brahmin_herdsman.fos  |
| [all_farmer.fos](all_farmer.fos.md) |  FOnline: 2238 Rotators  all_farmer.fos  |
| [antiblock.fos](antiblock.fos.md) |  FOnline: 2238 Rotators  antiblock.fos  |
| [attach.fos](attach.fos.md) |  FOnline: 2238 Rotators  attach.fos  |
| [bank_vault.fos](bank_vault.fos.md) |  FOnline: 2238 Rotators  bank_vault.fos  |
| [billboards.fos](billboards.fos.md) |  FOnline: 2238 Rotators  billboards.fos  |
| [blackjack.fos](blackjack.fos.md) | *< *  Main logic for the Blackjack module.  |
| [blackjack_card.fos](blackjack_card.fos.md) | *< *  Card class for Blackjack.  |
| [blackjack_deck.fos](blackjack_deck.fos.md) | *< *  Deck of cards for Blackjack.  |
| [blackjack_dialogues.fos](blackjack_dialogues.fos.md) | *< *  Dialogue calls for the Blackjack module.  |
| [blackjack_h.fos](blackjack_h.fos.md) | *< *  Blackjack - Card game for FOnline. *  What would be the most reasonable way that gambling skill would affect the course of the game? *  (It shall be true to gambling in rl, shall be fun, and shall not be exploitable or afk farmed easily (or at all?).) * *  Specification: *      1. Dialogue based with possibility to attach a new GUI for it. *      2. The pile of cards shall be pre-generated at each shuffle and not randomized at each draw. *      3. Gambling skill difference between host and player is checked, against a  roll, as usual. *          3.1 The advantage of higher gambling skill: *              3.1.1 Info over the the number of card packs used (which would be random 4 - 8 after each session). *              3.1.2 Frequency of shuffling would be lower with better gambling + speech skill checks. *              3.1.3 Card counting: available as long as gambling skill is higher than of host and the intellect of player is above X, *                      as this is the easiest ways to get advantage over host. *              3.1.4 Shuffle tracks: Occasionally on a critical or very hard roll on gambling + perception shuffling check, *                      the player will be notified if there are way more high or low cards in the next X cards, if that is the case. *          3.2 Disadvantage of lower gambling skill: *              3.2.1 Basically missing out on the benefits, like: the character does not pay attention when the shuffling of cards happens, *                      since he doesn't know that is important, so you miss that info. *          3.3 Other possibilities: *              3.3.1 Cheating 1: where the odds of high (7,8,9) or low cards (2,3,4) is reduced/raised, maybe the later could be added *                      to some mini/repeatable quest or the host could be sweet talked /payed into changing the packs or whatever.. *                      (would only create the possibility for it, but not the quest itself) In this case the host would give a hint for the player, *                      until the cards are replaced. *              3.3.2 Cheating 2: where the player will be notified if the hole card is an Ace or 10. *              3.3.3 Cheating 3: Casino could cheat as well, cutting down some cards for player session, this should be able to be find out *                      via mini quest/tip drunk gambler/speech etc. or simply by gambling check rolls. *          3.4. Different casinos could have different rules and special offers to promote themselves: *              3.4.1 Rule changes: *                  3.4.1.1 "Hit soft 17" - dealer has to draw a card if on soft 17. *                  3.4.1.2 "Dealer wins ties" - dealer will win ties. *                  3.4.1.3 "No Hole card" - dealer does not consult hole card until player finished his turns. (can't cheat to find out dealer's hole card) *                  3.4.1.4 "No Black Jack after splitting Aces" - no bonus on Black Jack after splitting Aces. *              3.4.2 Side bets: *                  3.4.2.1 "Royal Match" - Pays for suit matches. *                  3.4.2.2 "Perfect Pair" - is an extra bet option before drawing cards, the player can bet if he gets pairs (Perfect, Colored, Mixed, No pairs) *                  3.4.2.3 "Lucky Ladies" - pays for initial cards value of 20. (Pair of Queen of Hearts, Suit Pair, etc) *              3.4.3 Promotions: *                  3.4.3.1 "Real" Black Jack pays higher than regular Black Jack. (11 to 2 instead of 3 to 2). (Real mean Ace of spades with a black Jack card.) * *  What to keep in sight: *      1. It shall be configurable, so that mini quests or altering affects can differ from player to player and from session to session. *      2. Shall be expandable later on to a graphical design. *      3. Casino rules could be configurable, so that each session (or say,week) could be different, (or per player different odds) so that it can be tied to side quests to gather that info. (e.g.: Tip some wasted beggar or gambler to know the current situation / Or just the need to read the rules from dialogue so that botting is made harder.) * *  Author:     Slowhand *  Reviewer:   N/A *  Tester:     N/A  |
| [blackjack_manager.fos](blackjack_manager.fos.md) | *< *  Manager class for Blackjack module.  |
| [blackjack_shoe.fos](blackjack_shoe.fos.md) | *< *  Shoe class for Blackjack.  |
| [blueprints.fos](blueprints.fos.md) |  FOnline: 2238 Rotators  blueprints.fos  |
| [books.fos](books.fos.md) |  |
| [brahmin_pen.fos](brahmin_pen.fos.md) |  FOnline: 2238 Rotators  brahmin_pen.fos  |
| [brahmin_pen_h.fos](brahmin_pen_h.fos.md) |  FOnline: 2238 Rotators  brahmin_pen_h.fos  |
| [brahmin_pens.fos](brahmin_pens.fos.md) |  FOnline: 2238 Rotators  brahmin_pens.fos  |
| [brahmin_trader.fos](brahmin_trader.fos.md) |  FOnline: 2238 Rotators  brahmin_trader.fos  |
| [brahmin_trader_h.fos](brahmin_trader_h.fos.md) |  FOnline: 2238 Rotators  brahmin_trader_h.fos  |
| [brahmin_traders.fos](brahmin_traders.fos.md) |  FOnline: 2238 Rotators  brahmin_traders.fos  |
| [broadcast.fos](broadcast.fos.md) |  FOnline: 2238 Rotators  broadcast.fos  |
| [broadcast_h.fos](broadcast_h.fos.md) |  FOnline: 2238 Rotators  broadcast_h.fos  |
| [buffer.fos](buffer.fos.md) |  * WHINE TEAM * We Had Ini, Now Engine * * RunClientScript/RunServerScript data "packer" * Partially based on Serializator (TLA scripts) and BufferManager (FOnline engine) * * server and client module  |
| [buffer_h.fos](buffer_h.fos.md) |  * WHINE TEAM * We Had Ini, Now Engine * * RunClientScript/RunServerScript data "packer" * Partially based on Serializator (TLA scripts) and BufferManager (FOnline engine) * * server and client module  |
| [buffer_lazy.fos](buffer_lazy.fos.md) |  FOnline: 2238 Rotators  buffer_lazy.fos  |
| [buffer_lazy_h.fos](buffer_lazy_h.fos.md) |  FOnline: 2238 Rotators  buffer_lazy_h.fos  |
| [car.fos](car.fos.md) |  FOnline: 2238 Rotators  car.fos  |
| [car_seller.fos](car_seller.fos.md) |  FOnline: 2238 Rotators  car_seller.fos  |
| [caravans.fos](caravans.fos.md) |  FOnline: 2238 Rotators  caravans.fos  |
| [caravans_h.fos](caravans_h.fos.md) |  FOnline: 2238 Rotators  caravans_h.fos  |
| [cave.fos](cave.fos.md) |  FOnline: 2238 Rotators  cave.fos  |
| [cave_critter_h.fos](cave_critter_h.fos.md) |  FOnline: 2238 Rotators  cave_critter_h.fos  |
| [cave_critters.fos](cave_critters.fos.md) |  FOnline: 2238 Rotators  cave_critters.fos  |
| [cave_groups.fos](cave_groups.fos.md) |  FOnline: 2238 Rotators  cave_groups.fos  |
| [cave_h.fos](cave_h.fos.md) |  FOnline: 2238 Rotators  cave_h.fos  |
| [cave_item_h.fos](cave_item_h.fos.md) |  FOnline: 2238 Rotators  cave_item_h.fos  |
| [cave_items.fos](cave_items.fos.md) |  FOnline: 2238 Rotators  cave_items.fos  |
| [cavelog.fos](cavelog.fos.md) |  FOnline: 2238 Rotators  cavelog.fos  |
| [cfg_file.fos](cfg_file.fos.md) |  FOnline: 2238 Rotators  cfg_file.fos  |
| [cheats.fos](cheats.fos.md) |  |
| [cheats_core_h.fos](cheats_core_h.fos.md) |  FOnline: 2238 Rotators  cheats_core_h.fos  |
| [cheats_help.fos](cheats_help.fos.md) |  FOnline: 2238 Rotators  cheats_help.fos  |
| [chosen_actions_h.fos](chosen_actions_h.fos.md) |  FOnline: 2238 Rotators  chosen_actions_h.fos  |
| [chosen_tabs.fos](chosen_tabs.fos.md) |  FOnline: 2238 Rotators  chosen_tabs.fos  |
| [client\smart_cursor.fos](client\smart_cursor.fos.md) |  |
| [client_access.fos](client_access.fos.md) | Author: JohnPL Client access control |
| [client_access_h.fos](client_access_h.fos.md) | Author: JohnPL Client access control header |
| [client_anti_cheat.fos](client_anti_cheat.fos.md) |  FOnline: 2238 Rotators  client_anti_cheat.fos  |
| [client_anti_cheat_h.fos](client_anti_cheat_h.fos.md) |  FOnline: 2238 Rotators  client_anti_cheat_h.fos  |
| [client_broadcast.fos](client_broadcast.fos.md) |  FOnline: 2238 Rotators  client_broadcast.fos  |
| [client_combat.fos](client_combat.fos.md) |  FOnline: 2238 Rotators  client_combat.fos  |
| [client_container_addons.fos](client_container_addons.fos.md) |  FOnline: 2238 Rotators  client_container_volume.fos  |
| [client_critter_onhead.fos](client_critter_onhead.fos.md) |  |
| [client_cutscene.fos](client_cutscene.fos.md) |  FOnline: 2238 Rotators  client_cutscene.fos  |
| [client_dev_menu.fos](client_dev_menu.fos.md) |  FOnline: 2238 Rotators  client_dev_menu.fos  |
| [client_fef.fos](client_fef.fos.md) |  |
| [client_fixboy.fos](client_fixboy.fos.md) |  |
| [client_followers_menu.fos](client_followers_menu.fos.md) |  FOnline: 2238 Rotators  client_followers_menu.fos  |
| [client_fov.fos](client_fov.fos.md) |  FOnline: 2238 Rotators  client_fov.fos  |
| [client_gmtools.fos](client_gmtools.fos.md) |  FOnline: 2238 Rotators  client_gmtools.fos  |
| [client_gmtools_chat.fos](client_gmtools_chat.fos.md) |  FOnline: 2238 Rotators  client_gmtools_chat.fos  |
| [client_gmtools_macro.fos](client_gmtools_macro.fos.md) |  FOnline: 2238 Rotators  client_gmtools_macro.fos  |
| [client_gmtools_menu.fos](client_gmtools_menu.fos.md) |  FOnline: 2238 Rotators  client_gmtools_menu.fos  |
| [client_gui.fos](client_gui.fos.md) |  FOnline: 2238 Rotators  client_gui.fos  |
| [client_gui_barter.fos](client_gui_barter.fos.md) |  FOnline: 2238 Rotators  client_gui_barter.fos  |
| [client_gui_elevator.fos](client_gui_elevator.fos.md) |  FOnline: 2238 Rotators  client_gui_elevator.fos  |
| [client_gui_ex.fos](client_gui_ex.fos.md) |  FOnline: 2238 Rotators  client_gui_ex.fos  |
| [client_gui_h.fos](client_gui_h.fos.md) |  FOnline: 2238 Rotators  client_gui_h.fos  |
| [client_interface.fos](client_interface.fos.md) |  FOnline: 2238 Rotators  client_interface.fos  |
| [client_interface_h.fos](client_interface_h.fos.md) |  FOnline: 2238 Rotators  client_interface_h.fos  |
| [client_io.fos](client_io.fos.md) |  FOnline: 2238 Rotators  client_io.fos  |
| [client_keybinds.fos](client_keybinds.fos.md) |  FOnline: 2238 Rotators  client_keybinds.fos  |
| [client_keybinds_h.fos](client_keybinds_h.fos.md) |  FOnline: 2238 Rotators  client_keybinds_h.fos  |
| [client_main.fos](client_main.fos.md) |  FOnline: 2238 Rotators  client_main.fos  |
| [client_mapper_animation.fos](client_mapper_animation.fos.md) |  FOnline: 2238 Rotators  client_mapper_animation.fos  |
| [client_messages.fos](client_messages.fos.md) |  FOnline: 2238 Rotators  client_messages.fos  |
| [client_online_stats.fos](client_online_stats.fos.md) |  FOnline: 2238 Rotators  client_online_stats.fos  |
| [client_recording.fos](client_recording.fos.md) |  FOnline: 2238 Rotators  client_recording.fos  |
| [client_screen_gameinfo_h.fos](client_screen_gameinfo_h.fos.md) |  |
| [client_screen_picture.fos](client_screen_picture.fos.md) |  FOnline: 2238 Rotators  client_screen_picture.fos  |
| [client_screens.fos](client_screens.fos.md) |  FOnline: 2238 Rotators  client_screens.fos  |
| [client_screens_h.fos](client_screens_h.fos.md) |  FOnline: 2238 Rotators  client_screens_h.fos  |
| [client_spawn_npc.fos](client_spawn_npc.fos.md) |  FOnline: 2238 Rotators  client_spawn_npc.fos  |
| [client_timeouts.fos](client_timeouts.fos.md) |  FOnline: 2238 Rotators  client_timeouts.fos  |
| [client_utils.fos](client_utils.fos.md) |  FOnline: 2238 Rotators  client_utils.fos  |
| [client_utils_h.fos](client_utils_h.fos.md) |  FOnline: 2238 Rotators  client_utils_h.fos  |
| [combat.fos](combat.fos.md) |  FOnline: 2238 Rotators  combat.fos  |
| [combat_h.fos](combat_h.fos.md) |  FOnline: 2238 Rotators  combat_h.fos  |
| [combat_msg.fos](combat_msg.fos.md) |  FOnline: 2238 Rotators  combat_msg.fos  |
| [config.fos](config.fos.md) | Script for use in client, server, and a mapper - in start functions |
| [config_file.fos](config_file.fos.md) |  FOnline: 2238 Rotators  config_file.fos  |
| [config_file_h.fos](config_file_h.fos.md) |  FOnline: 2238 Rotators  config_file_h.fos  |
| [config_h.fos](config_h.fos.md) |  FOnline: 2238 Rotators  config_h.fos  |
| [critical_failures.fos](critical_failures.fos.md) |  FOnline: 2238 Rotators  critical_failures.fos  |
| [critical_table.fos](critical_table.fos.md) |  FOnline: 2238 Rotators  critical_table.fos  |
| [critter_age.fos](critter_age.fos.md) |  FOnline: 2238 Rotators  critter_age.fos  |
| [critter_age_h.fos](critter_age_h.fos.md) |  FOnline: 2238 Rotators  critter_age_h.fos  |
| [critter_description.fos](critter_description.fos.md) |  FOnline: 2238 Rotators  critter_description.fos  |
| [critter_item_movement.fos](critter_item_movement.fos.md) |  FOnline: 2238 Rotators  critter_item_movement.fos  |
| [critter_skin.fos](critter_skin.fos.md) |  Wipe/Rotators  critter_skin.fos  |
| [critter_skin_h.fos](critter_skin_h.fos.md) |  |
| [debug.fos](debug.fos.md) |  FOnline: 2238 Rotators  debug.fos  |
| [debug_h.fos](debug_h.fos.md) |  FOnline: 2238 Rotators  debug_h.fos  |
| [den_metzger_guard.fos](den_metzger_guard.fos.md) |  FOnline: 2238 Rotators  den_metzger_guard.fos  |
| [dev_menu.fos](dev_menu.fos.md) |  FOnline: 2238 Rotators  dev_menu.fos  |
| [devconnect.fos](devconnect.fos.md) |  FOnline: 2238 Rotators  devconnect.fos  |
| [dialog.fos](dialog.fos.md) |  |
| [dialog_altruist.fos](dialog_altruist.fos.md) |  FOnline: 2238 Rotators  dialog_altruist.fos  |
| [dialog_factions.fos](dialog_factions.fos.md) |  FOnline: 2238 Rotators  dialog_factions.fos  |
| [dialog_reputations.fos](dialog_reputations.fos.md) |  FOnline: 2238 Rotators  dialog_reputations.fos  |
| [drugs.fos](drugs.fos.md) | FOnline: 2238 Rotators  drugs.fos  |
| [drugs_data.fos](drugs_data.fos.md) |  FOnline: 2238 Rotators  drugs_data.fos  |
| [duel.fos](duel.fos.md) |  FOnline: 2238 Rotators  duel.fos  |
| [economy.fos](economy.fos.md) |  FOnline: 2238 Rotators  economy.fos  |
| [economy_bank.fos](economy_bank.fos.md) |  FOnline: 2238 Rotators  economy_bank.fos  |
| [economy_bankaccount.fos](economy_bankaccount.fos.md) |  FOnline: 2238 Rotators  economy_bankaccount.fos  |
| [economy_banker.fos](economy_banker.fos.md) |  FOnline: 2238 Rotators  economy_banker.fos  |
| [economy_h.fos](economy_h.fos.md) |  FOnline: 2238 Rotators  economy_h.fos  |
| [effects.fos](effects.fos.md) |  FOnline: 2238 Rotators  effects.fos  |
| [elevators.fos](elevators.fos.md) |  FOnline: 2238 Rotators  elevators.fos  |
| [elevators_h.fos](elevators_h.fos.md) |  FOnline: 2238 Rotators  elevators_h.fos  |
| [encounter_containers.fos](encounter_containers.fos.md) |  FOnline: 2238 Rotators  encounter_containers.fos  |
| [encounter_guard.fos](encounter_guard.fos.md) |  FOnline: 2238 Rotators  encounter_guard.fos  |
| [entire.fos](entire.fos.md) |  FOnline: 2238 Rotators  entire.fos  |
| [event_utils.fos](event_utils.fos.md) |  FOnline: 2238 Rotators  event_utils.fos  |
| [event_warzone.fos](event_warzone.fos.md) |  FOnline: 2238 Rotators  event_warzone.fos  |
| [eventboss.fos](eventboss.fos.md) |  FOnline: 2238 Rotators  eventboss.fos  |
| [eventboss_h.fos](eventboss_h.fos.md) |  FOnline: 2238 Rotators  eventboss_h.fos  |
| [explode.fos](explode.fos.md) |  FOnline: 2238 Rotators  explode.fos  |
| [faction_data.fos](faction_data.fos.md) |  FOnline: 2238 Rotators  faction_data.fos  |
| [factions.fos](factions.fos.md) |  FOnline: 2238 Rotators  factions.fos  |
| [factions_bases.fos](factions_bases.fos.md) |  FOnline: 2238 Rotators  factions_bases.fos  |
| [factions_bases_h.fos](factions_bases_h.fos.md) |  FOnline: 2238 Rotators  factions_bases_h.fos  |
| [factions_generic.fos](factions_generic.fos.md) |  FOnline: 2238 Rotators  factions_generic.fos  |
| [factions_generic_bartender.fos](factions_generic_bartender.fos.md) |  FOnline: 2238 Rotators  factions_generic_bartender.fos  |
| [factions_h.fos](factions_h.fos.md) |  FOnline: 2238 Rotators  factions_h.fos  |
| [factions_names.fos](factions_names.fos.md) |  FOnline: 2238 Rotators  factions_names.fos  |
| [factions_news.fos](factions_news.fos.md) |  FOnline: 2238 Rotators  factions_news.fos  |
| [factions_player.fos](factions_player.fos.md) |  FOnline: 2238 Rotators  factions_player.fos  |
| [factions_player_h.fos](factions_player_h.fos.md) |  FOnline: 2238 Rotators  factions_player_h.fos  |
| [factions_recognition.fos](factions_recognition.fos.md) |  FOnline: 2238 Rotators  factions_recognition.fos  |
| [factions_terminal.fos](factions_terminal.fos.md) |  FOnline: 2238 Rotators  factions_terminal.fos  |
| [factions_vc_q_scoutsf.fos](factions_vc_q_scoutsf.fos.md) |  FOnline: 2238 Rotators  factions_vc_q_scoutsf.fos  |
| [fix_boy.fos](fix_boy.fos.md) |  FOnline: 2238 Rotators  fix_boy.fos  |
| [fixboy.fos](fixboy.fos.md) |  FOnline: 2238 Rotators  fixboy.fos  |
| [fixboy_h.fos](fixboy_h.fos.md) |  FOnline: 2238 Rotators  fixboy_h.fos  |
| [floyd.fos](floyd.fos.md) |  FOnline: 2238 Rotators  floyd.fos  |
| [follower.fos](follower.fos.md) |  FOnline: 2238 Rotators  follower.fos  |
| [follower_capturing.fos](follower_capturing.fos.md) |  FOnline: 2238 Rotators  follower_capturing.fos  |
| [follower_common.fos](follower_common.fos.md) |  FOnline: 2238 Rotators  follower_common.fos  |
| [follower_common_h.fos](follower_common_h.fos.md) |  FOnline: 2238 Rotators  follower_common_h.fos  |
| [follower_h.fos](follower_h.fos.md) |  FOnline: 2238 Rotators  follower_h.fos  |
| [followers_menu.fos](followers_menu.fos.md) |  FOnline: 2238 Rotators  followers_menu.fos  |
| [geiger.fos](geiger.fos.md) |  FOnline: 2238 Rotators  geiger.fos  |
| [generator.fos](generator.fos.md) |  FOnline: 2238 Rotators  generator.fos  |
| [generic_guard.fos](generic_guard.fos.md) |  FOnline: 2238 Rotators  generic_guard.fos  |
| [globalmap_group.fos](globalmap_group.fos.md) |  FOnline: 2238 Rotators  globalmap_group.fos  |
| [gm.fos](gm.fos.md) |  FOnline: 2238 Rotators  gm.fos  |
| [gmtools.fos](gmtools.fos.md) |  FOnline: 2238 Rotators  gmtools.fos  |
| [gmtools_csc.fos](gmtools_csc.fos.md) |  FOnline: 2238 Rotators  gmtools_csc.fos  |
| [gmtools_h.fos](gmtools_h.fos.md) |  FOnline: 2238 Rotators  gmtools_h.fos  |
| [grave.fos](grave.fos.md) |  FOnline: 2238 Rotators  grave.fos  |
| [groups_h.fos](groups_h.fos.md) |  FOnline: 2238 Rotators  groups_h.fos  |
| [guard.fos](guard.fos.md) |  FOnline: 2238 Rotators  guard.fos  |
| [guard_h.fos](guard_h.fos.md) |  FOnline: 2238 Rotators  guard_h.fos  |
| [hexShot.fos](hexShot.fos.md) |  |
| [hexThrow.fos](hexThrow.fos.md) |  |
| [hub_guard.fos](hub_guard.fos.md) |  FOnline: 2238 Rotators  hub_guard.fos  |
| [ini_parser.fos](ini_parser.fos.md) |  FOnline: 2238 Rotators  ini_parser.fos  |
| [intellisense.fos](intellisense.fos.md) |  |
| [item_achievementbook.fos](item_achievementbook.fos.md) |  FOnline: Reloaded Kilgore  item_achievementbook.fos  |
| [item_attributes.fos](item_attributes.fos.md) |  FOnline: 2238 Rotators  item_attributes.fos  |
| [item_bag_container.fos](item_bag_container.fos.md) |  FOnline: 2238 Rotators  item_bag_container.fos  |
| [item_blueprint.fos](item_blueprint.fos.md) |  FOnline: 2238 Rotators  item_blueprint.fos  |
| [item_bonus.fos](item_bonus.fos.md) | Item bonuses  |
| [item_brahmin_dung.fos](item_brahmin_dung.fos.md) |  FOnline: 2238 Rotators  item_brahmin_dung.fos  |
| [item_dogtags.fos](item_dogtags.fos.md) |  FOnline: 2238 Rotators  item_dogtags.fos  |
| [item_dogtags_h.fos](item_dogtags_h.fos.md) |  FOnline: 2238 Rotators  item_dogtags_h.fos  |
| [item_dynamic.fos](item_dynamic.fos.md) |  FOnline: 2238 Rotators  item_dynamic.fos  |
| [item_dynamic_h.fos](item_dynamic_h.fos.md) |  FOnline: 2238 Rotators  item_dynamic_h.fos  |
| [item_flare.fos](item_flare.fos.md) |  FOnline: 2238 Rotators  item_flare.fos  |
| [item_holodisk.fos](item_holodisk.fos.md) |  FOnline: 2238 Rotators  item_holodisk.fos  |
| [item_lock.fos](item_lock.fos.md) |  FOnline: 2238 Rotators  item_lock.fos  |
| [item_mapdoor.fos](item_mapdoor.fos.md) |  FOnline: 2238 Rotators  item_mapdoor.fos  |
| [item_misc.fos](item_misc.fos.md) |  FOnline: 2238 Rotators  item_misc.fos  |
| [item_misc_h.fos](item_misc_h.fos.md) |  FOnline: 2238 Rotators  item_misc_h.fos  |
| [item_perks.fos](item_perks.fos.md) |  FOnline: 2238 Rotators  item_perks.fos  |
| [item_perks_h.fos](item_perks_h.fos.md) |  FOnline: 2238 Rotators  item_perks_h.fos  |
| [item_radio.fos](item_radio.fos.md) |  FOnline: 2238 Rotators  item_radio.fos  |
| [item_skills.fos](item_skills.fos.md) |  FOnline: 2238 Rotators  item_skills.fos  |
| [item_spawner_container.fos](item_spawner_container.fos.md) |  FOnline: 2238 Rotators  item_spawner_container.fos  |
| [item_stealth.fos](item_stealth.fos.md) |  FOnline: 2238 Rotators  item_stealth.fos  |
| [item_tent.fos](item_tent.fos.md) |  FOnline: 2238 Rotators  item_tent.fos  |
| [itempid.fos](itempid.fos.md) |  FOnline: 2238 Rotators  itempid.fos  |
| [itempid_h.fos](itempid_h.fos.md) |  FOnline: 2238 Rotators  itempid_h.fos  |
| [la_ady_guard.fos](la_ady_guard.fos.md) |  FOnline: 2238 Rotators  la_ady_guard.fos  |
| [lexems.fos](lexems.fos.md) |  FOnline: 2238 Rotators  lexems.fos  |
| [lexems_h.fos](lexems_h.fos.md) |  FOnline: 2238 Rotators  lexems_h.fos  |
| [linetracer.fos](linetracer.fos.md) |  FOnline: 2238 Rotators  linetracer.fos  |
| [linetracer_h.fos](linetracer_h.fos.md) |  FOnline: 2238 Rotators  linetracer_h.fos  |
| [lockers.fos](lockers.fos.md) |  FOnline: 2238 Rotators  lockers.fos  |
| [logging.fos](logging.fos.md) |  FOnline: 2238 Rotators  logging.fos  |
| [logging_critter.fos](logging_critter.fos.md) |  FOnline: 2238 Rotators  logging_critter.fos  |
| [logging_h.fos](logging_h.fos.md) |  FOnline: 2238 Rotators  logging_h.fos  |
| [main.fos](main.fos.md) |  FOnline: 2238 Rotators  main.fos  |
| [main_planes.fos](main_planes.fos.md) |  FOnline: 2238 Rotators  main_planes.fos  |
| [map_boneyard.fos](map_boneyard.fos.md) |  FOnline: 2238 Rotators  map_boneyard.fos  |
| [map_bos_lh.fos](map_bos_lh.fos.md) |  FOnline: 2238 Rotators  map_bos_lh.fos  |
| [map_broken.fos](map_broken.fos.md) |  FOnline: 2238 Rotators  map_broken.fos  |
| [map_denbus.fos](map_denbus.fos.md) |  FOnline: 2238 Rotators  map_denbus.fos  |
| [map_encounter.fos](map_encounter.fos.md) |  FOnline: 2238 Rotators  map_encounter.fos  |
| [map_gecko.fos](map_gecko.fos.md) |  FOnline: 2238 Rotators  map_gecko.fos  |
| [map_hub.fos](map_hub.fos.md) |  |
| [map_klamath.fos](map_klamath.fos.md) |  FOnline: 2238 Rotators  map_klamath.fos  |
| [map_modoc.fos](map_modoc.fos.md) |  FOnline: 2238 Rotators  map_modoc.fos  |
| [map_ncr_downtown.fos](map_ncr_downtown.fos.md) |  |
| [map_npcmap.fos](map_npcmap.fos.md) |  FOnline: 2238 Rotators  map_npcmap.fos  |
| [map_playerfaction_hq.fos](map_playerfaction_hq.fos.md) |  FOnline: 2238 Rotators  map_playerfaction_hq.fos  |
| [map_random_cave.fos](map_random_cave.fos.md) |  FOnline: 2238 Rotators  map_random_cave.fos  |
| [map_redding.fos](map_redding.fos.md) |  FOnline: 2238 Rotators  map_redding.fos  |
| [map_redding_bank_vault.fos](map_redding_bank_vault.fos.md) |  FOnline: 2238 Rotators  map_redding_bank_vault.fos  |
| [map_redding_lost.fos](map_redding_lost.fos.md) |  FOnline: 2238 Rotators  map_redding_lost.fos  |
| [map_redding_mine.fos](map_redding_mine.fos.md) |  FOnline: 2238 Rotators  map_redding_mine.fos  |
| [map_slaverun.fos](map_slaverun.fos.md) |  FOnline: 2238 Rotators  map_slaverun.fos  |
| [map_starter.fos](map_starter.fos.md) |  |
| [map_tent.fos](map_tent.fos.md) |  FOnline: 2238 Rotators  map_tent.fos  |
| [map_tent_h.fos](map_tent_h.fos.md) |  FOnline: 2238 Rotators  map_tent_h.fos  |
| [mapdata.fos](mapdata.fos.md) |  |
| [mapdata_h.fos](mapdata_h.fos.md) |  FOnline: 2238 Rotators  mapdata_h.fos  |
| [mapper_autowall.fos](mapper_autowall.fos.md) |  FOnline: 2238 Rotators  mapper_autowall.fos  |
| [mapper_crtypes.fos](mapper_crtypes.fos.md) |  FOnline: 2238 Rotators  mapper_crtypes.fos  |
| [mapper_generators.fos](mapper_generators.fos.md) |  FOnline: 2238 Rotators  mapper_generators.fos  |
| [mapper_grid.fos](mapper_grid.fos.md) |  FOnline: 2238 Rotators  mapper_grid.fos  |
| [mapper_gui.fos](mapper_gui.fos.md) |  FOnline: 2238 Rotators  mapper_gui.fos  |
| [mapper_main.fos](mapper_main.fos.md) |  FOnline: 2238 Rotators  mapper_main.fos  |
| [mapper_plugin.fos](mapper_plugin.fos.md) |  FOnline: 2238 Rotators  mapper_plugin.fos  |
| [mapper_plugin_h.fos](mapper_plugin_h.fos.md) |  FOnline: 2238 Rotators  mapper_plugin_h.fos  |
| [mapper_tilemap.fos](mapper_tilemap.fos.md) |  FOnline: 2238 Rotators  mapper_tilemap.fos  |
| [mapper_utils.fos](mapper_utils.fos.md) |  FOnline: 2238 Rotators  mapper_utils.fos  |
| [mapper_utils_h.fos](mapper_utils_h.fos.md) |  FOnline: 2238 Rotators  mapper_utils_h.fos  |
| [media.fos](media.fos.md) |  FOnline: 2238 Rotators  media.fos  |
| [merc_dialog.fos](merc_dialog.fos.md) |  FOnline: 2238 Rotators  merc_dialog.fos  |
| [mercs.fos](mercs.fos.md) |  FOnline: 2238 Rotators  mercs.fos  |
| [mercs_h.fos](mercs_h.fos.md) |  FOnline: 2238 Rotators  mercs_h.fos  |
| [messages_h.fos](messages_h.fos.md) |  FOnline: 2238 Rotators  messages_h.fos  |
| [mine.fos](mine.fos.md) |  FOnline: 2238 Rotators  mine.fos  |
| [mine_h.fos](mine_h.fos.md) |  FOnline: 2238 Rotators  mine_h.fos  |
| [minigames.fos](minigames.fos.md) |  FOnline: 2238 Rotators  minigames.fos  |
| [minigames_h.fos](minigames_h.fos.md) |  FOnline: 2238 Rotators  minigames_h.fos  |
| [mob.fos](mob.fos.md) |  FOnline: 2238 Rotators  mob.fos  |
| [mob_quest.fos](mob_quest.fos.md) |  |
| [mob_wave.fos](mob_wave.fos.md) |  FOnline: 2238 Rotators  mob_wave.fos  |
| [mob_wave_data.fos](mob_wave_data.fos.md) |  FOnline: 2238 Rotators  mob_wave_data.fos  |
| [mob_wave_h.fos](mob_wave_h.fos.md) |  FOnline: 2238 Rotators  mob_wave_h.fos  |
| [movable_container.fos](movable_container.fos.md) |  FOnline: 2238 Rotators  movable_container.fos  |
| [multihex.fos](multihex.fos.md) |  FOnline: 2238 Rotators  multihex.fos  |
| [multihex_data.fos](multihex_data.fos.md) |  FOnline: 2238 Rotators  multihex_data.fos  |
| [multihex_h.fos](multihex_h.fos.md) |  FOnline: 2238 Rotators  multihex_h.fos  |
| [name_colorizing.fos](name_colorizing.fos.md) |  FOnline: 2238 Rotators  name_colorizing.fos  |
| [ncr_guard.fos](ncr_guard.fos.md) |  FOnline: 2238 Rotators  ncr_guard.fos  |
| [noob_camp_dialog.fos](noob_camp_dialog.fos.md) |  |
| [noob_camp_guard.fos](noob_camp_guard.fos.md) |  |
| [noobhook.fos](noobhook.fos.md) |  FOnline: 2238 Rotators  noobhook.fos  |
| [npc_ai.fos](npc_ai.fos.md) |  FOnline: 2238 Rotators  npc_ai.fos  |
| [npc_barber.fos](npc_barber.fos.md) |  FOnline: 2238 Rotators  npc_barber.fos  |
| [npc_common.fos](npc_common.fos.md) |  FOnline: 2238 Rotators  npc_common.fos  |
| [npc_common_h.fos](npc_common_h.fos.md) |  FOnline: 2238 Rotators  npc_common_h.fos  |
| [npc_names.fos](npc_names.fos.md) |  FOnline: 2238 Rotators  npc_names.fos  |
| [npc_names_h.fos](npc_names_h.fos.md) |  FOnline: 2238 Rotators  npc_names_h.fos  |
| [npc_planes.fos](npc_planes.fos.md) |  FOnline: 2238 Rotators  npc_planes.fos  |
| [npc_planes_h.fos](npc_planes_h.fos.md) |  FOnline: 2238 Rotators  npc_planes_h.fos  |
| [npc_roles_h.fos](npc_roles_h.fos.md) |  FOnline: 2238 Rotators  npc_roles_h.fos  |
| [npc_shouter.fos](npc_shouter.fos.md) |  FOnline: 2238 Rotators  npc_shouter.fos  |
| [npc_unlootable.fos](npc_unlootable.fos.md) |  FOnline: 2238 Rotators  npc_unlootable.fos  |
| [online_stats.fos](online_stats.fos.md) |  FOnline: 2238 Rotators  online_stats.fos  |
| [online_stats_h.fos](online_stats_h.fos.md) |  FOnline: 2238 Rotators  online_stats_h.fos  |
| [parameters.fos](parameters.fos.md) |  FOnline: 2238 Rotators  parameters.fos  |
| [pdata.fos](pdata.fos.md) |  |
| [pdata_h.fos](pdata_h.fos.md) |  |
| [perks.fos](perks.fos.md) |  FOnline: 2238 Rotators  perks.fos  |
| [perks_data.fos](perks_data.fos.md) |  FOnline: 2238 Rotators  perks_data.fos  |
| [pids_groups.fos](pids_groups.fos.md) |  FOnline: 2238 Rotators  pids_groups.fos  |
| [player_dungeon_toxic.fos](player_dungeon_toxic.fos.md) |  |
| [player_dungeonla.fos](player_dungeonla.fos.md) |  |
| [player_dungeonlacity.fos](player_dungeonlacity.fos.md) |  |
| [player_house.fos](player_house.fos.md) |  |
| [poison.fos](poison.fos.md) |  FOnline: 2238 Rotators  poison.fos  |
| [polygon.fos](polygon.fos.md) |  FOnline: 2238 Rotators  polygon.fos  |
| [polygon_h.fos](polygon_h.fos.md) |  FOnline: 2238 Rotators  polygon_h.fos  |
| [polygon_towns.fos](polygon_towns.fos.md) |  FOnline: 2238 Rotators  polygon_towns.fos  |
| [prices_server_client.fos](prices_server_client.fos.md) |  FOnline: 2238 Rotators  prices_server_client.fos  |
| [prod_barrel_junk.fos](prod_barrel_junk.fos.md) |  FOnline: 2238 Rotators  prod_barrel_junk.fos  |
| [prod_broc_flower.fos](prod_broc_flower.fos.md) |  FOnline: 2238 Rotators  prod_broc_flower.fos  |
| [prod_chemicals.fos](prod_chemicals.fos.md) |  FOnline: 2238 Rotators  prod_chemicals.fos  |
| [prod_computer.fos](prod_computer.fos.md) |  FOnline: 2238 Rotators  prod_computer.fos  |
| [prod_flint.fos](prod_flint.fos.md) |  FOnline: 2238 Rotators  prod_flint.fos  |
| [prod_generic.fos](prod_generic.fos.md) |  FOnline: 2238 Rotators  prod_generic.fos  |
| [prod_ingredients.fos](prod_ingredients.fos.md) |  FOnline: 2238 Rotators  prod_ingredients.fos  |
| [prod_ingredients_h.fos](prod_ingredients_h.fos.md) |  FOnline: 2238 Rotators  prod_ingredients_h.fos  |
| [prod_machine.fos](prod_machine.fos.md) |  FOnline: 2238 Rotators  prod_machine.fos  |
| [prod_mine_h.fos](prod_mine_h.fos.md) |  FOnline: 2238 Rotators  prod_mine_h.fos  |
| [prod_nukacola.fos](prod_nukacola.fos.md) |  FOnline: 2238 Rotators  prod_nukacola.fos  |
| [prod_plant_barley.fos](prod_plant_barley.fos.md) |  FOnline: 2238 Rotators  prod_plant_barley.fos  |
| [prod_plant_fiber.fos](prod_plant_fiber.fos.md) |  FOnline: 2238 Rotators  prod_plant_fiber.fos  |
| [prod_plant_fruit.fos](prod_plant_fruit.fos.md) |  FOnline: 2238 Rotators  prod_plant_fruit.fos  |
| [prod_plant_h.fos](prod_plant_h.fos.md) |  FOnline: 2238 Rotators  prod_plant_h.fos  |
| [prod_plant_tobacco.fos](prod_plant_tobacco.fos.md) |  FOnline: 2238 Rotators  prod_plant_tobacco.fos  |
| [prod_rocks_minerals.fos](prod_rocks_minerals.fos.md) |  FOnline: 2238 Rotators  prod_rocks_minerals.fos  |
| [prod_rocks_ore.fos](prod_rocks_ore.fos.md) |  FOnline: 2238 Rotators  prod_rocks_ore.fos  |
| [prod_rocks_uranium.fos](prod_rocks_uranium.fos.md) |  FOnline: 2238 Rotators  prod_rocks_uranium.fos  |
| [prod_scavenge.fos](prod_scavenge.fos.md) |  !!! IMPORTANT !!! change PROD_REGEN_TIME value after tests  |
| [prod_still_rotgut.fos](prod_still_rotgut.fos.md) |  FOnline: 2238 Rotators  prod_still_rotgut.fos  |
| [prod_table_brahmin.fos](prod_table_brahmin.fos.md) |  FOnline: 2238 Rotators  prod_table_brahmin.fos  |
| [prod_tree_firewood.fos](prod_tree_firewood.fos.md) |  FOnline: 2238 Rotators  prod_tree_firewood.fos  |
| [prod_veins.fos](prod_veins.fos.md) |  FOnline: 2238 Rotators  prod_veins.fos  |
| [prod_xander_root.fos](prod_xander_root.fos.md) |  FOnline: 2238 Rotators  prod_xander_root.fos  |
| [production.fos](production.fos.md) |  FOnline: 2238 Rotators  production.fos  |
| [production_h.fos](production_h.fos.md) |  FOnline: 2238 Rotators  production_h.fos  |
| [prospect_guard.fos](prospect_guard.fos.md) |  FOnline: 2238 Rotators  prospect_guard.fos  |
| [prospect_miner.fos](prospect_miner.fos.md) |  FOnline: 2238 Rotators  prospect_miner.fos  |
| [prospect_owner.fos](prospect_owner.fos.md) |  FOnline: 2238 Rotators  prospect_owner.fos  |
| [prospects.fos](prospects.fos.md) |  FOnline: 2238 Rotators  prospects.fos  |
| [quest_advent.fos](quest_advent.fos.md) |  |
| [quest_advent2.fos](quest_advent2.fos.md) |  |
| [quest_advent3.fos](quest_advent3.fos.md) |  |
| [quest_advent4.fos](quest_advent4.fos.md) |  |
| [quest_advent5.fos](quest_advent5.fos.md) |  |
| [quest_advent6.fos](quest_advent6.fos.md) |  |
| [quest_advent7.fos](quest_advent7.fos.md) |  |
| [quest_bos_initiate.fos](quest_bos_initiate.fos.md) |  FOnline: 2238 Rotators  quest_bos_initiate.fos  |
| [quest_boss1.fos](quest_boss1.fos.md) |  |
| [quest_boss10.fos](quest_boss10.fos.md) |  |
| [quest_boss11.fos](quest_boss11.fos.md) |  |
| [quest_boss12.fos](quest_boss12.fos.md) |  |
| [quest_boss13.fos](quest_boss13.fos.md) |  |
| [quest_boss14.fos](quest_boss14.fos.md) |  |
| [quest_boss1sim.fos](quest_boss1sim.fos.md) |  |
| [quest_boss2.fos](quest_boss2.fos.md) |  |
| [quest_boss3.fos](quest_boss3.fos.md) |  |
| [quest_boss4.fos](quest_boss4.fos.md) |  |
| [quest_boss5.fos](quest_boss5.fos.md) |  |
| [quest_boss6.fos](quest_boss6.fos.md) |  |
| [quest_boss7.fos](quest_boss7.fos.md) |  |
| [quest_boss8.fos](quest_boss8.fos.md) |  |
| [quest_boss9.fos](quest_boss9.fos.md) |  |
| [quest_caesar_train.fos](quest_caesar_train.fos.md) |  FOnline: 2238 Rotators  quest_caesar_train.fos  |
| [quest_caravan_box.fos](quest_caravan_box.fos.md) |  FOnline: 2238 Rotators  quest_caravan_box.fos  |
| [quest_cop.fos](quest_cop.fos.md) |  |
| [quest_copsim.fos](quest_copsim.fos.md) |  |
| [quest_courier_boxes.fos](quest_courier_boxes.fos.md) |  FOnline: 2238 Rotators  quest_courier_boxes.fos  |
| [quest_dailycopboss.fos](quest_dailycopboss.fos.md) |  |
| [quest_dailyfarm1.fos](quest_dailyfarm1.fos.md) |  |
| [quest_drug1.fos](quest_drug1.fos.md) |  |
| [quest_drug2.fos](quest_drug2.fos.md) |  |
| [quest_drug3.fos](quest_drug3.fos.md) |  |
| [quest_evil.fos](quest_evil.fos.md) |  |
| [quest_first_tent.fos](quest_first_tent.fos.md) |  FOnline: 2238 Rotators  quest_first_tent.fos  |
| [quest_floaters.fos](quest_floaters.fos.md) |  |
| [quest_fota.fos](quest_fota.fos.md) |  |
| [quest_hub_sad_farmer.fos](quest_hub_sad_farmer.fos.md) |  |
| [quest_hubo.fos](quest_hubo.fos.md) |  |
| [quest_inde1.fos](quest_inde1.fos.md) |  |
| [quest_inde2.fos](quest_inde2.fos.md) |  |
| [quest_inde3.fos](quest_inde3.fos.md) |  |
| [quest_indea.fos](quest_indea.fos.md) |  |
| [quest_indeb.fos](quest_indeb.fos.md) |  |
| [quest_indec.fos](quest_indec.fos.md) |  |
| [quest_jarok.fos](quest_jarok.fos.md) |  |
| [quest_jarok1.fos](quest_jarok1.fos.md) |  |
| [quest_killmobs_h.fos](quest_killmobs_h.fos.md) |  FOnline: 2238 Rotators  quest_killmobs_h.fos  |
| [quest_la_dogs.fos](quest_la_dogs.fos.md) |  FOnline: 2238 Rotators  quest_la_dogs.fos  |
| [quest_la_gunr_caravan.fos](quest_la_gunr_caravan.fos.md) |  FOnline: 2238 Rotators  quest_la_gunr_caravan.fos  |
| [quest_la_warehouse.fos](quest_la_warehouse.fos.md) |  FOnline: 2238 Rotators  quest_la_warehouse.fos  |
| [quest_loan.fos](quest_loan.fos.md) |  |
| [quest_loansim.fos](quest_loansim.fos.md) |  |
| [quest_morm.fos](quest_morm.fos.md) |  |
| [quest_mutar.fos](quest_mutar.fos.md) |  |
| [quest_mutarsim.fos](quest_mutarsim.fos.md) |  |
| [quest_noire1.fos](quest_noire1.fos.md) |  |
| [quest_noire2.fos](quest_noire2.fos.md) |  |
| [quest_noire3.fos](quest_noire3.fos.md) |  |
| [quest_noire4.fos](quest_noire4.fos.md) |  |
| [quest_noire5.fos](quest_noire5.fos.md) |  |
| [quest_noire6.fos](quest_noire6.fos.md) |  |
| [quest_noire7.fos](quest_noire7.fos.md) |  |
| [quest_noire8.fos](quest_noire8.fos.md) |  |
| [quest_pending.fos](quest_pending.fos.md) |  |
| [quest_skyt.fos](quest_skyt.fos.md) |  |
| [questpool.fos](questpool.fos.md) |  FOnline: 2238 Rotators  questpool.fos  |
| [quests.fos](quests.fos.md) |  FOnline: 2238 Rotators  quests.fos  |
| [radiation.fos](radiation.fos.md) |  FOnline: 2238 Rotators  radiation.fos  |
| [radio.fos](radio.fos.md) |  FOnline: 2238 Rotators  radio.fos  |
| [raiders_attack.fos](raiders_attack.fos.md) |  FOnline: 2238 Rotators  raiders_attack.fos  |
| [raiders_gomes.fos](raiders_gomes.fos.md) |  FOnline: 2238 Rotators  raiders_gomes.fos  |
| [random_quests_h.fos](random_quests_h.fos.md) |  FOnline: 2238 Rotators  random_quests_h.fos  |
| [recycler.fos](recycler.fos.md) |  FOnline: 2238 Rotators  recycler.fos  |
| [recycler_h.fos](recycler_h.fos.md) |  FOnline: 2238 Rotators  recycler_h.fos  |
| [redd_marion.fos](redd_marion.fos.md) |  FOnline: 2238 Rotators  redd_marion.fos  |
| [reinforcements.fos](reinforcements.fos.md) |  FOnline: 2238 Rotators  reinforcements.fos  |
| [reinforcements_h.fos](reinforcements_h.fos.md) |  FOnline: 2238 Rotators  reinforcements_h.fos  |
| [repair.fos](repair.fos.md) |  FOnline: 2238 Rotators  repair.fos  |
| [replication.fos](replication.fos.md) |  |
| [replication_hell.fos](replication_hell.fos.md) |  |
| [reputations.fos](reputations.fos.md) |  FOnline: 2238 Rotators  reputations.fos  |
| [reputations_h.fos](reputations_h.fos.md) |  FOnline: 2238 Rotators  reputations_h.fos  |
| [reputations_modifiers.fos](reputations_modifiers.fos.md) |  FOnline: 2238 Rotators  reputations_modifiers.fos  |
| [reputations_tables.fos](reputations_tables.fos.md) |  FOnline: 2238 Rotators  reputations_tables.fos  |
| [rq_cave.fos](rq_cave.fos.md) |  FOnline: 2238 Rotators  rq_cave.fos  |
| [rq_fetcher.fos](rq_fetcher.fos.md) |  FOnline: 2238 Rotators  rq_fetcher.fos  |
| [scenario_mfc_craft.fos](scenario_mfc_craft.fos.md) |  FOnline: 2238 Rotators  scenario_mfc_craft.fos  |
| [scenery.fos](scenery.fos.md) |  FOnline: 2238 Rotators  scenery.fos  |
| [scypior_radiation.fos](scypior_radiation.fos.md) |  FOnline: 2238 Rotators  scypior_radiation.fos  |
| [scypior_radiation_h.fos](scypior_radiation_h.fos.md) |  FOnline: 2238 Rotators  scypior_radiation_h.fos  |
| [se_door.fos](se_door.fos.md) |  FOnline: 2238 Rotators  se_door.fos  |
| [serializator.fos](serializator.fos.md) |  FOnline: 2238 Rotators  serializator.fos  |
| [server_fixboy.fos](server_fixboy.fos.md) |  FOnline: 2238 Rotators  server_fixboy.fos  |
| [setentry.fos](setentry.fos.md) |  FOnline: 2238 Rotators  setentry.fos  |
| [show.fos](show.fos.md) |  FOnline: 2238 Rotators  show.fos  |
| [shuffling_spawner.fos](shuffling_spawner.fos.md) |  FOnline: 2238 Rotators  shuffling_spawner.fos  |
| [skills.fos](skills.fos.md) |  FOnline: 2238 Rotators  skills.fos  |
| [slaverun.fos](slaverun.fos.md) |  FOnline: 2238 Rotators  slaverun.fos  |
| [slaverun_dialog.fos](slaverun_dialog.fos.md) |  FOnline: 2238 Rotators  slaverun_dialog.fos  |
| [slaverun_h.fos](slaverun_h.fos.md) |  FOnline: 2238 Rotators  slaverun_h.fos  |
| [slaverun_init.fos](slaverun_init.fos.md) |  FOnline: 2238 Rotators  slaverun_init.fos  |
| [slaverun_slave_hostile.fos](slaverun_slave_hostile.fos.md) |  FOnline: 2238 Rotators  slaverun_slave_hostile.fos  |
| [slaverun_slave_normal.fos](slaverun_slave_normal.fos.md) |  FOnline: 2238 Rotators  slaverun_slave_normal.fos  |
| [slaverun_slaver.fos](slaverun_slaver.fos.md) |  FOnline: 2238 Rotators  slaverun_slaver.fos  |
| [slots.fos](slots.fos.md) | Slots by Kilgore |
| [spawner_container.fos](spawner_container.fos.md) |  FOnline: 2238 Rotators  spawner_container.fos  |
| [spawner_container_h.fos](spawner_container_h.fos.md) |  FOnline: 2238 Rotators  spawner_container_h.fos  |
| [spawner_nc.fos](spawner_nc.fos.md) |  --- SPAWNER FOR NOOB CAMP --- |
| [spawner_ntown.fos](spawner_ntown.fos.md) |  --- SPAWNER FOR UNSAFE TOWNS --- |
| [spawner_pvp.fos](spawner_pvp.fos.md) |  |
| [spawner_town.fos](spawner_town.fos.md) |  --- SPAWNER FOR SAFE TOWNS --- |
| [special_map_objects.fos](special_map_objects.fos.md) |  FOnline: 2238 Rotators  special_map_objects.fos  |
| [special_map_objects_floor.fos](special_map_objects_floor.fos.md) |  FOnline: 2238 Rotators  special_map_objects_floor.fos  |
| [special_map_objects_forcefield.fos](special_map_objects_forcefield.fos.md) |  FOnline: 2238 Rotators  special_map_objects_forcefield.fos  |
| [special_map_objects_steam.fos](special_map_objects_steam.fos.md) |  FOnline: 2238 Rotators  special_map_objects_steam.fos  |
| [sprite.fos](sprite.fos.md) |  FOnline: 2238 Rotators  sprite.fos  |
| [strtoint.fos](strtoint.fos.md) |  FOnline: 2238 Rotators  strtoint.fos  |
| [strtoint_h.fos](strtoint_h.fos.md) |  FOnline: 2238 Rotators  strtoint_h.fos  |
| [survival.fos](survival.fos.md) |  |
| [survivalclowns.fos](survivalclowns.fos.md) |  |
| [survivalfloat.fos](survivalfloat.fos.md) |  |
| [survivalgeckos.fos](survivalgeckos.fos.md) |  |
| [survivalrats.fos](survivalrats.fos.md) |  |
| [survivalzombies.fos](survivalzombies.fos.md) |  |
| [talchem.fos](talchem.fos.md) |  FOnline: 2238 Rotators  talchem.fos  |
| [tasks.fos](tasks.fos.md) |  FOnline: 2238 Rotators  tasks.fos  |
| [teslaRecharge.fos](teslaRecharge.fos.md) |  |
| [tests_astl.fos](tests_astl.fos.md) |  FOnline: 2238 Rotators  tests_astl.fos  |
| [throwing.fos](throwing.fos.md) |  FOnline: 2238 Rotators  throwing.fos  |
| [time.fos](time.fos.md) |  FOnline: 2238 Rotators  time.fos  |
| [town.fos](town.fos.md) |  FOnline: 2238 Rotators  town.fos  |
| [town_h.fos](town_h.fos.md) |  FOnline: 2238 Rotators  town_h.fos  |
| [town_militia.fos](town_militia.fos.md) |  FOnline: 2238 Rotators  town_militia.fos  |
| [towns.fos](towns.fos.md) |  FOnline: 2238 Rotators  towns.fos  |
| [tracking.fos](tracking.fos.md) |  FOnline: 2238 Rotators  tracking.fos  |
| [trader.fos](trader.fos.md) |  FOnline: 2238 Rotators  trader.fos  |
| [trader_container.fos](trader_container.fos.md) |  FOnline: 2238 Rotators  trader_container.fos  |
| [trader_h.fos](trader_h.fos.md) |  FOnline: 2238 Rotators  trader_h.fos  |
| [trader_mcgrew.fos](trader_mcgrew.fos.md) |  FOnline: 2238 Rotators  trader_mcgrew.fos  |
| [trains.fos](trains.fos.md) |  FOnline: 2238 Rotators  trains.fos  |
| [traps.fos](traps.fos.md) |  FOnline: 2238 Rotators  traps.fos  |
| [traps_h.fos](traps_h.fos.md) |  FOnline: 2238 Rotators  traps_h.fos  |
| [triggers.fos](triggers.fos.md) |  FOnline: 2238 Rotators  triggers.fos  |
| [triggers_funcs.fos](triggers_funcs.fos.md) |  FOnline: 2238 Rotators  triggers_funcs.fos  |
| [triggers_h.fos](triggers_h.fos.md) |  FOnline: 2238 Rotators  triggers_h.fos  |
| [unsafe_client.fos](unsafe_client.fos.md) |  FOnline: 2238 Rotators  unsafe_client.fos  |
| [utils.fos](utils.fos.md) |  FOnline: 2238 Rotators  utils.fos  |
| [utils_for_array.fos](utils_for_array.fos.md) |  FOnline: 2238 Rotators  utils_for_array.fos  |
| [utils_h.fos](utils_h.fos.md) |  FOnline: 2238 Rotators  utils_h.fos  |
| [wandering_ghoul.fos](wandering_ghoul.fos.md) |  FOnline: 2238 Rotators  wandering_ghoul.fos  |
| [watcher.fos](watcher.fos.md) |  FOnline: 2238 Rotators  watcher.fos  |
| [weap_anim_table.fos](weap_anim_table.fos.md) |  FOnline: 2238 Rotators  weap_anim_table.fos  |
| [weap_anim_table_h.fos](weap_anim_table_h.fos.md) |  FOnline: 2238 Rotators  weap_anim_table_h.fos  |
| [workbench.fos](workbench.fos.md) |  FOnline: 2238 Rotators  workbench.fos  |
| [world_common.fos](world_common.fos.md) |  FOnline: 2238 Rotators  world_common.fos  |
| [world_common_h.fos](world_common_h.fos.md) |  FOnline: 2238 Rotators  world_common_h.fos  |
| [worldmap.fos](worldmap.fos.md) |  FOnline: Reloaded   worldmap.fos  |
| [worldmap_data.fos](worldmap_data.fos.md) |  FOnline: 2238 Rotators  worldmap_data.fos  |
| [worldmap_h.fos](worldmap_h.fos.md) |  FOnline: 2238 Rotators  worldmap_h.fos  |
| [worldmap_players.fos](worldmap_players.fos.md) |  FOnline: 2238 Rotators  worldmap_players.fos  |
| [zzz.fos](zzz.fos.md) |  FOnline: 2238 Rotators  zzz.fos  |
