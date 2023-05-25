from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.strings.uuid4 import Uuid4

_nullable_cls = build_nullable(Uuid4)


class NullableUuid4(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value)
