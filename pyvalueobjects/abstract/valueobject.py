from abc import ABC

from pyvalueobjects.errors.ValueObjectError import ValueObjectError


class ValueObject(ABC):

    def __init__(self, value):
        self._validate(value)
        self._value = value

    def value(self):
        return self._value

    def str_value(self) -> str:
        return str(self._value)

    def _validate(self, value):
        pass

    def __hash__(self):
        return hash(self._value)

    def __eq__(self, other):
        if not isinstance(other, ValueObject):
            raise ValueObjectError('Comparing with a non value object.')
        return self._value == other.value()


