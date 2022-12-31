from valueobjects.errors.ValueObjectError import ValueObjectError
from valueobjects.value_object import ValueObject


class Int(ValueObject):

    _ALLOWED_INPUT_TYPES = {str, int, float}

    def __init__(self, value: int | str | float):
        self._validate(value)
        super().__init__(value)

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

        if input_type not in Int._ALLOWED_INPUT_TYPES:
            raise ValueObjectError(f'Input type should be: {Int._ALLOWED_INPUT_TYPES}.')

        if input_type in {str, float}:
            try:
                int(value)
            except Exception as _:
                raise ValueObjectError('Input cannot be converted to integer.')
