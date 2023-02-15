from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.numbers.negative_or_zero_int import NegativeOrZeroInt


class NegativeInt(NegativeOrZeroInt):

    def __init__(self, value: int):
        super().__init__(value)
        self._validate(value)

    def _validate(self, value):
        if value >= 0:
            raise ValueObjectError('Value must be less than 0.')
