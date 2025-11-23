# Script Collection Operator

## Table of Content

* [controlled_states](#controlled_states)
* [country_and_all_subjects](#country_and_all_subjects)
* [faction_members](#faction_members)
* [limit = PAYLOAD](#limit-payload)
* [owned_states](#owned_states)

## faction_members
Gets all the faction members of the provided country (including the country itself).
The collection will be empty if there are no faction members.

Will be used to localize if used as first operator after an input that accepts operator localization.

### Example
```
collection_size = {
    input = game:all_countries
    operators = { faction_members }
    value > 3
}
```


## owned_states
All states owned states by the current country.

Will be used to localize if used as first operator after an input that accepts operator localization.

### Example
```
collection_size = {
    input = game:all_countries
    operators = { owned_states }
    value > 5
}
```


## controlled_states
All states controlled by the current country.

Will be used to localize if used as first operator after an input that accepts operator localization.

### Example
```
collection_size = {
    input = game:all_countries
    operators = { controlled_states }
    value > 5
}
```


## country_and_all_subjects
The current country and all its subjects.
If the country has no subjects, then the collection will only contain the country itself.

Will be used to localize if used as first operator after an input that accepts operator localization.

### Example
```
collection_size = {
    input = game:scope
    operators = { country_and_all_subjects }
    value > 1
}
```


## limit = PAYLOAD
Filters the collection by a trigger.

### Example
```
collection_size = {
    input = game:all_countries
    operators = { trigger = { has_government = democratic } }
    value > 2
}
```


