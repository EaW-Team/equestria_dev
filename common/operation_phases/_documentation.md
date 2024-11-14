# Operation Phases

Every phase needs a `<unique id>`, which is `phase_test` in this case
```
phase_test = {
	# [[scripted localization]]
	name = "Run Forest Run"

	# [[scripted localization]]
	desc = "Moles are like cheetahs and can run faster than the enemy can spot them!"

	icon = "GFX_report_event_hitler_handshake"
	picture = "GFX_report_event_hitler_handshake"

	# [[scripted localization]]
	# Outcome text that is used to build the final outcome string
	outcome = "Our operatives outran our enemies without any problems."

#########################
## OPTIONAL BELOW HERE ##
#########################

	# map icon, will use regular icon if none specified
	map_icon = "GFX_report_event_hitler_handshake_map"  

	# [[scripted localization]]
	# Outcome text that is used to build the final outcome string - This happens if a risk_extra has happened ( something bad ) to at least one of the operatives
	# We usually only specify outcome_extra for exfiltration phases, technically all phases use outcome_extra, but if none is defined for it ( as in our use case it would not make sense ) then it will default fallback to outcome
	# Some modders might have a different use case for this, so support is there and it uses outocme_extra for all phases of an operation that had something risky happen. Can be used to build a different storyline from an operation where everthing went smooth.
	outcome_extra = "Last we heard our operatives were crossing the border, but they never checked in with us aftewards. Something must have happened."

	# requirements is a trigger that will be visible in the UI and determines the set of requirements necessary to start an operation
	# they are used for phase selection. If this trigger is not successful ( checked on a weekly basis ) then the phase is invalid.
	# PreSeeded operations will be ReSeeded with new phases if one of theirs becomes invalid
	# SCOPE_COUNTRY [ ROOT, FROM ]
	
	requirements = {
		has_full_control_of_state = 119
		NOT = { original_tag = GER }
	}

	# Default: no - will refund all equipment cost for this operation phase at the end of the operation [ operation costs have their own specifier in the operation database ]
	return_on_complete = yes

	# Equipment cost that is scalable by the multiplier defined in the operation
	# Note: Exceptionally supports `civilian_factories` as an equipment type. It works like the agency creation cost, where it allocates a number of factories over time
	
	equipment = {
		infantry_equipment = 5000
	}
}
```
