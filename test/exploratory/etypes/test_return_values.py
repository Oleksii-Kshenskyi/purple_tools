import unittest
from datetime import timedelta

from scripts.utils.time.checks import is_of_type
from scripts.utils.time.constants import *

class TestReturnValues(unittest.TestCase):
  def setUp(self):
    self.source_timedelta = timedelta(hours = 3, minutes = 37, seconds = 58)

  def test_is_divmod_returns_float(self):
    total_seconds = round(self.source_timedelta.total_seconds()) # timedelta.total_seconds() returns float!
    units = round(total_seconds / TIME_UNIT_LENGTH_IN_SECONDS, ROUND_UNITS_TO)
    (rest, secs) = divmod(total_seconds, SECONDS_IN_MINUTE)
    (hrs, mins) = divmod(rest, MINUTES_IN_HOUR)

    self.assertEqual(True, is_of_type(total_seconds, int))
    self.assertEqual(False, is_of_type(units, int))
    self.assertEqual(True, is_of_type(rest, int))
    self.assertEqual(True, is_of_type(hrs, int))
    self.assertEqual(True, is_of_type(mins, int))
    self.assertEqual(True, is_of_type(secs, int))

  def tearDown(self):
    pass

if __name__ == "__main__":
  unittest.main(verbosity=2)