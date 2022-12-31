from valueobjects.errors.ValueObjectError import ValueObjectError
from valueobjects.numbers.int import Int


class NaturalNumber(Int):

    def __init__(self, value: int):
        self._validate(value)
        super().__init__(value)

    def _validate(self, value):
        super()._validate(value)
        if value < 0:
            raise ValueObjectError('Value must be greater or equals to 0.')
