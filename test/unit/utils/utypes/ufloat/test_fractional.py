import unittest
from scripts.utils.utypes.ufloat.fractional import get_fractional_part_as_string
from scripts.utils.utypes.ufloat.fractional import is_fractional_part_significant

class TestFractionalUtils(unittest.TestCase):
  def setUp(self):
    pass

  def test_returns_fractional_part_as_string(self):
    self.assertEqual("", get_fractional_part_as_string("0.345"))
    self.assertEqual("", get_fractional_part_as_string(285))

    self.assertEqual("5", get_fractional_part_as_string(3.5))
    self.assertEqual("0", get_fractional_part_as_string(355.0))
    self.assertEqual("0", get_fractional_part_as_string(355.000000))
    self.assertEqual("85", get_fractional_part_as_string(3.85))
    self.assertEqual("155", get_fractional_part_as_string(235.155))
    self.assertEqual("123456", get_fractional_part_as_string(212.123456))

  def test_determines_fractional_significance(self):
    self.assertEqual(True, is_fractional_part_significant(3.3))
    self.assertEqual(True, is_fractional_part_significant(3.03))
    self.assertEqual(True, is_fractional_part_significant(3.003))
    self.assertEqual(True, is_fractional_part_significant(3.0003))
    self.assertEqual(True, is_fractional_part_significant(3.00003))
    self.assertEqual(True, is_fractional_part_significant(3.000003))

    self.assertEqual(False, is_fractional_part_significant(3.0))
    self.assertEqual(False, is_fractional_part_significant(256.0))
    self.assertEqual(False, is_fractional_part_significant(123456.000000))

  def tearDown(self):
    pass


if __name__ == "__main__":
  unittest.main(verbosity = 2)