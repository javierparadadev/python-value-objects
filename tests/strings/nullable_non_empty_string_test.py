import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.nullable_non_empty_string import NullableNonEmptyString


class TestNullableNonemptyStringValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        self.assertRaises(ValueObjectError, NullableNonEmptyString, '')

    def test_basic_string(self):
        vo = NullableNonEmptyString('patata')
        self.assertEqual('patata', vo.value())

    def test_none_return_none(self):
        vo = NullableNonEmptyString(None)
        self.assertEqual(None, vo.value())
