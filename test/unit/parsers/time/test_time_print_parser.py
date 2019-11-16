import unittest

from scripts.parsers.time.time_print_parser import TimePrintParser
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT

class TestTimePrintParser(unittest.TestCase):
  
  def setUp(self):
    self.wrapper = TimePrintParser()
    self.parser = self.wrapper._parser

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
    result = self.wrapper.execute_command(["3:44:12"])
    self.assertEqual("[8.968 U @ 03:44:12]", result)

    result = self.wrapper.execute_command(["00:25:00", "00:50:00", "108:64:1550"])
    self.assertEqual("[1 U @ 00:25:00]\n[2 U @ 00:50:00]\n[262.793 U @ 109:29:50]", result)

    result = self.wrapper.execute_command(["00:30:00", "3", "255", "148.716", "04:15:00"])
    self.assertEqual("[1.2 U @ 00:30:00]\n[3 U @ 01:15:00]\n[255 U @ 106:15:00]\n[148.716 U @ 61:57:54]\n[10.2 U @ 04:15:00]", result)

    result = self.wrapper.execute_command(["kek", "2", "1:00:0"])
    self.assertEqual(f'{ UNIFORM_TIME_STRING_DEFAULT }\n[2 U @ 00:50:00]\n[2.4 U @ 01:00:00]', result)

  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)