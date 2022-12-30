from valueobjects.errors.ValueObjectError import ValueObjectError
from valueobjects.numbers.int import Int
from valueobjects.value_object import ValueObject


class PositiveInt(ValueObject):

    def __init__(self, value: int | str | float):
        PositiveInt.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        Int.validate(value)
        if value < 1:
            raise ValueObjectError('Value must be greater than 0.')
