import uuid

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


class Uuid4(NonEmptyString):

    def __init__(self, value):
        super().__init__(value)
        self._validate(value)

    def _validate(self, value):
        try:
            uuid.UUID(str(value), version=4)
        except ValueError:
            raise ValueObjectError('Value must be valid a uuid4 format string.')
