import unittest

from scripts.parsers.purpleparser import PurpleParser
from scripts.utils.constants import PARSER_IDENTIFIER_NAME

class TestPurpleParser(unittest.TestCase):
  
  def setUp(self):
    self.parser = PurpleParser()
    self.parser.create_parser()

  def test_parser_processes_arguments(self):
    parse_result = self.parser.parser.parse_args([self.parser.time_parser.name,
                                                  self.parser.time_parser.subcommand_name_print,
                                                  "3"])
    self.assertEqual(["3"], parse_result.time)

    parse_result = self.parser.parser.parse_args([self.parser.test_parser.name, "unit"])
    self.assertEqual("unit", parse_result.kind)
    parse_result = self.parser.parser.parse_args([self.parser.test_parser.name, "exploratory"])
    self.assertEqual("exploratory", parse_result.kind)
    with self.assertRaises(ValueError):
      self.parser.parser.parse_args([self.parser.test_parser.name, "something"])

    with self.assertRaises(ValueError):
      self.parser.parser.parse_args([self.parser.time_parser.name, self.parser.time_parser.subcommand_name_print])

  def test_subparsers_are_identifiable(self):
    parse_result = self.parser.parser.parse_args([self.parser.time_parser.name, self.parser.time_parser.subcommand_name_print, "00:00:00"])
    self.assertEqual(self.parser.time_parser.name, getattr(parse_result, PARSER_IDENTIFIER_NAME))

  def test_endpoint_parser_executes(self):
    parser = PurpleParser()
    parser.create_parser()
    parse_result = parser.parser.parse_args([parser.time_parser.name, parser.time_parser.subcommand_name_print, "2"])

    execution_result = parser.run_endpoint(parse_result)
    self.assertEqual("[2 U @ 00:50:00]", execution_result)

  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)