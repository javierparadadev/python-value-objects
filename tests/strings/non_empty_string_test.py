import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


class TestNonemptyStringValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        self.assertRaises(ValueObjectError, NonEmptyString, '')

    def test_basic_string(self):
        vo = NonEmptyString('patata')
        self.assertEqual('patata', vo.value())

    def test_none_return_none(self):
        self.assertRaises(ValueObjectError, NonEmptyString, None)
