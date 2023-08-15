<h1 align="center"> Python Value-Objects</h1>

<div align="center">

![](https://img.shields.io/badge/PRs-welcome-green.svg)
[![GitHub](https://img.shields.io/github/license/jparadadev/python-value-objects)](https://github.com/jparadadev/python-value-objects/blob/main/LICENSE)
[![Pypi](https://img.shields.io/pypi/v/pyvalueobjects)](https://pypi.org/project/pyvalueobjects/)
[![Downloads](https://pepy.tech/badge/pyvalueobjects)](https://pepy.tech/project/pyvalueobjects)
[![GA](https://github.com/jparadadev/python-value-objects/workflows/Tests/badge.svg)](https://github.com/jparadadev/python-value-objects/actions/workflows/test.yml)
 
</div>

![](https://raw.githubusercontent.com/jparadadev/python-value-objects/assets/assets/logo.png)

A collection of Value Objects to save time by generalizing types and format validations.

* [Value-objects](#value-objects)
  * [Numeric value-objects](#numeric-value-objects)
    * [Int](#int)
    * [Nullable Int](#nullable-int)
  * [String value-objects](#string-value-objects)
    * [String](#string)
    * [Nullable String](#nullable-string)
    * [Uuid4](#uuid4)
    * [Nullable Uuid4](#nullable-uuid4)
  * [Date value-objects](#date-value-objects)
    * [ISO Date](#iso-date)

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

### Nullable String

```python
from pyvalueobjects import NullableString

# Creation
my_str = NullableString('potato')

# Getting raw value
my_str.value() # returns -> 'potato'

# Creation
my_nullable_str = NullableString(None)

# Getting raw value
my_nullable_str.value() # returns -> None
```

### Uuid4

```python
from pyvalueobjects import Uuid4

# Creation
my_uuid4 = Uuid4('6c7add12-bf35-459e-a6c5-3178a2a33011')

# Getting raw value
my_uuid4.value()  # returns -> '6c7add12-bf35-459e-a6c5-3178a2a33011'
```

### Nullable Uuid4

```python
from pyvalueobjects import NullableUuid4

# Creation
my_uuid4 = NullableUuid4('6c7add12-bf35-459e-a6c5-3178a2a33011')
my_null_uuid4 = NullableUuid4(None)

# Getting raw value
my_uuid4.value()  # returns -> '6c7add12-bf35-459e-a6c5-3178a2a33011'
my_null_uuid4.value()  # returns -> 'None'
```

## Date value-objects

### ISO Date

```python
from pyvalueobjects import IsoDate

# Creation
my_date = IsoDate('2023-08-15T04:55:12.076Z')

# Getting raw value
my_date.value()  # returns -> '2023-08-15T04:55:12.076Z'
```
