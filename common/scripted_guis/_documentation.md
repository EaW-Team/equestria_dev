# Scripted GUIs

Scripted guis can be used for adding moddable guis to the game

example:
```
scripted_gui = {
	scripted_gui_name = {

		# type of the gui. must be one of the following :
		# player_context # the scope will be player
		# selected_country_context # the scope will a target country, when you right click a country
		# selected_state_context # the scope will a target country, when you left click a state
		# diplomacy_target_context # the gui will be attached to diplomacy window & will target current selected country
		# decision_category # gui will be attached to a specific decision category (add scripted_gui = scripted_gui_name to category). scope is player
		# diplomatic_action # gui will be attached to a diplo action. check scripted diplomatic actions
		# national_focus_context # gui will be attached to a national focus view for the targeted country, the country which owns the national focus view
		# country_mapicon # a map icon will be for each country. the scope will be the country
		# state_mapicon # a map icon will be for each state. the scope will be the state
		context_type = player_context

		# name of the container that is defined under a gui file
		window_name = "container_name"

		# by default gui is attached to main window (unless context overrides it)
		# you can specify a token or a window to override it

		# token must be one of the following:
		# top_bar, decision_tab, technology_tab, trade_tab, construction_tab, production_tab, deployment_tab, logistics_tab, diplomacy_tab, national_focus, politics_tab, selected_country_view, selected_state_view, selected_country_view_info, selected_country_view_diplomacy, army_ledger, navy_ledger, civilian_ledger, air_ledger, tech_infantry_folder, tech_support_folder, tech_armor_folder, tech_artillery_folder, tech_land_doctrine_folder, tech_naval_folder, tech_naval_doctrine_folder, tech_air_techs_folder, tech_air_doctrine_folder, tech_electronics_folder, tech_industry_folder
		parent_window_token = top_bar

		# if there is no token you can use, use a container name instead. in this case the game will search through all uis and attack scripted gui to one with this name
		# may not work
		parent_window_window = "container_name"

		# you can also attach a scripted gui to another scripted gui
		parent_scripted_gui = "container_name"

		# add if you want ui to show up only in specific map modes
		map_mode = map_mode_name

		# only used for map icon scripted guis. uses similar targetting code to decisions
		# mapicon_targets = {
		#   #.. a targetting code similar to targeted decision targets
		# }

		# should return true if gui should be visible
		visible = {
			always = yes
		}

		# effects can be attached to buttons using its name. you can add right, alt, control and shift (button_name_alt_right_click) to execute the effect in a specific combination
		effects = {
			button_name_click = {
			}
		}

		# triggers can be used to disable/hide ui elements
		triggers = {
			button_name_click_enabled = {
			}
			icon_name_visible = {
			}
		}

		# properties can be used to modify icon textures and ui positions of elements
		properties = {
			icon_name = {
				image = "scripted_loc"
				frame = 1 # variable
			}
			gui_element_name = {
				x = 100 # variable
				y = 200 # variable
			}
		}

		# dynamic lists can be used for populating lists with gui elements using an array
		# it will use effects & triggers of this scripted gui
		dynamic_lists = {
			list_name = {
				array = array_name # it will create a gui element for each element in array
				value = val_name # while building the element gui, it will store the current value of array in this value (default v)
				index = index_name # while building the element gui, it will store the current index in array in this value (default i)
				change_scope = yes # if yes the game will change scope to the element in the array while building the child element

				# use following to pick container for entry (all scripted loc)
				entry_container = "container_name"
				country_scope_entry_container = "container_name"
				country_scope_entry_container = "container_name"

				# add in case you want to script an ai
				ai_weights = {
				}
			}
			gui_element_name = {
				x = 100 # variable
				y = 200 # variable
			}
		}

		# by default guis are updated every tick
		# you can use a variable name and force game to update a gui only if that variable changes
		# in effects for example just call add_to_variable = { var_name = 1 } to force update a gui
		dirty = var_name

		# AI

		# ai_enabled is checked once, if false the ai will ignore this gui for entire game (only check stuff like tag/original_tag)
		ai_enabled = { always = yes }

		# ai test interval & variance in hours.
		ai_test_interval = 24
		ai_test_variance = 24

		# ai_check is for each ai once for each gui. if it is false ai will ignore that gui in this tick
		ai_check = { always = yes }

		# for targeted guis you need to specify which countryies ai should chcek (if not specified, it will check everyone)
		# possible values are:
		#test_self_country, test_enemy_countries, test_ally_countries, test_neighbouring_countries, test_neighbouring_ally_countries, test_neighbouring_enemy_countries, test_self_owned_states, test_enemy_owned_states, test_ally_owned_states, test_self_controlled_states, test_enemy_controlled_states, test_ally_controlled_states, test_neighbouring_states, test_neighbouring_enemy_states, test_neighbouring_ally_states, test_our_neighbouring_states, test_our_neighbouring_states_against_allies, test_our_neighbouring_states_against_enemies, test_contesded_states, test_if_only_major, test_if_only_coastal
		you can add multiple of these
		ai_test_scopes = test_self_country

		# checked for each target. if false ai will ignore that target
		ai_check_scope  = { always = yes }

		ai_weights = {
			button_name_click = {
				ai_will_do = {
					base = 10
					modifier = {
						tag = GER

						add = 50
					}
				}
				ignore_lower_weights = yes # if yes ai will not call effects has lower weight than this
				weight = 50 # weight of this option
			}
		}
		ai_max_weight_taken_per_test = 100 # ai will only click buttons until it reaches this weight
	}
}
```
