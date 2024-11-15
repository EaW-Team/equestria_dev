# Examples and documentation of how to use the AI templates

Try to keep this reasonably up-to-date, please.
(updated 2024-08)

## Background
The AI template system has historically been confusing to use with a lot of unexpected behaviors.
It has recently (2023-10) undergone a period of bugfixing and revamping to make it work better and in a more understandable way.
Due to this, some of the old parameters are being deprecated or renamed and will sooner or later be cleaned up.

## How do AI templates work?
Scripters/modders are able to specify so called "target templates" that the AI try to reach when upgrading division templates.
Target templates are defined on a "role" level, and it's possible to define a number of different target templates for a specific role. The AI then chooses one of those target templates (based on scripted priorities) and aims for that.

For each role, the AI will select one target template based on the `prio`, `enable`, and `replace_with` parameters. This is referred to as the "currently targeted template".
The AI will then compare the existing division templates it has to find which one best matches the targeted template. This is referred to as the "best match" and the "match score"/"match" refers to how well it matches (100 % match = 1.0).
When the AI decides to upgrade a division template, it will make a copy of the best matching template and modify it so it gets a higher match score (i.e. looks more like the target template). (Note that the AI actually never does in-place modification of templates, it just makes a copy and modifies the copy instead.)
The AI strategy `role_ratio` determines how many divisions the AI wants for each role.

## Tips for debugging the AI templates
Use the `imgui show ai_templates` console command. This will show debug info about which templates are being targeted and which existing templates are the best matches.
Use the `imgui show ai_division_production` console command. This will show how many division the AI wants for each role.

-------------------------

## Examples
Below are some examples of AI templates, including the available parameters and what they do.
Note that some of these examples don't make sense from a gameplay perspective. The intention is just to demonstrate what the parameters do.


**A "role-level" template entry.** This in turn contains 1 or more actual target templates:
```
infantry_generic = {

	# Determines which countries will use this role-level template entry. Both 'blocked_for' and 'available_for' are possible to use. Use one or the other, if you use neither or both, the resulting behavior is undefined. (These two may be replaced by 'allowed' or something similar in the future.)
	# Generally you want to make sure that each country has max one role-level template entry targeting a role. So if you add custom AI templates for e.g. Germany you should make sure that only Germany is allowed for it, and you should also block Germany from using the generic AI templates for the same role.
	blocked_for = {
		GER
		JAP
	}

	# The role token that this role-level template entry targets. These tokens are defined by script and are targeted by the 'role_ratio' AI strategy.
	role = infantry

	# The role-level upgrade prio is used for weighted-random selection when the AI chooses which role to upgrade templates for. Set it to zero to prevent the AI from spending XP on upgrading templates for this role.
	# Example: If three role-level templates [A, B, C] have upgrade prio [1, 2, 1] respectively, then the probabilities for upgrading each template is [25%, 50%, 25%] respectively.
	upgrade_prio = {
		factor = 1

		modifier = {
			factor = 5
		}
	}

	## Below are the actual target templates belonging to this role ##
	# In this example, the AI will first try to reach a 6-inf (+support) template, before upgrading it to a 9-inf 2-arty (+support) template.
	# Since the 'upgrade_prio' is higher for the first template, that one will be targeted. And when the match score is good enough it will use the 'replace_with' to switch over to the larger template.
	# If two target templates have the same 'upgrade_prio', the first one will be preferred (so order matters in those cases).

	# Target template 1 (the smaller infantry template)
	infantry_1 = {

		# Optional: Determines the reinforcement prio of the resulting template. For example, garrison templates should use 0 (low prio) while elite templates should use 2 (high prio). Default 1 (normal prio).
		reinforce_prio = 0

		# Optional: Determines whether to use a custom icon for resulting template.
		custom_icon = 7

		# Optional: Specifies the division name group to use. By default uses the name group of the template "branched off" from.
		division_names_group = GER_MEC_01

		# The priority of this target template. This is used to determine (deterministically, no randomness involved) which of the target templates is the "currently targeted template".
		upgrade_prio = {
			factor = 1

			modifier = {
				factor = 1.5
			}
		}

		# Optional: Whether to evaluate this target template at all. Trigger with country scope. If false, the AI will pretend this target template doesn't exist.
		enable = {
			date < 1940.3.14
		}

		# Optional: Whether to allow upgrading divisions in the field. Trigger with country scope. If false, the AI will not field-upgrade divisions matching this target template. If true, the AI will consider field-upgrading divisions matching this target template to the target template defined by 'replace_with' (assuming they have enough manpower and equipment for it).
		can_upgrade_in_field = {
			has_equipment = { infantry_equipment > 3000 }
		}

		# The "meat" of the target template: the actual template contents.
		target_template = {

			# The desired support companies. The AI will try to add them to the template if allowed by research etc.
			support = {
				engineer = 1
				anti_air = 1
				artillery = 1
			}

			# The desired line regiments. The AI will try to add them to the template if allowed by research etc.
			regiments = {
				infantry = 6
			}
		}


		## Optional replace-with chain: If the match score is at least 'replace_at_match', then replace the currently targeted template with 'replace_with', as long as the match score between best matching template and the next target template is at least 'target_min_match'.

		# Optional: Match score of this target template.
		replace_at_match = 0.9

		# Optional: Other target template to replace currently targeted template with. Also affects fielded divisions when upgrading in the field.
		replace_with = infantry_2

		# Optional: Match score between the best matching template and the target template defined by 'replace_with' has to be at least this high in order for the switch to happen. Might be deprecated/changed in the future.
		target_min_match = 0.9
	}

	# Target template 2 (the larger infantry template)
	infantry_2 = {

		# See parameter documentation for the previous target template

		upgrade_prio = {
			factor = 1

			modifier = {
				factor = 1
			}
		}

		target_template = {

			support = {
				engineer = 1
				recon = 1
				field_hospital = 1
				anti_air = 1
				anti_tank = 1
			}

			regiments = {
				infantry = 9
				artillery_brigade = 2
			}
		}
	}
}
```



**Another example of a "role-level" template entry.** This one shows some examples of how one can do gated progression, i.e. only go to the next target template after a certain condition is fulfilled (in this case, tech is researched). In particular, look at the 'upgrade_prio' and 'replace_with' chains, those are the interesting things in this example.
```
armor_ENG = {

	available_for = {
		ENG
	}

	role = armor

	# When we research tank technology, increase the likelihood that the AI upgrades tank templates (compared to other types of templates)
	upgrade_prio = {
		factor = 2

		modifier = {
			factor = 7
			OR = {
				has_tech = basic_medium_tank
				has_tech = basic_medium_tank_chassis
			}
		}

		modifier = {
			factor = 2
			OR = {
				has_tech = main_battle_tank
				has_tech = main_battle_tank_chassis
			}
		}
	}

	light_armor_default_ENG = {
		# Intermediate template to get the AI to understand how to transition to the next one. Only needed since England's starting tank brigade is so different from light_armor_2_ENG.

		# This target template will only have highest prio at the start of the game
		upgrade_prio = {
			factor = 1

			modifier = {
				factor = 3
				date < 1938.1.1
			}
		}

		target_template = {

			support = {
				engineer = 1
			}

			regiments = {
				light_armor = 3
				motorized = 2
			}
		}

		# When we're getting close to the target template, switch over to the next one
		replace_at_match = 0.9
		replace_with = light_armor_2_ENG
		target_min_match = 0.3
	}

	light_armor_2_ENG = {

		# This target template will be targeted if the previous one (light_armor_default_ENG) is already reached and we switch over thanks to 'replace_with'. Apart from that, it will have the highest prio (compared to the other target templates) if we have researched light tanks but not medium tanks yet.
		upgrade_prio = {
			factor = 1

			modifier = {
				factor = 1.5
				OR = {
					has_tech = basic_light_tank
					has_tech = basic_light_tank_chassis
				}
			}

			modifier = {
				factor = 1.5
				OR = {
					has_tech = improved_light_tank
					has_tech = improved_light_tank_chassis
				}
			}
		}

		target_template = {

			support = {
				engineer = 1
				signal_company = 1
				maintenance_company = 1
				anti_air = 1
			}

			regiments = {
				light_armor = 4
				motorized = 5
				mot_artillery_brigade = 1
			}
		}

		replace_at_match = 0.8
		replace_with = medium_armor_default_ENG
		target_min_match = 0.5  # This prevents ENG from switching over to medium tanks until upgrade_prio takes over (this is a good thing). This is because the light tank target template is so different from the medium tank template, the match score is ca 0.10-0.15 something.
	}

	medium_armor_default_ENG = {

		# This target template will take priority if we have researched basic medium tanks
		upgrade_prio = {
			factor = 1

			modifier = {
				factor = 3
				OR = {
					has_tech = basic_medium_tank
					has_tech = basic_medium_tank_chassis
				}
			}
		}

		target_template = {

			support = {
				engineer = 1
				armored_car_recon = 1
				maintenance_company = 1
				logistics_company = 1
				anti_air = 1
			}

			regiments = {
				medium_armor = 4
				motorized = 5
				mot_artillery_brigade = 1
				mot_anti_tank_brigade = 1
			}
		}

		replace_at_match = 0.9
		replace_with = medium_armor_2_ENG
		target_min_match = 0.8  # Prevents premature upgrade to medium_armor_2_ENG, will wait for the upgrade_prio instead
	}

	medium_armor_2_ENG = {

		# This target template will take priority if we have researched improved medium tanks and we have a large enough number of military factories
		upgrade_prio = {
			factor = 1

			modifier = {
				factor = 3.5
				OR = {
					has_tech = improved_medium_tank
					has_tech = improved_medium_tank_chassis
				}
			}

			modifier = {
				factor = 0.1
				num_of_military_factories < 150
			}
		}

		target_template = {

			support = {
				engineer = 1
				maintenance_company = 1
				logistics_company = 1
				light_tank_recon = 1
				anti_air = 1
			}

			regiments = {
				medium_armor = 8
				motorized = 8
				mot_artillery_brigade = 1
			}
		}

		replace_at_match = 0.9
		replace_with = modern_armor_default_ENG
		target_min_match = 0.8
	}

	modern_armor_default_ENG = {

		# This target template will take priority if we have researched modern tanks and we have a large enough number of military factories
		upgrade_prio = {
			factor = 1

			modifier = {
				factor = 4
				OR = {
					has_tech = main_battle_tank
					has_tech = main_battle_tank_chassis
				}
			}

			modifier = {
				factor = 0.1
				num_of_military_factories < 150
			}
		}

		target_template = {

			support = {
				engineer = 1
				maintenance_company = 1
				logistics_company = 1
				light_tank_recon = 1
				anti_air = 1
			}

			regiments = {
				modern_armor = 8
				motorized = 4
				mechanized = 4
				mot_artillery_brigade = 1
			}
		}
	}
}
```
