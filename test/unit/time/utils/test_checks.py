import unittest
from datetime import timedelta

from scripts.time.utils.checks import is_valid_time_string
from scripts.time.utils.checks import is_of_type

class TestTimeChecks(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_checks_time_string(self):
    self.assertEqual(True, is_valid_time_string("03:54:06"))
    self.assertEqual(True, is_valid_time_string("00:00:00"))
    self.assertEqual(True, is_valid_time_string("00:01:01"))
    self.assertEqual(True, is_valid_time_string("01:00:00"))
    self.assertEqual(True, is_valid_time_string("00:01:00"))
    self.assertEqual(True, is_valid_time_string("303:210:54666"))

    self.assertEqual(False, is_valid_time_string("bkshlb"))
    self.assertEqual(False, is_valid_time_string("03-38-46"))
    self.assertEqual(False, is_valid_time_string("k3:14:10"))
    self.assertEqual(False, is_valid_time_string("208:54:3?"))
    self.assertEqual(False, is_valid_time_string("03:0*:18"))

  def test_checks_type(self):
    self.assertEqual(True, is_of_type(3.0, float))
    self.assertEqual(True, is_of_type(3565, int))
    self.assertEqual(True, is_of_type("This is yet another string!@#\\", str))
    self.assertEqual(True, is_of_type(timedelta(seconds = 2), timedelta))

    self.assertEqual(False, is_of_type(3, float))
    self.assertEqual(False, is_of_type(3.0, int))
    self.assertEqual(False, is_of_type("3.0", float))

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)