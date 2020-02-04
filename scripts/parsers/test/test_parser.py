import argparse

from scripts.parsers.base.basic_throwing_parser import BasicThrowingParser
from scripts.utils.constants import TEST_COMMAND_DESCRIPTION
from scripts.utils.constants import TEST_ARGUMENTS_KIND_HELP
from scripts.utils.constants import PROJECT_DIR
from scripts.utils.constants import KIND_OF_TEST
from scripts.utils.testing.batch.execute import run_tests_in_directory

def name(get_short_name = False):
  return "ts" if get_short_name else "test"

def create_parser():
  parser = BasicThrowingParser()

  return _perform_creation(parser)

def create_subparser(subparsers):
  parser = subparsers.add_parser(name(), aliases=[name(get_short_name=True)])

  return _perform_creation(parser)

def _perform_creation(parser):
  parser.description = TEST_COMMAND_DESCRIPTION

  parser.add_argument("kind", choices=['unit', 'u', 'exploratory', 'e'], help=TEST_ARGUMENTS_KIND_HELP)

  return parser

def __forward_number_from_argparse(number):
  try:
    return float(number)
  except ValueError:
    return number

def execute_command(parse_result):
  execute_command_choose_output(parse_result)
  return ''

def execute_command_choose_output(parse_result, out_stream=None):
  return run_tests_in_directory(PROJECT_DIR + f'/test/{KIND_OF_TEST[parse_result.kind]}', out_stream)
