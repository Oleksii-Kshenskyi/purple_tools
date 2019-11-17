import unittest

from scripts.parsers.basic_throwing_parser import BasicThrowingParser
import scripts.parsers.time.time_print_parser as time_print
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT

class TestTimePrintParser(unittest.TestCase):
  
  def setUp(self):
    self.parser = time_print.create_parser()

  def test_parser_processes_arguments(self):
    parsing_result = self.parser.parse_args(["one"])
    self.assertEqual("one", parsing_result.time[0])

    parsing_result = self.parser.parse_args(["one", "two", "three"])
    self.assertEqual("one", parsing_result.time[0])
    self.assertEqual("two", parsing_result.time[1])
    self.assertEqual("three", parsing_result.time[2])

    with self.assertRaises(ValueError):
      self.parser.parse_args([])

  def test_wrapper_executes_command(self):
    result = time_print.execute_command(self.parser, ["3:44:12"])
    self.assertEqual("[8.968 U @ 03:44:12]", result)

    result = time_print.execute_command(self.parser, ["00:25:00", "00:50:00", "108:64:1550"])
    self.assertEqual("[1 U @ 00:25:00]\n[2 U @ 00:50:00]\n[262.793 U @ 109:29:50]", result)

    result = time_print.execute_command(self.parser, ["00:30:00", "3", "255", "148.716", "04:15:00"])
    self.assertEqual("[1.2 U @ 00:30:00]\n[3 U @ 01:15:00]\n[255 U @ 106:15:00]\n[148.716 U @ 61:57:54]\n[10.2 U @ 04:15:00]", result)

    result = time_print.execute_command(self.parser, ["kek", "2", "1:00:0"])
    self.assertEqual(f'{ UNIFORM_TIME_STRING_DEFAULT }\n[2 U @ 00:50:00]\n[2.4 U @ 01:00:00]', result)

  def test_name(self):
    self.assertEqual("print", time_print.name())
    self.assertEqual("p", time_print.name(get_short_name=True))

  def test_as_subparser(self):
    parser = BasicThrowingParser()
    self.parser = time_print.create_subparser(parser.add_subparsers())
    self.test_parser_processes_arguments()
    self.test_wrapper_executes_command()

    parse_result = parser.parse_args([time_print.name(), "3", "00:00:01"])
    self.assertEqual(["3", "00:00:01"], parse_result.time)

    parse_result = parser.parse_args([time_print.name(get_short_name=True), "3", "00:00:01"])
    self.assertEqual(["3", "00:00:01"], parse_result.time)


  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)