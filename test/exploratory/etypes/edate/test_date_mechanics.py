import unittest
from datetime import date, timedelta

class TestDateMechanics(unittest.TestCase):
  def setUp(self):
    pass

  def test_date_formats_and_capabilities(self):
    self.assertEqual("2020-02-18", date(year = 2020, month = 2, day = 18).isoformat())
    self.assertEqual("2020-02-08", date(year = 2020, month = 2, day = 8).isoformat())
    self.assertEqual("0001-01-01", date(year = 1, month = 1, day = 1).isoformat())

    self.assertEqual("02/18/20", date(year = 2020, month = 2, day = 18).strftime("%m/%d/%y"))
    self.assertEqual("02/18/2020", date(year = 2020, month = 2, day = 18).strftime("%m/%d/%Y"))
    self.assertEqual("01/01/0001", date(year = 1, month = 1, day = 1).strftime("%m/%d/%Y"))
    
    self.assertEqual("9999-01-01", date(year = 9999, month = 1, day = 1).isoformat())
    with self.assertRaises(ValueError):
      date(year = 10000, month = 1, day = 1).isoformat()

    with self.assertRaises(ValueError):
      date(year = 2000000000, month = 2, day = 12).isoformat()
    with self.assertRaises(OverflowError):
      date(year = 20000000000000000000000000000000, month = 2, day = 12).isoformat()

    with self.assertRaises(ValueError):
      date(year = 2020, month = 13, day = 1).isoformat()
    with self.assertRaises(ValueError):
      date(year = 2020, month = 1, day = 32).isoformat()

  def test_date_difference_is_calculated_as_expected(self):
    self.assertEqual(timedelta(days = 14), date(year = 2020, month = 2, day = 7) - date(year = 2020, month = 1, day = 24))
    self.assertEqual(timedelta(days = 14), abs(date(year = 2020, month = 1, day = 24) - date(year = 2020, month = 2, day = 7)))

    regular_date = date(year = 2020, month = 1, day = 24)
    borked_date = date(year = 1, month = 2, day = 7)
    day_difference = regular_date - borked_date
    self.assertEqual(day_difference, abs(borked_date - regular_date))

    first_date = date(year = 2020, month = 3, day = 17)
    second_date = date(year = 2020, month = 2, day = 3)
    difference = timedelta(days = 43) # timedelta neither has years nor weeks, only days
    self.assertEqual(difference, first_date - second_date)
    # seems like the actual difference calculation will have to be made
    # based on the day count, the application will have to calculate 
    # years/months/weeks on its own

  def tearDown(self):
    pass


if __name__ == "__main__":
  unittest.main(verbosity = 2)