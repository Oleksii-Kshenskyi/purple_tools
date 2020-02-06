import argparse

from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.utils.constants import TEST_COMMAND_DESCRIPTION
from scripts.utils.constants import TEST_ARGUMENTS_KIND_HELP
from scripts.utils.constants import PROJECT_DIR
from scripts.utils.constants import KIND_OF_TEST
from scripts.utils.testing.batch.execute import run_tests_in_directory

class TestParser(AbstractParser):

  def __init__(self):
    super(TestParser, self).__init__()
    self.name = "test"
    self.short_name = "ts"

  def _perform_creation(self):
    self.parser.description = TEST_COMMAND_DESCRIPTION

    self.parser.add_argument("kind", choices=['unit', 'u', 'exploratory', 'e'], help=TEST_ARGUMENTS_KIND_HELP)

  def execute_command(self, parse_result):
    self.execute_command_choose_output(parse_result)
    return ''

  def execute_command_choose_output(self, parse_result, out_stream=None):
    return run_tests_in_directory(PROJECT_DIR + f'/test/{KIND_OF_TEST[parse_result.kind]}', out_stream)
