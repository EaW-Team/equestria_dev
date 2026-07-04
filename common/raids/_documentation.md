# Raid Categories
```
raid_category_id = {
    intel_source = air # The intel type used to detect this raid. air, naval, army or civilian
    visible = {
        # Whether the category should be visible or not (country scope)
    }
    available = {
        # Whether the category should be available (active) or not (country scope)
    }
    free_targeting = yes # If set, the UI will let you use this category to target any province (as for nuclear raids)
    # note that raid types still need province = any as the target type
}
```

# Raids
```
raid_type_id = {

	category = raid_category_id

	custom_map_icon = GFX_ref [Optional] - override for the automatic icon lookup (if this is not set, will look for "GFX_raid_type_icon_{raid_name} )" 
    custom_terrain_icon = GFX_ref [Optional] - override for the automatic background based on target province terrain
	target_loc_key = LOC_KEY #[Optional] - Custom loc key for overriding the target name. Use $LOCATION$ inside the loc key if you want to include the location name (state or VP).

	unit_icon = GFX_ref
	target_icon = GFX_ref
	equipment_icon = GFX_ref
	launch_sound = SFX_ref

	command_power = 20 # command power allocation cost

	arrow = {
		type = line # arrow type: line, ballistic, air, naval or land
	}

	unit_model = {

		# Entities to use as raid unit models, the game will try to find suitable entity in the following order:
		#	1. First, a country-specific override, for example: GER_entity_name
		#	2. Second, a culture-specific override, for example: westerngfx_entity_name
		#	3. Then, the basic entity: entity_name
		#	4. If still not found, the game will try to find the default_entity_name
		entity = entity_name
		default_entity = default_entity_name
		
		# Tells the game to use specific equipment's model as raid unit
		# NOTE - only air equipment is currently supported!
		equipment = air_transport

	    start_offset = 15 # offsets the starting position of a unit by an amount, mostly needed so that convoy entities start in the sea and not on the shore
	    scale = 0.5 # scale of the entity, is also multiplied by the global RAID_UNIT_ENTITY_BASE_SCALE define
	}

	# Optional. Drives entity animation across raid travel progress.
	# Stages must be listed in ascending at_progress order. The highest at_progress <= current progress wins.
	# Missing states on the loaded entity are silently skipped (so a basic-tier model can share the script with a multi-stage one).
	# Use a single stage with at_progress = 0 to lock the entity to one state for the whole raid.
	# Omit entirely to leave the entity on its default state for the duration of the raid.
	unit_animations = {
	    stage = { state = "idle" } # at_progress defaults to 0
	    stage = { state = "idle2" intro = "idle2_intro" at_progress = 0.33 }
	    stage = { state = "idle3" intro = "idle3_intro" at_progress = 0.66 }
	}

	ai_will_do = {
		# AI only wants to do raids if resulting AI weight is > 0
		# FROM refers to the target country
		# var:target_state and var:target_province can also be used when applicable

	    base = 2
		modifier = {
			factor = 0
			<triggers>
		}
	}

	ai_min_success_chance = 0.1 # [Optional] Per-type override of RAIDS_MIN_SUCCESS_FOR_LAUNCH (0.0-1.0).

	max_distance = 500 # [Optional] Hard cap on source-to-target path length, in universal distance units (same space as the engine's path lengths). Sources further away than this cannot be used. AI ignores this when unlimited_ai_range = yes.

	fire_only_once = yes # if the raid can only be executed once
	days_re_enable = 60 # How many days before the raid can be created again against the same target.
	                    # There is RAID_DEFAULT_TARGET_COOLDOWN_DAYS define which is used if no value is specified in script.
	                    # Set to 0 if you don't want any cooldown.

	days_to_prepare = 30
	speed_multiplier = 1.0 # optional unit speed multiplier, default = 1 (see also: RAID_UNIT_SPEED_MULTIPLIER in defines.lua)

	allowed = {
		# Mainly for Country Specific Raids and for dlc locks
	}

	# Whether the raid type should be visible or not, before considering potential targets
	visible = {
		# Keep these triggers simple for performance reasons
	}

	# Whether the raid type should be visible for a specific target
	show_target = {
        # Keep these triggers simple for performance reasons
		# Use FROM to refer to the target country, e.g. to prevent targeting allies
		# var:target_state and var:target_province can also be used when applicable
    }

	# Available represents being able to prepare a raid
	available = {
		# Keep these triggers simple for performance reasons
		# Use FROM to refer to the target country, e.g. to prevent targeting allies
		# var:target_state and var:target_province can also be used when applicable
	}

	# Launchable represents being able to start a raid
	launchable = {
		# Use FROM to refer to the target country, e.g. to require being at war
		# var:target_state and var:target_province can also be used when applicable
	}
	
	# Optional launchable trigger
	# The scope is the country controlling the starting point used for raid, for example:
	#  - the country that controls the territory where the starting base is located
	#  - OR the country owning the fleet that is used to start the raid
	launchable_from = {
		# Use FROM to refer to the target country, e.g. to require being at war
		# var:target_state and var:target_province can also be used when applicable
	}

	target_types = { target_type_tokens }
	#	target type tokens:
			province = any / id / array of IDs
			building = {
				type = <type/tag>
				level = { min = X max = Y }	# Optional. Max can also be omitted
				is_coastal = yes # Optional
			}
			state = { <triggers> }
	
    # Conditions on the starting point:
    starting_point = {
        types = { air_base, naval_base, rocket_site, carrier, submarine }
		building_types = { supply_node } # list of building ids or tags
		allow_faction_buildings = yes # whether buildings on allied territories can be used
    }

	show_target = {  }

	preparation_time = INT # number of days
	cost = INT # Command Power Allocation

	unit_requirements = {
		# Battalions...
		battalion_types = {  # Optional
			mountaineers = { min = 2 }
		}

		# ... or equipment...
		equipment = {  # Optional
			type = { tactical_bomber }
			modules = { engine_1_2x }  # Optional
			amount = { min = 80 max = 100 }  # Optional
		}
	}

	# NOTE : unit_requirements can occur multiple times in a script
	# any unit matching at least one of the unit_requirements blocks will be allowed to participate in the raid

	essential_equipment = {
        # list of equipment archetypes and numbers
        # Having this equipment (in stockpile) is a precondition for *creating* the raid, and
        # will be collected after a raid is created
		transport_plane_equipment = 5

		nukes = 1					# number of nukes (if using nukes). See: nuke_type
    }

	additional_equipment = {
		# list of equipment archetypes and numbers
		# This equipment is collected after a raid is created (not needed for creating the raid)
		# Note: essential_equipment and additional_equipment are not additive, instead the max of both is used
		# Note: ships (ship hulls) can also be used, and will be primarily be collected from existing fleets
		ship_hull_light = 5

		nukes = 1					# number of nukes (if using nukes). See: nuke_type
	}

	nuke_type = nuclear_bomb		# type of nuke to use: nuclear_bomb or thermonuclear_bomb

	# What happens depending on which level of access is achieved
	success_levels = {
		failure = {
                    # See Raid Outcomes below
                    [...]
		}
		limited_success = {
                    # See Raid Outcomes below
                    [...]
		}
		success = {
                    # See Raid Outcomes below
                    [...]
		}
		critical_success = {
                    # See Raid Outcomes below
                    [...]
		}
	}

	# What determines the probability of different outcomes
	success_factors = {
	    success = {
	        # See Success Chance Formulas below
	        [...]
	    }

	    critical = {
	        # See Success Chance Formulas below
	        [...]
	    }

	    disaster = {
	        # See Success Chance Formulas below
	        [...]
	    }
	}
}
```
## Raid Map Icons

Map icons can be assigned in the following ways:

1. Automatically based on a string lookup of "GFX_raid_type_icon_" + [raid_type_name]
2. A custom scripted icon set through "custom_map_icon = [name]"

In both of the above cases, the system will also try to find a customized icon for the target building type, by appending the building template to the end of the string:
`[1. or 2. from above] + "_" + [building_template_name]`

# Raid Outcomes

These are defined in the *success_levels* part of the RaidType.

There are four levels: *failure*, *limited_success*, *success*, and *critical_success*.

The following effects are supported, taking *failure* as an example:

```
failure = {
    # Effects that should be listed as affecting the raiding country
    # Raid instance scope
    actor_effects = {
        # Can run raid instance scope effects
        raid_add_unit_experience = 100

        # And also use the dynamic variables to change scope (see the variable list below)
		var:actor_country = {
			air_experience = 10
		}
    }

    # Effects that should be listed as affecting the raided country
    # Raid instance scope
    victim_effects = {
        var:victim_country = {
            add_relation_modifier = {
                target = var:ROOT.actor_country
                modifier = [...]
            }
        }

        var:target_state = {
            damage_building = {
                type = dam
                damage = 1 # levels of damage
                province = var:ROOT.target_province
            }
        }
    }

    # Division (unit) scope
    division_effects = {
        add_divisional_commander_xp = 10
    }

	# The percentage of additional equipment that gets destroyed
	# Default is 100%
	destroy_additional_equipment = 0.25
    custom_sound = SFX_ref [Optional] Custom sound effect to play for this outcome

    # Visual effect to spawn on the target province
    visual_effect = {
        entity = "nuke_entity" # name of the entity to spawn
        animation = "attack" # name of the entity animation state
    }
}

```

Note that *actor_effects* and *victim_effects* both use the same scope, but separating them allows for
easily separating them for UI purposes (showing separate lists of how the actor and victim country were affected by the outcome)

As another note on the terminology of these outcomes, unfortunately there were some changes to the naming during development which were not properly consolidated in time. 
**Failure**, **Critical Failure** and **Disaster** all refer to the same thing (the worst outcome).

# Success Chance Formulas & Modifiers

"Success Chance Formulas" are essentially lists of different **success chance modifiers** which can affect the probability of a certain
raid outcome. They are used in *success_factors* in the RaidType (see above). *success*, *critical* and *disaster* are all
scripted in the same way through this formula construct.

```
[success_formula] = {
    base = <value> # [Optional] A base chance of the outcome (default is 0.0)

    # Optional modifiers
    [modifier] = {
        weight = <value> # [Required] The maximum probability change applied by the modifier (positive or negative, additive)
        reference = <value> # [Optional] The value of the backing property at which the modifier will have full weight. Default is 1.0
        start_weight = <value> # [Optional] The weight of the modifier when the backing property is at 0.0 (or, instead, at start_reference if defined). Default is 0.0
        start_reference = <value> # [Optional] The value of the backing property at which the modifier will have 0 weight (or, instead, start_weight if defined).
    }
}
```

- *success* defines the probability of a raid being a success
- *critical* defines the probability of a successful raid being a critical success (conditional probability)
- *disaster* defines the probability of a raid being a critical failure (not conditional)

## Predefined success chance modifiers:

### Generic:
- *prep_time*: The preparation progress. Reference values from 0.0 (no preparation) to 1.0 (full preparation).
- *experience*: The experience of the unit assigned to the raid. Reference values from 0.0-1.0
- *anti_air*: The anti-air defense value of the target state. Reference values e.g. from 0 to 5 (meaning 5 basic AA buildings)
- *resistance*: The amount of resistance in the target state. Reference values from 0 to 100
- *enemy_units*: The number of enemy divisions in the target province. For province-target missions ONLY.
- *air_superiority*: The air superiority score (fraction) of the actor country in the target region. Reference values from 0.0 to 1.0

- *interception*: The number of enemy planes executing interception missions in the target region.
- *intel*: The amount of intel the actor country has on the target. Reference values depend on defines.

### Air Units Only:
- *air_defence*: The air defense value of the air unit assigned to the raid. Typical reference values from 0 to 50
- *air_agility*: The air agility value of the air unit assigned to the raid. Typical reference values from 0 to 50
- *strategic_bomber*: The strategic bombing value of the air unit assigned to the raid. Reference values from 0 to 1
- *reliability*: The reliability (fraction) of the air unit assigned to the raid. Reference values from 0 to 1

### Land Units Only:
- *recon*: The recon level of the land unit assigned to the raid, if there is one. Typical reference values from 0 to 10
- *organisation*: The organisation (absolute) of the land unit assigned to the raid, if there is one. Reference values from 0 to 100+
- *strength*: The strength (factor) of the land unit assigned to the raid, if there is one. Reference values from 0.0 to 1.0

Example of scripting the success factors for a raid type:
```
success_factors = {
    # Factors that determine the probability of a raid being successful
    success = {
        # The base chance of this outcome is 20%
        base = 0.5

        prep_time = {
            # As preparation progress approaches 1.0 (the default reference value), starting from 0.6,
            # gradually remove the penalty (from -30% to 0%)
            start_reference = 0.6
            start_weight = -0.3
            weight = 0
        }

        agility = {
            reference = 100.0
            # As air unit agility approaches 100 (as defined by the value above), increase chance by this value
            weight = 0.05
            # At 0 agility, the modifier will have negative effect.
            # The modifier will scale linearly, meaning at 50 agility, the modifier will be 0.
            start_weight = -0.05
        }

        reliability = {
            reference = 100.0
            # By defining a start reference, we can make the modifier have weight 0 until reliability reaches 50,
            # after which it will increase until it reaches 100
            start_reference = 50.0
            weight = 0.1
        }
    }

    # Factors that determine the probability of a successful raid being a critical success
    critical = {
        # The base chance of this outcome is 10%
        base = 0.1

        experience = {
            reference = 50.0
            # As unit experience approaches 50 (as defined by the value above), increase chance by this value
            weight = 0.05
        }
    }

    # Factors that determine the probability of a raid being a disaster (critical failure). Note that risk taking will impact disaster risk.
    disaster = {
        # The base chance of this outcome is 10%
        base = 0.1

        experience = {
            reference = 50.0
            # As unit experience approaches 50 (as defined by the value above), increase chance by this value
            weight = 0.05
        }
    }
}
```

## Custom success chance modifiers:

Success chance modifiers can also be scripted in a custom way, where a MTTH block is used to sample the "source" value that the modifier is based on.

For example, a success modifier can be scripted that scales based on the political power of the actor country, through the 'political_power' variable:
```
political_power_test = {
    scope = country # Needed because we need to sample a dynamic variable from the country scope
    formula = {
        # MTTH block
        base = 1
        modifier = {
            factor = political_power # Dynamically mapped name variable
        }
    }
    weight = 0.1
    reference = 500
    can_actor_affect = yes # If true, this modifier will be included in the list of measures the actor country can take to increase the success chance of the raid
    can_target_affect = no # If true, this modifier will be included in the list of countermeasures the target country can take to decreases the success chance of the raid
}
```
Since *weight = 0.1* and *reference = 500*, this means that if the actor country has 500 political power, the success chance will be increased by 10%.

You can also use custom success modifiers to do conditional checks, e.g. increasing success chance if the actor country has taken a certain focus:
```
completed_focus_test = {
    formula = {
        # MTTH block
        base = 0
        modifier = {
            has_completed_focus = GER_prioritize_economic_growth
            add = 1
        }
    }
    weight = 0.1
    can_actor_affect = yes # If true, this modifier will be included in the list of measures the actor country can take to increase the success chance of the raid
    can_target_affect = no # If true, this modifier will be included in the list of countermeasures the target country can take to decreases the success chance of the raid
}
```

### Scopes for custom success chance modifiers

Custom success chance modifiers generally support these scopes:
- *country*
- *state* (raid target)
- *character* (unit leader)
- *unit* (division)

Note that in the examples above, the *political_power_test* modifier has explicitly defined *scope = country*.
This is because it uses the *political_power* variable, which needs to be sampled from a country, but the dependence on country scope cannot be implicitly deduced from the variable alone.
Unfortunately, the system currently does not support sampling variables from multiple sources. Since the modifiers can support any of the three scopes above, we need to explicitly define the scope when using dynamic variables to make sure we are sampling the variable from the correct source.

In the second case, we do not need to explicitly define the scope, since the trigger *completed_focus* can be implicitly deduced to belong to country scope.

#### Some example of state-scoped custom success chance modifiers:

```
infrastructure = {
    scope = state # Needed because we need to sample a dynamic variable from the state scope
    formula = {
        base = 1
        modifier = {
            factor = infrastructure_level
        }
    }
    weight = -0.1
    reference = 5
    can_target_affect = yes
    can_actor_affect = no
}

capital = {
    formula = {
        base = 0
        modifier = {
            is_capital = yes
            add = 1
        }
    }
    weight = 0.1
    can_target_affect = no
    can_actor_affect = no
}
```

### Unit-based custom success chance modifiers

If a custom success chance modifier only uses unit or character scope, it will be displayed already in the unit selection menu. Here are some examples of how unit/character modifiers can be set up:

Sampling a dynamic variable from the unit leader, e.g. the planning skill level:
```
planning_skill_test = {
    scope = character # Needed because we need to sample a dynamic variable from the character scope
    formula = {
        base = 1
        modifier = {
            factor = planning_level
        }
    }
    weight = 0.1
    reference = 5
    can_target_affect = no
    can_actor_affect = yes
}
```

Using a unit-scope trigger:
```
division_check = {
    formula = {
        base = 0
        modifier = {
            division_has_battalion_in_template = marine
            add = 1
        }
    }
    weight = 0.15
    can_target_affect = no
    can_actor_affect = yes
}
```

### Localization for custom success chance modifiers

Given a custom success chance modifier named `political_power_test`, the game will look for the following loc strings to display the modifier in the UI:
```
success_modifier_political_power_test: "£pol_power §HPolitical Power§!"
success_modifier_political_power_test_negative: "low £pol_power §HPolitical Power§!" # Optional (displayed if the modifier has negative effect)
success_modifier_political_power_test_improvement: "- Increase £pol_power §HPolitical Power§!" # Optional (but required if can_actor_affect is true)
success_modifier_political_power_test_counterplay: "- Decrease enemy £pol_power §HPolitical Power§!" # Optional
success_modifier_political_power_test_source: "£pol_power $VAL|H0$/$MAX|H0$" # Optional
```

# Raid Instance Effects

These are new effects that operate on the *Raid Instance* scope.

## Dynamic variables

The raid instance scope supports these variables:

```
var:actor_country
var:victim_country
var:target_state
var:target_province
```


### raid_damage_units

Damage the units performing the raid in scope (the attackers inflict losses).

Damage is applied to ground units while damage to plane is defined as the amount of planes lost.
If 'ratio = yes', then all damage / losses are applied as a fraction of the current amount.
For units, damage can be defined through one value 'damage' or separately through 'org_damage' and 'str_damage'

The unit damage defined in a similar way to the 'damage_units' effect, with plane losses also being definable.

```
raid_damage_units = {
    # Amount of damage inflicted to units
    damage = <value>
    # Amount of organization damage inflicted to units (overrides 'damage' for org)
    org_damage = <value>
    # Amount of strength damage inflicted to units (overrides 'damage' for str)
    str_damage = <value>
    # Amount of planes lost
    plane_loss = <value>
    # Whether the damage/losses should be applied as a fraction of the current amount
    ratio = yes/no
}

examples:

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
```

### raid_add_unit_experience

Add experience to the units (e.g. divisions or air wings) performing the raid.
```
raid_add_unit_experience = <value> # The value is 0.0-1.0, representing progress towards the max level
```

example:

Gain 25% progress towards the max level
```
raid_add_unit_experience = 0.25
```
Supports both explicit values and variables
