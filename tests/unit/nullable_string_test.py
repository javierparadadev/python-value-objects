import unittest

from pyvalueobjects.strings.nullable_string import NullableString


class TestNullableStringValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = NullableString('')
        self.assertEqual('', vo.value())

    def test_basic_string(self):
        vo = NullableString('patata')
        self.assertEqual('patata', vo.value())

    def test_none_return_none(self):
        vo = NullableString(None)
        self.assertEqual(None, vo.value())
