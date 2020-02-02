import unittest
from argparse import ArgumentError
from scripts.utils.testing.exploratory.eargparse.simple_parser import ArithmeticParser

class TestArgparseCLI(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_utility_performs_arithmetic_operations(self):
    a = ArithmeticParser()
    self.assertEqual(178, a.run_operation("add", 33, 145))
    self.assertEqual(-112, a.run_operation("sub", 33, 145))
    self.assertEqual(4785, a.run_operation("mul", 33, 145))
    self.assertEqual(0.22758620689655173, a.run_operation("div", 33, 145))

    self.assertRaises(KeyError, lambda: a.run_operation("kek", 33, 145))
    self.assertRaises(TypeError, lambda: a.run_operation("add", "kek", 145))
    self.assertRaises(TypeError, lambda: a.run_operation("add", 33, "kek"))

  def test_utility_parses_arguments_correctly(self):
    parser = ArithmeticParser().parser

    args = parser.parse_args(["add", "3", "6"])
    self.assertEqual("add", args.operation)
    self.assertIsInstance(args.first, int)
    self.assertIsInstance(args.second, int)

    with self.assertRaises(ArgumentError):
      parser.parse_args(["kek", "4", "6"])

    with self.assertRaises(ArgumentError):
      parser.parse_args(["add", "four", "6"])

    with self.assertRaises(ArgumentError):
      parser.parse_args(["add", "4", "six"])

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)