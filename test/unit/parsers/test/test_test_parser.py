import unittest
# import os

from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.parsers.test.test_parser import TestParser

class TestTestParser(unittest.TestCase):
  
  def setUp(self):
    self.parser = TestParser()
    self.parser.create_parser()

  def test_parser_processes_arguments(self):
    parsing_result = self.parser.parser.parse_args(["unit"])
    self.assertEqual("unit", parsing_result.kind)

    parsing_result = self.parser.parser.parse_args(["exploratory"])
    self.assertEqual("exploratory", parsing_result.kind)

    parsing_result = self.parser.parser.parse_args(["e"])
    self.assertEqual("e", parsing_result.kind)

    parsing_result = self.parser.parser.parse_args(["u"])
    self.assertEqual("u", parsing_result.kind)

    with self.assertRaises(ValueError):
      self.parser.parser.parse_args(["third"])
    
    with self.assertRaises(ValueError):
      self.parser.parser.parse_args([])

    with self.assertRaises(ValueError):
      self.parser.parser.parse_args(["unit", "two"])

  # This unit test re-executes all exploratory tests to test if the test module
  # functionality works correctly in conjunction with the test parser. The unit test has 
  # been made sure that it passes.
  # However, it's disabled to not re-run all exploratory tests with unit tests every time.
  # In case test parser functionality ever breaks, it would be a good idea to enable this
  # and debug. Until then, this stays commented out.
  # def test_parser_module_executes_command(self):
  #   parse_result = self.parser.parser.parse_args(["exploratory"])
  #   out_file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), "output.txt")
  #   with open(out_file_name, "w") as the_stream:
  #     execution_result = self.parser.execute_command_choose_output(parse_result, the_stream)

  #   self.assertEqual(0, len(execution_result.failures))
  #   self.assertEqual(0, len(execution_result.errors))

  #   os.unlink(out_file_name)

  def test_name(self):
    self.assertEqual("test", self.parser.name)
    self.assertEqual("ts", self.parser.short_name)

  def test_as_subparser(self):
    self.papa_parser = AbstractParser()
    self.papa_parser.create_parser()
    self.parser.create_subparser(self.papa_parser)
    self.test_parser_processes_arguments()
    # self.test_parser_module_executes_command()


  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)