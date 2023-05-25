import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.string import String


class TestStringValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = String('')
        self.assertEqual('', vo.value())

    def test_basic_string(self):
        vo = String('patata')
        self.assertEqual('patata', vo.value())

    def test_none_raise_error(self):
        self.assertRaises(ValueObjectError, String, None)
