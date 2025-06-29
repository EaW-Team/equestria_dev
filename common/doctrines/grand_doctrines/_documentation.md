# Grand Doctrines

**Grand doctrines** are at the root of each doctrine *Folder*. The player can choose any available grand doctrine for that folder and activate it by paying an XP cost. Activating a grand doctrine gives immediate effects, like unit stat bonuses or unlocking tactics. Also, activating a grand doctrine makes available its corresponding *Subdoctrine Tracks*. For each track, the grand doctrine has a **Milestone** which is additional reward for completing that track.

## Script Examples

```
mobile_warfare = {
    folder = land   # Refers to the script name of a folder
    name = GRAND_DOCTRINE_MOBILE_WARFARE   # Bindable loc
    icon = GFX_mobile_warfare_medium  # Refers to the script name of an icon
    available = yes

    xp_cost = 100
    xp_type = army   # army, navy or air

    ai_will_do = { }

    tracks = {   # Refer to script names of tracks
        infantry
        artillery_support
        armor
        operations
    }

    # ACTIVATION EFFECTS - SEE BELOW

    milestones = {   # NOTE: milestones are in the same order as the tracks
        {
            # ACTIVATION EFFECTS - SEE BELOW
        }
        {
            # ACTIVATION EFFECTS - SEE BELOW
        }
        {
            # ACTIVATION EFFECTS - SEE BELOW
        }
        {
            # ACTIVATION EFFECTS - SEE BELOW
        }
    }
}
```

## Scripting Activation Effects

Grand Doctrines, Milestones, Subdoctrines and Rewards all support scripting the following things as "activation effects":

### Country-level modifiers:
```
planning_speed = 0.4
army_speed_factor = 0.10
```

If you prefer, the Modifiers can also be scripted in an explicit block, like so:
```
modifiers = {
    planning_speed = 0.4
    army_speed_factor = 0.10
}
```

### Enabling tactics:
```
enable_tactic = tactic_unexpected_thrust # Or any other tactic
enable_tactic = tactic_elastic_defense
```

### Add unit stat bonuses:
```
category_tanks = {
    max_organisation = 1
}
armored_car = {
    max_organisation = 2
}
```

### Any scripted effects:
```
effect = { 
    add_tech_bonus = {
        bonus = 0.5
        uses = 1
        category = cat_light_armor
    }
}
```
