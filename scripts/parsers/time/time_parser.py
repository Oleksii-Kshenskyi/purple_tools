import argparse

from scripts.parsers.basic_throwing_parser import BasicThrowingParser
from scripts.utils.time.constants import TIME_COMMAND_DESCRIPTION
from scripts.utils.time.constants import TIME_PRINT_COMMAND_DESCRIPTION
from scripts.utils.time.constants import TIME_PRINT_ARGUMENTS_TIME_HELP
from scripts.utils.constants import PARSER_IDENTIFIER_NAME
from scripts.calculate.pttime import construct_uniform_time_string

def name(get_short_name = False):
  return "t" if get_short_name else "time"

def name_of_print_subcommand(get_short_name = False):
  return "p" if get_short_name else "print"

def create_parser():
  parser = BasicThrowingParser()

  return _perform_creation(parser)

def create_subparser(subparsers):
  parser = subparsers.add_parser(name(), aliases=[name(get_short_name=True)])

  return _perform_creation(parser)

def _perform_creation(parser):
  parser.description = TIME_COMMAND_DESCRIPTION

  parser.add_argument("command", choices=[name_of_print_subcommand(),
                                          name_of_print_subcommand(get_short_name=True)])

  parser.add_argument("time", nargs="+", help=TIME_PRINT_ARGUMENTS_TIME_HELP)

  return parser

def execute_command(parse_result):
  return _get_subcommand_mapping()[parse_result.command](parse_result)

def _execute_print_subcommand(parse_result):
  result = []
  for item in parse_result.time:
    item_ready = _forward_number_from_argparse(item)
    result += [construct_uniform_time_string(item_ready)]

  return '\n'.join(result)


def _forward_number_from_argparse(number):
  try:
    return float(number)
  except ValueError:
    return number

def _get_subcommand_mapping():
  return {
    name_of_print_subcommand()                    : _execute_print_subcommand,
    name_of_print_subcommand(get_short_name=True) : _execute_print_subcommand
  }