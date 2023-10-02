import unittest

from pyvalueobjects.lists.nullable_array_list import NullableArrayList
from pyvalueobjects.numbers.int import Int
from pyvalueobjects.strings.string import String


class TestNullableArrayListValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = NullableArrayList(Int)([39])
        self.assertEqual([39], vo.value())

    def test_empty_list_value_return_input_value(self):
        vo = NullableArrayList(Int)([])
        self.assertEqual([], vo.value())

    def test_negative_value_return_input_value(self):
        vo = NullableArrayList(String)(['a', 'b'])
        self.assertEqual(['a', 'b'], vo.value())

    def test_none_value_return_none(self):
        vo = NullableArrayList(String)(None)
        self.assertEqual(None, vo.value())
