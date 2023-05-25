from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.numbers.positive_or_zero_int import PositiveOrZeroInt


def _validate(value):
    if value <= 0:
        raise ValueObjectError('Value must be greater than 0.')


class PositiveInt(PositiveOrZeroInt):

    def __init__(self, value: int):
        super().__init__(value)
        _validate(value)
