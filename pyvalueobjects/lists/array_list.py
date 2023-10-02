from __future__ import annotations

from typing import TypeVar

from pyvalueobjects.abstract.valueobject import ValueObject
from pyvalueobjects.errors.ValueObjectError import ValueObjectError

T = TypeVar('T')


def ArrayList(cls):
    class _ArrayList(ValueObject):

        def __init__(self, values: list[cls]):
            super().__init__(values)
            self._sub_value_objects = [cls(value) for value in values]

        def _validate(self, value):
            super()._validate(value)
            input_type = type(value)
            if input_type != list:
                raise ValueObjectError(f'Input type should be: list.')

    return _ArrayList
