import unittest
import argparse

from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.parsers.base.basic_throwing_parser import BasicThrowingParser

class TestAbstractParser(unittest.TestCase):
  
  def setUp(self):
    self.parser = AbstractParser()

  def test_names(self):
    self.assertEqual("abstraction", self.parser.name)
    self.assertEqual("short_abstraction", self.parser.short_name)

  def test_dummy_parser_creation(self):
    self.parser.create_parser()
    self.assertIsInstance(self.parser.parser, BasicThrowingParser)
    self.assertEqual("dummy_creation", self.parser._perform_creation())

  def test_dummy_subparser_creation(self):
    self.parser.create_parser()
    self.subparser = AbstractParser()
    self.subparser.create_subparser(self.parser)
    self.subsubparser = AbstractParser()
    self.subsubparser.create_subparser(self.subparser)

    parse_result = self.parser.parser.parse_args(["abstraction", "abstraction"])
    self.assertIsInstance(parse_result, argparse.Namespace)

    with self.assertRaises(ValueError):
      self.parser.parser.parse_args(["abtraction"])

    with self.assertRaises(ValueError):
      self.subparser.parser.parse_args(["abtraction"])

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)