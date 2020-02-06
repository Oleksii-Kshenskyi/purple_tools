import argparse

from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.utils.time.constants import TIME_COMMAND_DESCRIPTION
from scripts.utils.time.constants import TIME_ARGUMENTS_TIME_HELP
from scripts.utils.time.constants import TIME_ARGUMENTS_COMMAND_HELP
from scripts.utils.constants import PARSER_IDENTIFIER_NAME
from scripts.calculate.pttime import construct_uniform_time_string

class TimeParser(AbstractParser):
  def __init__(self):
    super(TimeParser, self).__init__()
    self.name = "time"
    self.short_name = "t"
    self.subcommand_name_print = "print"
    self.subcommand_short_name_print = "p"

  def _perform_creation(self):
    self.parser.description = TIME_COMMAND_DESCRIPTION

    self.parser.add_argument("command", choices=[self.subcommand_name_print,
                                                 self.subcommand_short_name_print],
                                  help=TIME_ARGUMENTS_COMMAND_HELP)

    self.parser.add_argument("time", nargs="+", help=TIME_ARGUMENTS_TIME_HELP)

  def execute_command(self, parse_result):
    return self._get_subcommand_mapping()[parse_result.command](parse_result)

  def _execute_print_subcommand(self, parse_result):
    result = []
    for item in parse_result.time:
      item_ready = self._forward_number_from_argparse(item)
      result += [construct_uniform_time_string(item_ready)]

    return '\n'.join(result)

  def _forward_number_from_argparse(self, number):
    try:
      return float(number)
    except ValueError:
      return number

  def _get_subcommand_mapping(self):
    return {
      self.subcommand_name_print       : self._execute_print_subcommand,
      self.subcommand_short_name_print : self._execute_print_subcommand
    }