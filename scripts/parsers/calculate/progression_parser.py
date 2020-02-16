from scripts.parsers.base.abstract_parser import AbstractParser
from scripts.utils.constants import LIMITER_PROGRESSION_RESULT
from scripts.utils.constants import SUM_PROGRESSION_RESULT
from scripts.utils.constants import PROGRESSIONS_ERROR_NO_ARGUMENT
from scripts.utils.constants import PROGRESSIONS_ARGUMENTS_BY_BOUNDS
from scripts.utils.constants import PROGRESSIONS_ARGUMENTS_BY_LIMITER
from scripts.utils.constants import PROGRESSIONS_COMMAND_DESCRIPTION
from scripts.calculate.progressions import determine_progression_parameters_by_sum_limiter
from scripts.calculate.progressions import calculate_sum_of_arithmetic_progression

class CalculateProgressionParser(AbstractParser):
  def __init__(self):
    super(CalculateProgressionParser, self).__init__()
    self.name = "progression"
    self.short_name = "pr"
    self.method_name_limiter = "--by-limiter"
    self.method_short_name_limiter = "-l"
    self.method_name_bounds = "--by-bounds"
    self.method_short_name_bounds = "-b"

  def _perform_creation(self):
    self.parser.description = PROGRESSIONS_COMMAND_DESCRIPTION
    group = self.parser.add_mutually_exclusive_group()
    group.add_argument(self.method_name_limiter, self.method_short_name_limiter, type=int, help = PROGRESSIONS_ARGUMENTS_BY_LIMITER, nargs = 1)
    group.add_argument(self.method_name_bounds, self.method_short_name_bounds, type = int, help = PROGRESSIONS_ARGUMENTS_BY_BOUNDS, nargs = 2)

  def execute_command(self, parse_result):
    if not parse_result.by_limiter and not parse_result.by_bounds:
      raise ValueError(PROGRESSIONS_ERROR_NO_ARGUMENT)

    if parse_result.by_limiter:
      (last_element, remainder) =  determine_progression_parameters_by_sum_limiter(parse_result.by_limiter[0])
      return LIMITER_PROGRESSION_RESULT.format(last_element, remainder)
    elif parse_result.by_bounds:
      [lower_bound, upper_bound] = parse_result.by_bounds
      progression_sum = calculate_sum_of_arithmetic_progression(lower_bound, upper_bound)
      return SUM_PROGRESSION_RESULT.format(lower_bound, upper_bound, progression_sum)