from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.security.cpe import Cpe

_nullable_cls = build_nullable(Cpe)


class NullableCpe(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value)
