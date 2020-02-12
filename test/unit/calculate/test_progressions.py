import unittest

from scripts.calculate.progressions import calculate_sum_of_arithmetic_progression
from scripts.calculate.progressions import find_progression_element_satisfying_condition, BinaryResult

class TestProgressionsCalculation(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_arithmetic_progression_sum_is_calculated_correctly(self):
    self.assertEqual(52, calculate_sum_of_arithmetic_progression(3, 10))
    self.assertEqual(33930, calculate_sum_of_arithmetic_progression(1, 260))
    self.assertEqual(0, calculate_sum_of_arithmetic_progression(-3, 3))
    self.assertEqual(-20055, calculate_sum_of_arithmetic_progression(-200, -10))
    self.assertEqual(1501500, calculate_sum_of_arithmetic_progression(1000, 2000))
    self.assertEqual(20000000100000000, calculate_sum_of_arithmetic_progression(1, 200000000))

    with self.assertRaises(ValueError):
      calculate_sum_of_arithmetic_progression(4, 3)

    with self.assertRaises(ValueError):
      calculate_sum_of_arithmetic_progression(-10, -11)

  def test_binary_search_finds_elements(self):
    self.assertEqual(3, find_progression_element_satisfying_condition(2, 14, 2, self._condition_equality_8))
    self.assertEqual(2, find_progression_element_satisfying_condition(2, 17, 3, self._condition_equality_8))
    self.assertEqual(6, find_progression_element_satisfying_condition(-16, 12, 4, self._condition_equality_8))

    self.assertEqual(4, find_progression_element_satisfying_condition(-7, 43, 10, self._condition_equality_33))
    self.assertEqual(1, find_progression_element_satisfying_condition(26, 68, 7, self._condition_equality_33))

    self.assertEqual(34240, find_progression_element_satisfying_condition(256, 2187469, 21, self._condition_equality_719296))

    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(26, 24, 1, self._condition_equality_33)
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(24, 26, 1, None)
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(24, 26, 1, "Kek")
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(1, 7, 4, self._condition_equality_8)

  def _condition_equality_8(self, searched):
    if searched < 8:
      return BinaryResult.MOVE_RIGHT
    elif searched == 8:
      return BinaryResult.OK
    elif searched > 8:
      return BinaryResult.MOVE_LEFT

  def _condition_equality_33(self, searched):
    if searched < 33:
      return BinaryResult.MOVE_RIGHT
    elif searched == 33:
      return BinaryResult.OK
    elif searched > 33:
      return BinaryResult.MOVE_LEFT

  def _condition_equality_719296(self, searched):
    if searched < 719296:
      return BinaryResult.MOVE_RIGHT
    elif searched == 719296:
      return BinaryResult.OK
    elif searched > 719296:
      return BinaryResult.MOVE_LEFT

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)