import os

PURPLE_DESCRIPTION = "A collection of various utilities called Purple Tools."

PARSER_IDENTIFIER_NAME = "which"

TEST_COMMAND_DESCRIPTION = "test command will run all unit tests or exploratory tests of the entire Purple Tools for you."

TEST_ARGUMENTS_KIND_HELP = "specify the kind of tests you want to run. unit: run all unit tests, exploratory: run all exploratory tests."

KIND_OF_TEST = {
  'unit' : 'unit',
  'u' : 'unit',
  'exploratory' : 'exploratory',
  'e' : 'exploratory'
}

PROJECT_DIR = os.environ['PT_PROJECT_DIR']