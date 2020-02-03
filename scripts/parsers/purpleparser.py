import argparse
import sys

from scripts.parsers.basic_throwing_parser import BasicThrowingParser
from scripts.utils.constants import PURPLE_DESCRIPTION
from scripts.utils.constants import PARSER_IDENTIFIER_NAME
import scripts.parsers.time.time_parser as time_parser
import scripts.parsers.test.test_parser as test_parser

ENDPOINT_PARSERS = {time_parser.name(): time_parser.execute_command,
                    time_parser.name(get_short_name=True): time_parser.execute_command,
                    test_parser.name(): test_parser.execute_command,
                    test_parser.name(get_short_name=True): test_parser.execute_command}

def name(get_short_name = False):
  return "pt" if get_short_name else "purple"

def create_parser():
  parser = BasicThrowingParser()

  return _perform_creation(parser)

def _perform_creation(parser):
  parser.description = PURPLE_DESCRIPTION

  purple_subparsers = parser.add_subparsers(dest = PARSER_IDENTIFIER_NAME)

  time_parser.create_subparser(purple_subparsers)
  test_parser.create_subparser(purple_subparsers)

  return parser

def run_endpoint(parse_result):
  return ENDPOINT_PARSERS[getattr(parse_result, PARSER_IDENTIFIER_NAME)](parse_result)
