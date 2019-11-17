import unittest

from scripts.parsers.basic_throwing_parser import BasicThrowingParser
import scripts.parsers.time.time_parser as time_parser
import scripts.parsers.time.time_print_parser as time_print
from scripts.utils.constants import PARSER_IDENTIFIER_NAME

class TestTimeParser(unittest.TestCase):
  
  def setUp(self):
    self.parser = time_parser.create_parser()

  def test_parser_processes_arguments(self):
    parse_result = self.parser.parse_args(["print", "3"])
    self.assertEqual(["3"], parse_result.time)

  def test_as_subparser(self):
    parser = BasicThrowingParser()
    self.parser = time_parser.create_subparser(parser.add_subparsers())
    self.test_parser_processes_arguments()

    parse_result = parser.parse_args([time_parser.name(), time_print.name(), "3", "00:00:01"])
    self.assertEqual(["3", "00:00:01"], parse_result.time)

    parse_result = parser.parse_args([time_parser.name(get_short_name=True), time_print.name(get_short_name=True), "3", "00:00:01"])
    self.assertEqual(["3", "00:00:01"], parse_result.time)

  def test_subparsers_are_identifiable(self):
    parse_result = self.parser.parse_args([time_print.name(), "3"])
    self.assertEqual(time_print.name(), getattr(parse_result, PARSER_IDENTIFIER_NAME))


  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)