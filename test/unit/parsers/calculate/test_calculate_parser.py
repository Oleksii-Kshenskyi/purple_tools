import unittest

from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.parsers.calculate.calculate_parser import CalculateParser
from scripts.utils.constants import LIMITER_PROGRESSION_RESULT
from scripts.utils.constants import SUM_PROGRESSION_RESULT

class TestCalculateParser(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_executes_command_as_subparser(self):
    papa_parser = AbstractParser()
    papa_parser.create_parser()
    parser = CalculateParser()
    parser.create_subparser(papa_parser)

    parse_result = papa_parser.parser.parse_args([parser.name, parser.progression_parser.name, parser.progression_parser.method_short_name_limiter, "120"])
    execution_result = parser.progression_parser.execute_command(parse_result)
    self.assertEquals(LIMITER_PROGRESSION_RESULT.format(15, 0), execution_result)

    parse_result = papa_parser.parser.parse_args([parser.short_name, parser.progression_parser.short_name, parser.progression_parser.method_short_name_bounds, "1", "20"])
    execution_result = parser.progression_parser.execute_command(parse_result)
    self.assertEquals(SUM_PROGRESSION_RESULT.format(1, 20, 210), execution_result)

  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)