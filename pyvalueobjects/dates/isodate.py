import datetime

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.string import String


class IsoDate(String):

    def __init__(self, value: str):
        super().__init__(value)

    def _validate(self, value):
        super()._validate(value)
        try:
            datetime.datetime.fromisoformat(value)
        except ValueError:
            raise ValueObjectError('Value must be valid a iso date format strings.')
