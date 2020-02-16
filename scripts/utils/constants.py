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

CALCULATE_COMMAND_DESCRIPTION = "Calculate command performs various calculations, works mostly with numbers and formulas."
CALCULATE_ARGUMENTS_SUBCOMMANDS = "Choose which type of calculation to perform.\n\t=> progresssion | pr: perform various calculations on arithmetic progressions."

PROGRESSION_SUM_INVALID_ARGUMENT_MESSAGE = "First argument must be <= second argument."
BINARY_SEARCH_BOUNDS_MIXED_UP = "Upper bound in binary search must be greater than lower bound"
BINARY_SEARCH_INTS_OF_WRONG_TYPE = "Lower bound, upper bound and step of a binary search have to be ints"
BINARY_SEARCH_CONDITION_NOT_CALLABLE = "Exit condition of a binary search has to be a function that returns values of the BinarySearch enum"
BINARY_SEARCH_INTS_DONT_MAKE_PROGRESSION = "Specified values of lower bound, upper bound and step in a binary search don't create a valid progression"
BINARY_SEARCH_STEP_MUST_BE_POSITIVE = "Value of step in progression can only be > 0."
BINARY_SEARCH_ELEMENT_NOT_IN_PROGRESSION = "You're trying to look for an element that is not in the specified progression."

LIMITER_PROGRESSION_LIMITER_IS_INCORRECT = "Progression limiter can only be positive."

LIMITER_PROGRESSION_RESULT = "The progression is: 1 .. {}\nLimiter-to-sum remainder: {}\n"
SUM_PROGRESSION_RESULT = "sum({} .. {}) = {}\n"
PROGRESSIONS_COMMAND_DESCRIPTION = "Progression command performs various calculations on arithmetic progressions."
PROGRESSIONS_ERROR_NO_ARGUMENT = "No arguments provided, expected progression calculation type. Please provide one of the arguments from the 'optional arguments' section."
PROGRESSIONS_ARGUMENTS_BY_LIMITER = "Calculates arithmetic progression parameters via a progression sum limiter. Expects the limiter (an integer number) to be the only argument. Calculates a progression with first element and step equal to 1. Determines progression's last element and the sum of elements such that the sum <= the specified limiter."
PROGRESSIONS_ARGUMENTS_BY_BOUNDS = "Calculates the sum of the arithmetic progression specified via its bounds (lower and upper bound / first and last element). Expects <lower_bound> (an integer number) to be the first argument, <upper_bound> (also an integer) to be the second argument."