# Effects

## Table of Content

* [CHARACTER](#effects-for-scope-character)
* [COUNTRY](#effects-for-scope-country)
* [INDUSTRIAL_ORG](#effects-for-scope-industrial_org)
* [OPERATION](#effects-for-scope-operation)
* [PURCHASE_CONTRACT](#effects-for-scope-purchase_contract)
* [RAID_INSTANCE](#effects-for-scope-raid_instance)
* [SPECIAL_PROJECT](#effects-for-scope-special_project)
* [STATE](#effects-for-scope-state)
* [STRATEGIC_REGION](#effects-for-scope-strategic_region)
* [any](#effects-for-scope-any)

## Effects for scope CHARACTER

* [add_advisor_role](#add_advisor_role)
* [add_attack](#add_attack)
* [add_coordination](#add_coordination)
* [add_corps_commander_role](#add_corps_commander_role)
* [add_country_leader_role](#add_country_leader_role)
* [add_country_leader_trait](#add_country_leader_trait)
* [add_defense](#add_defense)
* [add_dynamic_modifier](#add_dynamic_modifier)
* [add_field_marshal_role](#add_field_marshal_role)
* [add_logistics](#add_logistics)
* [add_maneuver](#add_maneuver)
* [add_max_trait](#add_max_trait)
* [add_nationality](#add_nationality)
* [add_naval_commander_role](#add_naval_commander_role)
* [add_planning](#add_planning)
* [add_random_trait](#add_random_trait)
* [add_scientist_level](#add_scientist_level)
* [add_scientist_role](#add_scientist_role)
* [add_scientist_trait](#add_scientist_trait)
* [add_scientist_xp](#add_scientist_xp)
* [add_skill_level](#add_skill_level)
* [add_temporary_buff_to_units](#add_temporary_buff_to_units)
* [add_timed_unit_leader_trait](#add_timed_unit_leader_trait)
* [add_trait](#add_trait)
* [add_unit_leader_trait](#add_unit_leader_trait)
* [boost_planning](#boost_planning)
* [capture_operative](#capture_operative)
* [clr_character_flag](#clr_character_flag)
* [clr_unit_leader_flag](#clr_unit_leader_flag)
* [demote_leader](#demote_leader)
* [force_operative_leader_into_hiding](#force_operative_leader_into_hiding)
* [force_update_dynamic_modifier](#force_update_dynamic_modifier)
* [free_operative](#free_operative)
* [gain_xp](#gain_xp)
* [harm_operative_leader](#harm_operative_leader)
* [injure_scientist_for_days](#injure_scientist_for_days)
* [kill_operative](#kill_operative)
* [modify_character_flag](#modify_character_flag)
* [modify_unit_leader_flag](#modify_unit_leader_flag)
* [operative_leader_event](#operative_leader_event)
* [print_variables](#print_variables)
* [promote_character](#promote_character)
* [promote_leader](#promote_leader)
* [remove_advisor_role](#remove_advisor_role)
* [remove_country_leader_role](#remove_country_leader_role)
* [remove_country_leader_trait](#remove_country_leader_trait)
* [remove_dynamic_modifier](#remove_dynamic_modifier)
* [remove_exile_tag](#remove_exile_tag)
* [remove_scientist_role](#remove_scientist_role)
* [remove_trait](#remove_trait)
* [remove_unit_leader](#remove_unit_leader)
* [remove_unit_leader_role](#remove_unit_leader_role)
* [remove_unit_leader_trait](#remove_unit_leader_trait)
* [replace_unit_leader_trait](#replace_unit_leader_trait)
* [retire](#retire)
* [set_can_be_fired_in_advisor_role](#set_can_be_fired_in_advisor_role)
* [set_character_flag](#set_character_flag)
* [set_character_name](#set_character_name)
* [set_leader_description](#set_leader_description)
* [set_leader_name](#set_leader_name)
* [set_leader_portrait](#set_leader_portrait)
* [set_nationality](#set_nationality)
* [set_portraits](#set_portraits)
* [set_unit_leader_flag](#set_unit_leader_flag)
* [supply_units](#supply_units)
* [swap_country_leader_traits](#swap_country_leader_traits)
* [turn_operative](#turn_operative)
* [unit_leader_event](#unit_leader_event)

## Effects for scope COUNTRY

* [activate_advisor](#activate_advisor)
* [activate_decision](#activate_decision)
* [activate_mission](#activate_mission)
* [activate_mission_tooltip](#activate_mission_tooltip)
* [activate_shine_on_focus](#activate_shine_on_focus)
* [activate_targeted_decision](#activate_targeted_decision)
* [add_ace](#add_ace)
* [add_advisor_role](#add_advisor_role)
* [add_ai_strategy](#add_ai_strategy)
* [add_autonomy_ratio](#add_autonomy_ratio)
* [add_autonomy_score](#add_autonomy_score)
* [add_breakthrough_points](#add_breakthrough_points)
* [add_breakthrough_progress](#add_breakthrough_progress)
* [add_cic](#add_cic)
* [add_civil_war_target](#add_civil_war_target)
* [add_collaboration](#add_collaboration)
* [add_command_power](#add_command_power)
* [add_contested_owner](#add_contested_owner)
* [add_corps_commander_role](#add_corps_commander_role)
* [add_country_leader_role](#add_country_leader_role)
* [add_country_leader_trait](#add_country_leader_trait)
* [add_days_mission_timeout](#add_days_mission_timeout)
* [add_days_remove](#add_days_remove)
* [add_decryption](#add_decryption)
* [add_design_template_bonus](#add_design_template_bonus)
* [add_doctrine_cost_reduction](#add_doctrine_cost_reduction)
* [add_dynamic_modifier](#add_dynamic_modifier)
* [add_equipment_bonus](#add_equipment_bonus)
* [add_equipment_production](#add_equipment_production)
* [add_equipment_subsidy](#add_equipment_subsidy)
* [add_equipment_to_stockpile](#add_equipment_to_stockpile)
* [add_field_marshal_role](#add_field_marshal_role)
* [add_fuel](#add_fuel)
* [add_ideas](#add_ideas)
* [add_intel](#add_intel)
* [add_legitimacy](#add_legitimacy)
* [add_manpower](#add_manpower)
* [add_mines](#add_mines)
* [add_mio_policy_cooldown](#add_mio_policy_cooldown)
* [add_mio_policy_cost](#add_mio_policy_cost)
* [add_named_threat](#add_named_threat)
* [add_naval_commander_role](#add_naval_commander_role)
* [add_nuclear_bombs](#add_nuclear_bombs)
* [add_offsite_building](#add_offsite_building)
* [add_operation_token](#add_operation_token)
* [add_opinion_modifier](#add_opinion_modifier)
* [add_political_power](#add_political_power)
* [add_popularity](#add_popularity)
* [add_relation_modifier](#add_relation_modifier)
* [add_relation_rule_override](#add_relation_rule_override)
* [add_research_slot](#add_research_slot)
* [add_resource](#add_resource)
* [add_scaled_political_power](#add_scaled_political_power)
* [add_scientist_role](#add_scientist_role)
* [add_stability](#add_stability)
* [add_state_claim](#add_state_claim)
* [add_state_core](#add_state_core)
* [add_tech_bonus](#add_tech_bonus)
* [add_threat](#add_threat)
* [add_timed_idea](#add_timed_idea)
* [add_to_faction](#add_to_faction)
* [add_to_tech_sharing_group](#add_to_tech_sharing_group)
* [add_to_war](#add_to_war)
* [add_trait](#add_trait)
* [add_unit_bonus](#add_unit_bonus)
* [add_units_to_division_template](#add_units_to_division_template)
* [add_war_support](#add_war_support)
* [ai_message](#ai_message)
* [air_experience](#air_experience)
* [annex_country](#annex_country)
* [army_experience](#army_experience)
* [become_exiled_in](#become_exiled_in)
* [break_embargo](#break_embargo)
* [capture_operative](#capture_operative)
* [career_profile_step_missiolini](#career_profile_step_missiolini)
* [character_list_tooltip](#character_list_tooltip)
* [clear_division_template_cap](#clear_division_template_cap)
* [clear_rule](#clear_rule)
* [clr_country_flag](#clr_country_flag)
* [complete_national_focus](#complete_national_focus)
* [complete_special_project](#complete_special_project)
* [country_event](#country_event)
* [country_lock_all_division_template](#country_lock_all_division_template)
* [create_colonial_division_template](#create_colonial_division_template)
* [create_corps_commander](#create_corps_commander)
* [create_country_leader](#create_country_leader)
* [create_equipment_variant](#create_equipment_variant)
* [create_faction](#create_faction)
* [create_field_marshal](#create_field_marshal)
* [create_import](#create_import)
* [create_intelligence_agency](#create_intelligence_agency)
* [create_navy_leader](#create_navy_leader)
* [create_operative_leader](#create_operative_leader)
* [create_production_license](#create_production_license)
* [create_ship](#create_ship)
* [create_wargoal](#create_wargoal)
* [damage_building](#damage_building)
* [deactivate_advisor](#deactivate_advisor)
* [deactivate_shine_on_focus](#deactivate_shine_on_focus)
* [declare_war_on](#declare_war_on)
* [delete_unit](#delete_unit)
* [delete_unit_template_and_units](#delete_unit_template_and_units)
* [delete_units](#delete_units)
* [destroy_ships](#destroy_ships)
* [diplomatic_relation](#diplomatic_relation)
* [dismantle_faction](#dismantle_faction)
* [division_template](#division_template)
* [drop_cosmetic_tag](#drop_cosmetic_tag)
* [end_exile](#end_exile)
* [end_puppet](#end_puppet)
* [every_allied_country](#every_allied_country)
* [every_army_leader](#every_army_leader)
* [every_character](#every_character)
* [every_controlled_state](#every_controlled_state)
* [every_core_state](#every_core_state)
* [every_country_division](#every_country_division)
* [every_country_with_original_tag](#every_country_with_original_tag)
* [every_enemy_country](#every_enemy_country)
* [every_military_industrial_organization](#every_military_industrial_organization)
* [every_navy_leader](#every_navy_leader)
* [every_neighbor_country](#every_neighbor_country)
* [every_occupied_country](#every_occupied_country)
* [every_operative](#every_operative)
* [every_other_country](#every_other_country)
* [every_owned_state](#every_owned_state)
* [every_subject_country](#every_subject_country)
* [every_unit_leader](#every_unit_leader)
* [force_update_dynamic_modifier](#force_update_dynamic_modifier)
* [free_operative](#free_operative)
* [free_random_operative](#free_random_operative)
* [generate_character](#generate_character)
* [generate_scientist_character](#generate_scientist_character)
* [get_highest_scored_country](#get_highest_scored_country)
* [get_highest_scored_country_temp](#get_highest_scored_country_temp)
* [get_sorted_scored_countries](#get_sorted_scored_countries)
* [get_sorted_scored_countries_temp](#get_sorted_scored_countries_temp)
* [get_supply_vehicles](#get_supply_vehicles)
* [get_supply_vehicles_temp](#get_supply_vehicles_temp)
* [give_guarantee](#give_guarantee)
* [give_market_access](#give_market_access)
* [give_military_access](#give_military_access)
* [give_resource_rights](#give_resource_rights)
* [global_every_army_leader](#global_every_army_leader)
* [goto_province](#goto_province)
* [hold_election](#hold_election)
* [inherit_technology](#inherit_technology)
* [kill_country_leader](#kill_country_leader)
* [kill_ideology_leader](#kill_ideology_leader)
* [kill_operative](#kill_operative)
* [launch_nuke](#launch_nuke)
* [leave_faction](#leave_faction)
* [load_focus_tree](#load_focus_tree)
* [load_oob](#load_oob)
* [mark_focus_tree_layout_dirty](#mark_focus_tree_layout_dirty)
* [mark_technology_tree_layout_dirty](#mark_technology_tree_layout_dirty)
* [modify_building_resources](#modify_building_resources)
* [modify_country_flag](#modify_country_flag)
* [modify_tech_sharing_bonus](#modify_tech_sharing_bonus)
* [modify_timed_idea](#modify_timed_idea)
* [navy_experience](#navy_experience)
* [news_event](#news_event)
* [party_leader](#party_leader)
* [print_variables](#print_variables)
* [promote_character](#promote_character)
* [puppet](#puppet)
* [random_allied_country](#random_allied_country)
* [random_army_leader](#random_army_leader)
* [random_character](#random_character)
* [random_controlled_state](#random_controlled_state)
* [random_core_state](#random_core_state)
* [random_country_division](#random_country_division)
* [random_enemy_country](#random_enemy_country)
* [random_military_industrial_organization](#random_military_industrial_organization)
* [random_navy_leader](#random_navy_leader)
* [random_neighbor_country](#random_neighbor_country)
* [random_occupied_country](#random_occupied_country)
* [random_operative](#random_operative)
* [random_owned_controlled_state](#random_owned_controlled_state)
* [random_owned_state](#random_owned_state)
* [random_purchase_contract](#random_purchase_contract)
* [random_subject_country](#random_subject_country)
* [random_unit_leader](#random_unit_leader)
* [recall_attache](#recall_attache)
* [recall_volunteers_from](#recall_volunteers_from)
* [recruit_character](#recruit_character)
* [release](#release)
* [release_autonomy](#release_autonomy)
* [release_on_controlled](#release_on_controlled)
* [release_puppet](#release_puppet)
* [release_puppet_on_controlled](#release_puppet_on_controlled)
* [remove_advisor_role](#remove_advisor_role)
* [remove_building](#remove_building)
* [remove_civil_war_target](#remove_civil_war_target)
* [remove_contested_owner](#remove_contested_owner)
* [remove_country_leader_role](#remove_country_leader_role)
* [remove_country_leader_trait](#remove_country_leader_trait)
* [remove_decision](#remove_decision)
* [remove_decision_on_cooldown](#remove_decision_on_cooldown)
* [remove_dynamic_modifier](#remove_dynamic_modifier)
* [remove_from_faction](#remove_from_faction)
* [remove_from_tech_sharing_group](#remove_from_tech_sharing_group)
* [remove_ideas](#remove_ideas)
* [remove_ideas_with_trait](#remove_ideas_with_trait)
* [remove_mission](#remove_mission)
* [remove_operation_token](#remove_operation_token)
* [remove_opinion_modifier](#remove_opinion_modifier)
* [remove_power_balance](#remove_power_balance)
* [remove_relation_modifier](#remove_relation_modifier)
* [remove_relation_rule_override](#remove_relation_rule_override)
* [remove_resource_rights](#remove_resource_rights)
* [remove_scientist_role](#remove_scientist_role)
* [remove_state_claim](#remove_state_claim)
* [remove_state_core](#remove_state_core)
* [remove_targeted_decision](#remove_targeted_decision)
* [remove_trait](#remove_trait)
* [remove_unit_leader](#remove_unit_leader)
* [remove_unit_leader_role](#remove_unit_leader_role)
* [remove_wargoal](#remove_wargoal)
* [reserve_dynamic_country](#reserve_dynamic_country)
* [retire_character](#retire_character)
* [retire_country_leader](#retire_country_leader)
* [retire_ideology_leader](#retire_ideology_leader)
* [reverse_add_opinion_modifier](#reverse_add_opinion_modifier)
* [scoped_play_song](#scoped_play_song)
* [scoped_sound_effect](#scoped_sound_effect)
* [send_embargo](#send_embargo)
* [send_equipment](#send_equipment)
* [send_equipment_fraction](#send_equipment_fraction)
* [set_air_oob](#set_air_oob)
* [set_autonomy](#set_autonomy)
* [set_can_be_fired_in_advisor_role](#set_can_be_fired_in_advisor_role)
* [set_capital](#set_capital)
* [set_character_name](#set_character_name)
* [set_collaboration](#set_collaboration)
* [set_cosmetic_tag](#set_cosmetic_tag)
* [set_country_flag](#set_country_flag)
* [set_country_leader_description](#set_country_leader_description)
* [set_country_leader_ideology](#set_country_leader_ideology)
* [set_country_leader_name](#set_country_leader_name)
* [set_country_leader_portrait](#set_country_leader_portrait)
* [set_division_force_allow_recruiting](#set_division_force_allow_recruiting)
* [set_division_template_cap](#set_division_template_cap)
* [set_division_template_lock](#set_division_template_lock)
* [set_equipment_fraction](#set_equipment_fraction)
* [set_equipment_version_number](#set_equipment_version_number)
* [set_faction_leader](#set_faction_leader)
* [set_faction_name](#set_faction_name)
* [set_faction_spymaster](#set_faction_spymaster)
* [set_fuel](#set_fuel)
* [set_fuel_ratio](#set_fuel_ratio)
* [set_keyed_oob](#set_keyed_oob)
* [set_legitimacy](#set_legitimacy)
* [set_major](#set_major)
* [set_mio_policy_cooldown](#set_mio_policy_cooldown)
* [set_mio_policy_cost](#set_mio_policy_cost)
* [set_nationality](#set_nationality)
* [set_naval_oob](#set_naval_oob)
* [set_occupation_law](#set_occupation_law)
* [set_occupation_law_where_available](#set_occupation_law_where_available)
* [set_oob](#set_oob)
* [set_party_name](#set_party_name)
* [set_party_rule](#set_party_rule)
* [set_political_party](#set_political_party)
* [set_political_power](#set_political_power)
* [set_politics](#set_politics)
* [set_popularities](#set_popularities)
* [set_portraits](#set_portraits)
* [set_power_balance](#set_power_balance)
* [set_province_controller](#set_province_controller)
* [set_relation_rule](#set_relation_rule)
* [set_research_slots](#set_research_slots)
* [set_rule](#set_rule)
* [set_stability](#set_stability)
* [set_state_controller](#set_state_controller)
* [set_state_owner](#set_state_owner)
* [set_technology](#set_technology)
* [set_truce](#set_truce)
* [set_war_support](#set_war_support)
* [show_ideas_tooltip](#show_ideas_tooltip)
* [show_mio_tooltip](#show_mio_tooltip)
* [show_unit_leaders_tooltip](#show_unit_leaders_tooltip)
* [start_civil_war](#start_civil_war)
* [start_peace_conference](#start_peace_conference)
* [state_event](#state_event)
* [steal_random_tech_bonus](#steal_random_tech_bonus)
* [swap_ideas](#swap_ideas)
* [swap_ruler_traits](#swap_ruler_traits)
* [teleport_railway_guns_to_deploy_province](#teleport_railway_guns_to_deploy_province)
* [transfer_navy](#transfer_navy)
* [transfer_ship](#transfer_ship)
* [transfer_state](#transfer_state)
* [transfer_units_fraction](#transfer_units_fraction)
* [turn_operative](#turn_operative)
* [uncomplete_national_focus](#uncomplete_national_focus)
* [unlock_decision_category_tooltip](#unlock_decision_category_tooltip)
* [unlock_decision_tooltip](#unlock_decision_tooltip)
* [unlock_military_industrial_organization_tooltip](#unlock_military_industrial_organization_tooltip)
* [unlock_national_focus](#unlock_national_focus)
* [upgrade_intelligence_agency](#upgrade_intelligence_agency)
* [white_peace](#white_peace)

## Effects for scope INDUSTRIAL_ORG

* [add_mio_design_team_assign_cost](#add_mio_design_team_assign_cost)
* [add_mio_design_team_change_cost](#add_mio_design_team_change_cost)
* [add_mio_funds](#add_mio_funds)
* [add_mio_funds_gain_factor](#add_mio_funds_gain_factor)
* [add_mio_industrial_manufacturer_assign_cost](#add_mio_industrial_manufacturer_assign_cost)
* [add_mio_research_bonus](#add_mio_research_bonus)
* [add_mio_size](#add_mio_size)
* [add_mio_size_up_requirement_factor](#add_mio_size_up_requirement_factor)
* [add_mio_task_capacity](#add_mio_task_capacity)
* [clr_mio_flag](#clr_mio_flag)
* [complete_mio_trait](#complete_mio_trait)
* [modify_mio_flag](#modify_mio_flag)
* [set_mio_design_team_assign_cost](#set_mio_design_team_assign_cost)
* [set_mio_design_team_change_cost](#set_mio_design_team_change_cost)
* [set_mio_flag](#set_mio_flag)
* [set_mio_funds](#set_mio_funds)
* [set_mio_funds_gain_factor](#set_mio_funds_gain_factor)
* [set_mio_icon](#set_mio_icon)
* [set_mio_industrial_manufacturer_assign_cost](#set_mio_industrial_manufacturer_assign_cost)
* [set_mio_name_key](#set_mio_name_key)
* [set_mio_research_bonus](#set_mio_research_bonus)
* [set_mio_size_up_requirement_factor](#set_mio_size_up_requirement_factor)
* [set_mio_task_capacity](#set_mio_task_capacity)
* [unlock_mio_trait_tooltip](#unlock_mio_trait_tooltip)

## Effects for scope OPERATION

* [every_operative](#every_operative)
* [execute_operation_coordinated_strike](#execute_operation_coordinated_strike)
* [random_operative](#random_operative)

## Effects for scope PURCHASE_CONTRACT

* [cancel_purchase_contract](#cancel_purchase_contract)

## Effects for scope RAID_INSTANCE

* [add_raid_history_entry](#add_raid_history_entry)
* [raid_add_unit_experience](#raid_add_unit_experience)
* [raid_damage_units](#raid_damage_units)

## Effects for scope SPECIAL_PROJECT

* [add_dynamic_modifier](#add_dynamic_modifier)
* [add_project_progress_ratio](#add_project_progress_ratio)
* [clr_project_flag](#clr_project_flag)
* [complete_prototype_reward_option](#complete_prototype_reward_option)
* [force_update_dynamic_modifier](#force_update_dynamic_modifier)
* [modify_project_flag](#modify_project_flag)
* [remove_dynamic_modifier](#remove_dynamic_modifier)
* [set_project_flag](#set_project_flag)

## Effects for scope STATE

* [activate_targeted_decision](#activate_targeted_decision)
* [add_building_construction](#add_building_construction)
* [add_claim_by](#add_claim_by)
* [add_compliance](#add_compliance)
* [add_contested_owner](#add_contested_owner)
* [add_core_of](#add_core_of)
* [add_dynamic_modifier](#add_dynamic_modifier)
* [add_extra_state_shared_building_slots](#add_extra_state_shared_building_slots)
* [add_manpower](#add_manpower)
* [add_province_modifier](#add_province_modifier)
* [add_resistance](#add_resistance)
* [add_resistance_target](#add_resistance_target)
* [add_resource](#add_resource)
* [add_state_modifier](#add_state_modifier)
* [cancel_resistance](#cancel_resistance)
* [clr_state_flag](#clr_state_flag)
* [construct_building_in_random_province](#construct_building_in_random_province)
* [damage_building](#damage_building)
* [every_neighbor_state](#every_neighbor_state)
* [every_state_division](#every_state_division)
* [force_disable_resistance](#force_disable_resistance)
* [force_enable_resistance](#force_enable_resistance)
* [force_update_dynamic_modifier](#force_update_dynamic_modifier)
* [modify_state_flag](#modify_state_flag)
* [print_variables](#print_variables)
* [raid_reduce_project_progress_ratio](#raid_reduce_project_progress_ratio)
* [random_neighbor_state](#random_neighbor_state)
* [random_state_division](#random_state_division)
* [remove_building](#remove_building)
* [remove_claim_by](#remove_claim_by)
* [remove_contested_owner](#remove_contested_owner)
* [remove_core_of](#remove_core_of)
* [remove_dynamic_modifier](#remove_dynamic_modifier)
* [remove_province_modifier](#remove_province_modifier)
* [remove_resistance_target](#remove_resistance_target)
* [remove_targeted_decision](#remove_targeted_decision)
* [reset_state_name](#reset_state_name)
* [set_border_war](#set_border_war)
* [set_building_level](#set_building_level)
* [set_compliance](#set_compliance)
* [set_demilitarized_zone](#set_demilitarized_zone)
* [set_faction_name](#set_faction_name)
* [set_garrison_strength](#set_garrison_strength)
* [set_occupation_law](#set_occupation_law)
* [set_occupation_law_where_available](#set_occupation_law_where_available)
* [set_resistance](#set_resistance)
* [set_state_category](#set_state_category)
* [set_state_controller_to](#set_state_controller_to)
* [set_state_flag](#set_state_flag)
* [set_state_name](#set_state_name)
* [set_state_owner_to](#set_state_owner_to)
* [set_state_province_controller](#set_state_province_controller)
* [start_resistance](#start_resistance)
* [state_event](#state_event)
* [teleport_armies](#teleport_armies)
* [transfer_state_to](#transfer_state_to)

## Effects for scope STRATEGIC_REGION

* [add_region_efficiency](#add_region_efficiency)

## Effects for scope any

* [add_power_balance_modifier](#add_power_balance_modifier)
* [add_power_balance_value](#add_power_balance_value)
* [add_to_array](#add_to_array)
* [add_to_temp_array](#add_to_temp_array)
* [add_to_temp_variable](#add_to_temp_variable)
* [add_to_variable](#add_to_variable)
* [add_victory_points](#add_victory_points)
* [build_railway](#build_railway)
* [cancel_border_war](#cancel_border_war)
* [change_tag_from](#change_tag_from)
* [clamp_temp_variable](#clamp_temp_variable)
* [clamp_variable](#clamp_variable)
* [clear_array](#clear_array)
* [clear_global_event_target](#clear_global_event_target)
* [clear_global_event_targets](#clear_global_event_targets)
* [clear_temp_array](#clear_temp_array)
* [clear_variable](#clear_variable)
* [clr_global_flag](#clr_global_flag)
* [create_dynamic_country](#create_dynamic_country)
* [create_entity](#create_entity)
* [create_purchase_contract](#create_purchase_contract)
* [create_railway_gun](#create_railway_gun)
* [create_unit](#create_unit)
* [custom_effect_tooltip](#custom_effect_tooltip)
* [custom_override_tooltip](#custom_override_tooltip)
* [damage_units](#damage_units)
* [destroy_entity](#destroy_entity)
* [divide_temp_variable](#divide_temp_variable)
* [divide_variable](#divide_variable)
* [effect_tooltip](#effect_tooltip)
* [event_option_tooltip](#event_option_tooltip)
* [every_active_scientist](#every_active_scientist)
* [every_country](#every_country)
* [every_possible_country](#every_possible_country)
* [every_purchase_contract](#every_purchase_contract)
* [every_scientist](#every_scientist)
* [every_state](#every_state)
* [finalize_border_war](#finalize_border_war)
* [find_highest_in_array](#find_highest_in_array)
* [find_lowest_in_array](#find_lowest_in_array)
* [for_each_loop](#for_each_loop)
* [for_each_scope_loop](#for_each_scope_loop)
* [for_loop_effect](#for_loop_effect)
* [force_update_map_mode](#force_update_map_mode)
* [goto_state](#goto_state)
* [hidden_effect](#hidden_effect)
* [if](#if)
* [log](#log)
* [meta_effect](#meta_effect)
* [modify_global_flag](#modify_global_flag)
* [modulo_temp_variable](#modulo_temp_variable)
* [modulo_variable](#modulo_variable)
* [multiply_temp_variable](#multiply_temp_variable)
* [multiply_variable](#multiply_variable)
* [play_song](#play_song)
* [random](#random)
* [random_active_scientist](#random_active_scientist)
* [random_country](#random_country)
* [random_country_with_original_tag](#random_country_with_original_tag)
* [random_list](#random_list)
* [random_other_country](#random_other_country)
* [random_scientist](#random_scientist)
* [random_scope_in_array](#random_scope_in_array)
* [random_state](#random_state)
* [randomize_temp_variable](#randomize_temp_variable)
* [randomize_variable](#randomize_variable)
* [randomize_weather](#randomize_weather)
* [remove_all_power_balance_modifiers](#remove_all_power_balance_modifiers)
* [remove_from_array](#remove_from_array)
* [remove_from_temp_array](#remove_from_temp_array)
* [remove_power_balance_modifier](#remove_power_balance_modifier)
* [reset_province_name](#reset_province_name)
* [resize_array](#resize_array)
* [resize_temp_array](#resize_temp_array)
* [round_temp_variable](#round_temp_variable)
* [round_variable](#round_variable)
* [save_event_target_as](#save_event_target_as)
* [save_global_event_target_as](#save_global_event_target_as)
* [set_border_war_data](#set_border_war_data)
* [set_entity_animation](#set_entity_animation)
* [set_entity_movement](#set_entity_movement)
* [set_entity_position](#set_entity_position)
* [set_entity_rotation](#set_entity_rotation)
* [set_entity_scale](#set_entity_scale)
* [set_global_flag](#set_global_flag)
* [set_power_balance_gfx](#set_power_balance_gfx)
* [set_province_name](#set_province_name)
* [set_temp_variable](#set_temp_variable)
* [set_temp_variable_to_random](#set_temp_variable_to_random)
* [set_variable](#set_variable)
* [set_variable_to_random](#set_variable_to_random)
* [set_victory_points](#set_victory_points)
* [sound_effect](#sound_effect)
* [start_border_war](#start_border_war)
* [subtract_from_temp_variable](#subtract_from_temp_variable)
* [subtract_from_variable](#subtract_from_variable)
* [unlock_mio_policy_tooltip](#unlock_mio_policy_tooltip)
* [while_loop_effect](#while_loop_effect)

## activate_advisor

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Place an advisor in their respective role slot

Example:
activate_advisor = GER_character_token_air_chief

```

## activate_decision

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Activates specified decision for scope country
```

## activate_mission

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Activates mission, ignoring its normal trigger conditions. Cannot activate a mission that is already active. 
Example: activate_mission = some_mission_here
```

## activate_mission_tooltip

* Supported Scopes: COUNTRY
* Supported Targets: none

```
shows mission will activate and name. Activation needs to be handled manually, effect is just an easier way to display name of mission.
Example: unlock_mission_tooltip = some_mission_here
```

## activate_shine_on_focus

* Supported Scopes: COUNTRY
* Supported Targets: any

Activates the shine effect on the focus with the given id. Focuses that are completed cannot have an activated shine effect.

Note that tooltips are only shown in debug mode.

### Example:
```
activate_shine_on_focus = GER_prioritize_economic_growth
```


## activate_targeted_decision

* Supported Scopes: STATE, COUNTRY
* Supported Targets: none

```
Activates targeted decisions or mission, ignoring its normal trigger conditions, cooldown and fire only once. Cannot activate if active in interface. 
Example: activate_targeted_decision = { target = TAG/STATE decision = decision_id_here
```

## add_ace

* Supported Scopes: COUNTRY
* Supported Targets: none

```
adds an air ace
```

## add_advisor_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
add advisor role to character
May directly activate (aka hire) using activate = yes

Example:
add_advisor_role = {
	character = "GER_Character_Token" # optional if inside character scope
	advisor = {
		slot = air_chief
		cost = 50
		idea_token = GER_character_token_air_chief
		traits = {
			air_chief_ground_support_2
		}
		allowed = {...}
	}
	activate = yes
}

```

## add_ai_strategy

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Adds strategy entry to country AI
```

## add_attack

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Adds attack skill to a character
Example: add_attack = 1
```

## add_autonomy_ratio

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Adds % freedom score to the autonomy.
Example:
add_autonomy_ratio={
value=0.005
localization="LOC_KEY"
}
```

## add_autonomy_score

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Adds exact freedom score to the autonomy.
Example:
add_autonomy_score={
value=50
localization="LOC_KEY"
}
```

## add_breakthrough_points

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Add breakthrough points to one specialization or all for a country scope.
	ex:
    add_breakthrough_points = {
	  specialization = <sp_specialization_id>
      value = 3
	}
    add_breakthrough_points = {
	  specialization = all
      value = -1
	}
"
```

## add_breakthrough_progress

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"![MD]
Add breakthrough progress to one specialization or all for a country scope.
The value can either be an absolute value or a script constant.

#### Example
Adding 3 breakthrough points to land specialization:
```
add_breakthrough_progress = {
	specialization = specialization_land
    value = 3
}
```
Adding -1 breakthrough points to all specializations:
```
add_breakthrough_progress = {
	specialization = all
    value = -1
}
```
Adding the value of the script constant `sp_breakthrough_progress.medium` to all specializations:
```
add_breakthrough_progress = {
	specialization = all
	value = sp_breakthrough_progress.medium
}
```
"
```

## add_building_construction

* Supported Scopes: STATE
* Supported Targets: none

```
Starts building construction for amount of levels in specified state or province
```

## add_cic

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add founds to the CIC bank of the country in scope.
Value can be negative to substract funds.
If the new total funds is negative, it will be set to 0.
ex:
var:my_country_var = {
  add_cic = 200
  add_cic = -100
}"
```

## add_civil_war_target

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Adds a country as a civil war target (added to both sides)

Example:
add_civil_war_target = TAG
```

## add_claim_by

* Supported Scopes: STATE
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Add state claim by country.
```

## add_collaboration

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Adds the collaboration in a target country with our currently scoped country
GER = {
  add_collaboration = {
    target = POL
    value = 0.3
  }
}

```

## add_command_power

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add command power to country
```

## add_compliance

* Supported Scopes: STATE
* Supported Targets: any

```
add compliance to a state. Example: add_compliance = 30
```

## add_contested_owner

* Supported Scopes: STATE, COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

Adds a contested owner to a state.
The effect can be used either from a country or a state scope and accepts the other as parameter.
The effect is localized with a localization environment containing `Country` and `State`.

### Example
The following example has the same end result and localization.
```
42 = {
	add_contested_owner = GER
}
GER = {
	add_contested_owner = 42
}
```
Standard scope accessors can also be used:
```
### Assuming current scope is a state and FROM is a country scope
add_contested_owner = FROM
```


## add_coordination

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Adds maneuver skill to a unit leader
Example: add_coordination = 1
```

## add_core_of

* Supported Scopes: STATE
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Add state as core of country
```

## add_corps_commander_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
add corps commander role to character

Example:
add_corps_commander_role = {
	character = GER_Character_token # optional if inside character scope
	traits = {  }
	skill = 4
	attack_skill = 2
	defense_skill = 3
	planning_skill = 3
	logistics_skill = 5
	}
}
```

## add_country_leader_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
add country leader role to character

Example:
add_country_leader_role = {
	character = "GER_Character_Token" # optional if inside character scope
	promote_leader = yes
	country_leader = {
		ideology = socialism
		expire = "1965.1.1.1"
		traits = {
			war_industrialist
		}
	}
}

```

## add_country_leader_trait

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
Add country leader trait to the scoped character or scoped country's leader.
In scoped character, will need to give the ideology if the character has several country leader roles.
Example 1: SOV_joseph_stalin = { add_country_leader_trait = underage_monarch }
Example 2: HUN_miklos_horthy = { add_country_leader_trait = { ideology = oligarchism trait = anti_communist } }
Example 3: SOV = { add_country_leader_trait = underage_monarch }
```

## add_days_mission_timeout

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add days to 'mission_timeout' value of a mission
Example:
add_days_mission_timeout  = {
    mission = <some_mission>
    days = 30
}

```

## add_days_remove

* Supported Scopes: COUNTRY
* Supported Targets: none

```
adds/removes days to 'days_remove' value of a decision
Example:
add_days_remove  = {
    decision = <some_decision>
    days = 30
}

```

## add_decryption

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add decryption against a target country. Example:
add_decryption = { 
 target = GER 
 # pick one amount = 1000 # a flat amount to be added
 ratio = 0.3 # a ratio of crypto defense of target to be added

```

## add_defense

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Adds defense skill to a unit leader
Example: add_defense = 1
```

## add_design_template_bonus

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"![MD]
Add free bonus design discount to given types with a set of uses.
The value for uses and cost_factor can either be an absolute value or a script constant.
Can use several equipment types, where 1 is mandatory

#### Example
Adding 40% discount to an equipment type:
```
add_design_template_bonus = {
	uses = 1
    cost_factor = 0.4
	equipment = light_tank_flame_chassis_0
	name = light_flame_chassis_loc
}
```
Adding 40% discount to an equipment type and archetype with scripted constant:
```
add_design_template_bonus = {
	uses = 2
    cost_factor = cost.high
	equipment = light_tank_flame_chassis_0
	equipment = light_tank_chassis
}
```
"
```

## add_divisional_commander_xp

* Supported Scopes: 
* Supported Targets: none

```
add divisional commander xp to unit: add_divisional_commander_xp = 10
```

## add_doctrine_cost_reduction

* Supported Scopes: COUNTRY
* Supported Targets: none

```
adds a limited use cost reduction for doctrines
```

## add_dynamic_modifier

* Supported Scopes: STATE, COUNTRY, CHARACTER, SPECIAL_PROJECT
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"adds a dynamic modifier to the containing scope (country / state / unit-leader / special-project).
Updates the cooldown if exists.
Optionaly you can give a scope that will restrict the dynamic modifier to it.
example :
12 = {
  add_dynamic_modifier = {
    modifier = dynamic_modifier_name
    days = 42 # will be temporary if specified, can be variable
    scope = GER # optional, state/countrytag or a variable containing that. 
				# if specified the dynamic variable will target that scope
				# in this example : adds the modifier to state 12 but only applies for country GER
  }
}"
```

## add_equipment_bonus

* Supported Scopes: COUNTRY
* Supported Targets: none

```
 Adds the specified equipment bonuses to the country. As description the given loc key or the name of given special project will be used. Same usage as in Ideas/National spirits.
Example:
add_equipment_bonus = {
	project = FROM # Optional special project scope for using special project name. If not set, the name will be used.
	bonus = {
		armor = { # Type of equipment
					armor_value = 3 # Bonus to apply to the stats of the equipment type
					soft_attack = 3
					instant = yes # Optional. Default no. If true, the bonus will be applied immediately. Otherwise it will be applied only on new equipment variant creation.
		}
		small_plane_naval_bomber_airframe = {
					air_range = 0.1 naval_strike_attack = 0.1
		}
	}
}

add_equipment_bonus = {
	name = SUPER_BONUS_NAME # Optional loc key to use as name.
	bonus = {
		small_plane_naval_bomber_airframe = {
					air_range = 0.1 naval_strike_attack = 0.1
		}
	}
}
```

## add_equipment_production

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Creates a new production line for the input equipment.
ex:
GER = {
	add_equipment_production = {
			equipment = {
					type = ship_hull_cruiser_submarine
					creator = "ITA"
					version_name = "Cagni Class"
			}
			name = "Ammiraglio Millo"
			requested_factories = 1 #Optional
			progress = 0.35 # Optional
			efficiency = 0.1 # Optional
			amount = 2 # Optional, accepts value or variable
			industrial_manufacturer = mio:generic_mio_organization_ship_submarine # Optional, accepts mio:token, variable or keyword
	}
}
}"
```

## add_equipment_subsidy

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Adds an equipment subsidy to the country in scope.
Example:
GER = {
	add_equipment_subsidy = 
	{
		cic = 100 # Amount of CIC for the subsidy.
		equipment_type = support_equipment # The target archetype of the subsidy
		seller_tags = {RAJ AST} # The possible sellers that this subsidy can apply to. [Mutually exclusive with seller_trigger]
		seller_trigger = scripted_trigger_name # The name of a scripted trigger to check whether to apply the subsidy or not. [Mutually exclusive with seller_tags]
	}
}"
```

## add_equipment_to_stockpile

* Supported Scopes: COUNTRY
* Supported Targets: any

```
Add or remove equipment from country stockpiles.
Example:
add_equipment_to_stockpile = {
	type = strat_bomber_equipment_2
	amount = 100 # May be a variable. Equipment will be removed if the value is negative.
	producer = USA # Optional. If not specified the effect will be applied to all creators.
}
```

## add_extra_state_shared_building_slots

* Supported Scopes: STATE
* Supported Targets: none

```
add extra shared building slot to state
```

## add_field_marshal_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
add field marshall role to character

Example:
add_field_marshal_role = {
	character = GER_Character_token # optional if inside character scope
	traits = {  }
	skill = 4
	attack_skill = 2
	defense_skill = 3
	planning_skill = 3
	logistics_skill = 5
	}
}
```

## add_fuel

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add fuel to the country
```

## add_history_entry

* Supported Scopes: 
* Supported Targets: none

```
add_history_entry = {
key = custom_localized_key
subject = "Custom String (not localized)"
allow = yes/no (allow medal award)
}
```

## add_ideas

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add idea(s) to country
```

## add_intel

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Add the specified amount of intel over a specified country
GER = {
  add_intel = {
    target = POL
    civilian_intel = 3
    army_intel = 1
    # zero field can be omitted
    # navy_intel = 0
    # airforce_intel = 0
  }
}

```

## add_legitimacy

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add_legitimacy = 10. Adds legitimacy to Scope country. Value has to be 0-100.
```

## add_logistics

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Adds logistics skill to a unit leader
Example: add_logistics = 1
```

## add_maneuver

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Adds maneuver skill to a unit leader
Example: add_maneuver = 1
```

## add_manpower

* Supported Scopes: STATE, COUNTRY
* Supported Targets: none

```
Adds manpower to the country in scope or locally on a state if in state scope
```

## add_max_trait

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Adds a max assignable trait slot for a general
Example: add_max_trait = 1
```

## add_mines

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Add mines to a strategic region for scoped country.
 add_mines = { region = 42 amount = 100 }
```

## add_mio_design_team_assign_cost

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add percentage to the daily PP cost to assign to research in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Value can be negative to reduce assign cost but final value cannot be negative (capped at 0, no error raised)
ex:
mio:my_mio = {
  add_mio_design_team_assign_cost = 0.2 # increase by 20%
  add_mio_design_team_assign_cost = -0.1 # reduce by 10%
  add_mio_design_team_assign_cost = var:my_number_var
}"
```

## add_mio_design_team_change_cost

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add percentage to the XP cost to change MIO in equipment designer for the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Value can be negative to reduce assign cost but final value cannot be negative (capped at 0, no error raised).
!!! NOTE that the result is rounded down so that i.e. 5 + 10% is still 5 = 5.5 rounded down !!!
ex:
mio:my_mio = {
  add_mio_design_team_change_cost = 0.2 # increase by 20%
  add_mio_design_team_change_cost = -0.1 # reduce by 10%
  add_mio_design_team_change_cost = var:my_number_var
}"
```

## add_mio_funds

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add funds to the military industrial organization in scope.
Value can be negative to substract funds.
If the new total funds go over the Size Up limit, the MIO will gain size(s).
If the new total funds is negative, it will be capped at 0 without retracting size.
ex:
var:my_mio_var = {
  add_mio_funds = 200
  add_mio_funds = -100
}"
```

## add_mio_funds_gain_factor

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add to the factor applied when gaining funds in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Value can be negative to reduce assign cost but final value cannot be negative (capped at 0, no error raised)
ex:
mio:my_mio = {
  add_mio_funds_gain_factor = 0.2
  add_mio_funds_gain_factor = -0.1
  add_mio_funds_gain_factor = var:my_number_var
}"
```

## add_mio_industrial_manufacturer_assign_cost

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add percentage to the daily PP cost to assign to production line in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Value can be negative to reduce assign cost but final value cannot be negative (capped at 0, no error raised)
ex:
mio:my_mio = {
  add_mio_industrial_manufacturer_assign_cost = 0.2 # increase by 20%
  add_mio_industrial_manufacturer_assign_cost = -0.1 # reduce by 10%
  add_mio_industrial_manufacturer_assign_cost = var:my_number_var
}"
```

## add_mio_policy_cooldown

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Add to the base cooldown (in days) after attaching a policy in the MIO policy, found in country in scope with input policy token.
This changes the base value. Modifiers will still apply over it.
Value can be negative to reduce cost, but final cooldown cannot be negative (capped at 0, no error raised)
ex:
SOV = {
  add_mio_policy_cooldown = {
	policy = my_policy_token
	value = 1
  }
  add_mio_policy_cooldown = {
	policy = my_policy_token
	value = -1
  }
  add_mio_policy_cooldown = {
	policy = my_policy_token
	value = var:my_number_var
  }
}"
```

## add_mio_policy_cost

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Add to the base cost (in PP) for attaching a policy in the MIO policy, found in country in scope with input policy token.
This changes the base value. Modifiers will still apply over it.
Value can be negative to reduce cost, but final cost cannot be negative (capped at 0, no error raised)
ex:
SOV = {
  add_mio_policy_cost = {
	policy = my_policy_token
	value = 1
  }
  add_mio_policy_cost = {
	policy = my_policy_token
	value = -1
  }
  add_mio_policy_cost = {
	policy = my_policy_token
	value = var:my_number_var
  }
}"
```

## add_mio_research_bonus

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add to the research bonus in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Value can be negative to reduce research bonus but final research bonus cannot be negative (capped at 0, no error raised)
ex:
mio:my_mio = {
  add_mio_research_bonus = 0.2
  add_mio_research_bonus = -0.1
  add_mio_research_bonus = var:my_number_var
}"
```

## add_mio_size

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add size levels to the military industrial organization in scope.
Input value cannot be negative.
The MIO will keep the same amount of funds it had before the effect.
ex:
var:my_mio_var = {
  add_mio_size = 2
  add_mio_size = var:my_number_var
}"
```

## add_mio_size_up_requirement_factor

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add to the factor applied to funds required to size up in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Value can be negative to reduce assign cost but final value cannot be negative (capped at 0, no error raised)
ex:
mio:my_mio = {
  add_mio_size_up_requirement_factor = 0.2
  add_mio_size_up_requirement_factor = -0.1
  add_mio_size_up_requirement_factor = var:my_number_var
}"
```

## add_mio_task_capacity

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add to the maximum task capacity in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Value can be negative to reduce capacity, but final capacity cannot be negative (capped at 0, no error raised)
If the capacity is reduced and the MIO becomes over-assigned, the current tasks will be allowed.
It's only later that the player will feel the new restrictions.
ex:
mio:my_mio = {
  add_mio_task_capacity = 1
  add_mio_task_capacity = -1
  add_mio_task_capacity = var:my_number_var
}"
```

## add_named_threat

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Adds country threat
```

## add_nationality

* Supported Scopes: CHARACTER
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Add the specified nationalty to the scoped-in operative. Examples:
add_nationality = ROOT
add_nationality = FRA

```

## add_naval_commander_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
Add naval commander to character

Example:
add_naval_commander_role = {
	character = GER_Character_token # optional if inside character scope
	traits = { spotter }
	skill = 4
	attack_skill = 3
	defense_skill = 3
	maneuvering_skill = 3
	coordination_skill = 4
	}
}
```

## add_nuclear_bombs

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add nukes to country
```

## add_offsite_building

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Add an offsite building to a country
```

## add_operation_token

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Adds a specific token against against another country
add_operation_token = {
	tag = GER
	token = some_token_id
}
```

## add_opinion_modifier

* Supported Scopes: COUNTRY
* Supported Targets: any

```
Add opinion modifier(s) to target(s)
```

## add_planning

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Adds planning skill to a unit leader
Example: add_planning = 1
```

## add_political_power

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add political power to country
```

## add_popularity

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add popularity to an ideology in a country

Example:
add_popularity = {
	ideology = neutrality
	popularity = 0.05
}
```

## add_power_balance_modifier

* Supported Scopes: any
* Supported Targets: none

```
adds static modifier to power balance

Example:
add_power_balance_modifier = {
	id = power_balance_id
	modifier = static_modifier_id # this must be defined in the static modifier database
}
```

## add_power_balance_value

* Supported Scopes: any
* Supported Targets: none

```
adds current value of a power balance

Example:
add_power_balance_value = {
	id = power_balance_id
	value = 0.42 # this value is added to the current value of the power balance
	tooltip_side = side_id # optional - add this to tell the game to show the name of the specific side in the tooltip
}
```

## add_project_progress_ratio

* Supported Scopes: SPECIAL_PROJECT
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Add progress to the project's prototype phase.
The input value is a ratio of the total needed progress to complete the special project, i.e. a decimal number between -1 and 1.
ex:
sp:my_project = {
  add_project_progress_ratio = 0.1
  add_project_progress_ratio = var:my_var
}"
```

## add_province_modifier

* Supported Scopes: STATE
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Adds static modifiers to specified province.
add_province_modifier = {
	static_modifiers = { mod_1 mod_2 }
	days = 42 # will be temporary if specified, can be variable
Select 1 province:
	province = 500
Or use:
	province = {
		id = 500 id = 501 id = 502 (evaluate for specified provinces)
		all_provinces (includes all in current state)
		limit_to_coastal (only coastal provinces)
		limit_to_border (only provinces bordering different country)
		limit_to_naval_base (only provinces with a naval base)
		limit_to_victory_point (only provinces with a VP)
	}
}
```

## add_raid_history_entry

* Supported Scopes: RAID_INSTANCE
* Supported Targets: none

```
Add history entry to a raid.
Example:
add_raid_history_entry = yes/no

```

## add_random_trait

* Supported Scopes: CHARACTER
* Supported Targets: none

```
add random trait from specified list to unit leader. add_random_trait = { old_guard brilliant_strategist inflexible_strategist }
```

## add_random_valid_trait_from_unit

* Supported Scopes: 
* Supported Targets: none

```
for use ONLY with root scope unit, target scope: character add_random_valid_trait_from_unit = FROM
```

## add_region_efficiency

* Supported Scopes: STRATEGIC_REGION
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
add efficiency factor to strategic region for from country
```

## add_relation_modifier

* Supported Scopes: COUNTRY
* Supported Targets: THIS

```
Adds a static modifier between current scope and target
Example: add_relation_modifier = {
	target = TAG # target of the relation
	modifier = static_modifier_name_here #Name of the modifier added
	}
}
```

## add_relation_rule_override

* Supported Scopes: COUNTRY
* Supported Targets: THIS

```
Adds an override rule to the country's relation to other countries. If there are multiple applicable overrides for a rule, then they are combined using AND logic for positive rules (e.g. can_access_market) and OR logic for negative rules (e.g. can_not_declare_war). 
The description of the effect is based on the trigger or the target country.The description when using the rule override is based: on the target country; the trigger at the time of effect evaluation; or the provided usage_desc.
The following rules are currently supported: can_send_volunteer, can_access_market
Alternative 1:
add_relation_rule_override = { 
 target = GER # [Required] Target country usage_desc = REASON_DESCRIPTION # [Optional] usage description can_not_declare_war = yes # [Required] 
}
Alternative 2:
add_relation_rule_override = { 
 trigger = is_democratic_country # [Required] Named trigger usage_desc = DEMOCRATIC_COUNTRY # [Optional] usage description can_not_declare_war = yes # [Required] 
}

```

## add_research_slot

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Adds a research slot (negative values subtracts)
```

## add_resistance

* Supported Scopes: STATE
* Supported Targets: any

```
add resistance to a state. Example: add_resistance = 30
```

## add_resistance_target

* Supported Scopes: STATE
* Supported Targets: any

```
adds resistance target to the scoped state :
add_resistance_target = 10
add_resistance_target = { 
  id = 123 #if set, id can be used for removing an added resistance target using remove_resistance_target effect  amount = 10 #original tag of new country
  occupied = GER #if set, the resistance target will only apply if the occupied country is GER
  occupier = ENG #if set, the resistance target will only apply if the occupier country is ENG
  days = 42 #if set the newly added resistance target will be only active for this many days
  tooltip = "BLABLA" #tooltip loc key to display in resistance target tooltips
}
```

## add_resource

* Supported Scopes: STATE, COUNTRY
* Supported Targets: none

```
Adds/removes resource production to state

Example:
add_resource = {
  type = steel #resource type to add/destroy  amount = 5 #amount to add
  state = 42 #can be also read from scope
  days = 60 #a resource can be added/removed temporarily
  show_state_in_tooltip = no #Should we show in which state we add the resource(default = yes)?
}

```

## add_scaled_political_power

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add political power to country scaled by the difference in IC between the receiver and another country
```

## add_scientist_level

* Supported Scopes: CHARACTER
* Supported Targets: none

```
"![MD]
Add levels to a special project specialization for a scientist character in scope.
The `level` parameter is a scoped variable

#### Example
```
my_character = {
	add_scientist_level = {
		level = 2 # accepts variables
		specialization = specialization_nuclear
	}
}
```"
```

## add_scientist_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
"Add scientist role to a character. The character can come from the scope or from an input parameter.
The scientist role format is the same as in the character DB.
Except the visible trigger - a scientist role created via effect cannot have triggers.
Examples:
# From character scope
my_character = {
	add_scientist_role = {
		scientist = {
			desc = desc_loc_key # Optional
			traits = { scientist_trait_token ... } # Optional
			skills = { specialization_token = 2 ... }
			# cf. game/common/characters/_documentation/md for full explanation
		}
	}
}

# From country scope
SOV = {
	add_scientist_role = {
		character = my_character / var:my_char_var / PREV # accepts variables and keywords
		scientist = { ... }
	}
}
"
```

## add_scientist_trait

* Supported Scopes: CHARACTER
* Supported Targets: none

```
"Add a trait to a scientist character in scope.
	ex: my_character = {
	  add_scientist_trait = my_trait_token
	}"
```

## add_scientist_xp

* Supported Scopes: CHARACTER
* Supported Targets: none

```
"![MD]
Add experience to a special project specialization for a scientist character in scope.
The `experience` parameter is a scoped variable.

#### Example
```
ex: my_character = {
	add_scientist_xp = {
		experience = 2 # accepts variables
		specialization = specialization_nuclear
	}
}
```"
```

## add_skill_level

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Adds a skill level to a unit leader
Example: add_skill_level = 1
```

## add_stability

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Adds the stability to the country in scope. Example: add_stability = 5
```

## add_state_claim

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add claim on state
```

## add_state_core

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add core on state
```

## add_state_modifier

* Supported Scopes: STATE
* Supported Targets: none

```
Adds a modifier to the state
Example: add_state_modifier = { modifier = { local_non_core_manpower = 0.2 } }
```

## add_tech_bonus

* Supported Scopes: COUNTRY
* Supported Targets: none

```
adds a limited use tech bonus
```

## add_temporary_buff_to_units

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Add buffs to units that are belongs to the army group/navy of this unit leader
```

## add_threat

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Adds country threat
```

## add_timed_idea

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Add a time-limited idea to country in scope
ex:
SOV = {
	add_timed_idea = {
		idea = my_idea_id
		days = 5
	}
	add_timed_idea = {
		idea = my_idea_id
		years = 1
		months = 2
		days = 5
		# NB: at least 1 of year/month/days is mandatory
		# NB: accept positive integer or variables
		# NB: tooltip will use the same year/month/day format as input
	}
}"
```

## add_timed_unit_leader_trait

* Supported Scopes: CHARACTER
* Supported Targets: none

```
add a timed trait to unit leader
```

## add_to_array

* Supported Scopes: any
* Supported Targets: none

```
Adds an element to an array
Example: add_to_array = {
	array = array_name
	value = 42 #optional, if not defined adds scope
	index = 3 #optional, default is end. otherwise elements are shifted
}
#shorter usage: add_to_array = { array_name = 42 }
```

## add_to_faction

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
adds specified country to faction
```

## add_to_tech_sharing_group

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Adds country to technology sharing group of specified name.
Example: add_to_tech_sharing_group = commonwealth_research
```

## add_to_temp_array

* Supported Scopes: any
* Supported Targets: none

```
Adds an element to a temporary array
Example: add_to_temp_array = {
	array = array_name
	value = 42 #optional, if not defined adds scope
	index = 3 #optional, default is end. otherwise elements are shifted
}
#shorter usage: add_to_temp_array = { array_name = 42 }
```

## add_to_temp_variable

* Supported Scopes: any
* Supported Targets: none

```
Adds a value or a variable to a temp variable
Example: add_to_temp_variable = {
var = num_dogs
	value = 42
	tooltip = loc_str_id_with_LEFT_and_RIGHT  #localized text with LEFT and RIGHT tokens in it, tokens will replaced by values
}
```

## add_to_variable

* Supported Scopes: any
* Supported Targets: none

```
Adds a value or a variable to another one
Example: add_to_variable = {
var = num_dogs
	value = 42
	tooltip = loc_str_id_with_LEFT_and_RIGHT  #localized text with LEFT and RIGHT tokens in it, tokens will replaced by values
}
```

## add_to_war

* Supported Scopes: COUNTRY
* Supported Targets: none

```
adds country to the specified war:
ENG = {
	add_to_war = {
	  targeted_alliance = SOV # Country to which side we want to join
	  enemy = PER # Which country we want to declare war on
	  hostility_reason = asked_to_join # The reason for joining the war
	  single_target_only = yes # yes if we want to target only the given country and not all enemies of targeted_alliance
  }
}
```

## add_trait

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
add trait from specified list to character.
add_trait = {
	character = GER_character_token # optional if inside character scope
	trait = brilliant_strategist
	slot = political_advisor #Only required for updating advisor
	ideology = fascism_ideology #Only required for updating country leader
}
```

## add_unit_bonus

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Adds permanent subunit and subunit category bonuses for country.

Example:
add_unit_bonus = {
  category_light_infantry = { # Subunit category bonuses
	   soft_attack = 0.05
	}
  
  cavalry = { # Subunit bonuses
	   soft_attack = 0.05
       hard_attack = 0.05
	}
}"
```

## add_unit_leader_trait

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Add trait to unit leader.
Example: SOV_konstantin_rokossovsky = { add_unit_leader_trait = media_personality }
```

## add_unit_medal_to_latest_entry

* Supported Scopes: 
* Supported Targets: none

```
add_unit_medal_to_latest_entry = { unit_medals = key }
```

## add_units_to_division_template

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Add units to division template for a country. Example:
add_units_to_division_template = {
  template_name = "Name of template" # not needed on done on specific division
  regiments = {
    infantry = 0 # (Adds infantry to first available slot on first column (x=0))
    cavalry = 2 # (Adds cavalry to first available slot on third column (x=2))
  }
  support = {
     military_police = 0 # (Adds military_police to first available slot on first (and likely only) column of supports (x=0))
  }
}
```

## add_victory_points

* Supported Scopes: any
* Supported Targets: any

```
adds victory point to province
add_victory_points = {
  province = 42
  value = 5
}
```

## add_war_support

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Adds the war support to the country in scope. Example: add_war_support = 5
```

## ai_message

* Supported Scopes: COUNTRY
* Supported Targets: none

```
ai message... ?
```

## air_experience

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add air experience for country
```

## annex_country

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL
## army_experience

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add army experience for country
```

## become_exiled_in

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Become exile in target nation. become_exiled_in = { target = TAG legitimacy = 0-100 (optional) }
```

## boost_planning

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Boost planning of units that are belongs to the army group/navy of this unit leader
```

## break_embargo

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
breaks an existing embargo from ROOT to the specified tag. Note this will only work if used on the sending country
```

## build_railway

* Supported Scopes: any
* Supported Targets: any

```
Builds/adds railway level between two provinces or along a path. Example:
build_railway = {
  level = 1 # Defaults to 1
  build_only_on_allied = yes # No by default. If yes and the effect scope is country, it will only build on allied territories for the country

  # You can specify a weight function that will be used in pathing. The scope will be the controller of the province it is trying to path to.
  # A negative value will make it not to path to that controller.
  # Non-negative values will be used as a path cost for that province.
  controller_priority = {
    base = 1

    modifier = {
      tag = MAN
      add = 2
    }
  }

  # The following options are used for picking a path. You can specify multiple options and it will pick in following order:
  fallback = yes # Default no. If yes, each option will try to fallback to next one.
  # option 1: List of provinces to draw railways. If fallback = yes uses start and end provinces of the path as fallback in option 2.
  path = { 10 20 30 40 }
  # option 2: Specify start & end province IDs. It will pick the shortest path. If provinces are not valid and if fallback = yes it will use states of those provs and use in option 3.
  start_province = 42
  target_province = 84
  # option 3: Specify start & end state IDs. It will pick provinces with the best node (capital > nodes > naval )
  start_state = 50
  target_state = 100
}

```

## cancel_border_war

* Supported Scopes: any
* Supported Targets: none

```
cancel border war between two states
```

## cancel_purchase_contract

* Supported Scopes: PURCHASE_CONTRACT
* Supported Targets: none

```
"Cancels the scoped purchase contract.
Example:
contract =  {cancel_purchase_contract = yes}"
```

## cancel_resistance

* Supported Scopes: STATE
* Supported Targets: any

```
cancels resistance activity for a core country.
use along with force_disable_resistance to disable resistance forever
Example : cancel_resistance = yes
```

## capture_operative

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: THIS, ROOT, PREV, FROM

```
Capture an operative
Can be used from a scope and a target that is either a country or a unit leader.
Examples:
GER = {
    capture_operative = PREV  # where PREV is an operative (unit leader)
    # or    capture_operative = {
        operative = PREV
        ignore_death_chance = yes  # optional: whether the death chance on capture should be ignored
    }
}

capture_operative = { captured_by = GER } # where the scope is an unit leader

```

## career_profile_step_missiolini

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Step completed Mussolini missions by one for the career profile
```

## change_division_template

* Supported Scopes: 
* Supported Targets: none

```
change_division_template = "My Template Name"
```

## change_tag_from

* Supported Scopes: any
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Changes player to other country
```

## character_list_tooltip

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Display in tooltip every character  (or "random_select_amount" of random characters if specified) that fulfills the "limit" trigger.
```

## clamp_temp_variable

* Supported Scopes: any
* Supported Targets: none

```
Clamps a temp variable a variable bet ween two a values or another variables
Example: clamp_temp_variable = {
var = num_dogs
min = 0
max = num_cats
}
```

## clamp_variable

* Supported Scopes: any
* Supported Targets: none

```
Clamps a variable between two values or variables.
Note that either min or max can be omitted.
The order in which the operations are applied is Max( Min( var, max ), min ).
An error will be logged if max < min as the result will be more often than not undesired (requires the game to run in debug mode).
Example: clamp_variable = {
    var = num_dogs
    min = 0
    max = num_cats
}

```

## clear_array

* Supported Scopes: any
* Supported Targets: none

```
Clears the contents of array
Example: clear_array = array_name
```

## clear_division_template_cap

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Clears division cap for a division template
Example: clear_division_template_cap = { division_template = <name>  }
```

## clear_global_event_target

* Supported Scopes: any
* Supported Targets: none

```
clear a global event target
```

## clear_global_event_targets

* Supported Scopes: any
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
clear all global event targets
```

## clear_rule

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Cleares rule added by set_rule. In the example it will clear can_not_declare_war = yes set by set_rule : 
clear_rule = { 
 can_not_declare_war = yes 
}
```

## clear_temp_array

* Supported Scopes: any
* Supported Targets: none

```
Clears the contents of a temporary array
Example: clear_temp_array = array_name
```

## clear_variable

* Supported Scopes: any
* Supported Targets: none

```
Clears a variable
Example: clear_variable = num_dogs
```

## clr_character_flag

* Supported Scopes: CHARACTER
* Supported Targets: none

```
clear character flag
```

## clr_country_flag

* Supported Scopes: COUNTRY
* Supported Targets: none

```
clear country flag
```

## clr_global_flag

* Supported Scopes: any
* Supported Targets: none

```
clear global flag
```

## clr_mio_flag

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: none

```
"Clear the matching flag in the military industrial organization in scope.
ex:
var:my_mio_var = {
  clr_mio_flag = my_flag
}"
```

## clr_project_flag

* Supported Scopes: SPECIAL_PROJECT
* Supported Targets: none

```
clear project flag
```

## clr_state_flag

* Supported Scopes: STATE
* Supported Targets: none

```
clear state flag
```

## clr_unit_leader_flag

* Supported Scopes: CHARACTER
* Supported Targets: none

```
clear unit leader flag
This effect is deprecated in favor of clr_character_flag.
```

## complete_mio_trait

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: none

```
"Complete a trait in the military industrial organization in scope.
This effect will not take into account the current state of the trait tree and will allow you to unlock a trait even if the one before is not unlocked.
Will also add 1 size to the MIO so that size and numbers of unlocked traits are always aligned.
ex:
var:my_mio_var = {
  complete_mio_trait = my_trait_token
  complete_mio_trait = {
	trait = my_trait_token
	show_modifiers = no # Optional, default = yes
  }
}"
```

## complete_national_focus

* Supported Scopes: COUNTRY
* Supported Targets: none

```
completes a focus for a country
```

## complete_prototype_reward_option

* Supported Scopes: SPECIAL_PROJECT
* Supported Targets: none

```
Complete a prototype reward option for the project in scope 
The effect will respect the fire only once and allowed property of prototype rewards.
ex:
complete_prototype_reward_option = 
{
	prototype_reward = my_reward
	prototyp_reward_option = my_option # Optional, if multiple choice use default one if not set
	show_modifiers = yes # Yes if the effects of the prototype reward should be shown (default no)
}
```

## complete_special_project

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Complete a special project for the country in scope.
This effect will not take into account the current state of the project tree and will allow you to unlock a project even if the one before is not unlocked.
Since the project is not completed within a facility, the facility state and scientist effects are NOT applied.
ex:
SOV = { complete_special_project = sp:my_project }
SOV = { complete_special_project = var:my_project_var }
SOV = { complete_special_project = PREV } # accepts variables and keywords
SOV = {
	complete_special_project = {
		# project, scientist, state accepts variables and keywords.
		project = sp:my_project
		scientist = my_scientist # Optional if no iteration_output, default to current scientists on the project if active otherwise to none
		state = my_state # Optional if no iteration_output, default to current state of the project if active otherwise to none
		iteration_output = { # Can be a single reward or reward = option, if it contains a multiple option choice but no option specified the default will be used. The reward must be available to the project
			my_reward
			my_other_reward # multiple choice, chose the default
			my_third_reward = my_option_1 # Specified option to use
		} # Optional amount of iteration rewards
		show_modifiers = no # Optional, default = yes
	}
}"
```

## construct_building_in_random_province

* Supported Scopes: STATE
* Supported Targets: none

```
"Set facility level in a random province of state and country scope.
	ex:
    GER = {
        65 = {
			construct_building_in_random_province = {
				land_facility = 1
			}
		}
	}
"
```

## country_event

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Fires a country event.
Example:
country_event = {
	id = germany.75 # The event to fire.
	# Optional Fields:
	hours = 12 # The number of hours to wait before firing the event.
	days = 5 # The number of days to wait before firing the event.
	months = 1 # The number of months to wait before firing the event, where a month is treated as 30 days.
	# Note:  hours, days, and months can all be used and will simply be added together.
	random_hours = 18 # A random amount of hours to be added to the delay before firing, from 0 up to but not including random_hours.
	random_days = 2 # A random amount of days to be added to the delay before firing, from 0 up to but one hour less than random_days.
	# Note:  random_hours and random_days can both be used and will simply be added together.
	random = 6 # Equivalent to random_hours; preserverd for backwards compatibility.
	random = { chance = 50 ... } # Specify a set of child effects to execute as part of this effect, with a percentage chance of randomly happening or not (as a group, not individually).
	tooltip = germany.75.t # Manually specify which tooltip to use for this effect.
}

```

## country_lock_all_division_template

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Lock all the division template at the country level. Note that you need to unlock them in the same way Can also supply the reason it is locked with localization key(You can't use 'set_division_template_lock' individually, because the lock at the country level will not be removed)Ex:country_lock_all_division_template = yescountry_lock_all_division_template = {  is_locked = yes  desc = LOC_KEY}
```

## create_colonial_division_template

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Create a colonial division template for overlord/owner. Available parameters are subject and division_template, where the subject parameter is the country tag for an overlords subject. And the division_template is the regular effect to create a division template.
Example.
In country scope of overlord, E.g. ROOT = ENG
create_colonial_division_template = {
    subject = RAJ # Country tag
    division_template = {
        name = "Infantry Division"
        division_names_group = RAJ_INF_01
        ...
        regiments = {
            infantry = { x = 0 y = 0 }
            infantry = { x = 0 y = 1 }
            }
        }
    }
}
```

## create_corps_commander

* Supported Scopes: COUNTRY
* Supported Targets: none

```
create corps commander for country
```

## create_country_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
creates a leader and adds it to proper party in country
if a character with the same token, or the same name already exists, then just add the country leader role.

Example:
create_country_leader = {
	name = "Leader Name"
	name = XXX_leader_name # optional, faster to find an already existing character
	desc = "LEADER_DESC_LOCALIZATION_TAG"
	picture = "Portrait_leader_name.dds" # picture = "...." also supported for backwards compatibility
	expire = "1965.1.1"
	ideology = despotism
	traits = {
		the_director
	}
}
```

## create_dynamic_country

* Supported Scopes: any
* Supported Targets: any

```
creates a dynamic country and runs child effects on it. example :
create_dynamic_country = { 
  original_tag = ITA #original tag of new country
  copy_tag = ITA # if set, it will copy stuff from copy tag instead of original_tag
 #...effects to run on new country}
```

## create_entity

* Supported Scopes: any
* Supported Targets: any

```
creates an entity on map
create_entity = {
  entity = entity_name #gfx entry 
  id = 123 # can be ommitted. if given you can use this id to access entity in later times. will replace existing entity if it exists
  var = var_name # can be ommitted. if given the id will be stored in this value so the entity can be accessed in later times 
  # position can be set using following. you can specify a province/state or can enter a manual coordinate. you can do both and the coordinate will shift the state/province coordinate 
  x = 42 
  y = 21 
  province = 123 
  state = 42 
  z = 3 #if wanted you can specify a z to shift height of the entity
  rotation = 1.2 # angle in radians 
  scale = 10.0 # scale of entity 
  min_zoom = 100.0 # min zoom needed to show entity 
  visible = scripted_trigger_name # a scripted trigger name to show or hide an entity. scope is player country}
```

## create_equipment_variant

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Creates a new equipment variant.
Example:
create_equipment_variant = {
	name = "Yorktown Class" # Optional.
	name_group = USA_CV_HISTORICAL # Optional. If not set, parent's name group will be inherited.
	type = ship_hull_carrier_1 # Must be a type and not an archetype.
	allow_without_tech = yes # Optional. Default no. If yes, create the variant even if the type hasn't been unlocked yet. Otherwise created the variant once the type research completes.
	parent_version = 3 # Default 0. If not found the default variant will be used (or created).
	obsolete = yes # Optional. Default no.
	mark_older_equipment_obsolete = yes # Optional. Default no. Marks all older (non-chassis) equipment variants as obsolete as long as the following matches: Archetype, niche, mission set (for planes).
	role_icon_index = 3 # Optional. Default 'auto', leverage AI design logic.
	upgrades = { # Optional. The level on each upgrade is inherited from the parent.
		ship_deckspace_upgrade = 1
		carrier_armor_upgrade = 2
	}
	modules = { # Optional. The module installed in each slot is inherit from the parent.
		fixed_ship_engine_slot = carrier_ship_engine_2
		fixed_ship_secondaries_slot = empty # Clears the slot if the parent has any module installed.
	}
	model = "GER_light_armor_2_entity" # Optional.
	icon = "gfx/interface/technologies/ger_basic_light_tank.dds" # Optional. GFX names are also supported e.g. "GFX_GER_basic_light_tank_medium".
    design_team = mio:my_mio_token # Optional. accepts mio:token, variable or keyword
}
```

## create_faction

* Supported Scopes: COUNTRY
* Supported Targets: none

```
create faction of specified name
```

## create_field_marshal

* Supported Scopes: COUNTRY
* Supported Targets: none

```
create field marshal for country
```

## create_import

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Creates trade between two countries
```

## create_intelligence_agency

* Supported Scopes: COUNTRY
* Supported Targets: none

```
create an Intelligence Agency for the country, if it is not already done. Example: 
create_intelligence_agency = yes # creates with historical ones, if exists. 
create_intelligence_agency = { 
  name = "M.I.B." 
  icon = "GFX_intelligence_agency_logo_ita" 
}
```

## create_navy_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
create navy leader for country
```

## create_operative_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
create operative for country
create_operative_leader = {
	bypass_recruitment = no # whether the operative is directly added to the list of available operatives 
	available_to_spy_master = yes # whether the operative can be recruited by the spy master. Only makes sense if bypass_recruitment is 'no'.
	portrait_tag_override = TAG # when selectiong the portrait for the operative, consider that tag instead of the country the operative will operate for gfx = GFX_portrait_alexander_rado # specify the GFX entry that the portrait will be based on, otherwise a random one will be generated.
	# Additionally supports the common token to other create_x_leader effects
 gender = male # or female. If not defined in script a random gender will be applied.}

```

## create_production_license

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Creates an equipment production license. If the selection criteria fails to match a variant no license will be created.
Example:
create_production_license = {
	target = TAG # Receiver of the license.
	cost_factor = 1.0 # Optional. Cost factor for production of the equipment.
	new_prioritised = no # Optional. Default yes. Ignore 'version' (but not 'version_name') below and instead select the latest variant.
	equipment = {
		type = small_plane_naval_bomber_airframe # The type of the variant to select. Must be specified.
		version = 1 # Optional. Default 0. Select the variant with the given version.
		version_name = "Do 22" # Optional. Select the variant with the given name.
	}
}
```

## create_purchase_contract

* Supported Scopes: any
* Supported Targets: none

```
"Creates a purchase contract between the countries.
Example:
create_purchase_contract = 
{
	seller = ENG
	buyer = RAJ
	civilian_factories = 2
	equipment = {
		type = infantry_equipment
		amount = 600
	}
	equipment = {
		type = armored_car1
		amount = 100
	}
}"
```

## create_railway_gun

* Supported Scopes: any
* Supported Targets: none

```
Create railway gun effect, just like in OOB, example:
create_railway_gun = {
	equipment = railway_gun_equipment_1
	name = "Created Railway Gun" #optional
	location = 12406 #optional, created in capital otherwise
}
```

## create_ship

* Supported Scopes: COUNTRY
* Supported Targets: none

```
create a ship from another country and assign it to the reserve fleet.
'creator' is optional. If not set, it will be the scoped country.
'name' is optional.
FRA = {
  create_ship = {
    type = ship_hull_submarine_1
    equipment_variant = "S Class"
    creator = ENG
    name = "My ship name"
    amount = 5 #amount to add
  }
}

```

## create_unit

* Supported Scopes: any
* Supported Targets: none

```
Create unit effect, just like in OOB, example: 
create_unit = { 
	# unit detauls 
	division = "name = \"1. Northern Redemption Army\" division_template = \"Redemption Army\" start_experience_factor = 0.5" 
	# country to spawn unit for 
	owner = MAN 
	 
	 
	# a prov id can be specified 
	prioritize_location = 12406 
	 
	# can be set to yes to be able to spawn units on enemy provs. 
	allow_spawning_on_enemy_provs = no 
	# province controllers can be scored using this scorer. otherwise it will prio your owned provs first, friendly provs second.  
	# it will also prio provs with scores and less units firstl 
	country_score = { 
		base = 100 
		 
		modifier = { 
			tag = MAN 
			add = 100 
		} 
	} 
   count = 1 # can be specified to spawn more than one units 
   id = 42 # an id can be given to delete units later on   divisional_commander_xp = 4 # give the division commander experience on unit creation }
```

## create_wargoal

* Supported Scopes: COUNTRY
* Supported Targets: none

```
creates wargoal for country in scope
```

## custom_effect_tooltip

* Supported Scopes: any
* Supported Targets: none

Append an extra tooltip to the effect. The tooltip is a [bindable localization](script_concept_documentation.md#bindable-localization).

### Examples
```
custom_effect_tooltip = MY_TOOLTIP # Simple loc key tooltip
```
```
custom_effect_tooltip = {
	localization_key = MY_TOOLTIP # Root look key
	IMPORTANT_QUESTION = { # ID IMPORTANT_QUESTION in MY_TOOLTIP will get value:
		localization_key = MEANING_OF_LIFE # Root loc key in IMPORTANT_QUESTION
		ANSWER = "42" # ID ANSWER in IMPORTANT_QUESTION will get value 42
	}
	JUST_AS_IMPORTANT = OR_NOT # ID JUST_AS_IMPORTANT in MY_TOOLTIP will get value OR_NOT
}
```


## custom_override_tooltip

* Supported Scopes: any
* Supported Targets: none

Executes the provided effects but with a custom tooltip surpressing all tooltips from all other effects inside this block.
The custom tooltip is a [bindable localization](script_concept_documentation.md#bindable-localization).

### Examples
```
custom_override_tooltip = {
	tooltip = MY_TOOLTIP # Simple loc key tooltip
	<other effects>
}
```

```
custom_override_tooltip = {
	tooltip = {
		localization_key = MY_TOOLTIP # Root look key
		IMPORTANT_QUESTION = { # ID IMPORTANT_QUESTION in MY_TOOLTIP will get value:
			localization_key = MEANING_OF_LIFE # Root loc key in IMPORTANT_QUESTION
			ANSWER = "42" # ID ANSWER in IMPORTANT_QUESTION will get value 42
		}
		JUST_AS_IMPORTANT = OR_NOT # ID JUST_AS_IMPORTANT in MY_TOOLTIP will get value OR_NOT
	}
	<other effects>
}
```


## damage_building

* Supported Scopes: STATE, COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Damages a building in a targeted state or province.
Example:
damage_building = {
	type = industrial_complex
	damage = 2.4
	repair_speed_modifier = -0.5 # repair will be 50% slower until building is fully repaired
}

The building can also be specified through tags.
Example: damage_building = {
	tags = facility # can be a single tag or a { }-wrapped list of tags
	damage = 2.4
	repair_speed_modifier = -0.5 # repair will be 50% slower until building is fully repaired
}

The above examples will only work in state scope where buildings can be found through the scope state,
and province buildings are recursively found from that state.

You can also manually specify either a state or province:

damage_building = {
	type = industrial_complex
	province = 500 # or a variable like var:target_province
	damage = 2.4
}

damage_building = {
	type = industrial_complex
	state = 35 # or a variable like var:target_state
	damage = 2.4
}

If the building is a province building but only a state has been specicied, all provinces in that state will be
searched to find the first matching province building.
"
```

## damage_units

* Supported Scopes: any
* Supported Targets: any

```
damages units for given conditions. no tooltip generated
damage_units = {
  #specify a location
  province = 42
  state = 5
  region = 5
  limit = { always = yes } #you can add a trigger for country check
  damage = 0.5 #if defined will damage both org & str damage with this amount
  org_damage = 0.5
  str_damage = 0.5
  ratio = yes #will damage a ratio damage to total org/str of unit if set
  template = "template_name" #you can limit army templates to damage  army = yes #will damage armies
  navy = yes #will damage navies
}
```

## deactivate_advisor

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Dismiss an advisor from their currently occupied role slot

Example:
deactivate_advisor = GER_character_token_air_chief

```

## deactivate_shine_on_focus

* Supported Scopes: COUNTRY
* Supported Targets: any

Deactivate the shine effect on the focus with the given id. The current focus cannot have it's shine effect removed.

Note that tooltips are only shown in debug mode.

### Example:
```
deactivate_shine_on_focus = GER_prioritize_economic_growth
```


## declare_war_on

* Supported Scopes: COUNTRY
* Supported Targets: none

```
declares war on specified country
```

## delete_unit

* Supported Scopes: COUNTRY
* Supported Targets: none

```
delete units of a country. no tooltip is generated. example: 

Example:
delete_unit = { 
	division_template = template_name # can be filtered a specific template 
	id = 42 # can be filtered to a given id in create unit effect 
	state = 64 # can be filtered by a given state 
	disband = yes # default is no. if set to yes the game will refund equipment/manpower
}
```

## delete_unit_template_and_units

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Delete a template and its units
Example: delete_unit_template_and_units = { 
division_template = <name> 
disband = no #if yes, will refund equipment/manpower. default is no
}
```

## delete_units

* Supported Scopes: COUNTRY
* Supported Targets: any

```
deletes units that uses a specific template :
delete_units = { 
  division_template = "Template Name"
  disband = no # if yes, equipment will be returned to country equipment. default is no
}
```

## demote_leader

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Demotes field marshal to general
```

## destroy_entity

* Supported Scopes: any
* Supported Targets: any

```
destroys an existing entity
destroy_entity = 123 #id

```

## destroy_ships

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Destroys ships of specified country and amount
Example: 
ENG={ 
	destroy_ships = {
		type=light_cruiser
		count=all #or number
	}
}
```

## destroy_unit

* Supported Scopes: 
* Supported Targets: none

```
destroy currently scoped unit
```

## diplomatic_relation

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Set up a diplomatic relation between two nations. Example: 
diplomatic_relation = { 
	country = POR #target country
	relation = military_access #type of relation
	active = yes #yes to add relation, no to cancel existing one
}
```

## dismantle_faction

* Supported Scopes: COUNTRY
* Supported Targets: none

```
dismantle faction led by the current country
```

## divide_temp_variable

* Supported Scopes: any
* Supported Targets: none

```
Divies a temp variable to a value or another variable
Example: divide_temp_variable = {
var = num_dogs
	value = 42
	tooltip = loc_str_id_with_LEFT_and_RIGHT  #localized text with LEFT and RIGHT tokens in it, tokens will replaced by values
	if_zero = 0 # the value to assign if the divisor is zero (default is zero)
}
```

## divide_variable

* Supported Scopes: any
* Supported Targets: none

```
Divies a variable to a value or another variable
Example: divide_variable = {
var = num_dogs
	value = 42
	tooltip = loc_str_id_with_LEFT_and_RIGHT  #localized text with LEFT and RIGHT tokens in it, tokens will replaced by values
}
```

## division_template

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add a division template to country
```

## drop_cosmetic_tag

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Drops country cosmetic tag.
Example: INS = { drop_cosmetic_tag }
```

## effect_tooltip

* Supported Scopes: any
* Supported Targets: any

```
Shows just tooltip of effects
```

## end_exile

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Ends the exile of of the current scope's country
```

## end_puppet

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Stops specefied country being a puppet of current country
```

## event_option_tooltip

* Supported Scopes: any
* Supported Targets: none

```
Shows the tooltip text of an event option in other tooltips(root and from scopes are swapped).
Example:
event_option_tooltip = mtg_usa_civil_war_fascists.1.a
```

## every_active_scientist

* Supported Scopes: any
* Supported Targets: none

```
"Executes children effects on every active scientist (or \"random_select_amount\" of random character if specified) of the country in scope, that fulfills the \"limit\" trigger.
	tooltip=key can be added to override tooltip title.
	By default the effects are only displayed once, you may display them for each matching character with display_individual_scopes.
	ex: GER = {
	  every_active_scientist = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		include_invisible = yes # Optional - default = no
		display_individual_scopes = yes # Optional - default = no
		... character scope effects ...
	  }
	}"
```

## every_allied_country

* Supported Scopes: COUNTRY
* Supported Targets: none

Executes children effects on every Allied Country different from the one in scope (or `random_select_amount` of random country if specified) that fulfills the `limit` trigger.
`tooltip` can be added to override tooltip title (supports [bindable localization](script_concept_documentation.md#bindable-localization)).
By default the effects are only displayed once, you may display them for each matching country with display_individual_scopes.

### Example
```
ENG = {
	every_allied_country = {
		tooltip = my_loc_key # Optional bindable localization
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		limit = my_limit_trigger # Optional
		... country scope effects ...
	}
}
```


## every_army_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every Army Leader (or \"random_select_amount\" of random leader if specified) of the country in scope, that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
ex: GER = {
  every_army_leader = {
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	include_invisible = yes # Optional - default = no
    ... character scope effects ...
  }
}"
```

## every_character

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every Character (or \"random_select_amount\" of random character if specified) of the country in scope, that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching character with display_individual_scopes.
ex: GER = {
  every_unit_leader = {
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	include_invisible = yes # Optional - default = no
    display_individual_scopes = yes # Optional - default = no
    ... character scope effects ...
  }
}"
```

## every_controlled_state

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every State controlled by the country in scope (or \"random_select_amount\" of random state if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching state with display_individual_scopes.
ex:
SOV = {
	every_controlled_state = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... state scope effects ...
	}
}"
```

## every_core_state

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every core State of the country in scope (or \"random_select_amount\" of random state if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching state with display_individual_scopes.
ex:
SOV = {
	every_core_state = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... state scope effects ...
	}
}"
```

## every_country

* Supported Scopes: any
* Supported Targets: none

```
"Executes children effects on every Country (or \"random_select_amount\" of random country if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching country with display_individual_scopes.
ex:
every_country = {
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	display_individual_scopes = yes # Optional - default = no
	... country scope effects ...
}"
```

## every_country_division

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every Division of the country in scope (or \"random_select_amount\" of random divisions if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching division with display_individual_scopes.
ex:
SOV = {
	every_country_division = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... division scope effects ...
	}
}"
```

## every_country_with_original_tag

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on a all countries with original tag (or \"random_select_amount\" of random country if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching country with display_individual_scopes.
ex:
every_country_with_original_tag = {
	original_tag_to_check = ENG # the effect will only run on countries that has this original tag
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	display_individual_scopes = yes # Optional - default = no
	... country scope effects ...
}"
```

## every_enemy_country

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every enemy Country of the country in scope (or \"random_select_amount\" of random country if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching country with display_individual_scopes.
ex:
SOV = {
	every_enemy_country = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... country scope effects ...
	}
}"
```

## every_military_industrial_organization

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every Military Industrial Organisation (or \"random_select_amount\" of random MIOs if specified) of the country in scope, that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching MIO with display_individual_scopes.
ex: GER = {
  every_military_industrial_organization = {
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	include_invisible = yes # Optional - default = no
	display_individual_scopes = yes # Optional - default = no
    ... MIO scope effects ...
  }
}"
```

## every_navy_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every Navy Leader (or \"random_select_amount\" of random leader if specified) of the country in scope, that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching unit leader with display_individual_scopes.
ex: GER = {
  every_navy_leader = {
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	include_invisible = yes # Optional - default = no
	display_individual_scopes = yes # Optional - default = no
    ... character scope effects ...
  }
}"
```

## every_neighbor_country

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every neighbor Country of the country in scope (or \"random_select_amount\" of random country if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching country with display_individual_scopes.
ex:
SOV = {
	every_neighbor_country = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... country scope effects ...
	}
}"
```

## every_neighbor_state

* Supported Scopes: STATE
* Supported Targets: none

```
"Executes children effects on every State neighboring the state in scope (or \"random_select_amount\" of random state if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching state with display_individual_scopes.
ex:
42 = {
	every_neighbor_state = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... state scope effects ...
	}
}"
```

## every_occupied_country

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every occupied Country by the country in scope (or \"random_select_amount\" of random country if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching country with display_individual_scopes.
ex:
SOV = {
	every_occupied_country = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... country scope effects ...
	}
}"
```

## every_operative

* Supported Scopes: COUNTRY, OPERATION
* Supported Targets: none

```
"Executes children effects on every operative (or \"random_select_amount\" of random operatives if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching operative with display_individual_scopes.
ex: GER = {
  every_operative = {
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
    display_individual_scopes = yes # Optional - default = no
    ... character scope effects ...
  }
}"
```

## every_other_country

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every Country different from the one in scope (or \"random_select_amount\" of random country if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching country with display_individual_scopes.
ex:
SOV = {
	every_other_country = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... country scope effects ...
	}
}"
```

## every_owned_state

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every State owned by the country in scope (or \"random_select_amount\" of random state if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching state with display_individual_scopes.
ex:
SOV = {
	every_owned_state = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... state scope effects ...
	}
}"
```

## every_possible_country

* Supported Scopes: any
* Supported Targets: none

```
"Executes children effects on every Country (or \"random_select_amount\" of random country if specified) that fulfills the \"limit\" trigger.
Difference with every_country is that it includes countries not yet present on the map.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching country with display_individual_scopes.
ex:
every_possible_country = {
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	display_individual_scopes = yes # Optional - default = no
	... country scope effects ...
}"
```

## every_purchase_contract

* Supported Scopes: any
* Supported Targets: none

```
"Executes children effects on every purchase contract (or \"random_select_amount\" of random purchase contracts if specified) of the country in scope, that fulfills the \"limit\" trigger.
tooltip = key need to be added to override the tooltip title.
By default the effects are only displayed once, you may display them for each matching purchase contract with display_individual_scopes.
ex: GER = {
  every_military_industrial_organization = {
	limit = { ... contract scope triggers ... }
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	display_individual_scopes = yes # Optional - default = no
    ... Purchase Contract scope effects ...
  }
}"
```

## every_scientist

* Supported Scopes: any
* Supported Targets: none

```
"Executes children effects on every scientist (or \"random_select_amount\" of random character if specified) of the country in scope, that fulfills the \"limit\" trigger.
	tooltip=key can be added to override tooltip title.
	By default the effects are only displayed once, you may display them for each matching character with display_individual_scopes.
	ex: GER = {
	  every_scientist = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		include_invisible = yes # Optional - default = no
		display_individual_scopes = yes # Optional - default = no
		... character scope effects ...
	  }
	}"
```

## every_state

* Supported Scopes: any
* Supported Targets: none

```
"Executes children effects on every State (or \"random_select_amount\" of random state if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching state with display_individual_scopes.
ex:
every_state = {
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	display_individual_scopes = yes # Optional - default = no
	... state scope effects ...
}"
```

## every_state_division

* Supported Scopes: STATE
* Supported Targets: CAPITAL

```
"Executes children effects on every Division currently in the state in scope (or \"random_select_amount\" of random divisions if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching division with display_individual_scopes.
ex:
SOV = {
	every_state_division = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... division scope effects ...
	}
}"
```

## every_subject_country

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every subject Country of the country in scope (or \"random_select_amount\" of random country if specified) that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching country with display_individual_scopes.
ex:
SOV = {
	every_subject_country = {
		tooltip = my_loc_key # Optional
		random_select_amount = 3 # Optional
		display_individual_scopes = yes # Optional - default = no
		... country scope effects ...
	}
}"
```

## every_unit_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every Unit Leader (or \"random_select_amount\" of random leader if specified) of the country in scope, that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching unit leader with display_individual_scopes.
ex: GER = {
  every_unit_leader = {
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	include_invisible = yes # Optional - default = no
	display_individual_scopes = yes # Optional - default = no
    ... character scope effects ...
  }
}"
```

## execute_operation_coordinated_strike

* Supported Scopes: OPERATION
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Special effect for executing the Coordinated Strike Operation. amount determines how often the simulation is run
```

## finalize_border_war

* Supported Scopes: any
* Supported Targets: none

```
finalizes border war between two states, wins or cancels it
```

## find_highest_in_array

* Supported Scopes: any
* Supported Targets: any

```
Runs a loop on for each element of an array, finds the highest value and stores result in temp variables
Example: find_highest_in_array = {
	array = array_name
	value = value_name #optional (default 'v') highest value in array will be stored in this temp variable
	index = index_name #optional (default 'i') index of highest value in array will be stored in this temp variable
}
```

## find_lowest_in_array

* Supported Scopes: any
* Supported Targets: any

```
Runs a loop on for each element of an array, finds the lowest value and stores result in temp variables
Example: find_lowest_in_array = {
	array = array_name
	value = value_name #optional (default 'v') lowest value in array will be stored in this temp variable
	index = index_name #optional (default 'i') index of lowest value in array will be stored in this temp variable
}
```

## for_each_loop

* Supported Scopes: any
* Supported Targets: any

```
Runs a loop on for each element of an array
Example: for_each_loop = {
	array = array_name
	value = value_name #optional (default 'v') current value in array will be stored in this temp variable
	index = index_name #optional (default 'i') current index in array will be stored in this temp variable
	break = break_name #optional (default 'break') set this temp variable to non zero to break the loop
 #effect 1
 #effect 2 ...
}
```

## for_each_scope_loop

* Supported Scopes: any
* Supported Targets: any

```
Runs a loop on for each element of an array and changes scope to current element in each iteration
Example: for_each_scope_loop = {
	array = array_name
	break = break_name #optional (default 'break') set this temp variable to non zero to break the loop
	tooltip = loc #if defined, the effect will output a tooltip for sub effects using this localization as title
 #effect 1
 #effect 2 ...
}
```

## for_loop_effect

* Supported Scopes: any
* Supported Targets: any

```
Runs a same effects through a loop. example will run the effects for value_name = -3, 0, 3, 6, 9 and then terminate
Example: for_loop_effect = {
	start = -3 (default 0) start value of loop
	end = 10 (default 0) end value of loop
	compare = less_than_or_equals (default less_than) comparison type between start and end val
	add = 3 (default 1) value to add to current value after each iteration
	value = value_name #optional (default 'v') current value of iteration will be stored in this temp variable
	break = break_name #optional (default 'break') set this temp variable to non zero to break the loop
 #effect 1
 #effect 2 ...
}
```

## force_disable_resistance

* Supported Scopes: STATE
* Supported Targets: any

```
force disables resistance for scoped state.  :
force_disable_resistance = GER # same as occupier = GER 
force_disable_resistance = { 
  clear = no #if yes, will clear previously disabled resistance
  occupier = GER #if set, the resistance will be disabled when the occupier is GER
  occupied = ENG #if set, the resistance will be disabled if the occupier country is target
}
```

## force_enable_resistance

* Supported Scopes: STATE
* Supported Targets: any

```
force enables resistance for scoped state. the resistance will be active even if other conditions doesn't satisfy (even if it is core or resistance check trigger is false)  :
force_enable_resistance = GER # same as occupier = GER 
force_enable_resistance = { 
  clear = no #if yes, will clear previously set resistance
  occupier = GER #if set, the resistance will be enabled when the occupier is GER
  occupied = ENG #if set, the resistance will be enabled if the occupier country is target
}
```

## force_operative_leader_into_hiding

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Force an operative into hiding, preventing him from performing mission. The specified values is subject to modifiers
force_operative_leader_into_hiding = 12

```

## force_update_dynamic_modifier

* Supported Scopes: STATE, COUNTRY, CHARACTER, SPECIAL_PROJECT
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
updates the modifiers in current scope (use if you don't want to wait for daily update to update them):
force_update_dynamic_modifier = yes

```

## force_update_map_mode

* Supported Scopes: any
* Supported Targets: any

```
force rebuilds map mode. no tooltip generated.
force_update_map_mode = { 
  limit = { always = yes } # limit to check against player
  mapmode = scripted_map_mode_name

```

## free_operative

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: THIS, ROOT, PREV, FROM

```
Free an operative
Can be used from a scope and a target that is either a country or a unit leader.
GER = { free_operative = PREV } # where PREV is an operative (unit leader)
free_operative = { captured_by = GER } # where the scope is an unit leader

```

## free_random_operative

* Supported Scopes: COUNTRY
* Supported Targets: any

```
Free a random captured operative of a certain tag by a certain tag
Can be used from a country scope of the operative in question.
`all` is optional, default value is no - if set to yes it will free all operatives captured by the target country
GER = { free_random_operative = { all = yes captured_by = ENG } }

```

## gain_xp

* Supported Scopes: CHARACTER
* Supported Targets: any

```
Grant experience to the scoped in unit leader. Cannot be used to remove experience.
The unit leader is promoted to the next skill level if applicable.
Example:
gain_xp = 5

```

## generate_character

* Supported Scopes: COUNTRY
* Supported Targets: any

```
Generates a character. Use in every_country in order to generates one copy of the character per country satisfying the limit conditions.
every_country = {
	limit = { OR = { original_tag = KOR original_tag = SER original_tag = ICE } }
	generate_character = { #create + recruit
		token_base = army_chief_defensive_1 # mandatory, character token will be token_base
		name = "Character's Name" # optional, no name provided means random name for each generated character
		# then whatever you would put when writing character
		advisor = {
			idea_token = ac # full idea token will be token_base_idea_token (to ensure unicity). optional, slot will be used if missing.
			slot = army_chief
			allowed = { original_tag = PREV }
			traits = { army_chief_defensive_1 }
		}
	}
}
```

## generate_scientist_character

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Generate a new character with a scientist role and recruit it in the country in scope.
Examples:
SOV = {
	generate_scientist_character = {
		portrait = GFX_portrait # optional - random portrait by default
		portrait_tag_override = CHI # optional - accepts variable and keyword - only relevant if using random portrait - by default use country in scope
		gender = male / female # optional - by default random gender
		skills = {
			# optional array
			# same format as in scientist role in character DB
			# by default all skills are at 1
			specialization_token = 2
		}
		traits = { trait_token } # optional array
	}
}
"
```

## get_highest_scored_country

* Supported Scopes: COUNTRY
* Supported Targets: none

```
calculates the highest scored country that is defined in a country scorer and sets it to a temp variable. Example: 
get_highest_scored_country = { 
  scorer = scorer_id 
  var = var_name # temp variable name that the result will be stored. default is highest_scored_country 
}
```

## get_highest_scored_country_temp

* Supported Scopes: COUNTRY
* Supported Targets: none

```
calculates the highest scored country that is defined in a country scorer and sets it to a variable. Example: 
get_highest_scored_country_temp = { 
  scorer = scorer_id 
  var = var_name # variable name that the result will be stored. default is highest_scored_country 
}
```

## get_sorted_scored_countries

* Supported Scopes: COUNTRY
* Supported Targets: none

```
calculates & sorts all countries in a country scorer and stores them and their scores in arrays. Example: 
get_sorted_scored_countries = { 
  scorer = scorer_id # id that is used in country scorer  array = array_name # a name to store sorted countries as an array (default to sorted_country_list) 
  scores = array_name # corresponding score array for countries stored in array (default to country_list_scores) 
}
```

## get_sorted_scored_countries_temp

* Supported Scopes: COUNTRY
* Supported Targets: none

```
calculates & sorts all countries in a country scorer and stores them and their scores in temp arrays. Example: 
get_sorted_scored_countries_temp = { 
  scorer = scorer_id # id that is used in country scorer  array = array_name # a name to store sorted countries as a temp array (default to sorted_country_list) 
  scores = array_name # corresponding score temp array for countries stored in array (default to country_list_scores) 
}
```

## get_supply_vehicles

* Supported Scopes: COUNTRY
* Supported Targets: none

```
sets a variable to the number of supply vehicles in stockpile or that are needed. example 
get_supply_vehicles = { 
	var = num_vehicles #variable to set 
	type = truck #can be truck or train 
	need = yes #default no. If yes, gets the number of needed vehicles 
} 

```

## get_supply_vehicles_temp

* Supported Scopes: COUNTRY
* Supported Targets: none

```
sets a temp variable to the number of supply vehicles in stockpile or that are needed. example 
get_supply_vehicles_temp = { 
	var = num_vehicles #variable to set 
	type = truck #can be truck or train 
	need = yes #default no. If yes, gets the number of needed vehicles 
} 

```

## give_guarantee

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
guarantees specified country
```

## give_market_access

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Gives market access to the specified country.
Example:
FRA =  {
  give_market_access = BRA  # France and Brazil will now have market access to each other
}"
```

## give_military_access

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
gives military access to the specified country
```

## give_resource_rights

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Gives rights to take resources from specified state.
	give_resource_rights = {
		receiver = <TAG> # accepts keyword or variable
		state = <id> # accepts keyword or variable
		resources = {<Resource Name>} # [optional] If provided, only gives rights to the prodived resources.
													If not provided gives rights to all resources in the states.
	}"
```

## global_every_army_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on every Army Leader (or \"random_select_amount\" of random leader if specified) for EVERY COUNTRY, that fulfills the \"limit\" trigger.
Better to use every_army_leader if you know the country to search in.
tooltip=key can be added to override tooltip title.
By default the effects are only displayed once, you may display them for each matching unit leader with display_individual_scopes.
global_every_army_leader = {
	tooltip = my_loc_key # Optional
	random_select_amount = 3 # Optional
	include_invisible = yes # Optional - default = no
	display_individual_scopes = yes # Optional - default = no
	... character scope effects ...
}"
```

## goto_province

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Goes to stated province.
```

## goto_state

* Supported Scopes: any
* Supported Targets: none

```
Goes to stated state.
```

## harm_operative_leader

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Harm an operative. The specified value is subject to modifiers.
harm_operative_leader = 12

```

## hidden_effect

* Supported Scopes: any
* Supported Targets: none

```
Effect not shown in tooltips
```

## hold_election

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Immediately holds an election in the target country
```

## if

* Supported Scopes: any
* Supported Targets: none

```
a conditional effect
```

## inherit_technology

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Copies over technology state from target
```

## injure_scientist_for_days

* Supported Scopes: CHARACTER
* Supported Targets: none

```
"Injure a scientist for x amount of days to a scientist character in scope.
	ex: my_character = {
	  injure_scientist_for_days = 12
	}"
```

## kill_country_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
kills a country leader and removes him completely, making the next in line the new party and country leader
```

## kill_ideology_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
removes a ideology leader as leader of his party, making the next in line the new party leader
```

## kill_operative

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: THIS, ROOT, PREV, FROM

```
Kills an operative. This will temporarily lock the slot they occupy
Examples:
GER = {
    kill_operative = PREV  # where PREV is an operative (unit leader)
    # or
    kill_operative = {
        operative = PREV
    }
}

kill_operative = { killed_by = GER } # where the scope is an unit leader

```

## launch_nuke

* Supported Scopes: COUNTRY
* Supported Targets: none

```
launch nuke at a state. usage : 
launch_nuke = { 
   provinve = 42 #will nuke this province if specified
   state = 42 #use either province or state. if state is used it will prefer enemies first while picking a province to nuke. otherwise it will pick one of the neutrals
   controller = GER #if state and controller is specified, the effect will pick a province that is controlled by this tag
   use_nuke = yes #will consume nuke if specified
   nuke_type = nuclear_bomb # type of nuke to use (e.g. nuclear_bomb, thermonuclear_bomb etc.)
} 

```

## leave_faction

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Country leaves the faction
```

## load_focus_tree

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Sets what focus tree a country uses, retains finished shared focuses.
```

## load_oob

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Immediately loads an Order of Battle (OOB) file.

Example:
load_oob = "ENG_1936"
```

## log

* Supported Scopes: any
* Supported Targets: none

```
Print message to game.log, console (if visible) and history logger (if running. you can use category|log to specify a category), Can be localized
```

## mark_focus_tree_layout_dirty

* Supported Scopes: COUNTRY
* Supported Targets: any

```
Forces the refresh of the tree layout for the scoped country
mark_focus_tree_layout_dirty = yes

```

## mark_technology_tree_layout_dirty

* Supported Scopes: COUNTRY
* Supported Targets: any

```
Forces the refresh of the hidden technologies for the scoped country
mark_technology_tree_layout_dirty = yes

```

## meta_effect

* Supported Scopes: any
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
meta effects can be used for building effects from strings and running them. following example will give Germany 42 pp:
meta_effect = {
    text = {
        [COUNTRY] = {
            add_political_power = [POW]
        }
    }
    COUNTRY = "GER"
    POW = 42
    debug = no #set to yes if you want to see what game actually executes
}

```

## modify_building_resources

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Modifies resource output of specific building for this country only
Example: modify_building_resources = {
	building = radar_station
	resource = oil
	amount = 2
}
```

## modify_character_flag

* Supported Scopes: CHARACTER
* Supported Targets: none

```
modify character flag. Only modifies if flag already exists.
Example: _modify_character_flag_ = { flag = <name> value = <number> }
```

## modify_country_flag

* Supported Scopes: COUNTRY
* Supported Targets: none

```
modify country flag. Only modifies if flag already exists.
Example: modify_country_flag = { flag = <name> value = <number> }
```

## modify_global_flag

* Supported Scopes: any
* Supported Targets: none

```
modify global flag. Only modifies if flag already exists.
Example: modify_global_flag = { flag = <name> value = <number> }
```

## modify_mio_flag

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: none

```
"Modify the matching flag in the military industrial organization in scope. Happens only if the flag already exists.
ex:
var:my_mio_var = {
  modify_mio_flag = {
    flag = my_flag
    value = 5 (optional, default = 0. Will be added to the current value)
    days = 13 (optional, default = 0. if > 0, the flag will be deleted after this number of days)
  }
}"
```

## modify_project_flag

* Supported Scopes: SPECIAL_PROJECT
* Supported Targets: none

```
modify project flag. Only modifies if flag already exists.
Example: modify_facility_flag = { flag = <name> value = <number> }
```

## modify_state_flag

* Supported Scopes: STATE
* Supported Targets: none

```
modify state flag. Only modifies if flag already exists.
Example: modify_state_flag = { flag = <name> value = <number> }
```

## modify_tech_sharing_bonus

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Modify country bonus for specified technology sharing group.
Example: modify_tech_sharing_bonus  = { id = commonwealth_research bonus = 0.2 }
```

## modify_timed_idea

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Modify amount of days of a timed idea for the country in scope
ex:
SOV = {
	modify_timed_idea = {
		idea = my_idea_id
		days = 5
		# Add 5 days to the my_idea_id time-limit
	}
	modify_timed_idea = {
		idea = my_idea_id
		days = -5
		# Subtract 5 days to the my_idea_id time-limit
	}
	modify_timed_idea = {
		idea = my_idea_id
		years = 1
		months = 2
		days = variable_name
		# NB: at least 1 of year/month/days is mandatory
		# NB: accept integer or variables
		# NB: tooltip will use the same year/month/day format as input
	}
}"
```

## modify_unit_leader_flag

* Supported Scopes: CHARACTER
* Supported Targets: none

```
modify unit leader flag. Only modifies if flag already exists.
Example: _modify_unit_leader_flag_ = { flag = <name> value = <number> }
This effect is deprecated in favor of modify_character_flag.
```

## modulo_temp_variable

* Supported Scopes: any
* Supported Targets: none

```
modulos a temp variable with another. Example: 
modulo_temp_variable = { 
  var = variable_to_modulo 
  value = divisior 
}
```

## modulo_variable

* Supported Scopes: any
* Supported Targets: none

```
modulos a variable with another. Example: 
modulo_variable = { 
  var = variable_to_modulo 
  value = divisior 
}
```

## multiply_temp_variable

* Supported Scopes: any
* Supported Targets: none

```
Multiplies a temp variable to a value or another variable
Example: set_temp_variable = {
var = num_dogs
	value = 42
	tooltip = loc_str_id_with_LEFT_and_RIGHT  #localized text with LEFT and RIGHT tokens in it, tokens will replaced by values
}
```

## multiply_variable

* Supported Scopes: any
* Supported Targets: none

```
Multiplies a variable to a value or another variable
Example: set_variable = {
var = num_dogs
	value = 42
	tooltip = loc_str_id_with_LEFT_and_RIGHT  #localized text with LEFT and RIGHT tokens in it, tokens will replaced by values
}
```

## navy_experience

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add naval experience for country
```

## news_event

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Fires a news event.
Example:
news_event = {
	id = news.251 # The event to fire.
	# Optional Fields:
	hours = 12 # The number of hours to wait before firing the event.
	days = 5 # The number of days to wait before firing the event.
	months = 1 # The number of months to wait before firing the event, where a month is treated as 30 days.
		# Note:  hours, days, and months can all be used and will simply be added together.
	random_hours = 18 # A random amount of hours to be added to the delay before firing, from 0 up to but not including random_hours.
	random_days = 2 # A random amount of days to be added to the delay before firing, from 0 up to but one hour less than random_days.
		# Note:  random_hours and random_days can both be used and will simply be added together.
	random = 6 # Equivalent to random_hours; preserverd for backwards compatibility.
	random = { chance = 50 ... } # Specify a set of child effects to execute as part of this effect, with a percentage chance of randomly happening or not (as a group, not individually).
	tooltip = news.251.t # Manually specify which tooltip to use for this effect.
}

```

## operative_leader_event

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Fires a operative leader event for owner country.
Example:
operative_leader_event = {
	id = generic.17 # The event to fire.
	# Optional Fields:
	originator = TAG # The originator of the event (default to the owner of the operative)
	recipient = TAG # The recipient of the event (default to the owner of the operative)
	hours = 12 # The number of hours to wait before firing the event.
	days = 5 # The number of days to wait before firing the event.
	months = 1 # The number of months to wait before firing the event, where a month is treated as 30 days.
		# Note:  hours, days, and months can all be used and will simply be added together.
	random_hours = 18 # A random amount of hours to be added to the delay before firing, from 0 up to but not including random_hours.
	random_days = 2 # A random amount of days to be added to the delay before firing, from 0 up to but one hour less than random_days.
		# Note:  random_hours and random_days can both be used and will simply be added together.
	random = 6 # Equivalent to random_hours; preserverd for backwards compatibility.
	random = { chance = 50 ... } # Specify a set of child effects to execute as part of this effect, with a percentage chance of randomly happening or not (as a group, not individually).
	tooltip = generic.17.t # Manually specify which tooltip to use for this effect.
	set_from = TAG # Set the scope of the From in the scripted localization
	set_from_from = TAG # Set the scope of the From.From in the scripted localization
	set_root = TAG # Set the scope of the Root in the scripted localization
}

```

## party_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes children effects on random characters that fulfills the "limit" trigger.
Has to use has_ideology in limit to determine the party (with ideology group)
tooltip=key can be added to override tooltip title

party_leader = {
	limit = { has_ideology = communism }
	set_character_flag = whatever_flag
}
```

## play_song

* Supported Scopes: any
* Supported Targets: none

```
Plays song from database
```

## print_variables

* Supported Scopes: STATE, COUNTRY, CHARACTER
* Supported Targets: none

```
prints all variables in scope and temp variables to a file
Example: print_variables = {
file = log_file
text = header_text
append = yes
print_global = yes
var_list = { a b c } #optional
}
```

## promote_character

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
promotes character to the head of their political party.If this is the ruling party, the character becomes country leader.if the character has several country leader role (i.e. several ideologies), then it is mandatory to provide the ideology to promote.

Example in country scope or scripted effects:
promote_character = GER_erwin_rommel
promote_character = {
  character = GER_erwin_rommel
  ideology = nazism
}


Example in character scope:
promote_character = yes
promote_character = nazism
promote_character = {
  ideology = nazism
}
```

## promote_leader

* Supported Scopes: CHARACTER
* Supported Targets: none

```
promotes general to field marshal
```

## promote_officer_to_general

* Supported Scopes: 
* Supported Targets: none

```
"Promote the officer of the division to a general.
Example:
promote_officer_to_general = yes # yes/no is ignored
"
```

## puppet

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Puppets specified country. By default, cancels the puppets existing war relations.
Example 1:
ENG = {
  puppet = ITA
}
Example 2:
ENG = {
  puppet = {
    target = ITA
    end_wars = yes  # Optional, default yes. Will not cancel non-civil wars if set to no.
    end_civil_wars = yes  # Optional, default yes. Will not cancel civil wars if set to no.
  }
}

```

## raid_add_unit_experience

* Supported Scopes: RAID_INSTANCE
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Give experience to the units performing the raid (raid instance scope).

Will give experience to any type of unit assigned to the raid, e.g. divisions or air wings.
The value defines the progress towards the max level, e.g. 0.2 = gain 20% of the experience needed to reach max level.

Can use either an explicit value or a variable

ex.
raid_add_unit_experience = 0.2"
```

## raid_damage_units

* Supported Scopes: RAID_INSTANCE
* Supported Targets: none

```
"Damage the units performing the raid in scope (the attackers inflict losses).

Damage is applied to ground units while damage to plane is defined as the amount of planes lost.
If 'ratio = yes', then all damage / losses are applied as a fraction of the current amount.
For units, damage can be defined through one value 'damage' or separately through 'org_damage' and 'str_damage'

ex:

# Apply 50% damage to units
raid_damage_units = {
	damage = 0.5
	ratio = yes
}

# Apply 10 strength loss and 20 organization loss to units
raid_damage_units = {
	org_damage = 20
	str_damage = 10
}

# Lose 40% of all planes
raid_damage_units = {
	plane_loss = 0.4
	ratio = yes
}

# Lose 5 planes
raid_damage_units = {
	plane_loss = 5
}

"
```

## raid_reduce_project_progress_ratio

* Supported Scopes: STATE
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Reduce progress to the special project in state. Root scope is raid instance scope.
The input value is a ratio of the total needed progress to complete the special project, i.e. a decimal number between 0 and 1.
ex:
# Root scope is raid
state = {
  raid_reduce_project_progress_ratio = 0.1 # Reduces the project progress by 10%
}"
```

## random

* Supported Scopes: any
* Supported Targets: none

```
a random effect
```

## random_active_scientist

* Supported Scopes: any
* Supported Targets: none

```
Executes children effects on random scientists that fulfills the "limit" trigger. tooltip=key can be added to override tooltip title
```

## random_allied_country

* Supported Scopes: COUNTRY
* Supported Targets: none

Executes children effects on a random Allied Country different from the one in scope that fulfills the `limit` trigger.
`tooltip` can be used to override tooltip title (supports [bindable localization](script_concept_documentation.md#bindable-localization)).

### Example
```
ENG = {
	random_allied_country = {
		tooltip = my_loc_key # Optional bindable localization
		limit = my_limit_trigger # Optional
		... country scope effects ...
	}
}
```


## random_army_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on a random Army Leader of the country in scope, that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
ex: GER = {
  random_army_leader = {
	tooltip = my_loc_key # Optional
	include_invisible = yes # Optional - default = no
    ... character scope effects ...
  }
}"
```

## random_character

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes children effects on random characters that fulfills the "limit" trigger. tooltip=key can be added to override tooltip title
```

## random_controlled_state

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes children effects on random controlled state that fulfills the "limit" trigger. 
prioritize = { <stateID> <stateID> } to pick those states first if they fulfull the limit
```

## random_core_state

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes children effects on random core state that fulfills the "limit" trigger. 
prioritize = { <stateID> <stateID> } to pick those states first if they fulfull the limit
```

## random_country

* Supported Scopes: any
* Supported Targets: none

```
Executes children effects on random country that fulfills the "limit" trigger.
```

## random_country_division

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes children effects on a random division that fulfill the "limit" trigger. tooltip=key can be added to override tooltip title
```

## random_country_with_original_tag

* Supported Scopes: any
* Supported Targets: none

```
Executes children effects on a random country with original tag. Example:
random_country_with_original_tag = { 
  original_tag_to_check = ENG # the effect will only run on countries that has this original tag 
  limit = { always = yes } # a limit can be defined to limit scopes
  # ... effects to execute 
}
```

## random_enemy_country

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes children effects on random enemy country that fulfills the "limit" trigger.
```

## random_list

* Supported Scopes: any
* Supported Targets: none

```
Picks a random effect from the list based on the weight associated.
The weight can be a variable valid in the current scope.
Example:
random_list = {
	# enable logging the dice role in game.log
	log = yes
	seed = var_name/const/random #if specified, it will use this seed instead of scope seed for picking a random
	# some effect with an associated weight
	10 = { add_political_power=10 }
	10 = { add_political_power=100 }
	some_var = { add_political_power=1000 }
}
```

## random_military_industrial_organization

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on a random Military Industrial Organisation of the country in scope, that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
ex: GER = {
  random_military_industrial_organization = {
	tooltip = my_loc_key # Optional
	include_invisible = yes # Optional - default = no
    ... MIO scope effects ...
  }
}"
```

## random_navy_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on a random Navy Leader of the country in scope, that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
ex: GER = {
  random_navy_leader = {
	tooltip = my_loc_key # Optional
	include_invisible = yes # Optional - default = no
    ... character scope effects ...
  }
}"
```

## random_neighbor_country

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes children effects on random neighbor country that fulfills the "limit" trigger.
```

## random_neighbor_state

* Supported Scopes: STATE
* Supported Targets: none

```
Executes children effects on random neighbor state that fulfills the "limit" trigger.
```

## random_occupied_country

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes children effects on random occupied country that fulfills the "limit" trigger.
```

## random_operative

* Supported Scopes: COUNTRY, OPERATION
* Supported Targets: none

```
Executes children effects on a random operatives that fulfills the "limit" trigger.
```

## random_other_country

* Supported Scopes: any
* Supported Targets: none

```
Executes children effects on random country that fulfills the "limit" trigger. Excludes current country
```

## random_owned_controlled_state

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes children effects on random owned and controlled state that fulfills the "limit" trigger.
prioritize = { <stateID> <stateID> } to pick those states first if they fulfull the limit
```

## random_owned_state

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes children effects on random owned state that fulfills the "limit" trigger. 
prioritize = { <stateID> <stateID> } to pick those states first if they fulfull the limit
```

## random_purchase_contract

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on a random purchase contract of the country in scope, that fulfills the \"limit\" trigger.
tooltip = key need to be added to override the tooltip title.
ex: GER = {
  random_purchase_contract = {
	limit = { ... contract scope triggers ... }
	tooltip = my_loc_key # Optional
    ... Purchase Contract scope effects ...
  }
}"
```

## random_scientist

* Supported Scopes: any
* Supported Targets: none

```
Executes children effects on random scientists that fulfills the "limit" trigger. tooltip=key can be added to override tooltip title
```

## random_scope_in_array

* Supported Scopes: any
* Supported Targets: any

```
Runs the effect for a random element in array
Example: random_scope_in_array = {
	array = array_name
	limit = { ... trigger ... } a trigger to limit scopes
	break = break_name #optional (default 'break') set this temp variable to non zero to break the loop
 #effect 1
 #effect 2 ...
}
```

## random_state

* Supported Scopes: any
* Supported Targets: none

```
Executes children effects on a random state that fulfills the "limit" trigger.
State ids can be specified with the "prioritize" attribute and they will be
picked first if they fulfill the trigger.

```

## random_state_division

* Supported Scopes: STATE
* Supported Targets: CAPITAL

```
Executes children effects on a random division that fulfill the "limit" trigger on a state. tooltip=key can be added to override tooltip title
```

## random_subject_country

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Executes child effects on random subject country that fulfills the limit.
```

## random_unit_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Executes children effects on a random Unit Leader of the country in scope, that fulfills the \"limit\" trigger.
tooltip=key can be added to override tooltip title.
ex: GER = {
  random_unit_leader = {
	tooltip = my_loc_key # Optional
	include_invisible = yes # Optional - default = no
    ... character scope effects ...
  }
}"
```

## randomize_temp_variable

* Supported Scopes: any
* Supported Targets: none

```
Randomize a temporary variable
randomize_temp_variable = num_dogs
# which is equivalient to
randomize_temp_variable = {
  var = num_dogs
  distribution = uniform
}
# which is equivalent to
randomize_temp_variable = {
  var = num_dogs
  distribution = uniform
  min = 0
  max = 1
}
# also allow for binomial distribution (with N=2)randomize_temp_variable = {
  var = num_dogs
  distribution = binomial
  min = 0               # optional
  max = 10              # required if min is specified
}
# also allow for the poisson distributionrandomize_temp_variable = {
  var = num_dogs
  distribution = poisson
  lambda = 10           # required
  min = 10              # optional
}

```

## randomize_variable

* Supported Scopes: any
* Supported Targets: none

```
refer to randomize_temp_variable
```

## randomize_weather

* Supported Scopes: any
* Supported Targets: any

```
Randomize weather effect
```

## recall_attache

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Scope country recalls attache from target country. Example: GER = { recall_attache = CHI } means Germany recalls attache from China.
```

## recall_volunteers_from

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
The scoped in country recall the volunteers sent to the target country.
Example:
# FRA recalls the volunteers it sent to SPR
FRA = { recall_volunteers_from = SPR }

```

## recruit_character

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Attach a character to a country. Must be in country scope.

Example:
GER = { recruit_character = GER_Character_token }

```

## release

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
releases specified country as a puppet using your owned states
```

## release_autonomy

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
releases specified country with specified level of autonomy.
Example:
ENG = { 
 release_autonomy = { 
  target = RAJ 
  autonomy_state = autonomy_puppet 
  freedom_level = 0.5 
  release_non_owned_controlled = yes # default no. if yes you will release states you only control as well  force_change_controller_for_non_ally_controlled = yes # default = no. if yes it will change the controller of the states you or your allies don't control (ie if an enemy occupying it, the ownership will change but not controller) }
}
```

## release_on_controlled

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
releases specified country as a puppet using your owned or controlled states
```

## release_puppet

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
releases specified country as puppet using states you own
```

## release_puppet_on_controlled

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
releases specified country as puppet using states you own or control
```

## remove_advisor_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
remove advisor role to character

Example:
remove_advisor_role = {
	character = "GER_Character_Token" # optional if inside character scope
	slot = air_chief}

```

## remove_all_power_balance_modifiers

* Supported Scopes: any
* Supported Targets: none

```
removes all static modifiers from power balance

Example:
remove_all_power_balance_modifiers = {
	id = power_balance_id
}
```

## remove_building

* Supported Scopes: STATE, COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Removes a building in a targeted state or province.
Example:

remove_building = {
	type = air_base
	level = 1 # how many levels to remove
	state = 32 # or a variable like var:target_state
}

The building can also be specified through tags.
Example:
remove_building = {
	tags = facility # can be a single tag or a { }-wrapped list of tags
	level = 1 # how many levels to remove
	province = 500 # or a variable like var:target_province
}

You can manually specify either a state or province as per the examples above. Both values and variables are supported.
The effect can also be called without specifying province or state if used within a state scope:

remove_building = {
	type = air_base
	level = 1 # how many levels to remove
}

In this case, the building type must be a state building.

Note that this effect will NOT recursively find province buildings from a state when no province has been specified.
"
```

## remove_civil_war_target

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Removes a country as a civil war target (removed from both sides)

Example:
remove_civil_war_target = TAG
```

## remove_claim_by

* Supported Scopes: STATE
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Removes state claim by country.
```

## remove_contested_owner

* Supported Scopes: STATE, COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

Removes a contested owner to a state.
The effect can be used either from a country or a state scope and accepts the other as parameter.
The effect is localized with a localization environment containing `Country` and `State`.

### Example
The following example has the same end result and localization.
```
42 = {
	remove_contested_owner = GER
}
GER = {
	remove_contested_owner = 42
}
```
Standard scope accessors can also be used:
```
### Assuming current scope is a state and FROM is a country scope
remove_contested_owner = FROM
```


## remove_core_of

* Supported Scopes: STATE
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Removes state as core of country
```

## remove_country_leader_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
Remove country leader role from character.
Example:
remove_country_leader_role = {
	character = "GER_Character_Token" # optional if inside character scope
	ideology = socialism
}

```

## remove_country_leader_trait

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
Remove country leader trait from the scoped character or scoped country's leader.
In scoped character, will need to give the ideology if the character has several country leader roles.
Example 1: SOV_joseph_stalin = { remove_country_leader_trait = underage_monarch }
Example 2: HUN_miklos_horthy = { remove_country_leader_trait = { ideology = oligarchism trait = anti_communist } }
Example 3: SOV = { remove_country_leader_trait = underage_monarch }
```

## remove_decision

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Remove specified active decision for scope country - Does not run the remove_effect or put the decision on cooldown. Ignores fire_only_once
```

## remove_decision_on_cooldown

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Removes decision on cooldown to reactivate or remove. 
Example: remove_decision_on_cooldown = some_decision_here
```

## remove_dynamic_modifier

* Supported Scopes: STATE, COUNTRY, CHARACTER, SPECIAL_PROJECT
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"removes a dynamic modifier from the containing scope (country / state / unit-leader / special-project).
example :
remove_dynamic_modifier = {
  modifier = dynamic_modifier_name
  scope = GER # optional, must match the scope input used in add_dynamic_modifier (if any)
}"
```

## remove_exile_tag

* Supported Scopes: CHARACTER
* Supported Targets: none

```
remove exile tag from scope unit leader. remove_exile_tag = yes
```

## remove_from_array

* Supported Scopes: any
* Supported Targets: none

```
Removes an element from an array using value or index
Example: remove_from_array = {
	array = array_name
	value = 42 #optional, use index or this. if neither it removes last element
	index = 3 #optional, use value or this. if neither it removes last element
}
#shorter usage: remove_from_array = { array_name = 42 }
```

## remove_from_faction

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
removes specified country from faction
```

## remove_from_tech_sharing_group

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Removes country from technology sharing group of specified name.
Example: remove_from_tech_sharing_group = commonwealth_research
```

## remove_from_temp_array

* Supported Scopes: any
* Supported Targets: none

```
Removes an element from a temporary array using value or index
Example: remove_from_temp_array = {
	array = array_name
	value = 42 #optional, use index or this. if neither it removes last element
	index = 3 #optional, use value or this. if neither it removes last element
}
#shorter usage: remove_from_temp_array = { array_name = 42 }
```

## remove_ideas

* Supported Scopes: COUNTRY
* Supported Targets: none

```
remove idea(s) from country
```

## remove_ideas_with_trait

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Remove all ideas with specified trait from country
```

## remove_mission

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Removes mission without running complete or timeout effects. 
Example: remove_mission = some_mission_here
```

## remove_operation_token

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Remove a specific token against against another country
remove_operation_token = {
	tag = GER
	token = some_token_id
}
```

## remove_opinion_modifier

* Supported Scopes: COUNTRY
* Supported Targets: any

```
Remove opinion modifier from target
```

## remove_power_balance

* Supported Scopes: COUNTRY
* Supported Targets: none

```
removes power balance from country

Example:
remove_power_balance = {
	id = power_balance_id
}
```

## remove_power_balance_modifier

* Supported Scopes: any
* Supported Targets: none

```
removes static modifier from power balance

Example:
remove_power_balance_modifier = {
	id = power_balance_id
	modifier = static_modifier_id # this must be defined in the static modifier database
}
```

## remove_province_modifier

* Supported Scopes: STATE
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Removes a static modifiers to specified province
remove_province_modifier = {
	static_modifiers = { mod_1 mod_2 }
Select 1 province:
	province = 500
Or use:
	province = {
		id = 500 id = 501 id = 502 (evaluate for specified provinces)
		all_provinces (includes all in current state)
		limit_to_coastal (only coastal provinces)
		limit_to_border (only provinces bordering different country)
		limit_to_naval_base (only provinces with a naval base)
		limit_to_victory_point (only provinces with a VP)
	}
}
```

## remove_relation_modifier

* Supported Scopes: COUNTRY
* Supported Targets: THIS

```
Removes a static modifier between current scope and target
Example: add_relation_modifier = {
	target = TAG # target of the relation
	modifier = static_modifier_name_here #Name of the modifier added
	}
}
```

## remove_relation_rule_override

* Supported Scopes: COUNTRY
* Supported Targets: THIS

```
Removes an override rule to the country's relation to other countries.The desc key can be used to supply a custom description for the effect when a named trigger is used as key
Alternative 1:
remove_relation_rule_override = { 
 target = GER # [Required] Target country can_not_declare_war = yes 
}
Alternative 2:
remove_relation_rule_override = { 
 trigger = is_democratic_country # [Required] Named trigger can_not_declare_war = yes 
}

```

## remove_resistance_target

* Supported Scopes: STATE
* Supported Targets: any

```
removes a previously added resistance target using its id. No tooltips are generated.:
remove_resistance_target = 42

```

## remove_resource_rights

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Remove resource right to state for scope country. remove_resource_rights = ID
```

## remove_scientist_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
"Remove the scientist role from a character.The character can come from the scope or from an input parameter.
The scientist role format is the same as in the character DB.
Except the visible trigger - a scientist role created via effect cannot have triggers.
Examples:
# From character scope
my_character = {
	remove_scientist_role = yes
}

# From country scope
SOV = {
	remove_scientist_role = {
		character = my_character / var:my_char_var / PREV # accepts variables and keywords
	}
}"
```

## remove_state_claim

* Supported Scopes: COUNTRY
* Supported Targets: none

```
remove claim on state
```

## remove_state_core

* Supported Scopes: COUNTRY
* Supported Targets: none

```
remove core on state
```

## remove_targeted_decision

* Supported Scopes: STATE, COUNTRY
* Supported Targets: none

```
Removes targeted decisions or mission. 
Example: remove_targeted_decision = { target = TAG decision = decision_id_here
```

## remove_trait

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
remove trait from specified list to character.
remove_trait = {
	character = GER_character_token # optional if inside character scope
	trait = brilliant_strategist
	slot = political_advisor #Only required for updating advisor
	ideology = fascism_ideology #Only required for updating country leader
}
```

## remove_unit_leader

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
remove a unit leader ( remove_unit_leader=ID )
```

## remove_unit_leader_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
Remove unit leader role to character

Example:
remove_corps_commander_role = {
	character = GER_Character_token 
}
remove_corps_commander_role = yes # inside a character scope

```

## remove_unit_leader_trait

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Remove trait from unit leader
Example: SOV_konstantin_rokossovsky = { remove_unit_leader_trait = media_personality }
```

## remove_wargoal

* Supported Scopes: COUNTRY
* Supported Targets: none

```
removes war goal type targetting nation targetExample:
remove_wargoal = {
	type = take_state
	target = FRA
}
```

## replace_unit_leader_trait

* Supported Scopes: CHARACTER
* Supported Targets: none

```
add trait to unit leader
```

## reseed_division_commander

* Supported Scopes: 
* Supported Targets: none

```
reseed_division_commander = 9999 [Debug & Testing Effect]
```

## reserve_dynamic_country

* Supported Scopes: COUNTRY
* Supported Targets: any

```
reserves a dynamic country so it won't be recycled for civil wars. A dynamic country with no owned states must be reserved after it is created and unreserved once it is no longer going to be used. example :
reserve_dynamic_country = yes
reserve_dynamic_country = no

```

## reset_province_name

* Supported Scopes: any
* Supported Targets: none

```
reset name of a province back to localization one.
```

## reset_state_name

* Supported Scopes: STATE
* Supported Targets: none

```
reset_state_name = yes - Resets the current states name to the original one
```

## resize_array

* Supported Scopes: any
* Supported Targets: none

```
Resizes array
Example: resize_array = {
	array = array_name
	value = 42 #optional, if not specified and array grows the new elements are set to this (default 0)
	size = 3 #if higher than old size, new elements are added to end. otherwise last elements are removed to match to new size
}
#shorter usage: resize_array = { array_name = 3 }
```

## resize_temp_array

* Supported Scopes: any
* Supported Targets: none

```
Resizes a temp array
Example: resize_temp_array = {
	array = array_name
	value = 42 #optional, if not specified and array grows the new elements are set to this (default 0)
	size = 3 #if higher than old size, new elements are added to end. otherwise last elements are removed to match to new size
}
#shorter usage: resize_temp_array = { array_name = 3 }
```

## retire

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Retires character, use in character scope
```

## retire_character

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Un-assigns a character from a nation and all its corresponding jobs, advisor, unit leader, country leader

Example:
retire_character = GER_Character_Token

```

## retire_country_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
retires a country leader and removes him as leader of his party, making the next in line the new party and country leader
```

## retire_ideology_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
kills a ideology leader and removes him completely, making the next in line the new party leader
```

## reverse_add_opinion_modifier

* Supported Scopes: COUNTRY
* Supported Targets: any

```
Add opinion modifier(s) to target(s)
```

## round_temp_variable

* Supported Scopes: any
* Supported Targets: none

```
Rounds a temporary variable
Example: round_temp_variable = num_dogs
```

## round_variable

* Supported Scopes: any
* Supported Targets: none

```
Rounds a variable
Example: round_variable = num_dogs
```

## save_event_target_as

* Supported Scopes: any
* Supported Targets: none

```
save an event target
```

## save_global_event_target_as

* Supported Scopes: any
* Supported Targets: none

```
save a global event target
```

## scoped_play_song

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Plays song from database only on in current scope's player
```

## scoped_sound_effect

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Plays sound effect only on in current scope's player
```

## send_embargo

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
embargos specified tag
```

## send_equipment

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Sends to target scope specified amount of equipment.
```

## send_equipment_fraction

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Sends to target scope specified fraction of equipment.
Example:
send_equipment_fraction = {
	target = FROM
	value = 0.3 # Clamped in code to the range [0,1].
}
```

## set_air_oob

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Registers an Order of Battle (OOB) file to be loaded for a country at game start, replacing any previously registered OOB (with key "air") on that country.
Only intended to be used within history files.

Example:
set_air_oob = "ENG_1936_Air"
```

## set_autonomy

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
makes autonomy of specified level and country.
Example:
set_autonomy = {
  target=ENG 
  autonomy_state = autonomy_puppet 
  freedom_level=0.5 
  end_wars  = yes # default yes. will not cancel non-civil wars if set to no
  end_civil_wars = yes # default yes. will not cancel civil wars if set to no
}
```

## set_border_war

* Supported Scopes: STATE
* Supported Targets: none

```
starts a border war in a state with neighbouring state that also has border war
```

## set_border_war_data

* Supported Scopes: any
* Supported Targets: none

```
update border war properties
```

## set_building_level

* Supported Scopes: STATE
* Supported Targets: none

```
Sets specific level of a building construction for amount of levels in specified state or province
```

## set_can_be_fired_in_advisor_role

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
"Set the value (yes/no) to the "can be fired" flag in Advisor Role. When set to No, the advisor cannot be fired once hired.

Example:
some_country_scope = {
  set_can_be_fired_in_advisor_role = {
    character = my_character_token # or keyword, variable...
    slot = political_advisor # mandatory if the character has several advisor role
    value = no
  }
}

some_character_scope = {
  set_can_be_fired_in_advisor_role = {
    slot = political_advisor # mandatory if the character has several advisor role
    value = no
  }
}"
```

## set_capital

* Supported Scopes: COUNTRY
* Supported Targets: none

```
move capital to state
Example:
set_capital = {
	state = 1234
	remember_old_capital = no #default = yes
}
```

## set_character_flag

* Supported Scopes: CHARACTER
* Supported Targets: none

```
set character flag
```

## set_character_name

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
"set name for the target character. Either localization key or direct name.
example:
set_character_name = {
	character = my_character # optional, use if not in a character scope
	name = my_name # either loc key or direct name
}
my_character = {
	set_character_name = my_name # only possible in character scope
}
```

## set_collaboration

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Sets the collaboration in a target country with our currently scoped country
GER = {
  set_collaboration = {
    target = POL
    value = 0.3
  }
}

```

## set_compliance

* Supported Scopes: STATE
* Supported Targets: any

```
set compliance of a state. Example: set_compliance = 30
```

## set_cosmetic_tag

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Sets country cosmetic tag.
Example: INS = { set_cosmetic_tag = IN1 }
```

## set_country_flag

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set country flag
```

## set_country_leader_description

* Supported Scopes: COUNTRY
* Supported Targets: any

```
changes the description of country leader. no tooltip is generated
set_country_leader_name = {
  ideology = neutrality # can be ommitted. if so it will change the portrait of current ruler
  desc = "DESC_KEY"
}
```

## set_country_leader_ideology

* Supported Scopes: COUNTRY
* Supported Targets: none

```
change the ideology of active leader
```

## set_country_leader_name

* Supported Scopes: COUNTRY
* Supported Targets: any

```
changes the name of country leader. no tooltip is generated
set_country_leader_name = {
  ideology = neutrality # can be ommitted. if so it will change the name of current ruler
  name = "James Boned"
}
```

## set_country_leader_portrait

* Supported Scopes: COUNTRY
* Supported Targets: any

```
changes the portrait of country leader. no tooltip is generated
set_country_leader_name = {
  ideology = neutrality # can be ommitted. if so it will change the portrait of current ruler
  portrait = "GFX_portrait_italy_emperor_mussolini"
}
```

## set_demilitarized_zone

* Supported Scopes: STATE
* Supported Targets: none

```
sets the demilitarized status for currently scoped state
```

## set_division_force_allow_recruiting

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Force allows division recruiting for a division template
Example: set_division_force_allow_recruiting = { division_template = <name> force_allow_recruiting = <bool (default:yes)> }
```

## set_division_template_cap

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Set division cap for a division template
Example: set_division_template_cap = { division_template = <name> division_cap = <int (default:1)> }
```

## set_division_template_lock

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Set lock status for a division template
Example: set_division_template_lock = { division_template = <name> is_locked = <bool (default:true)> }
```

## set_entity_animation

* Supported Scopes: any
* Supported Targets: any

```
sets the rotation of existing entity
set_entity_animation = {
  id = 123 # id of entity 
  animation = "shoot_lasers" 
}
```

## set_entity_movement

* Supported Scopes: any
* Supported Targets: any

```
sets the position & rotation of an existing entity using two coordinates
set_entity_movement = {
  id = 123 # id of entity 
  start = { 
    # position can be set using following 
    x = 42 
    y = 21 
    province = 123 
    state = 42 
    z = 3 #if wanted you can specify a z to shift height of the entity
  } 
  target = { 
    # position can be set using following 
    x = 42 
    y = 21 
    province = 123 
    state = 42 
    z = 3 #if wanted you can specify a z to shift height of the entity
  } 
  ratio = 0.5 # a ratio in between 0 - 1. the entity is positioned in between start & target position using this ratio 
  rotation = 1.2 # angle in radio, entity is rotated using the direction and this angle is added after that 
}
```

## set_entity_position

* Supported Scopes: any
* Supported Targets: any

```
sets the position of existing entity
set_entity_position = {
  id = 123 # id of entity 
  # position can be set using following 
  x = 42 
  y = 21 
  province = 123 
  state = 42 
  z = 3 #if wanted you can specify a z to shift height of the entity
}
```

## set_entity_rotation

* Supported Scopes: any
* Supported Targets: any

```
sets the rotation of existing entity
set_entity_rotation = {
  id = 123 # id of entity 
  rotation = 0.23 # angle in radians 
}
```

## set_entity_scale

* Supported Scopes: any
* Supported Targets: any

```
sets the scale of existing entity
set_entity_scale = {
  id = 123 # id of entity 
  scale = 5.0 
}
```

## set_equipment_fraction

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Modify all equipments by factor
```

## set_equipment_version_number

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"![MD]
Changes current version number for a given equipment type to N.
The next equipment variant created from that type will have version number N+1.

#### Example
```
set_equipment_version_number = {
	type = small_plane_airframe_1
	version = 4
}
```
"
```

## set_faction_leader

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set current country as leader of its faction
```

## set_faction_name

* Supported Scopes: STATE, COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
set_faction_name = NEW_LOC_KEY. Sets the faction name to whatever the new key localises to.
```

## set_faction_spymaster

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set current country as spy master of its faction
```

## set_fuel

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set fuel for country
```

## set_fuel_ratio

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Set country's current fuel ratio relative to its capacity
```

## set_garrison_strength

* Supported Scopes: STATE
* Supported Targets: any

```
set initial garrison strength. Example: set_garrison_strength = 0.5
```

## set_global_flag

* Supported Scopes: any
* Supported Targets: none

```
set global flag
```

## set_keyed_oob

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Registers an Order of Battle (OOB) file to be loaded for a country at game start, replacing any previously registered OOB (with the given key) on that country.
Only intended to be used within history files.

Example:
set_keyed_oob = {
	key = naval
	name = "ENG_1936_Naval"
}
```

## set_leader_description

* Supported Scopes: CHARACTER
* Supported Targets: any

```
changes the description of unit leader. no tooltip is generated
set_leader_description = "DESC_KEY"

```

## set_leader_name

* Supported Scopes: CHARACTER
* Supported Targets: any

```
changes the name of unit leader. no tooltip is generated
set_leader_name = "James Boned"

```

## set_leader_portrait

* Supported Scopes: CHARACTER
* Supported Targets: any

```
changes the portrait of unit leader. no tooltip is generated
set_leader_portrait = "GFX_portrait_italy_emperor_mussolini"

```

## set_legitimacy

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set_legitimacy = 10. Sets legitimacy on scope country to specified value. Value has to be 0-100.
```

## set_major

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Sets mandatory major country flag. A country can still become a major if their industry is strong enough and they are not a subject.
Example:
DEN = { set_major = yes }
```

## set_mio_design_team_assign_cost

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Set the daily PP cost to assign to research in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Input value cannot be negative.
ex:
mio:my_mio = {
  set_mio_design_team_assign_cost = 0.3
  set_mio_design_team_assign_cost = var:my_number_var
}"
```

## set_mio_design_team_change_cost

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Set the XP cost to change MIO in equipment designer for the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Input value cannot be negative.
ex:
mio:my_mio = {
  set_mio_design_team_change_cost = 3
  set_mio_design_team_change_cost = var:my_number_var
}"
```

## set_mio_flag

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: none

```
"Set flag in the military industrial organization in scope.
ex:
var:my_mio_var = {
  set_mio_flag = my_flag
  set_mio_flag = {
    flag = my_flag (mandatory)
	value = 3 (optional, default = 1)
    days = 12 (optional, default = 0. if > 0, the flag will be deleted after this number of days)
  }
}"
```

## set_mio_funds

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Set the amount of funds for the military industrial organization in scope.
Input value cannot be negative.
If the new total funds go over the Size Up limit, the MIO will gain size(s).
ex:
var:my_mio_var = {
  set_mio_funds = 100
  set_mio_funds = var:my_number_var
}"
```

## set_mio_funds_gain_factor

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Set the factor applied when gaining funds in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Input value cannot be negative.
ex:
mio:my_mio = {
  set_mio_funds_gain_factor = 0.9
  set_mio_funds_gain_factor = var:my_number_var
}"
```

## set_mio_icon

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Set the icon GFX for the military industrial organization in scope.
ex:
mio:my_mio = {
  set_mio_icon = MY_NEW_MIO_ICON_GFX
}"
```

## set_mio_industrial_manufacturer_assign_cost

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Set the daily PP cost to assign to production line in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Input value cannot be negative.
ex:
mio:my_mio = {
  set_mio_industrial_manufacturer_assign_cost = 0.3
  set_mio_industrial_manufacturer_assign_cost = var:my_number_var
}"
```

## set_mio_name_key

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Set the localisation key used to generate the name of the military industrial organization in scope.
The localisation key may be a scripted localisation (triggers evaluated in MIO scope).
ex:
mio:my_mio = {
  set_mio_name_key = MY_NEW_MIO_NAME_KEY
}"
```

## set_mio_policy_cooldown

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Set the base cooldown (in days) after attaching a policy in the MIO policy, found in country in scope with input policy
token. This changes the base value. Modifiers will still apply over it. 
Input value cannot be negative.
ex:
SOV = {
  set_mio_policy_cooldown = {
	policy = my_policy_token
	value = 3
  }
  set_mio_policy_cooldown = {
	policy = my_policy_token
	value = var:my_number_var
  }
}"
```

## set_mio_policy_cost

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Set the base cost (in PP) for attaching a policy in the MIO policy, found in country in scope with input policy
token. This changes the base value. Modifiers will still apply over it. 
Input value cannot be negative.
ex: 
SOV = { 
  set_mio_policy_cost = { 
	policy = my_policy_token
	value = 3
  }
  set_mio_policy_cost = {
	policy = my_policy_token
	value = var:my_number_var
  }
}"
```

## set_mio_research_bonus

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Set the research bonus in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Input value cannot be negative.
ex:
mio:my_mio = {
  set_mio_research_bonus = 0.3
  set_research_bonus = var:my_number_var
}"
```

## set_mio_size_up_requirement_factor

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Set to the factor applied to funds required to size up in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Input value cannot be negative.
ex:
mio:my_mio = {
  set_mio_size_up_requirement_factor = 0.9
  set_mio_size_up_requirement_factor = var:my_number_var
}"
```

## set_mio_task_capacity

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Set the maximum task capacity in the military industrial organization in scope.
This changes the base value. Modifiers will still apply over it.
Input value cannot be negative.
If the capacity is reduced and the MIO becomes over-assigned, the current tasks will be allowed.
It's only later that the player will feel the new restrictions.
ex:
mio:my_mio = {
  set_mio_task_capacity = 3
  set_mio_task_capacity = var:my_number_var
}"
```

## set_nationality

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
Transfer from one country to another for the character in scope.
Note that this is not related to operative nationalities added via add_nationality.
Note that for operative, this will temporarily lock their slot on the country of origin.

Examples:
SOV = { # origin country
	my_character = {
	set_nationality = POL # target country
}
SOV = { # origin country
	set_nationality = {
		target_country = POL
		character = my_character
	}
}

```

## set_naval_oob

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Registers an Order of Battle (OOB) file to be loaded for a country at game start, replacing any previously registered OOB (with key "naval") on that country.
Only intended to be used within history files.

Example:
set_naval_oob = "ENG_1936_Naval"
```

## set_occupation_law

* Supported Scopes: STATE, COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"Sets the occupation law for an occupied country, occupied state, or the default occupation law of an occupying country.

- If THIS is a country and it's the same as the PREV country, then THIS's default law is set.
- If THIS is a country and it's different from the PREV country, then PREV's country law override for THIS is set.
- If THIS is a state, then PREV's state law override for THIS is set.

The token default_law is used to remove a country or state override, or to set a country's default law to the law defined with starting_law=yes.

Example:
GER = { set_occupation_law = foreign_civilian_oversight }
GER = { POL = { set_occupation_law = default_law } }
GER = { 123 = { set_occupation_law = military_governor_occupation } }"
```

## set_occupation_law_where_available

* Supported Scopes: STATE, COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
"See set_occupation_law for basic functionality. What differentiates this effect is that if the law is not available on the given level it will attempt to set it on a level below. I.e. if the law can't be set as the default law it will try to set it on each country, and if that fails it will try to set it on each state. Any existing law overrides below a level at which a law is successfully set will be cleared.

Example:
ITA = { set_occupation_law_where_available = colonial_police } # Set law in all countries/states where it's available.
ITA = { every_occupied_country = { set_occupation_law_where_available = default_law } } # Remove all country and state overrides."
```

## set_oob

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Registers an Order of Battle (OOB) file to be loaded for a country at game start, replacing any previously registered OOB (with no key) on that country.
Only intended to be used within history files.

Example:
set_oob = "ENG_1936"
```

## set_party_name

* Supported Scopes: COUNTRY
* Supported Targets: none

```
change partyname for an ideology in a country
```

## set_party_rule

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Adds rule to the country's party.
set_party_rule = { 
 ideologly = communism # [Required] selection criteria for the party desc = desc_key # a description can be given to rule (you can get original tooltip using DESC key) 
 can_not_declare_war = yes 
}
```

## set_political_party

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set popularity of a political party

Example:
set_political_party = {
	ideology = neutrality
	popularity = 50
}
```

## set_political_power

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set political power for country
```

## set_politics

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set_politics: 
ruling_party = key of new ruling ideology
elections_allowed = yes/no
optional (renames the ruling party and displays correct loc):
long_name = loc_key
name = loc_key
```

## set_popularities

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set popularities for all ideologies in a country. If an ideology is not specified its popularity will be set to zero. The popularities specified must add up to exactly 100

Example:
set_popularities = {
	neutrality = 54.5
	fascism = 45.5
}
```

## set_portraits

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: none

```
set portraits for the target character. Syntax is similar to character files.

example:
set_portraits = {
		character = my_character # optional, use if not in a character scope		army = { small ="MySmallCharacterGFX"}
		civilian = { large ="MyLargeCharacterGFX" }
}

```

## set_power_balance

* Supported Scopes: COUNTRY
* Supported Targets: none

```
sets active power balance for country or sets parameters of the already active power balance

Example:
set_power_balance = {
	id = power_balance_id
	left_side = left_side_id
	right_side = right_side_id
	set_default = yes/no # default = no
	set_value = 0.5 # if used, will set the new value of the power balance
}
```

## set_power_balance_gfx

* Supported Scopes: any
* Supported Targets: none

```
sets gfx for power balance side

Example:
set_power_balance_gfx = {
	id = power_balance_id
	side = power_balance_side_id
	gfx = gfx_name
}
```

## set_project_flag

* Supported Scopes: SPECIAL_PROJECT
* Supported Targets: none

```
set project flag
```

## set_province_controller

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
set controller for province
```

## set_province_name

* Supported Scopes: any
* Supported Targets: none

```
set_province_name = { id = <province id> name = <string> } - Set name for a province
```

## set_relation_rule

* Supported Scopes: COUNTRY
* Supported Targets: THIS

```
DEPRECATED: See add_relation_rule_override
```

## set_research_slots

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Sets the number of research slots
```

## set_resistance

* Supported Scopes: STATE
* Supported Targets: any

```
set resistance of a state. Example: set_resistance = 30
```

## set_rule

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Adds rule to country. This one overrides all other rules on country 
set_rule = { 
 desc = desc_key # A description of why the rule is set (you can get original tooltip using DESC key) 
 can_not_declare_war = yes 
}
```

## set_stability

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Sets the stability to the country in scope. Example: set_stability = 80
```

## set_state_category

* Supported Scopes: STATE
* Supported Targets: none

```
Sets the category of a state
Example: set_state_category = large_town
```

## set_state_controller

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set controller for state
```

## set_state_controller_to

* Supported Scopes: STATE
* Supported Targets: THIS

```
Set controller of a state to a given country
Example:\n"
USA {
	random_core_state = {
		set_state_controller_to = JAM
	}
}

```

## set_state_flag

* Supported Scopes: STATE
* Supported Targets: none

```
set state flag
```

## set_state_name

* Supported Scopes: STATE
* Supported Targets: none

```
set_state_name = <string> - Set the current states name
```

## set_state_owner

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set owner for state
```

## set_state_owner_to

* Supported Scopes: STATE
* Supported Targets: THIS

```
Set owner of a state to a given country
Example:\n"
USA {
	random_core_state = {
		set_state_owner_to = JAM
	}
}

```

## set_state_province_controller

* Supported Scopes: STATE
* Supported Targets: any

```
sets the controller of provinces belong to a state and fullfils a condition. no tooltip is built
set_state_province_controller = { 
 controller = ITA
  limit = { 
     # will be checked old controller of each province. will only update controller if true
  } 
}
```

## set_technology

* Supported Scopes: COUNTRY
* Supported Targets: none

```
sets technology level(s) on country. example : set_technology = { 
	infantry_weapons = 1 
	infantry_weapons1 = 1 
	infantry_weapons2 = 1 
	improved_infantry_weapons = 1 
	popup = no # default is yes. if set to no, no pop up will display for player 
}
```

## set_temp_variable

* Supported Scopes: any
* Supported Targets: none

```
Sets a temp variable to a value or another variable
Example: set_temp_variable = {
var = num_dogs
	value = 42
	tooltip = loc_str_id_with_LEFT_and_RIGHT  #localized text with LEFT and RIGHT tokens in it, tokens will replaced by values
}
```

## set_temp_variable_to_random

* Supported Scopes: any
* Supported Targets: none

```
sets a temp variable to a random value. example 
set_temp_variable_to_random = num_dogs #sets num_dogs a random value between [0, 1) 
set_temp_variable_to_random = { 
	var = num_dogs #variable to set 
	min = 5 #default 0. value will be set in between [min, max) 
	max = 10 #default 1. value will be set in between [min, max) 
	integer = yes #default no. if yes the number value will be an integer 
} 

```

## set_truce

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Sets a truce between scope country and target for days duration. 
Example set_truce = { target = GER days = 90 }
```

## set_unit_leader_flag

* Supported Scopes: CHARACTER
* Supported Targets: none

```
set unit leader flag
This effect is deprecated in favor of set_character_flag.
```

## set_unit_organization

* Supported Scopes: 
* Supported Targets: none

```
set unit organization to current * value: set_unit_organization = 0.5, values between 0 and 1
```

## set_variable

* Supported Scopes: any
* Supported Targets: none

```
Sets a variable to a value or another variable
Example: set_variable = {
var = num_dogs
	value = 42
	tooltip = loc_str_id_with_LEFT_and_RIGHT  #localized text with LEFT and RIGHT tokens in it, tokens will replaced by values
}
```

## set_variable_to_random

* Supported Scopes: any
* Supported Targets: none

```
sets a variable to a random value. example 
set_variable_to_random = num_dogs #sets num_dogs a random value between [0, 1) 
set_variable_to_random = { 
	var = num_dogs #variable to set 
	min = 5 #default 0. value will be set in between [min, max) 
	max = 10 #default 1. value will be set in between [min, max) 
	integer = yes #default no. if yes the number value will be an integer 
} 

```

## set_victory_points

* Supported Scopes: any
* Supported Targets: any

```
sets victory points for a province
set_victory_points = {
  province = 42
  value = 5
}
```

## set_war_support

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Sets the war support to the country in scope. Example: set_war_support = 80
```

## show_ideas_tooltip

* Supported Scopes: COUNTRY
* Supported Targets: none

```
show what idea does
```

## show_mio_tooltip

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Show the name of the input MIO with the name of the initial trait (if any)
ex:
SOV = {
	show_mio_tooltip = my_mio_token
	show_mio_tooltip = var:my_mio_var
}"
```

## show_unit_leaders_tooltip

* Supported Scopes: COUNTRY
* Supported Targets: none

```
show unit leader's name
```

## sound_effect

* Supported Scopes: any
* Supported Targets: none

```
Plays sound effect
```

## start_border_war

* Supported Scopes: any
* Supported Targets: none

```
start a border war between two states. Example:
start_border_war = {
	change_state_after_war = no #overrides the transfer of state at the end of war
	combat_width = 80 #combat width for border war
	minimum_duration_in_days = 14 #minimum duration for combat
	attacker = {
		state = 527 # state to start border war
		num_provinces = 4 #number of provinces we want border war to be
		on_win = japan_border_conflict.2 #effect to call if wins
		on_lose = japan_border_conflict.3 #effect to call if loses
		on_cancel = japan_border_conflict.4 #effect to call if cancels
		leader_score = { #score for selecting a leader
			base = 1
			modifier = {
				check_variable = { likes_border_wars = 1 }
				add = 2
			}
		}
		modifier = 0.5 #combat modifier (default value: 0.0)
		dig_in_factor = 0.5 #dig in modifier factor (default value: 1.0)
		terrain_factor = 0.5 #terrain modifier factor(default value: 1.0)
	}
	
	defender = {
		state = 408 # state to start border war
		num_provinces = 4 #number of provinces we want border war to be
		on_win = japan_border_conflict.2 #effect to call if wins
		on_lose = japan_border_conflict.3 #effect to call if loses
		on_cancel = japan_border_conflict.4 #effect to call if cancels
	}
}

```

## start_civil_war

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

Given ideology starts a civil war in the country.

For 'keep triggers', the scope is :
THIS = Character
FROM = Target country

Example :
```
start_civil_war = {
	ideology = revolting ideology
	ruling_party = ruling party for country
	size = 0-1 Size modifier of the revolt. Affects stockpile, army, air and navy as well
	army_ratio = 0-1 Overrides size modifier for army
	navy_ratio = 0-1 Overrides size modifier for navy
	air_ratio = 0-1 Overrides size modifier for air
	states = {...} States that go to the revolter. Use \"all\" to include all states.
	states_filter = {...} States that go to the revolter. Filtering trigger on the states scripted to go to the revolter.
	keep_all_characters = yes - keep all characters on target country side - will ignore all following keep_ parameters - default value = no
	keep_unit_leaders = {...} specify ID of unit leaders that remain with the original country
	keep_unit_leaders_trigger = {...} Trigger for unit leaders to remain with the original country
	keep_scientists_trigger = {...} Trigger for scientist to remain with the original country
	keep_political_leader = yes/no # optional, default is no; If yes, the party leader of the revolting ideology will not join the revolter as its leader.
	keep_political_party_members = yes/no # optional, default is no; If yes, it will keep the non main leaders of the party leaders in original country
	 ... effect list ... # you can list effects that will run on civil war country
}
```


## start_peace_conference

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Starts a limited peace conference between the two countries if at war. Only the specified loser country and their potential subjects are included as losers in the conference. ROOT is the winner while the target tag is the loser.
Example:
SOV = {
  start_peace_conference = {
    tag = FIN  # main loser
    score_factor = 0.2  # 0-1, the fraction of conference score allocated to winners. Can use a variable like eg PREV.surrender_progress. 0.0 implies a white peace.
    
    # winner_scope and loser_scope can be ALL (all relevant countries), FACTION (members of main country's faction and overlordship), LIMITED_FACTION (faction members if main country is faction leader, and subjects if main country is overlord), and LIMITED (main country and their subjects)
    winner_scope = FACTION  # optional, default is LIMITED_FACTION
    loser_scope = FACTION  # optional, default is LIMITED_FACTION
    message = FIN_agree_peace  # optional, custom message to display in post-conference popup
  }
}
```

## start_resistance

* Supported Scopes: STATE
* Supported Targets: any

```
starts resistance activity for a core country. 
Use along with force_enable_resistance if you are enabling resistance
in a state that is not possible (ie core).
Example : start_resistance = POL or start_resistance = yes
```

## state_event

* Supported Scopes: STATE, COUNTRY
* Supported Targets: none

```
Fires a state event.
Example:
state_event = {
	id = usa.61 # The event to fire.
	# Optional Fields:
	hours = 12 # The number of hours to wait before firing the event.
	days = 5 # The number of days to wait before firing the event.
	months = 1 # The number of months to wait before firing the event, where a month is treated as 30 days.
		# Note:  hours, days, and months can all be used and will simply be added together.
	random_hours = 18 # A random amount of hours to be added to the delay before firing, from 0 up to but not including random_hours.
	random_days = 2 # A random amount of days to be added to the delay before firing, from 0 up to but one hour less than random_days.
		# Note:  random_hours and random_days can both be used and will simply be added together.
	random = 6 # Equivalent to random_hours; preserverd for backwards compatibility.
	random = { chance = 50 ... } # Specify a set of child effects to execute as part of this effect, with a percentage chance of randomly happening or not (as a group, not individually).
	tooltip = usa.61.t # Manually specify which tooltip to use for this effect.
	trigger_for = GER # Indicate which country this state effect applies to. Value can be any of the following:
		# controller - The country that currently controls the state.
		# owner - The country that currently owns the state.
		# occupied - The country that has been occupied in the state by the current controller.
		# from - The country of the from scope.
		# prev - The country of the prev scope.
		# root - The country of the root scope.
		# TAG - A hard-coded country tag such as GER or ENG.
}

```

## steal_random_tech_bonus

* Supported Scopes: COUNTRY
* Supported Targets: none

```
adds a random limited use tech bonus from country of categories that is it ahead in compared to you.
it must have atleast one category or folder. But it can contain any number of them in any combination
Note: if a country does not have a tech to be stolen a random tech bonus will be applied based on base_bonus 
Example: steal_random_tech_bonus = {
	category = air_equipment
	folder = naval_folder
	ahead_reduction = ???
	bonus = ???
	base_bonus = 0.05
	instant = yes # instant unlock instead of bonus
	dynamic = yes # swaps bonus types from instant to category dependig on type as well as uses weights on tech progress
	name = ???
	target = ???
	uses = 1
}

```

## subtract_from_temp_variable

* Supported Scopes: any
* Supported Targets: none

```
Subtracts a value or a variable to a temp variable
Example: subtract_from_temp_variable = {
var = num_dogs
	value = 42
	tooltip = loc_str_id_with_LEFT_and_RIGHT  #localized text with LEFT and RIGHT tokens in it, tokens will replaced by values
}
```

## subtract_from_variable

* Supported Scopes: any
* Supported Targets: none

```
Subtracts a value or a variable to another one
Example: subtract_from_variable = {
var = num_dogs
	value = 42
	tooltip = loc_str_id_with_LEFT_and_RIGHT  #localized text with LEFT and RIGHT tokens in it, tokens will replaced by values
}
```

## supply_units

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Give [hours] of supply to units being controlled by this leader. 
Example supply_units = 24
```

## swap_country_leader_traits

* Supported Scopes: CHARACTER
* Supported Targets: none

```
swap 2 traits on a country leader. 
 Syntax: swap_country_leader_traits = { remove = <trait> add = <trait> [ideology = <ideology>] }
```

## swap_ideas

* Supported Scopes: COUNTRY
* Supported Targets: none

```
swap 2 ideas. 
 Syntax: swap_idea = {
  remove_idea = <idea>
  add_idea = <idea>
  add_days = 10 #optional, will add/subtract duration for new idea that replaces the old one with duration
  days = 25 #optional, will set the duration for the new idea
}
```

## swap_ruler_traits

* Supported Scopes: COUNTRY
* Supported Targets: none

```
swap 2 traits on current ruler. 
 Syntax: swap_ruler_traits = { remove = <trait> add = <trait> }
```

## teleport_armies

* Supported Scopes: STATE
* Supported Targets: any

```
teleport armies in state to another state or province. example :
teleport_armies = { 
  #only define one. if neither is defined will teleport to unit to their capital  to_state = 123 #id of the state to teleport
  to_state_array = array_name #an array of states to teleport (will be randomly picked)
  to_province = 123 #id of the province to teleport

  limit = { 
     # trigger will be checked for owner of armies and will only teleport if true. scope if the owner of the army and prev is the scope that calls teleport_armies
  } 
}
```

## teleport_railway_guns_to_deploy_province

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Teleport the target country's railway guns to the province to which railway guns are deployed.
```

## transfer_navy

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Transfers the entire navy from scope country to target country. Does not support carriers!
Example:
ENG={
	target = NZL
	is_government_in_exile = yes #optional, default is no; the navy will be tagged as exile if this is yes so that it will return to owner if they return from exile.
}
```

## transfer_ship

* Supported Scopes: COUNTRY
* Supported Targets: none

```
Transfers ship from scope country to target country.
Example:
ENG={
  transfer_ship={
    prefer_name = "HMS Achilles"
    type = light_cruiser
    target = NZL
    exclude_refitting = yes #optional, default is no; Exclude ships currently being refitted from the search.
  }
}
```

## transfer_state

* Supported Scopes: COUNTRY
* Supported Targets: none

```
set owner and controller for state
```

## transfer_state_to

* Supported Scopes: STATE
* Supported Targets: THIS

```
Set owner and controller of a state to a given country
Example:\n"
USA {
	every_core_state = {
		transfer_state_to = JAM
	}
}

```

## transfer_units_fraction

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

Transfer units (air, army, navy) to another country.
Also transfer the stockiled equipment (you can set it to zero if it is undesired) as well as unit leaders.

For 'keep  triggers', the scope is :
THIS = Character
FROM = Target country

Example:
```
transfer_units_fraction = {
	target = ROOT          # the recipient
	size = 0.4             # [0,1] Default value for the ratio below if they are not specified
	stockpile_ratio = 0.3  # [0,1] Overrides size modifier for the stockpiled equipment and fuel
	army_ratio = 0.1       # [0,1] Overrides size modifier for army
	navy_ratio = 0.2       # [0,1] Overrides size modifier for navy
	air_ratio = 0.4        # [0,1] Overrides size modifier for air
	keep_unit_leaders = {  # specify IDs of unit leaders that remain with the original country
		700 701
	}
	keep_unit_leaders_trigger = {	# Trigger for unit leaders to remain with the original country
									# THIS is the unit leader being evaluated"
									# ROOT is the recipient"
									# FROM is the sender"
									# PREV is unset"
		[... triggers ...]
	}
}
```


## turn_operative

* Supported Scopes: COUNTRY, CHARACTER
* Supported Targets: THIS, ROOT, PREV, FROM

```
An operative is turned by the specified country.
This transfers the operative to the target country and make it appear as killed to the country of origin (increases the death counter and lock the slot).
This fires the on_action on_operative_death with as killer the target country.
If the target country is the owner of the operative, this has no effect and an error is logged.

WARN: the on_action might execute immediatly, before any effect listed after the occurence of turn_operative.

Examples:
GER = {
    turn_operative = PREV  # where PREV is an operative (unit leader)
    # or
    turn_operative = {
        operative = PREV
    }
}

turn_operative = { turned_by = GER } # where the scope is an unit leader

```

## uncomplete_national_focus

* Supported Scopes: COUNTRY
* Supported Targets: none

```
uncompletes a focus for a country. If specified, the 'on_uncomplete' effect will be executed on each uncompleted focus.
Example: uncomplete_national_focus = {
	focus = GER_oppose_hitler
	uncomplete_children = yes # Optional. Default is no. If yes, all proceeding focuses will also be uncompleted if their prerequisite aren't met after the preceeding focuses are uncompleted.
	refund_political_power = no # Optional. Default is no. If yes, the country is refunded the political power invested in the current focus if it's canceled as a result of its prerequisites being uncompleted.
}

```

## unit_leader_event

* Supported Scopes: CHARACTER
* Supported Targets: none

```
Fires a unit leader event for owner country.
Example:
unit_leader_event = {
	id = generic.17 # The event to fire.
	# Optional Fields:
	hours = 12 # The number of hours to wait before firing the event.
	days = 5 # The number of days to wait before firing the event.
	months = 1 # The number of months to wait before firing the event, where a month is treated as 30 days.
		# Note:  hours, days, and months can all be used and will simply be added together.
	random_hours = 18 # A random amount of hours to be added to the delay before firing, from 0 up to but not including random_hours.
	random_days = 2 # A random amount of days to be added to the delay before firing, from 0 up to but one hour less than random_days.
		# Note:  random_hours and random_days can both be used and will simply be added together.
	random = 6 # Equivalent to random_hours; preserverd for backwards compatibility.
	random = { chance = 50 ... } # Specify a set of child effects to execute as part of this effect, with a percentage chance of randomly happening or not (as a group, not individually).
	tooltip = generic.17.t # Manually specify which tooltip to use for this effect.
}

```

## unlock_decision_category_tooltip

* Supported Scopes: COUNTRY
* Supported Targets: none

```
localizes name of category and displays tooltip that shows it will be unlocked
```

## unlock_decision_tooltip

* Supported Scopes: COUNTRY
* Supported Targets: none

```
show what decision does
Example: unlock_decision_tooltip = some_decision_here
Example:
unlock_decision_tooltip = {
    decision = <some_decision>
    show_effect_tooltip = yes # default is no
    show_modifiers = yes # default is no
}

```

## unlock_military_industrial_organization_tooltip

* Supported Scopes: COUNTRY
* Supported Targets: none

```
"Display a tooltip saying the MIO is made available (aka unlocked).
Accepts MIO token, variables or keywords
ex:
FIN = {
	unlock_military_industrial_organization_tooltip = mio:my_mio_token
	unlock_military_industrial_organization_tooltip = var:my_mio_var
}
"
```

## unlock_mio_policy_tooltip

* Supported Scopes: any
* Supported Targets: none

```
"Display a tooltip saying the MIO policy is made available (aka unlocked).
ex:
unlock_mio_policy_tooltip = my_policy_token
unlock_mio_policy_tooltip = {
	policy = my_policy_token
	show_modifiers = no # show bonuses in tooltip - optional, default = yes
}
"
```

## unlock_mio_trait_tooltip

* Supported Scopes: INDUSTRIAL_ORG
* Supported Targets: none

```
"Display a tooltip saying the trait is made available (aka unlocked).
ex:
mio:my_mio = {
  unlock_mio_trait_tooltip = trait
  unlock_mio_trait_tooltip = {
	trait = my_trait_token
	show_modifiers = no # Optional, default = yes
  }
}"
```

## unlock_national_focus

* Supported Scopes: COUNTRY
* Supported Targets: none

```
unlocks a focus for a country
```

## upgrade_intelligence_agency

* Supported Scopes: COUNTRY
* Supported Targets: none

```
add an upgrade to the Intelligence Agency (must be created):
upgrade_intelligence_agency = upgrade_army_department
```

## while_loop_effect

* Supported Scopes: any
* Supported Targets: any

```
Runs the effect as long as a trigger is true
Example: while_loop_effect = {
	limit = { ... trigger ... } a trigger to test before each iteration
	break = break_name #optional (default 'break') set this temp variable to non zero to break the loop
 #effect 1
 #effect 2 ...
}
```

## white_peace

* Supported Scopes: COUNTRY
* Supported Targets: THIS, ROOT, PREV, FROM, OWNER, CONTROLLER, OCCUPIED, CAPITAL

```
Makes a white peace between the two countries if at war. ROOT is considered the winner while the target tag is considered the loser (which affects things like name of the PC as well as PC related on-actions).
Example:
SOV = {
  white_peace = {
    tag = FIN
    message = FIN_agree_peace
  }
}
```

