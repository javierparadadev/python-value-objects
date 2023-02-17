from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.strings.string import String

_nullable_cls = build_nullable(String)


class NullableString(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value)
