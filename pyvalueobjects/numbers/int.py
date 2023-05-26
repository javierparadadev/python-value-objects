from pyvalueobjects.abstract.valueobject import ValueObject
from pyvalueobjects.errors.ValueObjectError import ValueObjectError


class Int(ValueObject):

    _ALLOWED_INPUT_TYPES = {str, int, float}

    def __init__(self, value: int):
        super().__init__(value)

    @classmethod
    def from_float(cls, value: float):
        if type(value) != float:
            raise ValueObjectError('Input type should be float.')

        if not value.is_integer():
            raise ValueObjectError('Input type should be float without decimals.')

        try:
            return cls(int(value))
        except Exception as _:
            raise ValueObjectError('Input type should be valid float.')

    @classmethod
    def from_str(cls, value: str):
        try:
            decimal_value = float(value)

            if not decimal_value.is_integer():
                raise ValueObjectError('Input type shouldnot have decimals.')

            int_value = int(decimal_value)

            return cls(int_value)
        except Exception as _:
            raise ValueObjectError('Input type should be number format strings.')

    def _validate(self, value):
        super()._validate(value)
        input_type = type(value)
        if input_type != int:
            raise ValueObjectError(f'Input type should be: int.')
