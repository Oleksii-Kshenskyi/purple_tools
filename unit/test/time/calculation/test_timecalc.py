import unittest
from scripts.time.calculation.timecalc import add

class TestTimeCalculation(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_add(self):
      self.assertEqual(5.465, add(2.132, 3.333))
      self.assertEqual(20000000000000000000000001, add(10000000000000000000000000, 10000000000000000000000001))

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)