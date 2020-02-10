import unittest
from datetime import timedelta

from scripts.calculate.pttime import construct_uniform_time_string
from scripts.calculate.pttime import get_timedelta_sum_as_uniform_time_sting
from scripts.calculate.pttime import get_timedelta_diff_as_uniform_time_sting
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT
from scripts.utils.time.constants import labeled_uniform_time_string_default
from scripts.utils.time.constants import DEFAULT_LABEL

class TestTimeCalculation(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_constructs_correct_uniform_time_string(self):
    self.assertEqual("[2.559 U @ 01:03:58]", construct_uniform_time_string("01:03:58"))
    self.assertEqual("[503 U @ 209:35:00]", construct_uniform_time_string("208:65:1800"))
    self.assertEqual("[28 U @ 11:40:00]", construct_uniform_time_string(28))
    self.assertEqual("[4.3 U @ 01:47:30]", construct_uniform_time_string(4.3))
    self.assertEqual("[2.75 U @ 01:08:45]", construct_uniform_time_string(2.75))
    self.assertEqual("[35.156 U @ 14:38:54]", construct_uniform_time_string(35.156))
    self.assertEqual("[2.749 U @ 01:08:44]", construct_uniform_time_string(2.74856942))

    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, construct_uniform_time_string(0))
    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, construct_uniform_time_string(0.000))
    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, construct_uniform_time_string(-28.3))
    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, construct_uniform_time_string("blah"))
    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT,
                     construct_uniform_time_string(timedelta(seconds = 0)))
    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, construct_uniform_time_string("-00:03:07"))

  def test_constructs_uniform_time_string_after_addition(self):
    self.assertEqual("[0.24 U @ 00:06:00]", get_timedelta_sum_as_uniform_time_sting(["1m", "2m", "3m"]))
    self.assertEqual("[0.04 U @ 00:01:00]", get_timedelta_sum_as_uniform_time_sting(["30s", "kek", "30s"]))
    self.assertEqual("[10 U @ 04:10:00]", get_timedelta_sum_as_uniform_time_sting([1, 2, 3, 4, "kek"]))
    self.assertEqual("[0.04 U @ 00:01:00]", get_timedelta_sum_as_uniform_time_sting(["0:1:0"]))

    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, get_timedelta_sum_as_uniform_time_sting([0, 0, 0, 0, "kek"]))
    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, get_timedelta_sum_as_uniform_time_sting(["0m"]))
    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, get_timedelta_sum_as_uniform_time_sting(["kek", "kek", "kekekk", "$$@@#!"]))

    self.assertEqual(labeled_uniform_time_string_default("WEIGHT"), get_timedelta_sum_as_uniform_time_sting(["kek", "kek", "kekekk", "$$@@#!"], "WEIGHT"))
    self.assertEqual("[label: 1 U @ 00:25:00]", get_timedelta_sum_as_uniform_time_sting([0.5, 0.5], "label"))

  def test_constructs_uniform_time_string_after_subtraction(self):
    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, get_timedelta_diff_as_uniform_time_sting(["3m", "2m", "1m"]))
    self.assertEqual("[0.007 U @ 00:00:10]", get_timedelta_diff_as_uniform_time_sting(["30s", "kek", "20s"]))
    self.assertEqual("[0.04 U @ 00:01:00]", get_timedelta_diff_as_uniform_time_sting([10, "4h", "00:09:00", "kek"]))
    self.assertEqual("[0.04 U @ 00:01:00]", get_timedelta_diff_as_uniform_time_sting(["0:1:0"]))

    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, get_timedelta_diff_as_uniform_time_sting([0, 0, 0, 0, "kek"]))
    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, get_timedelta_diff_as_uniform_time_sting(["0m"]))
    self.assertEqual(UNIFORM_TIME_STRING_DEFAULT, get_timedelta_diff_as_uniform_time_sting(["kek", "kek", "kekekk", "$$@@#!"]))

    self.assertEqual(labeled_uniform_time_string_default("WEIGHT"), get_timedelta_diff_as_uniform_time_sting(["kek", "kek", "kekekk", "$$@@#!"], "WEIGHT"))
    self.assertEqual("[label: 1 U @ 00:25:00]", get_timedelta_diff_as_uniform_time_sting([2, "00:25:00"], "label"))

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)