import argparse

from scripts.parsers.base.basic_throwing_parser import BasicThrowingParser

class AbstractParser:
  def __init__(self):
    self.name = "abstraction"
    self.short_name = "short_abstraction"

  def create_parser(self):
    self.parser = BasicThrowingParser()
    self._perform_creation()

  def create_subparser(self, abstract_parser):
    self.parser = abstract_parser.parser.add_subparsers().add_parser(self.name, aliases=[self.short_name])

    self._perform_creation()

  def _perform_creation(self):
    return "dummy_creation"

  