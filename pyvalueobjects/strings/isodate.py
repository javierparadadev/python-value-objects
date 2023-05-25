import datetime

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


class IsoDate(NonEmptyString):

    def __init__(self, value: str):
        super().__init__(value)
        self._validate(value)

    def _validate(self, value):
        try:
            datetime.datetime.fromisoformat(value)
        except ValueError:
            raise ValueObjectError('Value must be valid a iso date format string.')
