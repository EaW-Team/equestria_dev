# Script Collection Input

## Table of Content

* [collection NAME](#collection-name)
* [constant NAME](#constant-name)
* [game all_countries](#game-all_countries)
* [game all_possible_countries](#game-all_possible_countries)
* [game all_states](#game-all_states)
* [game scope](#game-scope)

## game all_countries
All existing countries (including government in exile).
### Example
```
has_resources_in_collection = {
	collection = game:all_countries
	resource = steel
	amount > 799
	extracted = yes
}
```


## game all_possible_countries
All countries (including those that doesn't exist).

### Example
```
has_resources_in_collection = {
	collection = collection:all_possible_countries
	resource = steel
	amount > 799
	extracted = yes
}
```


## game all_states
All existing states.

### Example
Check if there are more than 42 states in the game.
```
collection_size = {
	input = game:all_states
	value > 42
}
```


## game scope
Current scope object.

### Example
Check if there are more than 42 members in the faction of the current scope (assumes current scope is country scope).
```
collection_size = {
    input = {
        input = game:scope
        operators = { faction_members }
    }
	value > 42
}
```


## collection NAME
Use a named collection as input.

### Example
Checks if there are more than 42 members in the collection named "my_named_collection".
```
collection_size = {
    input = collection:my_named_collection
    value > 42
}
```


## constant NAME
Use a constant as input.
### Example
Checks if there are more than 42 members in the collection named "my_named_collection".
```
collection_size = {
	input = constant:my_constant
	value > 42
}
```

