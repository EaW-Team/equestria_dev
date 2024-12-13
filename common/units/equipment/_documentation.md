# Equipment

Syntax:
```
equipments = {
	<equipment type name> = {
		year = <4-digit year>

		is_archetype = <yes|no>
		is_buildable = <yes|no>
		priority = <value>
		archetype = <equipment archetype name>
		parent = <equipment type name>
		is_frame = <yes|no>  # Default yes for modular equipment, not applicable for non-modular equipment. Frame refers to tank chassis, ship hulls, and airplane frames.

		# Land types
		type = <armor|infantry|motorized|mechanized|anti_air|artillery|anti_tank|rocket|support>
		# or Naval types
		type = <capital_ship|submarine|screen_ship|carrier|convoy|naval_transport>
		# or Air types
		type = <air_transport|figher|cas|interceptor|tactical_bomber|strategic_bomber|naval_bomber|missile|suicide>
		
		# Limit the amount of military factories or dockyards assignable to the type
		# Military factories types (excluding railway guns)
		max_military_factories = <amount>
		# Dockyards
		max_dockyard_factories = <amount>
		

		# The AI by default uses 'type' to connect archetypes to strategies e.g. unit_ratio. This can be overriden by
		# ai_type, and allows you to set different unit_ratios for e.g. fighter, carrier fighter and heavy fighter even
		# though they all have the type 'fighter'.
		ai_type = <cv_fighter|cv_interceptor|cv_cas|cv_naval_bomber|cv_suicide|heavy_fighter>

		upgrades = {
			# List of upgrade names
		}

		can_be_produced = {
			# a trigger to check if a country can produce this equipment type/archetype
		}
		
		can_be_lend_leased = {
			# a trigger to check if a country can lend lease to another country. scope is country, from is the country we will lend lease to
		}
		
		module_slots = {
			# List of module slots and their details
			
			# Fixed slots will be grouped together in the equipment designer window, and always start with "fixed_"
			# They represent slots that are used for a single purpose or related purposes,
			# and thus usually have a restrictive list of allowed module categories, and are usually required.
			fixed_<slot name> = {
				required = <yes|no>
				allowed_module_categories = {
					# List of module category names
				}
			}
			
			# Custom slots will be grouped together in the equipment designer window, and cannot start with "fixed_"
			# They represent slots that can be used for a lot of different purposes,
			# and thus usually have a flexible list of allowed module categories, and are usually optional.
			<custom slot name> = {
				required = <yes|no>
				allowed_module_categories = {
					# List of module category names
				}
			}
			
			# A later slot can inherit the exact same attributes from an earlier slot.
			<slot name> = <earlier slot name>
			
			# A slot can inherit the exact same attributes from the parent equipment type.
			<slot name> = inherit
		}
		
		#Alternatively, all parent module slots can be directly inherited with no modifications.
		module_slots = inherit
		
		# Any number of module count limits can be specified.
		# They are automatically inherited by child equipment types.
		# An inherited limit is overridden if the child has a limit with exactly the same match conditions.
		module_count_limit = {
			# Match conditions:  A module or slot only needs to match one of the specified conditions for the limit to apply.
			module = <module name> # Match a specific module.
			category = <module category name> # Match any module belonging to a category.
			module = any # Match any module.
			category = any # Match any module.
			module = empty # Match an empty module slot.
			
			# Specify the upper limit on the number of matching modules.
			count < <number>
			# -or- Specify the lower limit on the number of matching modules.
			count > <number>
			# -or- Specify the exact requirement on the number of matching modules.
			count = <number>
			# -or- Allow any number of matching modules.  Useful for overriding limits inherited from parent equipment type.
			count = any

			# Optional override of the limitation title used in tool tips.
			# If not specified, the single module, category, any, or empty configuration will be used if possible.
			title = <text or localization key>
		}
		
		default_modules = {
			# List of modules assigned to module slots for the default equipment variant for this type.
			<slot name> = <module name>
			
			# A slot can specifically be set to empty
			<slot name> = empty
		}

		# Base values on various unit stats before upgrades and modules from specific equipment variants are included.
		<unit stat name> = <value>
		
		# Resources needed for producing one unit of the equipment.
		resources = {
			<resource name> = <value>
		}
		
		# Manpower required to produce one unit of the equipment (naval only)
		manpower = <value>
	}
}
```
