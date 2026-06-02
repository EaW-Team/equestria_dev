# Script Math Functions

## Table of Content

* [<](#)
* [>](#)
* [add](#add)
* [clamp](#clamp)
* [divide](#divide)
* [equals](#equals)
* [every_collection](#every_collection)
* [greater_than_or_equals](#greater_than_or_equals)
* [if](#if)
* [less_than_or_equals](#less_than_or_equals)
* [max](#max)
* [min](#min)
* [multiply](#multiply)
* [not_equals](#not_equals)
* [round](#round)
* [subtract](#subtract)

## <
Returns 1 if the accumulator is less than the value, otherwise 0.

### Example
```
{ value = 2  less_than = 5 }
```


## >
Returns 1 if the accumulator is greater than the value, otherwise 0.

### Example
```
{ value = 10  greater_than = 5 }
```


## add
Adds a value to the accumulator.

### Example
```
{ value = 5.0  add = num_factories }
```


## clamp
Clamps the accumulator between a minimum and maximum bound. Note that arguments are order sensitive.

### Example
```
{ value = num_units  clamp = { min = 0 max = 100 } }
```


## divide
Divides the accumulator by a value.

### Example
```
{ value = 100  divide = 5 }
```


## equals
Returns 1 if the accumulator equals the value, otherwise 0.

### Example
```
{ value = 7  equals = 7 }
```


## every_collection
Iterates over a named collection, applying statements to the accumulator for each element.

### Example
```
{ value = 0
  every_collection = {
    named_collection = my_collection
    add = element_value } }
```


## greater_than_or_equals
Returns 1 if the accumulator is greater than or equal to the value, otherwise 0.

### Example
```
{ value = 5  greater_than_or_equals = 5 }
```


## if
Conditional statement that modifies the accumulator based on a condition.
Note that the limit is a math expression. It is considered true if the value is anything but 0.

### Example
```
{ value = x
  if = { limit = { value = x  greater_than = 10 }  add = 100 }
  else = { subtract = 1 } }
```


## less_than_or_equals
Returns 1 if the accumulator is less than or equal to the value, otherwise 0.

### Example
```
{ value = 5  less_than_or_equals = 5 }
```


## max
Sets the accumulator to the maximum of itself and the value.

### Example
```
{ value = 9  max = 15 }
```


## min
Sets the accumulator to the minimum of itself and the value.

### Example
```
{ value = 9  min = 4 }
```


## multiply
Multiplies the accumulator by a value.

### Example
```
{ value = 2.3  multiply = num_units }
```


## not_equals
Returns 1 if the accumulator does not equal the value, otherwise 0.

### Example
```
{ value = 7  not_equals = 5 }
```


## round
Rounds the accumulator to the nearest integer.

### Example
```
{ value = 3.7  round = yes }
```


## subtract
Subtracts a value from the accumulator.

### Example
```
{ value = 20  subtract = 5 }
```


