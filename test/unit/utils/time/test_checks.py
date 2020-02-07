import unittest
from datetime import timedelta

from scripts.utils.time.checks import is_valid_time_string
from scripts.utils.time.checks import is_valid_duration_string
from scripts.utils.time.checks import is_of_type

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

  def test_checks_duration_string(self):
    self.assertEqual(True, is_valid_duration_string("1h"))
    self.assertEqual(True, is_valid_duration_string("35h5m2s"))
    self.assertEqual(True, is_valid_duration_string("2m34s"))
    self.assertEqual(True, is_valid_duration_string("333h2222222m34343535s"))
    self.assertEqual(True, is_valid_duration_string("5h25s"))
    self.assertEqual(True, is_valid_duration_string("34s45h2m"))
    self.assertEqual(True, is_valid_duration_string("1h25m"))
    self.assertEqual(True, is_valid_duration_string("3m"))
    self.assertEqual(True, is_valid_duration_string("44s"))

    self.assertEqual(False, is_valid_duration_string("1h3.5m"))
    self.assertEqual(False, is_valid_duration_string("1h2m3k"))
    self.assertEqual(False, is_valid_duration_string("kk2mkk"))
    self.assertEqual(False, is_valid_duration_string("hh2m1s"))
    self.assertEqual(False, is_valid_duration_string("hhmmss"))
    self.assertEqual(False, is_valid_duration_string("h1m2s"))
    self.assertEqual(False, is_valid_duration_string(" h3m44s"))
    self.assertEqual(False, is_valid_duration_string("1h1m2"))
    self.assertEqual(False, is_valid_duration_string("1h1 2s"))
    self.assertEqual(False, is_valid_duration_string("1h 2s"))
    self.assertEqual(False, is_valid_duration_string(" "))
    self.assertEqual(False, is_valid_duration_string("1m1m1m"))
    self.assertEqual(False, is_valid_duration_string("1h1m1s1h"))
    self.assertEqual(False, is_valid_duration_string("1s1s"))
    self.assertEqual(False, is_valid_duration_string("1m1h1m"))

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)