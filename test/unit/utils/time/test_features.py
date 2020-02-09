import unittest
from datetime import timedelta

from scripts.utils.time.features import add_timedeltas

class TestTimeChecks(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_adds_timedeltas(self):
    self.assertEqual(float(30000), add_timedeltas([timedelta(seconds = 10000),
                                   timedelta(seconds = 10000),
                                   timedelta(seconds = 10000)]).total_seconds())

    self.assertEqual(float(0), add_timedeltas([timedelta(seconds = 0), timedelta(seconds = 0)]).total_seconds())

    self.assertEqual(float(150), add_timedeltas([timedelta(seconds = 150)]).total_seconds())

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)