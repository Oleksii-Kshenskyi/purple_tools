import unittest
from datetime import timedelta

class TestTypeCheck(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_type_string_check_behavior(self):
    self.assertEqual("int", type(354).__name__)
    self.assertEqual("float", type(3.054).__name__)
    self.assertEqual("str", type("this is a string").__name__)
    self.assertEqual("timedelta", type(timedelta(seconds = 2)).__name__)

  def test_type_check_behavior(self):
    self.assertEqual(int, type(354))
    self.assertEqual(float, type(3.054))
    self.assertEqual(float, type(3.0))
    self.assertEqual(str, type("this is a string"))
    self.assertEqual(timedelta, type(timedelta(seconds = 2)))

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)