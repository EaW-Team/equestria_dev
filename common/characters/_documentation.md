# Character database

Historical characters are listed within the `characters` root property. E.g.

```
characters = {
	# characters go here
}
```

The following definition is supported inside:
```
my_character_token = {
}
```

## Scientist role

```
my_character_token = {
	scientist = {
		# Optional - desc key for flavor description
		desc = desc_loc_key
		# Optional - traits array from Country Leader trait DB (Scientist trait DB when it will be ready)
		traits = { trait_token }
		# Optional - skill levels per specialization
		skills = {
			# By default all specialization start with level 1
			# Put here the ones to override
			specialization_token = 2
		}
		# Optional - trigger to decide if the scientist role is visible (default is yes)
		# ROOT: character
		visible = { ...	}
	}
}
```
