import argparse

from scripts.parsers.basic_throwing_parser import BasicThrowingParser
from scripts.utils.time.constants import TIME_PRINT_COMMAND_DESCRIPTION
from scripts.utils.time.constants import TIME_PRINT_ARGUMENTS_TIME_HELP
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT
from scripts.time.calculation.timecalc import construct_uniform_time_string

class TimePrintParser:

  def __init__(self):
    self._parser = BasicThrowingParser()
    self._parser.description = TIME_PRINT_COMMAND_DESCRIPTION

    self._parser.add_argument("time", nargs="+", help=TIME_PRINT_ARGUMENTS_TIME_HELP)

  def __forward_number_from_argparse(self, number):
    try:
      return float(number)
    except ValueError:
      return number


  def execute_command(self, arguments):
    parse_result = self._parser.parse_args(arguments)
    result = []
    for item in parse_result.time:
      item_ready = self.__forward_number_from_argparse(item)
      result += [construct_uniform_time_string(item_ready)]

    return '\n'.join(result)