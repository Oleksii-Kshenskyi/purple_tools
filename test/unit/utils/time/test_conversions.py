import unittest
from datetime import timedelta

from scripts.utils.time.conversions import check_float_validity_and_convert_from_string
from scripts.utils.time.conversions import convert_float_to_timedelta
from scripts.utils.time.conversions import convert_time_string_to_timedelta
from scripts.utils.time.conversions import convert_duration_string_to_timedelta
from scripts.utils.time.conversions import convert_to_timedelta
from scripts.utils.time.conversions import convert_timedelta_to_uniform_time_string
from scripts.utils.time.constants import TIME_UNIT_LENGTH_IN_SECONDS
  
class TestConversions(unittest.TestCase):
  def setUp(self):
    pass

  def __float_conversion_test(self, test_func):
    self.assertEqual(timedelta(seconds = 34.156 * TIME_UNIT_LENGTH_IN_SECONDS), test_func(34.156))
    self.assertEqual(timedelta(seconds = 0 * TIME_UNIT_LENGTH_IN_SECONDS), test_func(0.0))
    self.assertEqual(timedelta(seconds = 3 * TIME_UNIT_LENGTH_IN_SECONDS), test_func(3.0))
    self.assertEqual(timedelta(hours = 1, minutes = 8, seconds = 44), test_func(2.749))

    self.assertEqual(None, test_func(-5.46))
    self.assertEqual(None, test_func("344"))

  def __time_string_conversion_test(self, test_func):
    self.assertEqual(timedelta(hours = 2, minutes = 53, seconds = 13), test_func("02:53:13"))
    self.assertEqual(timedelta(hours = 34, minutes = 3658, seconds = 553421), test_func("34:3658:553421"))
    self.assertEqual(timedelta(hours = 1, minutes = 2, seconds = 3), test_func("1:2:3"))

    self.assertEqual(None, test_func("-02:03:45"))
    self.assertEqual(None, test_func("02:03:04:05"))
    self.assertEqual(None, test_func("02-03-11"))
    self.assertEqual(None, test_func("0k:12:48"))
    self.assertEqual(None, test_func("@@:$$:!!"))

  def __duration_string_conversion_test(self, test_func):
    self.assertEqual(timedelta(hours = 35, seconds = 3), test_func("35h3s"))
    self.assertEqual(timedelta(hours = 2, minutes = 77, seconds = 3), test_func("2h77m3s"))
    self.assertEqual(timedelta(hours = 2, minutes = 3, seconds = 1), test_func("1s2h3m"))
    self.assertEqual(timedelta(hours = 2), test_func("2h"))
    self.assertEqual(timedelta(hours = 1, minutes = 3), test_func("3m1h"))
    self.assertEqual(timedelta(minutes = 160, seconds = 2440), test_func("160m2440s"))

    self.assertEqual(None, test_func("1s2h3m1s"))
    self.assertEqual(None, test_func("-1s"))

  def test_checks_float_validity(self):
    self.assertEqual(0.0, check_float_validity_and_convert_from_string("0"))
    self.assertEqual(0.765484612, check_float_validity_and_convert_from_string("0.765484612"))
    self.assertEqual(234564.0, check_float_validity_and_convert_from_string("234564"))
    self.assertEqual(58975.4946548, check_float_validity_and_convert_from_string("58975.4946548"))
    self.assertEqual(-3454641.12361, check_float_validity_and_convert_from_string("-3454641.12361"))
    self.assertEqual(34454.54242, check_float_validity_and_convert_from_string("34454.54242"))

    self.assertEqual(None, check_float_validity_and_convert_from_string("34454.54k42"))
    self.assertEqual(None, check_float_validity_and_convert_from_string("@.36"))
    self.assertEqual(None, check_float_validity_and_convert_from_string("34454..54242"))
    self.assertEqual(None, check_float_validity_and_convert_from_string("7.554!"))

  def test_converts_float_to_timedelta(self):
    self.__float_conversion_test(test_func = convert_float_to_timedelta)

  def test_converts_time_string_to_timedelta(self):
    self.__time_string_conversion_test(test_func = convert_time_string_to_timedelta)

  def test_converts_duration_string_to_timedelta(self):
    self.__duration_string_conversion_test(test_func = convert_duration_string_to_timedelta)

  def test_converts_to_timedelta(self):
    self.__float_conversion_test(test_func = convert_to_timedelta)
    self.__time_string_conversion_test(test_func = convert_to_timedelta)
    self.__duration_string_conversion_test(test_func = convert_to_timedelta)

  def test_converts_timedelta_to_uniform_time_string(self):
    self.assertEqual("[0 U @ 00:00:00]", 
      convert_timedelta_to_uniform_time_string(3))
    self.assertEqual("[22 U @ 09:10:00]", 
      convert_timedelta_to_uniform_time_string(timedelta(hours = 9, minutes = 10)))
    self.assertEqual("[0 U @ 00:00:00]", 
      convert_timedelta_to_uniform_time_string(timedelta(seconds = 0)))
    self.assertEqual("[8.757 U @ 03:38:56]",
      convert_timedelta_to_uniform_time_string(timedelta(hours = 3, minutes = 38, seconds = 56)))
    self.assertEqual("[295.432 U @ 123:05:48]",
      convert_timedelta_to_uniform_time_string(timedelta(seconds = 443148)))

  def tearDown(self):
    pass


if __name__ == "__main__":
  unittest.main(verbosity=2)