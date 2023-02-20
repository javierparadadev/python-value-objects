import unittest

from pyvalueobjects.strings.nullable_string import NullableString


class TestNullableStringValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = NullableString('')
        self.assertEqual('', vo.value())

    def test_from_string_method_returns_string(self):
        vo = NullableString.from_int(39)
        self.assertEqual('39', vo.value())

    def test_from_float_method_returns_int_format_string(self):
        vo = NullableString.from_float(39.0)
        self.assertEqual('39.0', vo.value())

    def test_zero_value_return_input_value(self):
        vo = NullableString.from_int(0)
        self.assertEqual('0', vo.value())

    def test_basic_string(self):
        vo = NullableString('patata')
        self.assertEqual('patata', vo.value())

    def test_none_return_none(self):
        vo = NullableString(None)
        self.assertEqual(None, vo.value())
