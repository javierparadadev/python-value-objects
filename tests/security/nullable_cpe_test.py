import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.security.nullable_cpe import NullableCpe


class TestNullableCpeValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        self.assertRaises(ValueObjectError, NullableCpe, '')

    def test_basic_cpe(self):
        vo = NullableCpe('cpe:/a:openjdk:openjdk:8u282')
        self.assertEqual('cpe:/a:openjdk:openjdk:8u282', vo.value())

    def test_none_return_none(self):
        vo = NullableCpe(None)
        self.assertEqual(None, vo.value())

