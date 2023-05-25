from pyvalueobjects.abstract.valueobject import ValueObject
from pyvalueobjects.errors.ValueObjectError import ValueObjectError


class String(ValueObject):

    _ALLOWED_INPUT_TYPES = {str, int, float, bool}

    def __init__(self, value: str):
        super().__init__(value)

    def _validate(self, value):
        super()._validate(value)
        input_type = type(value)
        if input_type != str:
            raise ValueObjectError(f'Input type should be: str.')
