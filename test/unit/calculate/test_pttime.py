import unittest
from datetime import timedelta

from scripts.calculate.pttime import construct_uniform_time_string
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT

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

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)