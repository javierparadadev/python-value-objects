# Python Value-Objects

![](https://img.shields.io/badge/PRs-welcome-green.svg)
[![GitHub](https://img.shields.io/github/license/jparadadev/python-value-objects)](https://github.com/jparadadev/python-value-objects/blob/main/LICENSE)
[![Pypi](https://img.shields.io/pypi/v/pyvalueobjects)](https://pypi.org/project/pyvalueobjects/)
[![Downloads](https://pepy.tech/badge/pyvalueobjects)](https://pepy.tech/project/pyvalueobjects)
[![GA](https://github.com/jparadadev/python-value-objects/workflows/Tests/badge.svg)](https://github.com/jparadadev/python-value-objects/actions/workflows/test.yml)

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