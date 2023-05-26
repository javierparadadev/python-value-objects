import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.security.cpe import Cpe
from pyvalueobjects.security.cve_id import CveId


class TestCveIdValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = Cpe('cpe:/a:openjdk:openjdk:8u282')
        self.assertEqual('cpe:/a:openjdk:openjdk:8u282', vo.value())

    def test_bad_format_cve_raise_error(self):
        self.assertRaises(ValueObjectError, Cpe, 'no-format')

    def test_none_raise_error(self):
        self.assertRaises(ValueObjectError, Cpe, None)
