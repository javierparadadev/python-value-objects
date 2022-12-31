import unittest

from valueobjects.numbers.int import Int


class TestIntValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = Int(39)
        self.assertEqual(39, vo.value())

    def test_from_string_method_returns_int(self):
        vo = Int.from_str('39')
        self.assertEqual(39, vo.value())

    def test_from_float_method_returns_int(self):
        vo = Int.from_float(39.0)
        self.assertEqual(39, vo.value())
