from pyvalueobjects.abstract.valueobject import ValueObject
from pyvalueobjects.errors.ValueObjectError import ValueObjectError


class String(ValueObject):

    _ALLOWED_INPUT_TYPES = {str, int, float, bool}

    def __init__(self, value: str):
        super().__init__(value)
        self._validate(value)

    def _validate(self, value):
        input_type = type(value)
        if input_type != str:
            raise ValueObjectError(f'Input type should be: str.')

    @classmethod
    def from_float(cls, value: float):
        if type(value) != float:
            raise ValueObjectError('Input type should be float.')

        try:
            return cls(str(value))
        except Exception as _:
            raise ValueObjectError('Input type should be valid float.')

    @classmethod
    def from_int(cls, value: int):
        if type(value) != int:
            raise ValueObjectError('Input type should be int.')

        try:
            return cls(str(value))
        except Exception as _:
            raise ValueObjectError('Input type should be valid int.')
