import unittest

class TestFractionalBehavior(unittest.TestCase):
  def setUp(self):
    pass

  def test_non_fractional_float_is_equal_to_int(self):
    the_int = 355
    the_float = 355.0
    self.assertEqual(the_int, the_float)
    self.assertEqual(True, the_int == the_float)

  def tearDown(self):
    pass


if __name__ == "__main__":
  unittest.main(verbosity = 2)