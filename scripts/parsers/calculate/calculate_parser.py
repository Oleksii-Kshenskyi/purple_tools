from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.parsers.calculate.progression_parser import CalculateProgressionParser
from scripts.utils.constants import CALCULATE_COMMAND_DESCRIPTION
from scripts.utils.constants import CALCULATE_ARGUMENTS_SUBCOMMANDS
from scripts.utils.constants import PARSER_IDENTIFIER_NAME

class CalculateParser(AbstractParser):
  def __init__(self):
    super(CalculateParser, self).__init__()
    self.name = "calculate"
    self.short_name = "c"
    self.progression_parser = CalculateProgressionParser()

  def _perform_creation(self):
    self.parser.description = CALCULATE_COMMAND_DESCRIPTION
    self.subparsers = self.parser.add_subparsers(dest = PARSER_IDENTIFIER_NAME, help = CALCULATE_ARGUMENTS_SUBCOMMANDS)

    self.progression_parser.create_subparser(self)