import argparse

from scripts.parsers.basic_throwing_parser import BasicThrowingParser
from scripts.parsers.time.time_print_parser import TimePrintParser
from scripts.utils.time.constants import TIME_COMMAND_DESCRIPTION
from scripts.utils.time.constants import TIME_PRINT_COMMAND_DESCRIPTION
from scripts.utils.time.constants import TIME_PRINT_ARGUMENTS_TIME_HELP

TIME_PRINT_PARSER_NAME = 'print'
TIME_PRINT_PARSER_SHORT_NAME = 'p'

class TimeParser:

  def __init__(self):
    self._wrappers = {}
    self._wrappers[TIME_PRINT_PARSER_NAME] = TimePrintParser()

    self._parser = BasicThrowingParser()
    self._parser.description = TIME_COMMAND_DESCRIPTION

    subparsers = self._parser.add_subparsers()

    self._print_parser = subparsers.add_parser(TIME_PRINT_PARSER_NAME, aliases=[TIME_PRINT_PARSER_SHORT_NAME])
    self._print_parser.description = TIME_PRINT_COMMAND_DESCRIPTION
    self._print_parser.add_argument("time", nargs="+", help=TIME_PRINT_ARGUMENTS_TIME_HELP)

