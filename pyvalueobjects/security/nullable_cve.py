from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.security.cve import Cve

_nullable_cls = build_nullable(Cve)


class NullableCve(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value)
