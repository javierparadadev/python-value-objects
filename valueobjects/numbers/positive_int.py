from valueobjects.errors.ValueObjectError import ValueObjectError
from valueobjects.numbers.int import Int


class PositiveInt(Int):

    def __init__(self, value: int | str | float):
        self._validate(value)
        super().__init__(value)

    def _validate(self, value):
        super()._validate(value)
        if value < 1:
            raise ValueObjectError('Value must be greater than 0.')
