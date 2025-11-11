# Script Concepts

## Table of Content

* [Bindable Localization](#bindable-localization)
* [Contextual Localization](#contextual-localization)
* [Formatted Localization](#formatted-localization)
* [Script Constants](#script-constants)

## Formatted Localization
Formatted localization is a concept for generating texts based on a specific token. It can for example, be used to
generate a description of an idea from the ideas token. A formatted localization entry also accepts standard localization keys
and raw localization strings giving the following allowed options:
* A localization tag.
* A string (can for example be used to inject things based on the [Localization Scope Object](#localization_scope_object) if one exists).
* A formatter and it's associated tag.

Documentation for the existing formatters can be found at [Localization formatter](localization_formatter.md).

### Example
```
# Using a  formatter
custom_effect_tooltip = idea_desc|canadian_pacific_railway

# Using a standard loc key
custom_effect_tooltip = WHILE_FOCUSING

# Using a loc string with a localization scope object
custom_effect_tooltip = "[ROOT.GetName]"
```


## Bindable Localization
Bindable localization is a modular way of binding localization parameters in script for the specified localization key.
Any variable that accepts a bindable localization accepts the following:
* A [formatted localization](#formatted_localization).
* A bound localization object.

The bound localization object has the following members:
* `localization_key = KEY`: The localization key that is used for the object.
* `PARAMETER = BINDABLE_LOC`: A parameter to the localization key that is replaced with the localized version `BINDABLE_LOC`,
   where `BINDABLE_LOC` is a bound localization object itself.

#### Examples
The following are example usages where the `tooltip` is a bindable localization:
```
tooltip = MY_TOOLTIP # Simple loc key tooltip

### Loc entries
MY_TOOLTIP = "This is a tooltip"

### Localized result
This is a tooltip
```

```
tooltip = {
	localization_key = MY_TOOLTIP # Root look key
	IMPORTANT_QUESTION = { # ID IMPORTANT_QUESTION in MY_TOOLTIP will get value:
		localization_key = MEANING_OF_LIFE # Root loc key in IMPORTANT_QUESTION
		ANSWER = "42" # ID ANSWER in IMPORTANT_QUESTION will get value 42
	}
	THE_REST_IS = UNIMPORTANT
}

### Loc entries
MY_TOOLTIP = "The thing everyone wonders is if $IMPORTANT_QUESTION$. The rest is $THE_REST_IS$."
MEANING_OF_LIFE = "the meaning of life is $ANSWER$"
UNIMPORTANT = "unimportant"

### Result
The thing everyone wonders is if the meaning of life is 42. The rest is unimportant.
```

```
# Using a formatter
custom_effect_tooltip = idea_desc|canadian_pacific_railway
```


## Script Constants
Script constants are a way to define constants in scripts that can be reused in any script file (except for other script constants files).
In general, script constants can be used instead of the script macro operator `@` that is file local.
Note that the script constants has a negligible load time impact and no runtime performance cost.
Like many other concepts, the script constant is only supported where explicitly stated that it is supported. However, all scoped variables
accepts script constants that are pointing to a single fixed point value, by using the prefix `constant:`.

#### Reloading
A script constant is a bit specific when it comes to reloading the database.
It's not enough to reload the script constant database itself since script constants are injected into the script on load.
Instead one have to first reload the script constant database, and then reload the database that uses the script constant.

#### Example
In the script constant file, the following constant file definition is made:
```
numeric_constants = {
    schema = {
        any_key = yes
        data = fixed_point # floating point
    }
	pi = 3.14159
	e = 2.71828
}
```

These can then be used in a script file like this:
```
some_scoped_variable = constant:numeric_constants.pi
some_fixed_point_supporting_constants = numeric_constants.e
```



## Contextual Localization
Contextual localization is a way to access data from Localization Objects when localizing a string.
The concept differs slightly from standard values ($VAL$) that can be injected into the localization string by allowing the localization string
to select which properties to add to the resulting string and where.
When a string is contextually localized with a localization object, then there's one root object (either a [Scope](loc_objects_documentation.md#scope) or [Localization Environment(loc_objects_documentation.md#localization_environment)].
In general this object can only be used for two purposes: Accessing other objects and getting the current date.

The documentation for the different localization objects can be found at [Localization Objects](loc_objects_documentation.md).

### Using a localization object
The localization objects are used with the following syntax: `[(Object.)+Property]`.
`(Object.)+` refers to a sequence of at least one object accessor and `Property` is the property
that is accessed by the last object in the sequence. For example, if the localization string is localized with an [Character](loc_objects_documentation.md#character) object
the following queries would get the character's name and the name of the country that the character belongs to `[Character.GetName]`
and `[Character.Owner.GetName]`, respectively.

### Condition in contextual localization
Conditions in contextual localization can be used to check if objects are null or not. The basic syntax for the condition is `[(OBJECT ? TRUE_CASE : FALSE_CASE)]`.
Where:
* `OBJECT` is any object you can use to access a property from (for example, `Character` and `Character.Owner` are valid objects).
* `TRUE_CASE` and `FALSE_CASE` are what is to be localized if `OBJECT` is not null and null, respectively. These can hold one of the following values:
   1. `'LOC_KEY` - A localization key (`LOC_KEY`, note the prepending `'` that means that it's a localization key) that will be localized using the same context as the root contextual localization.
   2. `(OBJECT.)+Property` - Standard access of a property from an object (discards the object before the `?`). `(OBJECT.)+` stands for a sequence of at least one object, with dots as separators.
   3. (true case only) `.(OBJECT.)*Property` - Continue that object sequence from the object before the `?`. `(OBJECT.)*` stands for a potentially empty sequence of objects with dots as separators. This is more efficient than the second option since it will not redo the object getters before the `?`.

### Relation to Event Scopes
When a localization string is localized from a scoped context (for example effects or triggers), then the root [Scope](loc_objects_documentation.md#scope) is created
from the event scope of that context. For example, an effect that creates a trade route between two countries `FROM` and `THIS`
could be localized with: `LOC_KEY: "Creates a trade route between [FROM.GetName] and [THIS.GetName]"`. For more information on
how the scope accessors `FROM`, `THIS`, `PREV` and `ROOT` works on `Scope` see TODO: Add link.

### Documentation of localized objects
In general a scoped context (for example, effects and triggers) are localized using a [Scope](loc_objects_documentation.md#scope) object based on the scope of that context.
However, there are legacy systems where this may not hold. For other places where localization keys are provided, please see the documentation
for which localization objects that are defined for that context.

