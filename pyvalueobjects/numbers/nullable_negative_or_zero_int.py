from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.numbers.negative_or_zero_int import NegativeOrZeroInt

_nullable_cls = build_nullable(NegativeOrZeroInt)


class NullableNegativeOrZeroInt(_nullable_cls):

    def __init__(self, value: int = None):
        super().__init__(value)
