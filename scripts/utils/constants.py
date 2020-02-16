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

PROGRESSION_SUM_INVALID_ARGUMENT_MESSAGE = "First argument must be <= second argument."
BINARY_SEARCH_BOUNDS_MIXED_UP = "Upper bound in binary search must be greater than lower bound"
BINARY_SEARCH_INTS_OF_WRONG_TYPE = "Lower bound, upper bound and step of a binary search have to be ints"
BINARY_SEARCH_CONDITION_NOT_CALLABLE = "Exit condition of a binary search has to be a function that returns values of the BinarySearch enum"
BINARY_SEARCH_INTS_DONT_MAKE_PROGRESSION = "Specified values of lower bound, upper bound and step in a binary search don't create a valid progression"
BINARY_SEARCH_STEP_MUST_BE_POSITIVE = "Value of step in progression can only be > 0."
BINARY_SEARCH_ELEMENT_NOT_IN_PROGRESSION = "You're trying to look for an element that is not in the specified progression."

LIMITER_PROGRESSION_LIMITER_IS_INCORRECT = "Progression limiter can only be positive."