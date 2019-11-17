import argparse

from scripts.parsers.basic_throwing_parser import BasicThrowingParser
import scripts.parsers.time.time_print_parser as time_print
from scripts.utils.time.constants import TIME_COMMAND_DESCRIPTION
from scripts.utils.time.constants import TIME_PRINT_COMMAND_DESCRIPTION
from scripts.utils.time.constants import TIME_PRINT_ARGUMENTS_TIME_HELP
from scripts.utils.constants import PARSER_IDENTIFIER_NAME

def name(get_short_name = False):
  return "t" if get_short_name else "time"

def create_parser():
  parser = BasicThrowingParser()

  return _perform_creation(parser)

def create_subparser(subparsers):
  parser = subparsers.add_parser(name(), aliases=[name(get_short_name=True)])

  return _perform_creation(parser)

def _perform_creation(parser):
  parser.description = TIME_COMMAND_DESCRIPTION

  subparsers = parser.add_subparsers(dest = PARSER_IDENTIFIER_NAME)

  time_print.create_subparser(subparsers)

  return parser

