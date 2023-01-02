from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.numbers.int import Int

_nullable_cls = build_nullable(Int)


class NullableInt(_nullable_cls):

    def __init__(self, value: int = None):
        super().__init__(value)
