import unittest

from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.parsers.time.time_parser import TimeParser
from scripts.utils.constants import PARSER_IDENTIFIER_NAME
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT

class TestTimeParser(unittest.TestCase):
  
  def setUp(self):
    self.parser = TimeParser()
    self.parser.create_parser()

  def test_parser_processes_arguments(self):
    parse_result = self.parser.parser.parse_args(["print", "3"])
    self.assertEqual(["3"], parse_result.time)

    with self.assertRaises(ValueError):
      parse_result = self.parser.parser.parse_args([])

  def test_as_subparser(self):
    self.papa_parser = AbstractParser()
    self.papa_parser.create_parser()
    self.parser = TimeParser()
    self.parser.create_subparser(self.papa_parser)
    self.test_parser_processes_arguments()

    parse_result = self.papa_parser.parser.parse_args([self.parser.name, self.parser.subcommand_name_print, "3"])
    self.assertEqual(["3"], parse_result.time)

  def test_time_parser_executes_print_subcommand(self):
    parse_result = self.parser.parser.parse_args([self.parser.subcommand_name_print, "00:25:00", "00:50:00", "108:64:1550"])
    execution_result = self.parser.execute_command(parse_result)
    self.assertEqual("[1 U @ 00:25:00]\n[2 U @ 00:50:00]\n[262.793 U @ 109:29:50]", execution_result)

    parse_result = self.parser.parser.parse_args([self.parser.subcommand_name_print, "kek", "2", "1:00:0"])
    execution_result = self.parser.execute_command(parse_result)
    self.assertEqual(f'{ UNIFORM_TIME_STRING_DEFAULT }\n[2 U @ 00:50:00]\n[2.4 U @ 01:00:00]', execution_result)

    parse_result = self.parser.parser.parse_args([self.parser.subcommand_name_print, "25h40m21s"])
    execution_result = self.parser.execute_command(parse_result)
    self.assertEqual('[61.614 U @ 25:40:21]', execution_result)

  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)