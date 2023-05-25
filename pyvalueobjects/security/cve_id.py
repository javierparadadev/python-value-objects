import re
from re import Pattern

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


def _validate(value):
    matches = CveId.get_validator().match(value)
    if not matches:
        raise ValueObjectError('Value must be valid a CVE id format string.')


class CveId(NonEmptyString):

    @staticmethod
    def get_validator() -> Pattern:
        return re.compile(r'^CVE-\d{4}-\d{4,}$')

    def __init__(self, value: str):
        super().__init__(value)
        _validate(value)
