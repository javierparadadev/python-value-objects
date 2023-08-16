from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.strings.non_empty_string import NonEmptyString

_nullable_cls = build_nullable(NonEmptyString)


class NullableNonEmptyString(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value)
