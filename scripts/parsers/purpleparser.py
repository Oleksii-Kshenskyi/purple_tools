import argparse
import sys

from scripts.parsers.basic_throwing_parser import BasicThrowingParser
from scripts.utils.constants import PURPLE_DESCRIPTION
from scripts.utils.constants import PARSER_IDENTIFIER_NAME
import scripts.parsers.time.time_parser as time_parser

import scripts.parsers.time.time_print_parser as time_print

ENDPOINT_PARSERS = {time_print.name(): time_print.execute_command,
                    time_print.name(get_short_name=True): time_print.execute_command}

def name(get_short_name = False):
  return "pt" if get_short_name else "purple"

def create_parser():
  parser = BasicThrowingParser()

  return _perform_creation(parser)

def _perform_creation(parser):
  parser.description = PURPLE_DESCRIPTION

  time_parser.create_subparser(parser.add_subparsers(dest = PARSER_IDENTIFIER_NAME))

  return parser

def run_endpoint(parse_result):
  return ENDPOINT_PARSERS[getattr(parse_result, PARSER_IDENTIFIER_NAME)](parse_result)
