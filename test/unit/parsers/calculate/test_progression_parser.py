import unittest

from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.parsers.calculate.progression_parser import CalculateProgressionParser
from scripts.utils.constants import PARSER_IDENTIFIER_NAME
from scripts.utils.constants import LIMITER_PROGRESSION_RESULT, SUM_PROGRESSION_RESULT

class TestCalculateProgressionParser(unittest.TestCase):
  
  def setUp(self):
    self.parser = CalculateProgressionParser()
    self.parser.create_parser()

  def test_parser_processes_arguments(self):
    parse_result = self.parser.parser.parse_args([self.parser.method_name_limiter, "100"])
    self.assertEqual([100], parse_result.by_limiter)
    self.assertIsInstance(parse_result.by_limiter[0], int)
    parse_result = self.parser.parser.parse_args([self.parser.method_short_name_limiter, "2560"])
    self.assertEqual([2560], parse_result.by_limiter)
    self.assertIsInstance(parse_result.by_limiter[0], int)

    parse_result = self.parser.parser.parse_args([self.parser.method_name_bounds, "3", "100"])
    self.assertEqual([3, 100], parse_result.by_bounds)
    self.assertIsInstance(parse_result.by_bounds[0], int)
    self.assertIsInstance(parse_result.by_bounds[1], int)
    parse_result = self.parser.parser.parse_args([self.parser.method_short_name_bounds, "3", "100"])
    self.assertEqual([3, 100], parse_result.by_bounds)
    self.assertIsInstance(parse_result.by_bounds[0], int)
    self.assertIsInstance(parse_result.by_bounds[1], int)

    with self.assertRaises(ValueError):
      self.parser.parser.parse_args([self.parser.method_name_limiter, "100", self.parser.method_name_bounds, "55", "100"])

  def test_as_subparser(self):
    self.papa_parser = AbstractParser()
    self.papa_parser.create_parser()
    self.parser = CalculateProgressionParser()
    self.parser.create_subparser(self.papa_parser)

    parse_result = self.papa_parser.parser.parse_args([self.parser.name, self.parser.method_name_limiter, "100"])
    self.assertEqual([100], parse_result.by_limiter)

  def test_parser_executes_subcommand(self):
    parse_result = self.parser.parser.parse_args([self.parser.method_name_limiter, "100"])
    execution_result = self.parser.execute_command(parse_result)
    self.assertEqual(LIMITER_PROGRESSION_RESULT.format(13, 9), execution_result)

    parse_result = self.parser.parser.parse_args([self.parser.method_name_bounds, "3", "20"])
    execution_result = self.parser.execute_command(parse_result)
    self.assertEqual(SUM_PROGRESSION_RESULT.format(3, 20, 207), execution_result)

    with self.assertRaises(ValueError):
      parse_result = self.parser.parser.parse_args([])
      execution_result = self.parser.execute_command(parse_result)

  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)