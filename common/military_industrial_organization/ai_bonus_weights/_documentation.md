# AI Bonus Weights

This database contains numbers that influence how much each trait bonus affects the desire of the AI to pick traits with that bonus.

The format is very simple:
```
equipment_archetype = {
	bonus_1 = weight
	bonus_2 = weight
	bonus_3 = weight
	...
}
```

For example:
```
infantry_equipment = {
	# Prefer infantry equipment with high air superiority bonus!
	air_superiority = 9.999
}
```

Each bonus will affect the desire of the AI greater the greater the value of the bonus.

Every bonus used by any of the MIOs should have a weight. If no archetype-specific weight is provided for a bonus, the default value will be used.

Default values live in their own section:
```
default = {
	bonus_1 = weight
	bonus_2 = weight
	bonus_3 = weight
	...
}
```

If neither archetype-specific nor default value is provided, the game will log an error.
