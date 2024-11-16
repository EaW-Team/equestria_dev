# Scripted map modes

Scripted map modes can be used to add new map modes to game_map_mode_factions

Example:
```
scripted_map_modes = {
	test_map_mode = {
	# the game will use name of the map mode for some strings:
	# MAPMODE_TEST_MAP_MODE MAPMODE_TEST_MAP_MODE_NAME MAPMODE_TEST_MAP_MODE_DESCRIPTION as name & desc
	# test_map_mode_tooltip & test_map_mode_tooltip_delayed for tooltips
	# GFX_mapmode_buttons_deselected_small_test_map_mode GFX_mapmode_buttons_selected_small_test_map_mode for the icons

	# there are two layers for a map mode. bottom & top
	# both are same except during rendering they will be rendered in that order
	# for each layer the game will figure out what borders to render and will ask script to pick a color for those
	top = {

		# type represents which borders will be used for rendering for this layer
		# or it can represent one of the hard coded map mode layers
		# must be one of following:
		#   none #will render nothing for this layer
		#   country #will render using country provinces
		#   state #will render using state provinces
		#   state_controller #will render using state provinces & controllers. if a state is shared between countries it will be called for each country

		#   game_map_mode_country (these are hard coded map mode layers. if these are used all other layer entries are ignored)
		#   game_map_mode_states
		#   game_map_mode_diplomacy
		#   game_map_mode_players
		#   game_map_mode_factions
		#   game_map_mode_ideology
		type = country

		# this trigger will be used for setting the color of a specific border
		# if trigger returns true then it will render that border
		# scope depends on type of the layer
		# scope is player
		# from scope depends on type
		#   country: current country that will be rendered
		#   state: current state that will be rendered
		#   state_controller: current state that will be rendered and from from scope will be the controller of current portion of the state
		# if return value is true the game expects you to set some temp variables which will be used as border color etc

		color = {
			set_temp_variable = { red = 0.0 }
			set_temp_variable = { blue = 1.0 }
			set_temp_variable = { green = 0.0 }
			set_temp_variable = { alpha = 1.0 }

			# only needed if thickness = yes on parent
			# specify layer thickness
			set_temp_variable = { thickness = 10.0 }

			# if set border will pulsate
			set_temp_variable = { highlighted = 1.0 }

			#always = yes
		}


		# a target list that can be used to limit which scopes will be rendered on map
		# similar to targeted decisions
		# highly recommended for perfomance, otherwise it will try to render for every scope
		targets = {
			#target_array = robot_map_icon_array
			#targets
			#target_trigger
			#... everything targeted decisions support
		}

		# if the border has thickness then set
		thickness = yes
	}

	bottom = {
		# same structure as top

		type = none
	}


	# if we want to show texts on map this you can set far_text & near_text
	# must be one of the:
	#  none
	#  country
	#  state
	#  faction
	#  player

	far_text = country
	near_text = state

	# if yes, the game will update the map mode daily_update
	# otherwise force_update_map_mode effect can be used
	update_daily = yes

	}
}
```
