import argparse

from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.utils.time.constants import TIME_COMMAND_DESCRIPTION
from scripts.utils.time.constants import TIME_ARGUMENTS_TIME_HELP
from scripts.utils.time.constants import TIME_ARGUMENTS_COMMAND_HELP
from scripts.utils.time.constants import DEFAULT_LABEL
from scripts.utils.time.constants import TIME_ARGUMENTS_LABEL_HELP
from scripts.utils.constants import PARSER_IDENTIFIER_NAME
from scripts.utils.time.features import add_timedeltas
from scripts.utils.time.conversions import forward_number_from_argparse
from scripts.calculate.pttime import construct_uniform_time_string
from scripts.calculate.pttime import get_timedelta_sum_as_uniform_time_sting

class TimeParser(AbstractParser):
  def __init__(self):
    super(TimeParser, self).__init__()
    self.name = "time"
    self.short_name = "t"
    self.subcommand_name_print = "print"
    self.subcommand_short_name_print = "p"
    self.subcommand_name_add = "add"
    self.subcommand_short_name_add = "a"
    self.optional_name_label = "--label"
    self.optional_short_name_label = "-l"

  def _perform_creation(self):
    self.parser.description = TIME_COMMAND_DESCRIPTION

    self.parser.add_argument("command", choices=[self.subcommand_name_print,
                                                 self.subcommand_short_name_print,
                                                 self.subcommand_name_add,
                                                 self.subcommand_short_name_add],
                                  help=TIME_ARGUMENTS_COMMAND_HELP)

    self.parser.add_argument(self.name, nargs="+", help=TIME_ARGUMENTS_TIME_HELP)
    self.parser.add_argument(self.optional_short_name_label, self.optional_name_label, nargs="?", const=DEFAULT_LABEL, help=TIME_ARGUMENTS_LABEL_HELP)

  def execute_command(self, parse_result):
    return self._get_subcommand_mapping()[parse_result.command](parse_result)

  def _execute_print_subcommand(self, parse_result):
    result = []
    for item in parse_result.time:
      item_ready = forward_number_from_argparse(item)
      if not parse_result.label:
        result += [construct_uniform_time_string(item_ready)]
      else:
        result += [construct_uniform_time_string(item_ready, parse_result.label)]

    return '\n'.join(result)

  def _execute_add_subcommand(self, parse_result):
    return get_timedelta_sum_as_uniform_time_sting(parse_result.time, parse_result.label)

  def _get_subcommand_mapping(self):
    return {
      self.subcommand_name_print       : self._execute_print_subcommand,
      self.subcommand_short_name_print : self._execute_print_subcommand,
      self.subcommand_name_add : self._execute_add_subcommand,
      self.subcommand_short_name_add : self._execute_add_subcommand
    }