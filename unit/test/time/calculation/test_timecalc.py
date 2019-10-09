import unittest
from scripts.time.calculation.timecalc import *

class TestTimeCalculation(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_constructs_correct_uniform_time_string(self):
    self.assertEqual("[2.559 U @ 01:03:58]", construct_uniform_time_string("01:03:58"))
    self.assertEqual("[503 U @ 209:35:00]", construct_uniform_time_string("208:65:1800"))
    self.assertEqual("[35.156 U @ 14:38:54]", construct_uniform_time_string(35.156))
    self.assertEqual("[2.749 U @ 01:08:44]", construct_uniform_time_string(2.74856942))
    self.assertEqual("[28 U @ 11:40:00]", construct_uniform_time_string(28))

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)