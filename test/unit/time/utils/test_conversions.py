import unittest
from scripts.time.utils.conversions import check_float_validity_and_convert_from_string
  
class TestConversions(unittest.TestCase):
  def setUp(self):
    pass

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

  def tearDown(self):
    pass


if __name__ == "__main__":
  unittest.main(verbosity=2)