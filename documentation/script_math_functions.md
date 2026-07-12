# Script Math Functions

## Table of Content

* [<](#)
* [>](#)
* [add](#add)
* [clamp](#clamp)
* [cos](#cos)
* [divide](#divide)
* [equals](#equals)
* [every_collection](#every_collection)
* [greater_than_or_equals](#greater_than_or_equals)
* [if](#if)
* [less_than_or_equals](#less_than_or_equals)
* [log](#log)
* [max](#max)
* [min](#min)
* [mod](#mod)
* [multiply](#multiply)
* [not_equals](#not_equals)
* [pow](#pow)
* [root](#root)
* [round](#round)
* [sin](#sin)
* [subtract](#subtract)
* [tan](#tan)

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


## cos
Sets the accumulator to the cosine of itself. The angle is expressed in radians.

### Example
```
{ value = 0  cos = yes }
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


## log
Sets the accumulator to its logarithm in the given base.

Note: this is computed with a numerical approximation and may produce small rounding errors (e.g. 3.00001 instead of 3). Follow with `round = yes` if you need an exact integer result.

### Example
```
{ value = 1000  log = 10 }
{ value = 1000  log = 10  round = yes }
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


## mod
Sets the accumulator to the remainder of dividing it by the value.

### Example
```
{ value = 17  mod = 5 }
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


## pow
Raises the accumulator to the given power.

Integer exponents are computed exactly by repeated multiplication. Fractional exponents (e.g. `pow = 0.5`) use a numerical approximation and may produce small rounding errors; follow with `round = yes` if you need an exact integer result.

### Example
```
{ value = 2  pow = 10 }
{ value = 2  pow = 10  round = yes }
```


## root
Takes the root of the accumulator. The argument is the degree of the root, so 2 gives the square root, 3 the cube root and so on.

Note: this is a numerical approximation and may produce small rounding errors (e.g. 4.00001 instead of 4). Follow with `round = yes` if you need an exact integer result.

### Example
```
{ value = 16  root = 2 }
{ value = 27  root = 3 }
{ value = 16  root = 2  round = yes }
```


## round
Rounds the accumulator to the nearest integer.

### Example
```
{ value = 3.7  round = yes }
```


## sin
Sets the accumulator to the sine of itself. The angle is expressed in radians.

### Example
```
{ value = 0  sin = yes }
```


## subtract
Subtracts a value from the accumulator.

### Example
```
{ value = 20  subtract = 5 }
```


## tan
Sets the accumulator to the tangent of itself. The angle is expressed in radians.

### Example
```
{ value = 0  tan = yes }
```


