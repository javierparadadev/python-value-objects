import unittest
import uuid

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.uuid4 import Uuid4


class TestUuid4ValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        the_uuid = str(uuid.uuid4())
        vo = Uuid4(the_uuid)
        self.assertEqual(the_uuid, vo.value())

    def test_none_raise_error(self):
        self.assertRaises(ValueObjectError, Uuid4, None)

    def test_empty_string_raise_error(self):
        self.assertRaises(ValueObjectError, Uuid4, '')

    def test_random_string_raise_error(self):
        self.assertRaises(ValueObjectError, Uuid4, 'patata')

    def test_old_uuid_version_raise_error(self):
        self.assertRaises(ValueObjectError, Uuid4, uuid.uuid1())
