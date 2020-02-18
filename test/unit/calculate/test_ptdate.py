import unittest

from scripts.calculate.ptdate import calculate_date_difference_as_day_count

class TestDateCalculation(unittest.TestCase):
  def setUp(self):
    pass

  def test_calculating_date_difference(self):
    self.assertEqual(395, calculate_date_difference_as_day_count("02/25/2020", "03/26/2021"))
    self.assertEqual(20, calculate_date_difference_as_day_count("08/26/1993", "09/15/1993"))
    self.assertEqual(737514, calculate_date_difference_as_day_count("01/01/0001", "03/31/2020"))
    self.assertEqual(0, calculate_date_difference_as_day_count("03/03/2000", "03/03/2000"))
    self.assertEqual(1, calculate_date_difference_as_day_count("12/31/1991", "01/01/1992"))
    self.assertEqual(1, calculate_date_difference_as_day_count("01/01/2017", "12/31/2016"))
    self.assertEqual(730, calculate_date_difference_as_day_count("05/05/2017", "05/05/2019"))
    self.assertEqual(32, calculate_date_difference_as_day_count("01/31/2016", "03/03/2016"))

  def tearDown(self):
    pass

if __name__ == "__main__":
  unittest.main(verbosity = 2)