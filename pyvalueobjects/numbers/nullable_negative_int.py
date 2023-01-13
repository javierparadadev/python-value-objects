from pyvalueobjects import NegativeInt
from pyvalueobjects.abstract.nullablevalueobject import build_nullable

_nullable_cls = build_nullable(NegativeInt)


class NullableNegativeInt(_nullable_cls):

    def __init__(self, value: int = None):
        super().__init__(value)
