import unittest

import scripts.parsers.purpleparser as purple
from scripts.parsers.time.time_parser import name as tname
from scripts.parsers.time.time_parser import name_of_print_subcommand as pname
from scripts.parsers.test.test_parser import name as tsname
from scripts.utils.constants import PARSER_IDENTIFIER_NAME

class TestPurpleParser(unittest.TestCase):
  
  def setUp(self):
    self.parser = purple.create_parser()

  def test_parser_processes_arguments(self):
    parse_result = self.parser.parse_args([tname(), pname(), "3"])
    self.assertEqual(["3"], parse_result.time)

    parse_result = self.parser.parse_args([tsname(), "unit"])
    self.assertEqual("unit", parse_result.kind)
    parse_result = self.parser.parse_args([tsname(), "exploratory"])
    self.assertEqual("exploratory", parse_result.kind)
    with self.assertRaises(ValueError):
      self.parser.parse_args([tsname(), "something"])

    with self.assertRaises(ValueError):
      self.parser.parse_args([tname(), pname()])

  def test_subparsers_are_identifiable(self):
    parse_result = self.parser.parse_args([tname(), pname(), "00:00:00"])
    self.assertEqual(tname(), getattr(parse_result, PARSER_IDENTIFIER_NAME))

  def test_endpoint_parser_executes(self):
    parser = purple.create_parser()
    parse_result = parser.parse_args([tname(), pname(), "2"])

    execution_result = purple.run_endpoint(parse_result)
    self.assertEqual("[2 U @ 00:50:00]", execution_result)

  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)