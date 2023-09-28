import re

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


class Cve(NonEmptyString):

    __MATCHER = re.compile(r'^CVE-\d{4}-\d{4,}$')

    def __init__(self, value: str):
        super().__init__(value)

    def _validate(self, value: str):
        super()._validate(value)
        try:
            is_correct = Cve.__MATCHER.match(value)
            if not is_correct:
                raise ValueObjectError('Value must be valid a CVE id format strings.')
        except ValueError:
            raise ValueObjectError('Value must be valid a CVE id format strings.')

