import unittest

from valueobjects.errors.ValueObjectError import ValueObjectError
from valueobjects.numbers.int import Int
from valueobjects.numbers.positive_int import PositiveInt


class TestPositiveIntValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = PositiveInt(39)
        self.assertEqual(39, vo.value())

    def test_from_string_method_returns_int(self):
        vo = PositiveInt.from_str('39')
        self.assertEqual(39, vo.value())

    def test_from_float_method_returns_int(self):
        vo = PositiveInt.from_float(39.0)
        self.assertEqual(39, vo.value())

    def test_zero_value_raises_error(self):
        self.assertRaises(ValueObjectError, PositiveInt, 0)

    def test_zero_from_string_method_raises_error(self):
        self.assertRaises(ValueObjectError, PositiveInt.from_str, 0)

    def test_zero_from_float_method_raises_error(self):
        self.assertRaises(ValueObjectError, PositiveInt.from_float, 0.0)

    def test_negative_value_raises_error(self):
        self.assertRaises(ValueObjectError, PositiveInt, -39)

    def test_from_string_method_raises_error(self):
        self.assertRaises(ValueObjectError, PositiveInt.from_str, '-39')

    def test_from_float_method_returns_negative_int(self):
        self.assertRaises(ValueObjectError, PositiveInt.from_float, -39.0)

    def test_from_string_with_not_numerical_format_raise_error(self):
        self.assertRaises(ValueObjectError, PositiveInt.from_str, 'patata')

    def test_from_float_with_decimals_raise_error(self):
        self.assertRaises(ValueObjectError, PositiveInt.from_float, 39.1)

    def test_from_str_number_with_no_decimals(self):
        vo = PositiveInt.from_str('39.0')
        self.assertEqual(39, vo.value())

    def test_from_str_negative_number_with_no_decimals(self):
        self.assertRaises(ValueObjectError, PositiveInt.from_str, '-39.0')

    def test_from_str_number_with_decimals_raises_error(self):
        self.assertRaises(ValueObjectError, PositiveInt.from_float, '39.1')

    def test_from_str_negative_number_with_decimals_raises_error(self):
        self.assertRaises(ValueObjectError, PositiveInt.from_float, '-39.1')
