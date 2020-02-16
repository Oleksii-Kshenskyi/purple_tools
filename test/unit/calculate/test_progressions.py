import unittest

from scripts.utils.progressions.conditionals import EqualityConditional
from scripts.calculate.progressions import calculate_sum_of_arithmetic_progression
from scripts.calculate.progressions import find_progression_element_satisfying_condition
from scripts.calculate.progressions import determine_progression_parameters_by_sum_limiter

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
    self.assertEqual(3, find_progression_element_satisfying_condition(2, 14, 2, EqualityConditional(8)))
    self.assertEqual(2, find_progression_element_satisfying_condition(2, 17, 3, EqualityConditional(8)))
    self.assertEqual(6, find_progression_element_satisfying_condition(-16, 12, 4, EqualityConditional(8)))

    self.assertEqual(4, find_progression_element_satisfying_condition(-7, 43, 10, EqualityConditional(33)))
    self.assertEqual(1, find_progression_element_satisfying_condition(26, 68, 6, EqualityConditional(32)))
    self.assertEqual(1, find_progression_element_satisfying_condition(26, 68, 7, EqualityConditional(33)))
    self.assertEqual(1, find_progression_element_satisfying_condition(0, 24, 3, EqualityConditional(3)))
    self.assertEqual(7, find_progression_element_satisfying_condition(0, 24, 3, EqualityConditional(21)))
    self.assertEqual(1, find_progression_element_satisfying_condition(101, 909, 101, EqualityConditional(202)))

    self.assertEqual(34240, find_progression_element_satisfying_condition(256, 2187469, 21, EqualityConditional(719296)))
    self.assertEqual(429, find_progression_element_satisfying_condition(1037, 100937, 100, EqualityConditional(43937)))
    self.assertEqual(2073455, find_progression_element_satisfying_condition(102457, 2141981472, 1033, EqualityConditional(2141981472)))
    self.assertEqual(2, find_progression_element_satisfying_condition(10500, 249999999999999999999999999999999999999999999510500, 500000, EqualityConditional(1010500)))
    self.assertEqual(499999999999999999999999999999999999999999997, find_progression_element_satisfying_condition(10500, 249999999999999999999999999999999999999999999510500, 500000, EqualityConditional(249999999999999999999999999999999999999999998510500)))

    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(26, 24, 1, EqualityConditional(33))
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(24, 26, 1, None)
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(24, 26, 1, "Kek")
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(1, 7, 4, EqualityConditional(8))
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(1, 7, -1, EqualityConditional(8))
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(2, 26, 0, EqualityConditional(8))
    with self.assertRaises(ValueError):
      self.assertEqual(1, find_progression_element_satisfying_condition(26, 68, 5, EqualityConditional(31)))

    # this section checks that binary search raises ValueError if you're looking for an element that is not in the progression
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(2, 14, 2, EqualityConditional(3))
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(256, 2187469, 21, EqualityConditional(43937))
    with self.assertRaises(ValueError):
      find_progression_element_satisfying_condition(10500, 249999999999999999999999999999999999999999999510500, 500000, EqualityConditional(249999999999999999999999999999999999999999998510501))

  def test_remainder_and_upper_bound_calculated_correctly_through_limiter(self):
    self.assertEqual((13, 9), determine_progression_parameters_by_sum_limiter(100))
    self.assertEqual((10, 0), determine_progression_parameters_by_sum_limiter(55))
    self.assertEqual((23041, 10104), determine_progression_parameters_by_sum_limiter(265465465))
    self.assertEqual((27158623, 1339473), determine_progression_parameters_by_sum_limiter(368795416546849))
    self.assertEqual((33587647923147296813023991, 18435338379684661078750468), determine_progression_parameters_by_sum_limiter(564065046504650460460540654065046546540650456046504))

    self.assertEqual((1, 0), determine_progression_parameters_by_sum_limiter(1))
    self.assertEqual((1, 1), determine_progression_parameters_by_sum_limiter(2))
    self.assertEqual((2, 0), determine_progression_parameters_by_sum_limiter(3))
    self.assertEqual((2, 1), determine_progression_parameters_by_sum_limiter(4))
    self.assertEqual((2, 2), determine_progression_parameters_by_sum_limiter(5))
    self.assertEqual((3, 0), determine_progression_parameters_by_sum_limiter(6))
    self.assertEqual((3, 1), determine_progression_parameters_by_sum_limiter(7))
    self.assertEqual((3, 2), determine_progression_parameters_by_sum_limiter(8))
    self.assertEqual((3, 3), determine_progression_parameters_by_sum_limiter(9))
    self.assertEqual((4, 0), determine_progression_parameters_by_sum_limiter(10))

    with self.assertRaises(ValueError):
      determine_progression_parameters_by_sum_limiter(-3)
    with self.assertRaises(ValueError):
      determine_progression_parameters_by_sum_limiter(0)

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)