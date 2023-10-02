import unittest

from pyvalueobjects.lists.array_list import ArrayList
from pyvalueobjects.numbers.int import Int
from pyvalueobjects.strings.string import String


class TestArrayListValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = ArrayList(Int)([39])
        self.assertEqual([39], vo.value())

    def test_value_return_input_string_value(self):
        vo = ArrayList(String)(['a'])
        self.assertEqual(['a'], vo.value())

    def test_value_return_empty_array(self):
        vo = ArrayList(Int)([])
        self.assertEqual([], vo.value())

    def test_value_return_empty_string_array(self):
        vo = ArrayList(String)([])
        self.assertEqual([], vo.value())

    def test_value_return_multiple_input_values(self):
        vo = ArrayList(Int)([39, 100])
        self.assertEqual([39, 100], vo.value())

    def test_value_return_input_multiple_string_values(self):
        vo = ArrayList(String)(['a', 'b'])
        self.assertEqual(['a', 'b'], vo.value())