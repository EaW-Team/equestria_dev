# Policy database for Military Industrial Organization (MIO)

For each MIO, the player is able to attach 1 policy to get extra bonuses.
1 policy is similar to 1 trait. The bonuses only applies to the equipment variant or production line the MIO is assigned to.

This database defines a list of policies, and for each MIO, the triggers will be evaluated to compute the list of eligible policies.

Example with all possible parts:
```
my_policy_token = {
	name = loc_key # optional
	# if name provided, use loc_key
	# if loc key TAG_my_MIO_token exists, use it (where TAG is the tag of the MIO owner)
	# else use loc key my_MIO_token
	# loc key may use scripted loc, scope will be set with the country owning the policy

	icon = GFX_key # optional
	# if icon provided, use GFX_key
	# if gfx key GFX_TAG_my_MIO_token exists, use it (where TAG is the tag of the MIO owner)
	# if gfx key GFX_my_MIO_token exists, use it
	# else use GFX_idea_unknown

	cost = 10 # optional, default is define DEFAULT_INITIAL_POLICY_ATTACH_COST
	cooldown = 60 # optional, default is DEFAULT_INITIAL_ATTACH_POLICY_COOLDOWN

	allowed = { ... } # mandatory
	# MIO scope
	# allowed is evaluated when starting the game for all MIOs
	# if trigger returns false, the policy will never be considered for this MIO later in-game

	visible = { ... } # optional, default is always = yes
	# current MIO scope
	# visible is evaluated when displaying the MIO UIs / policy screen
	# if trigger returns false, then the policy is not visible for the player

	available = { ... } # optional, default is always = yes
	# current MIO scope
	# available is evaluated when displaying the MIO UIs / policy screen
	# if trigger returns false, then the policy is visible but disabled and greyed-out

	# Defines the bonus given when the policy is attached to a MIO, and the MIO is assigned to an equipment variant
	# Note it's different from equipment_bonus in traits. Here you have to give the equipment group/category/archetype/type.
	equipment_bonus = {
		infantry_equipment = { # cf. script enum script_enum_equipment_bonus_type for possible values
			reliability = 0.2
			soft_attack = 0.1 # accepts as many stats as needed
		}
		armor = { ... } # accepts as many type as needed
		same_as_mio = { ... } # can use this keyword to apply to all equipments in departments of the attached MIO
	}

	# Defines the bonus given when the policy is attached to a MIO, and the MIO is assigned to a production line
	# Note it's different from equipment_bonus in traits. Here you have to give the equipment group/category/archetype/type.
	production_bonus = {
		infantry_equipment = { # cf. script enum script_enum_equipment_bonus_type for possible values
			production_cost_factor = -0.1
			production_capacity_factor = 0.1 # accepts as many stats as needed
		}
		armor = { ... } # accepts as many type as needed
		same_as_mio = { ... } # can use this keyword to apply to all equipments in departments of the attached MIO
	}

	# Defines modifiers that will apply on the MIO the policy is attached to.
	# Only use modifiers relevant for MIOs - full list below.
	organization_modifier = {
		military_industrial_organization_research_bonus = 0.1
		military_industrial_organization_design_team_assign_cost = -0.33
		military_industrial_organization_design_team_change_cost = -0.5
		military_industrial_organization_industrial_manufacturer_assign_cost = -0.66
		military_industrial_organization_task_capacity = 2
		military_industrial_organization_size_up_requirement = -0.2
		military_industrial_organization_funds_gain = 0.5
	}

	# Effects executed when the policy is attached to a MIO
	# Using the MIO scope
	on_add = { ... }

	# Effects executed when the policy is un-attached from a MIO
	# Using the MIO scope
	on_remove = { ... }

	# AI weight modifier for this policy
	# For documentation, see examples of ai_will_do throughout the content
	# Note : this affects how likely AI is to spend PP on this policy
	ai_will_do = {
		...
	}
}
```
