from argparse import RawTextHelpFormatter

from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.utils.constants import PURPLE_DESCRIPTION
from scripts.utils.constants import PARSER_IDENTIFIER_NAME
from scripts.parsers.time.time_parser import TimeParser
from scripts.parsers.test.test_parser import TestParser
from scripts.parsers.calculate.calculate_parser import CalculateParser


class PurpleParser(AbstractParser):
  def __init__(self):
    super(PurpleParser, self).__init__()
    self.name = "purple"
    self.short_name = "pt"
    self.test_parser = TestParser()
    self.time_parser = TimeParser()
    self.calculate_parser = CalculateParser()
    self.endpoint_parsers = {self.time_parser.name: self.time_parser.execute_command,
                             self.time_parser.short_name: self.time_parser.execute_command,
                             self.test_parser.name: self.test_parser.execute_command,
                             self.test_parser.short_name: self.test_parser.execute_command,
                             self.calculate_parser.progression_parser.name: self.calculate_parser.progression_parser.execute_command,
                             self.calculate_parser.progression_parser.short_name: self.calculate_parser.progression_parser.execute_command}

  def _perform_creation(self):
    self.parser.description = PURPLE_DESCRIPTION

    self.subparsers = self.parser.add_subparsers(dest = PARSER_IDENTIFIER_NAME)

    self.time_parser.create_subparser(self, RawTextHelpFormatter)
    self.test_parser.create_subparser(self)
    self.calculate_parser.create_subparser(self, RawTextHelpFormatter)

  def run_endpoint(self, parse_result):
    return self.endpoint_parsers[getattr(parse_result, PARSER_IDENTIFIER_NAME)](parse_result)
