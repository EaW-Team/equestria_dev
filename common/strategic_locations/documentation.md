# Strategic location
Create a strategic location that contains province buildings extra max level value

## Define a strategic location
A strategic location is defined using the following syntax
```
my_strategic_location = { # A list of province buildings
	coastal_fort = 2 # Coastal forts will get 2 extra max level in the province
	...
	naval_base = -2 # Reduce naval base max level in province
}
```

## Applying the strategic location to a province
Use the effect strategic_location_building.

```
555 = { # State scope
	strategic_location = {
		my_strategic_region = 3258 # Province ID
	}
}
```