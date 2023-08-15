import datetime
import unittest

from pyvalueobjects.dates.isodate import IsoDate
from pyvalueobjects.errors.ValueObjectError import ValueObjectError


class TestIsoDateValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        the_date = datetime.datetime.now().isoformat()
        vo = IsoDate(the_date)
        self.assertEqual(the_date, vo.value())

    def test_none_raise_error(self):
        self.assertRaises(ValueObjectError, IsoDate, None)

    def test_ctime_format_raise_error(self):
        self.assertRaises(ValueObjectError, IsoDate, datetime.datetime.now().ctime())

    def test_empty_string_raise_error(self):
        self.assertRaises(ValueObjectError, IsoDate, '')

    def test_random_string_raise_error(self):
        self.assertRaises(ValueObjectError, IsoDate, 'patata')
