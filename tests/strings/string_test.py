import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.string import String


class TestStringValueObject(unittest.TestCase):

    def __init__(self, *args):
        super().__init__(*args)
        self._cls = String

    def test_vo_equal_hash(self):
        original_vo_hash = hash(self._cls('patata'))
        equal_vo_hash = hash(self._cls('patata'))
        self.assertEqual(original_vo_hash, equal_vo_hash)

    def test_vo_different_hash(self):
        original_vo_hash = hash(self._cls('patata'))
        not_equal_vo_hash = hash(self._cls('tomato'))
        self.assertNotEqual(original_vo_hash, not_equal_vo_hash)

    def test_value_return_input_value(self):
        vo = String('')
        self.assertEqual('', vo.value())

    def test_basic_string(self):
        vo = String('patata')
        self.assertEqual('patata', vo.value())

    def test_none_raise_error(self):
        self.assertRaises(ValueObjectError, String, None)
