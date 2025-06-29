# Doctrine Tracks

Doctrine tracks are made available to the player after they have selected a *Grand Doctrine*. Each track represents the player with further customization of their doctrines, in the form of:
* A **Subdoctrine** at the root
* A series of **Rewards** derived from the subdoctrine that will gradually unlock automatically
* A **Milestone** derived from the grand doctrine activate once all of the rewards are unlocked
 
## Script Example
```
infantry = { 
    progress_type = #TODO
    name = DOCTRINE_TRACK_INFANTRY   # Bindable loc
    mastery = {
        multiplier = 0.5 # Scales how much XP is converted to mastery
        sub_units = { # Which subunits contribute to mastery gain?
            # Any specific subunits could go here, but probably best left for subdoctrine overrides
        }
        categories = { # Which subunit categories constribute to mastery gain?
	        category_all_infantry
	        category_cavalry
        }
    }
}
```

## TODO - Progression Criteria