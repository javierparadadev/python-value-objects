import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.security.nullable_cve import NullableCve


class TestNullableCveValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        self.assertRaises(ValueObjectError, NullableCve, '')

    def test_basic_cve(self):
        vo = NullableCve('CVE-2023-33000')
        self.assertEqual('CVE-2023-33000', vo.value())

    def test_none_return_none(self):
        vo = NullableCve(None)
        self.assertEqual(None, vo.value())

