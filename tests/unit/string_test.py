import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.string import String


class TestStringValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = String('')
        self.assertEqual('', vo.value())

    def test_from_string_method_returns_string(self):
        vo = String.from_int(39)
        self.assertEqual('39', vo.value())

    def test_from_float_method_returns_int_format_string(self):
        vo = String.from_float(39.0)
        self.assertEqual('39.0', vo.value())

    def test_zero_value_return_input_value(self):
        vo = String.from_int(0)
        self.assertEqual('0', vo.value())

    def test_basic_string(self):
        vo = String('patata')
        self.assertEqual('patata', vo.value())

    def test_none_raise_error(self):
        self.assertRaises(ValueObjectError, String, None)
