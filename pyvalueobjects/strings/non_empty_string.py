from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.string import String


def _validate(value):
    if value == '':
        raise ValueObjectError('Value must be a non empty string.')


class NonEmptyString(String):

    def __init__(self, value: str):
        super().__init__(value)
        _validate(value)
