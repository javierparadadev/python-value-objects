import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.nullable_non_empty_string import NullableNonEmptyString


class TestNullableNonemptyStringValueObject(unittest.TestCase):

    def __init__(self, *args):
        super().__init__(*args)
        self._cls = NullableNonEmptyString

    def test_vo_equal_hash(self):
        original_vo_hash = hash(self._cls('patata'))
        equal_vo_hash = hash(self._cls('patata'))
        self.assertEqual(original_vo_hash, equal_vo_hash)

    def test_vo_different_hash(self):
        original_vo_hash = hash(self._cls('patata'))
        not_equal_vo_hash = hash(self._cls('tomato'))
        self.assertNotEqual(original_vo_hash, not_equal_vo_hash)

    def test_value_return_input_value(self):
        self.assertRaises(ValueObjectError, NullableNonEmptyString, '')

    def test_basic_string(self):
        vo = NullableNonEmptyString('patata')
        self.assertEqual('patata', vo.value())

    def test_none_return_none(self):
        vo = NullableNonEmptyString(None)
        self.assertEqual(None, vo.value())
