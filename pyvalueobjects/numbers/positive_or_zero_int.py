from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.numbers.int import Int


class PositiveOrZeroInt(Int):

    def __init__(self, value: int):
        super().__init__(value)
        self._validate(value)

    def _validate(self, value):
        if value < 0:
            raise ValueObjectError('Value must be greater or equals to 0.')
