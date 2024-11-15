# Equipment Group Database

The purpose of this database is to be able to group various equipment types into categories while optionally providing a reasonably short description.

For example:
```
useless_junk = {
	description = "Useless Junk" # optional, this can be a loc key
	equipment_type = {
		light_tank_chassis_0 # this can be a type, an archetype or a category
		light_tank_chassis_1
		...
	}
}
```

You can also include existing groups in the equipment type list:
```
useless_junk_plus_carriers = {
	equipment_type = {
		useless_junk
		carrier
	}
}
```

The equipment group can also be used to set equipment bonuses:
```
equipment_bonus = {
	useless_junk = {
		instant = yes
		build_cost_ic = -0.05
	}
}
```