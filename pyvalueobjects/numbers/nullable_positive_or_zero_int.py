from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.numbers.positive_or_zero_int import PositiveOrZeroInt

_nullable_cls = build_nullable(PositiveOrZeroInt)


class NullablePositiveOrZeroInt(_nullable_cls):

    def __init__(self, value: int = None):
        super().__init__(value)
