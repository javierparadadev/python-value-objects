import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.security.cve_id import CveId


class TestIntValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = CveId('CVE-2007-0994')
        self.assertEqual('CVE-2007-0994', vo.value())

    def test_from_str_number_with_decimals_raises_error(self):
        self.assertRaises(ValueObjectError, CveId.from_float, '39.1')

    def test_from_str_negative_number_with_decimals_raises_error(self):
        self.assertRaises(ValueObjectError, CveId.from_float, '-39.1')

    def test_none_raise_error(self):
        self.assertRaises(ValueObjectError, CveId, None)
