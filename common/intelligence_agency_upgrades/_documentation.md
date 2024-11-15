# Intelligence Agency Upgrades

Syntax:
```
<agency branch name> = {

	<upgrade name> = { # upgrade_name must be unique across all branches
		
		# Note : There is no "description" field. To add a description, you only need to add an entry "upgrade name" + "_desc" in the localisation files.
	
		picture = <GFX entry>
		
		frame = <GFX entry> # GFX entry of the border for the icon, without the suffixe (suffix are _available, _completed and _unavailable ) Optional, "upgrade_frame_1" by default.
		
		sound = <Sound entry> # Optional, "click_default" by default.
		
		ai_will_do = {
			# modifiable value. Example :
			factor = 2
			modifier = {
				factor = 20
				is_major = yes
			}
		}
		
		modifiers_during_progress = {
			# Modifiers to apply while the upgrade is being done.
			# For example, the factory cost of doing this upgrade:
			civilian_factory_use = 15
		}
		
		visible = {
			# trigger visible, like decisions. Optional. Example :
			original_tag = GER
		}
		
		available = {
			# trigger available, like decisions. Optional. If not available, the upgrade will be visible but locked. Example :
			has_done_agency_upgrade = upgrade_form_department
		}
		
		level = {
			modifier = {
				# Modifiers for the first level of the upgrade. Example :
				intelligence_agency_defense = 1.5
			}
			
			complete_effect = {
				# Effects when this level is researched. Example :
				add_political_power = 200
			}
		}
		
		level = {
			modifier = {
				# Modifiers for the second level of the upgrade (if there is a second level). And so forth. Example :
				intelligence_agency_defense = 1.25
			}
		}
		
	}
	
	<upgrade name> = {
		# Etc.
	}
}
```
