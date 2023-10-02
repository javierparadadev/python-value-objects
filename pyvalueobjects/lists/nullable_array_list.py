from __future__ import annotations

from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.lists.array_list import ArrayList


def NullableArrayList(cls):

    _nullable_cls = build_nullable(ArrayList(cls))
    class _NullableArrayList(_nullable_cls):

        def __init__(self, values: list[cls] | None):
            super().__init__(values)

        def _validate(self, value):
            super()._validate(value)
            input_type = type(value)
            if input_type != list:
                raise ValueObjectError(f'Input type should be: list.')

    return _NullableArrayList
