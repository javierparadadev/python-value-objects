from valueobjects.errors.ValueObjectError import ValueObjectError
from valueobjects.value_object import ValueObject


class Int(ValueObject):

    _ALLOWED_INPUT_TYPES = {str, int, float}

    def __init__(self, value: int):
        super().__init__(value)
        self._validate(value)

    @classmethod
    def from_float(cls, value: float):
        try:
            return cls(int(value))
        except Exception as _:
            raise ValueObjectError('Input type should valid float.')

    @classmethod
    def from_str(cls, value: str):
        try:
            return cls(int(value))
        except Exception as _:
            raise ValueObjectError('Input type should be number format string.')

    def _validate(self, value):
        input_type = type(value)
        if input_type != int:
            raise ValueObjectError(f'Input type should be: int.')
