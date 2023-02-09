# Python Value-Objects

A collection of Value Objects to save time by generalizing types and format validations.

* [Value-objects](#value-objects)
  * [Numeric value-objects](#numeric-value-objects)
    * [Int](#int)
    * [Nullable Int](#nullable-int)
  * [String value-objects](#string-value-objects)
    * [String](#string)


# Value-objects

## Numeric value-objects

### Int

Integer numbers without a fractional component that don't support decimal points.

```python
from pyvalueobjects import Int

# Creation
my_integer = Int(9)

# Getting raw value
my_integer.value() # returns -> 9
```

### Nullable Int

Integer numbers and None.

```python
from pyvalueobjects import NullableInt

# Creation
my_integer = NullableInt(9)

# Creating from None
my_nullable_integer = NullableInt(None)

# Getting raw value
my_integer.value() # returns -> 9
my_nullable_integer.value() # returns -> None
```

## String value-objects

### String

```python
from pyvalueobjects import String

# Creation
my_str = String('potato')

# Getting raw value
my_str.value() # returns -> 'potato'
```