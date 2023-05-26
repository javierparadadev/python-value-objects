import unittest
import uuid

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.nullable_uuid4 import NullableUuid4


class TestNullableUuid4ValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        the_uuid = str(uuid.uuid4())
        vo = NullableUuid4(the_uuid)
        self.assertEqual(the_uuid, vo.value())

    def test_none_return_none(self):
        vo = NullableUuid4(None)
        self.assertTrue(vo.value() is None)

    def test_empty_string_raise_error(self):
        self.assertRaises(ValueObjectError, NullableUuid4, '')

    def test_random_string_raise_error(self):
        self.assertRaises(ValueObjectError, NullableUuid4, 'patata')
