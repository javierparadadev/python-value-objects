from valueobjects.errors.ValueObjectError import ValueObjectError
from valueobjects.numbers.int import Int
from valueobjects.value_object import ValueObject


class NaturalNumber(ValueObject):

    def __init__(self, value: int | str | float):
        NaturalNumber.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        Int.validate(value)
        if value < 0:
            raise ValueObjectError('Value must be greater or equals to 0.')
