# Dynamic Variables

Dynamic variables are read only variables that can be used in effects &
triggers that accept variables.

When they are used, the game will compute and return the value of the dynamic
variable.

## Table of Content

* [global](#dynamic-variables-for-scope-global)
* [country](#dynamic-variables-for-scope-country)
* [state](#dynamic-variables-for-scope-state)
* [unit_leader](#dynamic-variables-for-scope-unit_leader)
* [military_industrial_organization](#dynamic-variables-for-scope-military_industrial_organization)
* [special_project](#dynamic-variables-for-scope-special_project)

## Dynamic variables for scope global

### countries
* description: get array of all countries (including non existing

### date
* description: get date value that can be comparable to other date values and localized using GetDateString/GetDateStringShortMonth/GetDateStringNoHour/GetDateStringNoHourLong scripted locs

### difficulty
* description: check if the difficulty is above or below specified value 0-2 (difficulty enum). Example: difficulty > 0 (above easy)
* (Auto generated using the trigger with same name)

### ideology_groups
* description: array of objects in ideology_groups database

### majors
* description: get array of all majors (including non existing

### num_days
* description: current total days

### num_of_career_profile_points
* description: check amount of gained career points
* (Auto generated using the trigger with same name)

### operations
* description: array of objects in operations database

### pc_turn
* description: Checks turn number in PC.
Example:
pc_turn > 20
* (Auto generated using the trigger with same name)

### power_balance_daily_change
* description: compares current total daily change of a power balance

Example:
power_balance_daily_change = {
	id = power_balance_id
	value > 0.5 # supported operators are: >, < and =
}
* (Auto generated using the trigger with same name)

### power_balance_value
* description: compares current value of a power balance

Example:
power_balance_value = {
	id = power_balance_id
	value > 0.5 # supported operators are: >, < and =
}
* (Auto generated using the trigger with same name)

### power_balance_weekly_change
* description: compares current total weekly change of a power balance

Example:
power_balance_weekly_change = {
	id = power_balance_id
	value > 0.5 # supported operators are: >, < and =
}
* (Auto generated using the trigger with same name)

### province_controllers
* description: get array of all province controllers. Example: province_controllers^4135

### states
* description: get array of all states

### technology
* description: array of objects in technology database

### threat
* description: check the global threat value (world tension). 0-1 value
* (Auto generated using the trigger with same name)

### year
* description: current year

## Dynamic variables for scope country

### agency_upgrade_number
* description: Checks the number of upgrade done in the intelligence agency. 
agency_upgrade_number > 4
* (Auto generated using the trigger with same name)

### ai_attitude_allied_weight
* description: weight for an ai attitude attitude_alliedagainst country. Example: GER.ai_attitude_allied_weight@ENG

### ai_attitude_friendly_weight
* description: weight for an ai attitude attitude_friendlyagainst country. Example: GER.ai_attitude_friendly_weight@ENG

### ai_attitude_hostile_weight
* description: weight for an ai attitude attitude_hostileagainst country. Example: GER.ai_attitude_hostile_weight@ENG

### ai_attitude_is_threatened
* description: returns 1 if ai is threatened

### ai_attitude_neutral_weight
* description: weight for an ai attitude attitude_neutralagainst country. Example: GER.ai_attitude_neutral_weight@ENG

### ai_attitude_outraged_weight
* description: weight for an ai attitude attitude_outragedagainst country. Example: GER.ai_attitude_outraged_weight@ENG

### ai_attitude_protective_weight
* description: weight for an ai attitude attitude_protectiveagainst country. Example: GER.ai_attitude_protective_weight@ENG

### ai_attitude_threatened_weight
* description: weight for an ai attitude attitude_threatenedagainst country. Example: GER.ai_attitude_threatened_weight@ENG

### ai_attitude_wants_ally
* description: returns 1 if ai wants ally

### ai_attitude_wants_antagonize
* description: returns 1 if ai wants antagonize

### ai_attitude_wants_ignore
* description: returns 1 if ai wants ignore

### ai_attitude_wants_protect
* description: returns 1 if ai wants protect

### ai_attitude_wants_weaken
* description: returns 1 if ai wants weaken

### ai_irrationality
* description: check the ai irrationality value
* (Auto generated using the trigger with same name)

### ai_strategy_activate_crypto
* description: ai strategy value activate_crypto against country. Example: GER.ai_strategy_activate_crypto@ENG

### ai_strategy_alliance
* description: ai strategy value alliance against country. Example: GER.ai_strategy_alliance@ENG

### ai_strategy_antagonize
* description: ai strategy value antagonize against country. Example: GER.ai_strategy_antagonize@ENG

### ai_strategy_befriend
* description: ai strategy value befriend against country. Example: GER.ai_strategy_befriend@ENG

### ai_strategy_conquer
* description: ai strategy value conquer against country. Example: GER.ai_strategy_conquer@ENG

### ai_strategy_consider_weak
* description: ai strategy value consider_weak against country. Example: GER.ai_strategy_consider_weak@ENG

### ai_strategy_contain
* description: ai strategy value contain against country. Example: GER.ai_strategy_contain@ENG

### ai_strategy_declare_war
* description: ai strategy value declare_war against country. Example: GER.ai_strategy_declare_war@ENG

### ai_strategy_decrypt_target
* description: ai strategy value decrypt_target against country. Example: GER.ai_strategy_decrypt_target@ENG

### ai_strategy_dont_defend_ally_borders
* description: ai strategy value dont_defend_ally_borders against country. Example: GER.ai_strategy_dont_defend_ally_borders@ENG

### ai_strategy_force_defend_ally_borders
* description: ai strategy value force_defend_ally_borders against country. Example: GER.ai_strategy_force_defend_ally_borders@ENG

### ai_strategy_ignore
* description: ai strategy value ignore against country. Example: GER.ai_strategy_ignore@ENG

### ai_strategy_ignore_claim
* description: ai strategy value ignore_claim against country. Example: GER.ai_strategy_ignore_claim@ENG

### ai_strategy_influence
* description: ai strategy value influence against country. Example: GER.ai_strategy_influence@ENG

### ai_strategy_invade
* description: ai strategy value invade against country. Example: GER.ai_strategy_invade@ENG

### ai_strategy_occupation_policy
* description: ai strategy value occupation_policy against country. Example: GER.ai_strategy_occupation_policy@ENG

### ai_strategy_prepare_for_war
* description: ai strategy value prepare_for_war against country. Example: GER.ai_strategy_prepare_for_war@ENG

### ai_strategy_protect
* description: ai strategy value protect against country. Example: GER.ai_strategy_protect@ENG

### ai_strategy_send_volunteers_desire
* description: ai strategy value send_volunteers_desire against country. Example: GER.ai_strategy_send_volunteers_desire@ENG

### ai_strategy_support
* description: ai strategy value support against country. Example: GER.ai_strategy_support@ENG

### ai_wants_divisions
* description: Will compare towards the amount of divisions an ai wants to have.
* (Auto generated using the trigger with same name)

### air_chief
* description: returns the currently hired air chief of the country

### air_experience
* description: air experience of a country

### air_intel
* description: air intel against a target country. example GER.air_intel@ENG

### alliance_naval_strength_ratio
* description: Compares the estimated naval strength between the scope country, his allies and his enemies.
* (Auto generated using the trigger with same name)

### alliance_strength_ratio
* description: Compares the estimated army strength between the scope country, his allies and his enemies.
* (Auto generated using the trigger with same name)

### allies
* description: array of allies (faction members). prefer using faction_members instead

### amount_manpower_in_deployment_queue
* description: Checks for amount manpower currently in deploymentview. amount_manpower_in_training > 10
* (Auto generated using the trigger with same name)

### amount_research_slots
* description: check number of research current research slots 
 amount_research_slots > 2
* (Auto generated using the trigger with same name)

### any_war_score
* description: compares the warscore of all wars in a country to see if any fullfills the comparison condition 0-100 - Example: any_war_score > 40
* (Auto generated using the trigger with same name)

### army_chief
* description: returns the currently hired army chief of the country

### army_experience
* description: army experience of a country

### army_intel
* description: army intel against a target country. example GER.army_intel@ENG

### army_leaders
* description: all army leaders of a country

### autonomy_ratio
* description: autonomy of scope country. -1 if not a subject

### capital
* description: capital state of the country

### casualties
* description: Check the amount of casualties a country has suffered in all of it's wars
* (Auto generated using the trigger with same name)

### casualties_k
* description: Check the amount of casualties in thousands a country has suffered in all of it's wars
* (Auto generated using the trigger with same name)

### civilian_intel
* description: civilian intel against a target country. example GER.civilian_intel@ENG

### command_power
* description: total command power of country

### command_power_daily
* description: Checks if daily command power increase is more or less that specified value 
 command_power_daily > 1.5
* (Auto generated using the trigger with same name)

### compare_autonomy_progress_ratio
* description: check if autonomy progress ratio is higher than value, example:
compare_autonomy_progress_ratio > 0.5
* (Auto generated using the trigger with same name)

### controlled_states
* description: array of controlled states

### convoy_threat
* description: A trigger to check convoy threat for a country. Controlled by NAVAL_CONVOY_DANGER defines. Returns a value between 0 and 1. Example convoy_threat > 0.5 
* (Auto generated using the trigger with same name)

### core_compliance
* description: returns core compliance of target country

### core_resistance
* description: returns core resistance of target country

### core_states
* description: array of core states

### country_leader
* description: returns the current country leader of the country

### cryptology_defense_level
* description: cryptology defense level of a country

### current_party_ideology_group
* description: returns the token for current party ideology group

### days_decision_timeout
* description: timeout in days for a specific timed decision, decision type token is defined in target. example: days_decision_timeout@SOV_propaganda_knowledge

### days_mission_timeout
* description: timeout in days for a specific timed mission, mission type token is defined in target. example: days_mission_timeout@GER_mefo_bills_mission

### days_since_capitulated
* description: Checks the number of days since the country last capitulated, even if it is no longer capitulated.
	If it has not ever capitulated, the value is extremely large.
	It is recommended to combine this with has_capitulated = yes when you specifically want to ignore non-active capitulations.
Examples:
	HOL = { has_capitulated = yes days_since_capitulated > 60 } # The Netherlands has been capitulated for more than two months
	FRA = { has_capitulated = yes days_since_capitulated < 21 } # France has capitulated sometime within the past three weeks
	GER = { OR = { has_capitulated = no days_since_capitulated > 14 } } # Germany is not both actively and recently capitulated

* (Auto generated using the trigger with same name)

### decryption_progress
* description: checks decryption ratio against a country. Example: 
decryption_progress = { 
 target = GER
 value > 0.5
} 
#or decryption_progress@GER as variable

* (Auto generated using the trigger with same name)

### decryption_speed
* description: total encryption strength of a country that is needed

### deployed_airforce_manpower_k
* description: total deployed air manpower of country in thousands. Does not include exile manpower

### deployed_army_manpower_k
* description: total deployed army manpower of country in thousands.

### deployed_navy_manpower_k
* description: total deployed navy manpower of country in thousands.

### deployed_total_manpower_k
* description: total deployed manpower of country in thousands.

### encryption_strength
* description: total encryption strength of a country that is needed

### enemies
* description: array of enemies at war with

### enemies_naval_strength_ratio
* description: Compares the estimated navy strength between the scope country and all its enemies
* (Auto generated using the trigger with same name)

### enemies_of_allies
* description: array of enemies of allies

### enemies_strength_ratio
* description: Compares the estimated army strength between the scope country and all its enemies
* (Auto generated using the trigger with same name)

### exiles
* description: exile host of this country

### faction_leader
* description: faction leader of this country's faction

### faction_members
* description: array of faction members

### foreign_manpower
* description: check the amount of foreign garrison manpower we have
* (Auto generated using the trigger with same name)

### fuel_k
* description: total fuel of country in thousands

### fuel_ratio
* description: Compares the fuel ratio to a variable.
Example: fuel_ratio > 0.5
* (Auto generated using the trigger with same name)

### garrison_manpower_need
* description: check the amount of manpower needed by garrisons
* (Auto generated using the trigger with same name)

### has_added_tension_amount
* description: Compare if the country has added above or below the specified ammount of tension
* (Auto generated using the trigger with same name)

### has_bombing_war_support
* description: check value of bombing malus to war support 0-1: Example has_bombing_war_support < 0.1
* (Auto generated using the trigger with same name)

### has_casualties_war_support
* description: check value of casualties malus to war support 0-1: Example has_casualties_war_support < 0.1
* (Auto generated using the trigger with same name)

### has_collaboration
* description: checks the collaboration in a target country with our currently scoped country. Example: 
has_collaboration = { 
 target = GER
 value > 0.5
} 
#or has_collaboration@GER as variable

* (Auto generated using the trigger with same name)

### has_convoys_war_support
* description: check value of convoys sunk malus to war support 0-1: Example has_convoys_war_support < 0.1
* (Auto generated using the trigger with same name)

### has_legitimacy
* description: Check scope country legitimacy 0-100: Example has_legitimacy < 60
* (Auto generated using the trigger with same name)

### has_manpower
* description: check amount of manpower
* (Auto generated using the trigger with same name)

### has_political_power
* description: check amount of political power
* (Auto generated using the trigger with same name)

### has_stability
* description: check value of stability 0-1: Example has_stability < 0.6
* (Auto generated using the trigger with same name)

### has_war_support
* description: check value of war_support 0-1: Example has_war_support < 0.6
* (Auto generated using the trigger with same name)

### high_command
* description: returns an array with the currently hired high command of the country

### highest_party_ideology
* description: ideology of the most popular party. Can exclude the ruling party by using @exclude_ruling_party. Example: highest_party_ideology OR highest_party_ideology@exclude_ruling_party

### highest_party_popularity
* description: popularity size of the most popular party [0.00, 1.00]. Can exclude the ruling party by using @exclude_ruling_party. Example: highest_party_popularity OR highest_party_popularity@exclude_ruling_party

### host
* description: exile host of this country

### land_doctrine_level
* description: checks researched land doctrine level
* (Auto generated using the trigger with same name)

### legitimacy
* description: legitimacy of scope country. -1 if not an exile

### longest_war_length
* description: Check number of months the country has been at war
* (Auto generated using the trigger with same name)

### manpower
* description: DEPRECATED, MAY OVERFLOW. total manpower of country

### manpower_k
* description: total manpower of country in thousands

### manpower_per_military_factory
* description: Number of available manpower per factory the country has. Excluding dockyards.
manpower_per_military_factory < 1000
* (Auto generated using the trigger with same name)

### max_available_manpower
* description: DEPRECATED, MAY OVERFLOW. total available manpower of country

### max_available_manpower_k
* description: total available manpower of country in thousands

### max_fuel_k
* description: max fuel of country in thousands

### max_manpower
* description: DEPRECATED, MAY OVERFLOW. maximum manpower of country

### max_manpower_k
* description: maximum manpower of country in thousands

### mine_threat
* description: A trigger to check how dangerous enemy mines are for a country. Controlled by NAVAL_MINE_DANGER defines. Returns a value between 0 and 1. Example mine_threat > 0.5 
* (Auto generated using the trigger with same name)

### modifier
* description: a modifier stored in country scope

### navy_chief
* description: returns the currently hired navy chief of the country

### navy_experience
* description: navy experience of a country

### navy_intel
* description: navy intel against a target country. example GER.navy_intel@ENG

### navy_leaders
* description: all navy leaders of a country

### neighbors
* description: array of neighbors

### neighbors_owned
* description: array of neighbors to owned states

### network_national_coverage
* description: checks network national coverage you have over a country. Example: 
network_national_coverage = { 
 target = GER
 value > 0.5
} 

* (Auto generated using the trigger with same name)

### num_armies
* description: number of armies

### num_armies_in_state
* description: number of armies in state, state is in target. example num_armies_in_state@123

### num_armies_with_type
* description: number of armies with dominant type, dominant type is defined in target. example: num_armies_with_type@light_armor

### num_battalions
* description: number of battalions

### num_battalions_with_type
* description: number of battalions with sub unit type, sub unit type is defined in target. example: num_battalions_with_type@light_armor

### num_controlled_states
* description: number of controlled states

### num_core_states
* description: number of core states

### num_deployed_planes
* description: number of deployed planes

### num_deployed_planes_with_type
* description: number of deployed planes with equipment type. example num_deployed_planes_with_type@fighter

### num_divisions
* description: Will compare towards the amount of divisions a country has control over, if strength matters use has_army_size.
* (Auto generated using the trigger with same name)

### num_equipment
* description: number of equipment in country. example num_equipment@infantry_equipment

### num_equipment_in_armies
* description: number of equipment in armies of the country, equipment type token is defined in target. example num_equipment_in_armies@infantry_equipment

### num_equipment_in_armies_k
* description: number of equipment in armies of the country in thousands, equipment type token is defined in target. example num_equipment_in_armies_k@infantry_equipment

### num_faction_members
* description: Compares the number of members in the faction for the current country. 
 Example: num_faction_members > 10
* (Auto generated using the trigger with same name)

### num_fake_intel_divisions
* description: Will compare towards the amount of fake intel divisions a country has control over. .
* (Auto generated using the trigger with same name)

### num_free_operative_slots
* description: Checks the number of operative a country can recruit right now.
Note that this is not necessarily greater than zero if num_operative_slots returned a number greater than the number of operative.
* (Auto generated using the trigger with same name)

### num_nukes_being_dropped
* description: total number of nukes that are currently ready to be dropped
* (Auto generated using the trigger with same name)

### num_nukes_left_to_drop
* description: number of nukes left to drop during this game tick (only useful in-between nuke drops, like in on_nuke_drop on-action, for example)
* (Auto generated using the trigger with same name)

### num_occupied_states
* description: check the number of states occupied by nation
* (Auto generated using the trigger with same name)

### num_of_available_civilian_factories
* description: check amount of available civilian factories
* (Auto generated using the trigger with same name)

### num_of_available_military_factories
* description: check amount of available military factories
* (Auto generated using the trigger with same name)

### num_of_available_naval_factories
* description: check amount of available naval factories
* (Auto generated using the trigger with same name)

### num_of_civilian_factories
* description: check amount of civilian factories
* (Auto generated using the trigger with same name)

### num_of_civilian_factories_available_for_projects
* description: check amount of civilian factories available for a new project to use
* (Auto generated using the trigger with same name)

### num_of_civilian_factories_in_cores
* description: calculates the number of civilian factories on core states of current country scope, on those states that are under control of @Tag <Tag | ROOT | my_var> example num_of_civilian_factories_in_cores@GER

### num_of_controlled_factories
* description: check the number of factories in controlled states excluding any gained or lost through trade, relations, modifiers etc.
* (Auto generated using the trigger with same name)

### num_of_controlled_states
* description: check amount of controlled stats
* (Auto generated using the trigger with same name)

### num_of_factories
* description: Check amount of available factories (excluding temporary sources like trade and lend-lease)
Example:
GER = { num_of_factories < 50 }
* (Auto generated using the trigger with same name)

### num_of_military_factories
* description: check amount of military factories
* (Auto generated using the trigger with same name)

### num_of_military_factories_in_cores
* description: calculates the number of civilian factories on core states of current country scope, on those states that are under control of @Tag  <Tag | ROOT | my_var> example num_of_military_factories_in_cores@GER

### num_of_naval_factories
* description: check amount of naval factories
* (Auto generated using the trigger with same name)

### num_of_naval_factories_in_cores
* description: calculates the number of civilian factories on core states of current country scope, on those states that are under control of @Tag  <Tag | ROOT | my_var> example num_of_naval_factories_in_cores@my_var

### num_of_nukes
* description: check amount of nukes
* (Auto generated using the trigger with same name)

### num_of_operatives
* description: Checks the number of operatives the country controls
* (Auto generated using the trigger with same name)

### num_of_owned_factories
* description: check the number of factories in owned states excluding any gained or lost through trade, relations, modifiers etc.
* (Auto generated using the trigger with same name)

### num_of_supply_nodes
* description: check amount of supply nodes
* (Auto generated using the trigger with same name)

### num_operative_slots
* description: Checks the number of available operative slots a country has.
If this differs from the number of operative, this does not mean the country can recruit an operative, but that it will eventually be able to.
* (Auto generated using the trigger with same name)

### num_orders_groups
* description: number of orders groups

### num_owned_controlled_states
* description: number of owned and core states

### num_owned_states
* description: number of owned states

### num_researched_technologies
* description: Number of researched technologies
* (Auto generated using the trigger with same name)

### num_ships
* description: number of ships

### num_ships_with_type
* description: number of ships controlled in country, ship type is defined in target. example num_ships_with_type@carrier. can be a sub unit def type or one of carrier,capital,screen, submarine

### num_subjects
* description: check the number of subjects of nation
* (Auto generated using the trigger with same name)

### num_target_equipment_in_armies
* description: number of equipment required in armies of the country, equipment type token is defined in target. example num_target_equipment_in_armies@infantry_equipment

### num_target_equipment_in_armies_k
* description: number of equipment required in armies of the country in thousands, equipment type token is defined in target. example num_target_equipment_in_armies_k@infantry_equipment

### num_tech_sharing_groups
* description: checks how many groups a nation is a member of
* (Auto generated using the trigger with same name)

### occupied_countries
* description: array of occupied countries

### operatives
* description: all operatives of a country

### opinion
* description: opinion of a country targeted on another one. example GER.opinion@ENG

### original_research_slots
* description: check number of research slots at start of game
* (Auto generated using the trigger with same name)

### original_tag
* description: returns the original tag of a country

### overlord
* description: master of this subject

### owned_controlled_states
* description: array owned and core states

### owned_states
* description: array of owned states

### party_popularity
* description: popularity of targeted party [0.00, 1.00]. example party_popularity@democratic. May also target ruling_party. This also supports country variables, so you can party_popularity@my_var_name for variables that store ideologies

### party_popularity_100
* description: popularity of targeted party [0.00, 100.00]. example party_popularity_100@democratic. May also target ruling_party. This also supports country variables, so you can party_popularity_100@my_var_name for variables that store ideologies

### pc_current_score
* description: Checks country's total peace conference score. Only usable if the country is on the winning side.
Example:
CZE = { pc_current_score > 400 }
* (Auto generated using the trigger with same name)

### pc_total_score
* description: Checks country's total peace conference score. Only usable if the country is on the winning side.
Example:
CZE = { pc_total_score > 400 }
* (Auto generated using the trigger with same name)

### political_advisor
* description: returns an array with the currently hired political advisors of the country

### political_power
* description: total political power of country

### political_power_daily
* description: Checks if daily political power increase is more or less that specified value 
 political_power_daily > 1.5
* (Auto generated using the trigger with same name)

### political_power_growth
* description: Check the value of political power daily growth.Exacmple: political_power_growth > 0
* (Auto generated using the trigger with same name)

### potential_and_current_enemies
* description: array of potential and actual enemies

### power_balance_daily
* description: current total power balance daily change

### power_balance_value
* description: current power balance value

### power_balance_weekly
* description: current total power balance weekly change

### researched_techs
* description: returns the array of researched technologies

### resource
* description: number of surplus resources in country, resource type is defined in target resource@steel

### resource_consumed
* description: number of resources consumed by country, resource type is defined in target resource_consumed@steel

### resource_exported
* description: number of resources exported by country, resource type is defined in target resource_exported@steel

### resource_imported
* description: number of resources imported by country, resource type is defined in target resource_imported@steel

### resource_produced
* description: number of resources produced by country, resource type is defined in target. example resource_produced@steel

### stability
* description: stability of a country

### subjects
* description: array of subjects

### surrender_progress
* description: check if a country is close to surrendering
* (Auto generated using the trigger with same name)

### theorist
* description: returns the currently hired theorist of the country

### total_constructed_air_base
* description: Total constructions of air_base

### total_constructed_anti_air
* description: Total constructions of anti_air

### total_constructed_civilian_factory
* description: Total constructions of civilian_factory

### total_constructed_dockyard
* description: Total constructions of dockyard

### total_constructed_fuel_silo
* description: Total constructions of fuel_silo

### total_constructed_gun_emplacement
* description: Total constructions of gun_emplacement

### total_constructed_infrastructure
* description: Total constructions of infrastructure

### total_constructed_land_fort
* description: Total constructions of land_fort

### total_constructed_military_factory
* description: Total constructions of military_factory

### total_constructed_naval_fort
* description: Total constructions of naval_fort

### total_constructed_nuclear_reactor
* description: Total constructions of nuclear_reactor

### total_constructed_other
* description: Total constructions of other

### total_constructed_port
* description: Total constructions of port

### total_constructed_radar
* description: Total constructions of radar

### total_constructed_refinery
* description: Total constructions of refinery

### total_constructed_rocket_site
* description: Total constructions of rocket_site

### total_constructed_supply_node
* description: Total constructions of supply_node

### total_equipment_produced_
* description: Total produced equipment of type

### total_equipment_produced_air_transport
* description: Total produced equipment of typeair_transport

### total_equipment_produced_amphibious
* description: Total produced equipment of typeamphibious

### total_equipment_produced_anti_air
* description: Total produced equipment of typeanti_air

### total_equipment_produced_anti_tank
* description: Total produced equipment of typeanti_tank

### total_equipment_produced_armor
* description: Total produced equipment of typearmor

### total_equipment_produced_artillery
* description: Total produced equipment of typeartillery

### total_equipment_produced_ballistic_missile
* description: Total produced equipment of typeballistic_missile

### total_equipment_produced_capital_ship
* description: Total produced equipment of typecapital_ship

### total_equipment_produced_carrier
* description: Total produced equipment of typecarrier

### total_equipment_produced_cas
* description: Total produced equipment of typecas

### total_equipment_produced_convoy
* description: Total produced equipment of typeconvoy

### total_equipment_produced_emplacement_gun_ammo
* description: Total produced equipment of typeemplacement_gun_ammo

### total_equipment_produced_fighter
* description: Total produced equipment of typefighter

### total_equipment_produced_flame
* description: Total produced equipment of typeflame

### total_equipment_produced_floating_harbor
* description: Total produced equipment of typefloating_harbor

### total_equipment_produced_heavy_fighter
* description: Total produced equipment of typeheavy_fighter

### total_equipment_produced_infantry
* description: Total produced equipment of typeinfantry

### total_equipment_produced_interceptor
* description: Total produced equipment of typeinterceptor

### total_equipment_produced_land_cruiser
* description: Total produced equipment of typeland_cruiser

### total_equipment_produced_maritime_patrol_plane
* description: Total produced equipment of typemaritime_patrol_plane

### total_equipment_produced_mechanized
* description: Total produced equipment of typemechanized

### total_equipment_produced_missile
* description: Total produced equipment of typemissile

### total_equipment_produced_missile_launcher
* description: Total produced equipment of typemissile_launcher

### total_equipment_produced_motorized
* description: Total produced equipment of typemotorized

### total_equipment_produced_naval_bomber
* description: Total produced equipment of typenaval_bomber

### total_equipment_produced_nuclear_missile
* description: Total produced equipment of typenuclear_missile

### total_equipment_produced_railway_gun
* description: Total produced equipment of typerailway_gun

### total_equipment_produced_rocket
* description: Total produced equipment of typerocket

### total_equipment_produced_sam_missile
* description: Total produced equipment of typesam_missile

### total_equipment_produced_scout_plane
* description: Total produced equipment of typescout_plane

### total_equipment_produced_screen_ship
* description: Total produced equipment of typescreen_ship

### total_equipment_produced_strategic_bomber
* description: Total produced equipment of typestrategic_bomber

### total_equipment_produced_submarine
* description: Total produced equipment of typesubmarine

### total_equipment_produced_suicide
* description: Total produced equipment of typesuicide

### total_equipment_produced_support
* description: Total produced equipment of typesupport

### total_equipment_produced_tactical_bomber
* description: Total produced equipment of typetactical_bomber

### total_equipment_produced_train
* description: Total produced equipment of typetrain

## Dynamic variables for scope state

### arms_factory_level
* description: military factory level in the state

### building_level
* description: building level of a building with type, uses target as building type. example building_level@arms_factory

### compliance
* description: Compares the current compliance level of a state to a value. Example: compliance > 50 
* (Auto generated using the trigger with same name)

### compliance_speed
* description: Compares the current compliance speed of a state to a value. Example: compliance_speed > 50 
* (Auto generated using the trigger with same name)

### controller
* description: controller of the state

### core_countries
* description: countries that cores the state

### damaged_building_level
* description: damaged building level of a building with type, uses target as building type. example damaged_building_level@arms_factory

### days_since_last_strategic_bombing
* description: Checks the days since last strategic bombing.
days_since_last_strategic_bombing < 10

* (Auto generated using the trigger with same name)

### distance_to
* description: distance to another state, uses target as another state. example: 123.distance_to@124

### industrial_complex_level
* description: civilian factor level in the state

### infrastructure_level
* description: infrastructure level in the state

### modifier
* description: value of modifier stored in this state, uses target as modifier token, example: 123.modifier@local_manpower

### non_damaged_building_level
* description: non damaged building level of a building with type, uses target as building type. example non_damaged_building_level@arms_factory

### owner
* description: owner of the state

### resistance
* description: Compares the current resistance level of a state to a value. Example: resistance > 50 
* (Auto generated using the trigger with same name)

### resistance_speed
* description: Compares the current resistance speed of a state to a value. Example: resistance_speed > 50 
* (Auto generated using the trigger with same name)

### resistance_target
* description: Compares the target resistance level of a state to a value. Example: resistance_target > 50 
* (Auto generated using the trigger with same name)

### resource
* description: resources produced in state. example resource@steel

### state_and_terrain_strategic_value
* description: Checks for state strategic value
* (Auto generated using the trigger with same name)

### state_population
* description: check the population in the state
* (Auto generated using the trigger with same name)

### state_population_k
* description: check the population in the state in thousands (use to avoid variable overflows)
* (Auto generated using the trigger with same name)

### state_strategic_value
* description: Checks for state strategic value
* (Auto generated using the trigger with same name)

## Dynamic variables for scope unit_leader

### army_attack_level
* description: attack level of the leader

### army_defense_level
* description: defense level of the leader

### attack_level
* description: attack level of the leader

### attack_skill_level
* description: Compares attack skill level of a unit leader.
Example: attack_skill_level > 5
* (Auto generated using the trigger with same name)

### average_stats
* description: average stats of unit leader

### avg_combat_status
* description: average progress of all combats

### avg_defensive_combat_status
* description: average progress of defensive combats

### avg_offensive_combat_status
* description: average progress of offensive combats

### avg_unit_planning_ratio
* description: average planning ratio of all units

### avg_units_acclimation
* description: average unit acclimatization for a specific climate, acclimatization type is defined in target. example avg_units_acclimation@cold_climate

### coordination_level
* description: coordination level of the leader

### defense_level
* description: defense level of the leader

### defense_skill_level
* description: Compares defense skill level of a unit leader.
Example: defense_skill_level > 5
* (Auto generated using the trigger with same name)

### has_orders_group
* description: 1 if leader has orders group, zero otherwise

### intel_yield_factor_on_capture
* description: Rate at which intel is extracted from this operative by an enemy country.

### leader_modifier
* description: value of a modifier stored in leader modifier, modifier token is defined in target. example leader_modifier@navy_max_range

### logistics_level
* description: logistics level of the leader

### logistics_skill_level
* description: Compares logistics skill level of a unit leader.
Example: logistics_skill_level > 5
* (Auto generated using the trigger with same name)

### maneuvering_level
* description: maneuvering level of the leader

### num_armored
* description: number of units with armored dominant type

### num_artillery
* description: number of units with artillery dominant type

### num_assigned_traits
* description: number of assigned traits the leader has

### num_basic_traits
* description: number of basic traits a leader has

### num_battalions
* description: number of battalions

### num_battalions_with_type
* description: number of battalions with sub unit type, sub unit type is defined in target. example: num_battalions_with_type@light_armor

### num_battle_plans
* description: number of battle plans of unit leader

### num_cavalry
* description: number of units with cavalry dominant type

### num_equipment
* description: number of equipment in army of a leader, equipment type token is defined in target. example num_equipment@infantry_equipment

### num_infantry
* description: number of units with infantry dominant type

### num_max_traits
* description: number of maximum assignable traits a leader can have

### num_mechanized
* description: number of units with mechanized dominant type

### num_motorized
* description: number of units with motorized dominant type

### num_personality_traits
* description: number of personality traits a leader has

### num_rocket
* description: number of units with rocket dominant type

### num_ships
* description: number of ships controlled by leader

### num_ships_with_type
* description: number of ships controlled by leader, ship type is defined in target. example num_ships_with_type@carrier

### num_special
* description: number of units with special dominant type

### num_status_traits
* description: number of status traits a leader has

### num_target_equipment
* description: number of equipment required in army of a leader, equipment type token is defined in target. example num_target_equipment@infantry_equipment

### num_terrain_traits
* description: number of terrain traits a leader has

### num_traits
* description: number of traits a leader has

### num_units
* description: number of units controlled by leader

### num_units_crossing_river
* description: number of units currently passing through a river

### num_units_defensive_combats
* description: number of units in defensive combats

### num_units_defensive_combats_on
* description: number of units that are defensively fighting on a terrain, terrain type is defined as target. example: num_units_defensive_combats_on@plains

### num_units_in_combat
* description: number of units current fighting

### num_units_in_state
* description: number of units controlled by leader in state, state is in target. example num_units_in_state@123

### num_units_offensive_combats
* description: number of units in offensive combats

### num_units_offensive_combats_against
* description: number of units that are offensively fighting against a terrain, terrain type is defined as target. example: num_units_offensive_combats_against@plains

### num_units_on_climate
* description: number of units that are on an acclimatization required location, acclimatization type is defined in target. example num_units_on_climate@hot_climate

### num_units_with_type
* description: number of units with dominant type controlled by leader, dominant type is defined in target. example: num_units_with_type@light_armor

### operation_country
* description: the country location the operative is assigned. 0 if it is not assigned to a country

### operation_state
* description: the state location the operative is assigned. 0 if it is not assigned to a state

### operation_type
* description: returns the operation token the operative is assigned

### operative_captor
* description: returns the country tag that captured the operative

### own_capture_chance_factor
* description: The chance this operative has to be captured, taking into account the country it is operating for and the country it is operating against.

### own_forced_into_hiding_time_factor
* description: The time factor applied to the status "forced into hiding". Takes into account the country it is operating for and the country it is operating against.

### own_harmed_time_factor
* description: The time factor applied to the status "harmed". Takes int accountthe country it is operating for and the country it is operating against.

### planning_level
* description: planning level of the leader

### planning_skill_level
* description: Compares planning skill level of a unit leader.
Example: planning_skill_level > 5
* (Auto generated using the trigger with same name)

### skill
* description: compare leader skill levels
* (Auto generated using the trigger with same name)

### skill_level
* description: skill level of the leader

### sum_unit_terrain_modifier
* description: sum of terrain modifiers of each army's location, terrain type is defined in target. example: sum_unit_terrain_modifier@sickness_chance 

### unit_modifier
* description: value of a modifier stored in unit modifier, modifier token is defined in target. example unit_modifier@army_attack_factor

### unit_ratio_ready_for_plan
* description: ratio of units that are ready for plan

## Dynamic variables for scope military_industrial_organization

### funds
* description: Funds of the military industrial organization

### max_task_capacity
* description: Maximum task capacity of the military industrial organization.

### modifier
* description: Value of the modifier stored in the military industrial organization.
ex: modifier@military_industrial_organization_research_bonus

### number_of_currently_assigned_tasks
* description: Number of tasks the military industrial organization is currently assigned to

### number_of_unlocked_traits
* description: Number of unlocked traits of the military industrial organization.

### number_of_unused_trait_points
* description: Number of unused trait points of the military industrial organization

### research_bonus
* description: Research bonus of the military industrial organization when assigned to a research slot

### size
* description: Size of the military industrial organization

## Dynamic variables for scope special_project

### facility_province_id
* description: The province that the project is researched in

### facility_state
* description: State that the project is researched in

### scientist
* description: The scientist that researches the project

