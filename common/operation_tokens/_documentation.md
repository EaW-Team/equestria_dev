# Operation Tokens

There can only ever be one token that one country can acquire against another. They are not stackable.

Every token needs a `<unique id>`, which is `token_test` in this case
```
token_test = {
	# Every token needs a name to be displayed
	name = ""
	
	# Every token needs a description to show what it is about
	desc = ""
	
	# Every token needs an icon for display purposes
	icon = ""
	
	# Every token can have any number of targeted modifier listed as demonstrated below
	# Those will be applied to the relation between the origin country and the target country of the operation
	# For as long as the origin country that receives the token posses the token, when the token is consumed the modifiers will go away
	targeted_modifier = targeted_modifier_id1
	targeted_modifier = targeted_modifier_id2
	
	# Intel Source Gains
	# - A token may grant intel gains against of one value for one source per token. Multiple intel gains per token are NOT supported
	# - Supported sources are: navy, army, civilian, airforce
	intel_source = navy
	intel_gain = 1.0
}
```
