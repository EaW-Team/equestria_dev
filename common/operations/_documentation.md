# Operations

```
Definition: SCOPE_OPERATION
------------------------------------------
FROM = the target country of the operation
ROOT = the origin country of the operation
------------------------------------------
```

Every operation needs a `<unique id>`, which is `operation_test` in this case
```
operation_test = {

	#
	# Visuals
	#

	icon = GFX_operation_test_icon

	# [[scripted localization]]
	name = "Operation: Mole Invasion"

	# [[scripted localization]]
	desc = "Deep in the jungles of Luxembourg the mole population is revolting and prepares to invade neighbouring countries"

	# Priority determines in which order they are listed from the list of operations in the Intelligence Agency window
	# The higher the number the earlier in the list it will be
	priority = 15

	#
	# Every operation needs a duration in days that it takes to execute it
	#
	
	days = 15

	# The danger level the target country will perceived once this operation is initiated (default = 0)
	danger_level = 5

	#
	# The number of operatives requires to be assigned to an operation for it to start
	#
	
	operatives = 2

	#
	# Every operation has a hard requirement of network strength in the target country
	# Integer [0-100]
	#
	
	network_strength = 100

	#
	# This is where all the separate phases are defined
	# There can be any number of phases, they will be evenly split over the total duration of the operation
	#
	
	phases = {
		# Each phase for an operation may have a single actual phase assigned to it, which is determined here
		# Every <phase id> can have a base chance as well as any number of modifiers
		phase_test = { base = 10 }
		phase_1 = {
			modifier = {
				factor = 0
			}
			modifier = {
				add = 10
			}
			base = 90
		}
	}
	phases = {
		phase_1 = { base = 100 }
	}

#########################
## OPTIONAL BELOW HERE ##
#########################

	#
	# Behaves like any other ai_will_do
	# IF the total weight factor falls below OPERATION_AI_MINIMUM_SCORE
	# THEN the AI will cancel the operation if it was currently planning it
	#
	
	ai_will_do = {
		factor = 11
	}

	#
	# Determines whether the operation is visible to the player
	# Default = { always = yes }
	# SCOPE_COUNTRY [ ROOT ]
	#
	
	allowed = { 
		original_tag = GER
	}

	#
	# Determines whether the operation can be launched by the player
	# Default = { always = yes }
	# SCOPE_COUNTRY [ ROOT, FROM ]
	#
	
	available = { 
		always = no
	}

	#
	# Determines the potentially awarded token(s) - this is for display purposes only in tooltips
	#

	awarded_tokens = {
		token_airforce
		token_army
	}

	#
	# List of traits that affect the cost of an operation
	#
	
	cost_modifiers = { trait_grease_machine traits_smooth_operator }

	#
	# If no operation_target is defined it will be allowed for all countries
	# SCOPE_COUNTRY [ ROOT ]
	#
	
	operation_target = {
		targets = { ENG }
	}

	#
	# Determines the valid countries for province selection. If set this will enable the UI to select a target province
	# SCOPE_COUNTRY [ ROOT, FROM, FROM.FROM : SCOPE_STATE ]
	#
	
	selection_target = {
		targets = { ROOT }
	}

	#
	# Determines the selector type. Currently supported are: [ province, strategic_region ]
	# Default: province
	#
	
	target_type = strategic_region

	#
	# Equipment base cost for the operation
	# Note: Exceptionally supports `civilian_factories` as an equipment type. It works like the agency creation cost, where it allocates a number of factories over time
	#
	
	equipment = {
		medium_tank_equipment = 20
		infantry_equipment = 5000
	}

	#
	# Determines required token(s) - against target country - to launch the operation
	#

	required_tokens = {
		token_airforce
		token_army
	}

	#
	# Determines requirements other than equipment to launch the operation. If the requirements are not met anymore while the operation is running, it is cancelled.
	# SCOPE_COUNTRY [ ROOT, FROM ]
	#

	requirements = {
	
	}

	#
	# Default: no - will refund all equipment cost for this operation at the end of the operation [ operation phases costs have their own specifier in the operation database ]
	#
	
	return_on_complete = yes

	#
	# Executed when an operation starts
	# SCOPE_OPERATION [ ROOT, FROM ]
	#
	
	on_start = {
		
	}
	
	#
	# For description purposes only. This is the effect that generates that text shown as a potential reward for completing the operation
	# SCOPE_OPERATION [
	#	ROOT, FROM
	#	FROM.FROM : SCOPE_STATE ( will only be set if the operation has a specific selection_target )
	# ]
	#
	
	outcome_potential = {
		FROM = {
			set_popularities = {
				democratic = 100
			}
			
			ROOT = {
				create_wargoal = {
					type = annex_everything
					target = PREV
				}
			}
		}
	}
	
	#
	# Chance for outcome_execute_extra to happen (assuming it exists), otherwise outcome_extra will be executed
	# 
	
	outcome_extra_chance = 50
	
	#
	# List of modifiers that apply to outcome_chance
	#
	
	outcome_modifiers = { trait_perfectionist trait_planner }
	
	#
	# Executed when the operation has completed [ once per operation ]
	# SCOPE_OPERATION [
	#	ROOT, FROM
	#	FROM.FROM : SCOPE_STATE ( will only be set if the operation has a specific selection_target )
	# ]
	#
	
	outcome_execute = {
		FROM = {
			set_popularities = {
				democratic = 100
			}
		}
		
		random_list = {
			25 = {
				FROM = {
					ROOT = {
						create_wargoal = {
							type = annex_everything
							target = PREV
						}
					}
				}
			}
			75 = {
				custom_effect_tooltip = GAME_OVER_TT
			}
		}
	}
	
	# 
	# Same as outcome_execute
	#
	
	outcome_extra_execute = {
		# ...
	}

	#
	# ON_ACTION :: TODO move to onactions
	# Executed when the operation has completed [ once per assigned operative ]
	# SCOPE_UNIT_LEADER [
	#	ROOT, FROM
	#	FROM.FROM : SCOPE_STATE ( will only be set if the operation has a specific selection_target )
	# ]
	#

	#
	# Determines whether the operation will be visible to the player
	# If no trigger used it will fall back to a default where it shows 
	# operations with network strength below NOperatives::INTEL_NETWORK_MIN_DEFAULT_FOR_SHOWING 
	# or when reachign half its network requirements. It will also only show operations with one 
	# level higher operation count than you currently have.
	#
	# SCOPE_COUNTRY [ ROOT, FROM ]
	#
	
	visible = { 
		always = no
	}

	#
	# Used to warn the AI about an upcoming war with the target of the operation
	#

	will_lead_to_war_with = yes
}
```
