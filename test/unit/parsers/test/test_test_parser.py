import unittest

from scripts.parsers.basic_throwing_parser import BasicThrowingParser
import scripts.parsers.test.test_parser as test_parser

class TestTestParser(unittest.TestCase):
  
  def setUp(self):
    self.parser = test_parser.create_parser()

  def test_parser_processes_arguments(self):
    parsing_result = self.parser.parse_args(["unit"])
    self.assertEqual("unit", parsing_result.kind)

    parsing_result = self.parser.parse_args(["exploratory"])
    self.assertEqual("exploratory", parsing_result.kind)

    with self.assertRaises(ValueError):
      self.parser.parse_args(["third"])
    
    with self.assertRaises(ValueError):
      self.parser.parse_args([])

    with self.assertRaises(ValueError):
      self.parser.parse_args(["unit", "two"])

  def test_parser_module_executes_command(self):
    # functionality testing required
    pass

  def test_name(self):
    self.assertEqual("test", test_parser.name())
    self.assertEqual("ts", test_parser.name(get_short_name=True))

  def test_as_subparser(self):
    parser = BasicThrowingParser()
    self.parser = test_parser.create_subparser(parser.add_subparsers())
    self.test_parser_processes_arguments()
    self.test_parser_module_executes_command()

    # functionality testing required


  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)