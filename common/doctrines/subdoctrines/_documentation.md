# Subdoctrines

**Subdoctrines** are at the root of each doctrine *Track*. The player can choose any available subdoctrine for that track and activate it by paying an XP cost. Activating a subdoctrine gives immediate effects, like unit stat bonuses or unlocking tactics. Also, activating a subdoctrine starts the automatic activation of a sequence of *Rewards*.

### TODO - how unlocking of rewards works

## Script Examples

```
bicycle_heroes = {
    track = infantry   # Refers to the script name of a track
    name = SUBDOCTRINE_BICYCLE_HEROES   # Bindable loc
    icon = GFX_subdoctrine_bicycle_heroes   # Refers to the script name of an icon
    available = yes

    xp_cost = 100
    xp_type = army   # army, navy or air

    ai_will_do = { }

    # ACTIVATION EFFECTS - SEE GRAND DOCTRINES DOCUMENTATION

    rewards = {
        {
            mastery = 150 # Optional - if set, will overide NDefines::NDoctrines::DEFAULT_REWARD_MASTERY
            # ACTIVATION EFFECTS - SEE GRAND DOCTRINES DOCUMENTATION
        }
        {
            # ACTIVATION EFFECTS - SEE GRAND DOCTRINES DOCUMENTATION
        }
        {
            # ACTIVATION EFFECTS - SEE GRAND DOCTRINES DOCUMENTATION
        }
        {
            # ACTIVATION EFFECTS - SEE GRAND DOCTRINES DOCUMENTATION
        }
    }
    
    mastery = { # This will override the default mastery conditions for the track
        multiplier = 10.0 # Scales how much XP is converted to mastery
        sub_units = { # Which subunits contribute to mastery gain?
            bicycle_battalion
        }
        categories = { # Which subunit categories constribute to mastery gain?
        }
    }
}
```