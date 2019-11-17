import argparse

from scripts.parsers.basic_throwing_parser import BasicThrowingParser
from scripts.utils.time.constants import TIME_PRINT_COMMAND_DESCRIPTION
from scripts.utils.time.constants import TIME_PRINT_ARGUMENTS_TIME_HELP
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT
from scripts.time.calculation.timecalc import construct_uniform_time_string


def create_parser():
  parser = BasicThrowingParser()
  parser.description = TIME_PRINT_COMMAND_DESCRIPTION

  parser.add_argument("time", nargs="+", help=TIME_PRINT_ARGUMENTS_TIME_HELP)

  return parser

def __forward_number_from_argparse(number):
  try:
    return float(number)
  except ValueError:
    return number

def execute_command(parser, arguments):
  parse_result = parser.parse_args(arguments)
  result = []
  for item in parse_result.time:
    item_ready = __forward_number_from_argparse(item)
    result += [construct_uniform_time_string(item_ready)]

  return '\n'.join(result)