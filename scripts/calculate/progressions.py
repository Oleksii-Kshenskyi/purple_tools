from scripts.utils.constants import PROGRESSION_SUM_INVALID_ARGUMENT_MESSAGE
from scripts.utils.constants import BINARY_SEARCH_BOUNDS_MIXED_UP
from scripts.utils.constants import BINARY_SEARCH_CONDITION_NOT_CALLABLE
from scripts.utils.constants import BINARY_SEARCH_INTS_DONT_MAKE_PROGRESSION
from scripts.utils.constants import BINARY_SEARCH_INTS_OF_WRONG_TYPE
from scripts.utils.constants import BINARY_SEARCH_STEP_MUST_BE_POSITIVE
from scripts.utils.constants import BINARY_SEARCH_ELEMENT_NOT_IN_PROGRESSION

from scripts.utils.progressions.conditionals import BinaryResult, EqualityConditional

def calculate_sum_of_arithmetic_progression(first_num, last_num):
  if first_num > last_num:
    raise ValueError(PROGRESSION_SUM_INVALID_ARGUMENT_MESSAGE)

  return int((last_num - first_num + 1) * ((first_num + last_num) / 2))

def find_progression_element_satisfying_condition(lower_bound, upper_bound, step, conditional):
  _check_args_of_binary_search(lower_bound, upper_bound, step, conditional)

  current_index = _get_initial_index(lower_bound, upper_bound, step)
  (current_index, current_value) = _bisect_once(current_index, lower_bound, step)  
  current_condition = conditional.check(current_value)
  current_lower = lower_bound
  absolute_index = current_index

  old_index = -1
  search_is_stuck = 0

  while current_condition != BinaryResult.OK:
    old_index = current_index
    current_condition = conditional.check(current_value)

    if current_condition == BinaryResult.MOVE_LEFT:
      (current_index, current_value) = _bisect_once(current_index, current_lower, step)
      absolute_index = _advance_absolute_index(absolute_index, current_index, current_condition, old_index)

    elif current_condition == BinaryResult.MOVE_RIGHT:
      current_lower = _get_value_by_index(current_index + 1, current_lower, step) 
      (current_index, current_value) = _bisect_once(current_index, current_lower, step)
      absolute_index = _advance_absolute_index(absolute_index, current_index, current_condition)

    if(current_index == old_index == 1):
      search_is_stuck += 1
    if(search_is_stuck > 1):
      raise ValueError(BINARY_SEARCH_ELEMENT_NOT_IN_PROGRESSION)

  return absolute_index - 1



def _advance_absolute_index(current_absolute_index, current_index, current_condition, old_index = 0):
  if current_condition == BinaryResult.MOVE_RIGHT:
    return current_absolute_index + current_index
  elif current_condition == BinaryResult.MOVE_LEFT:
    return current_absolute_index - current_index if old_index % 2 == 0 else current_absolute_index - (current_index - 1)

def _get_initial_index(lower_bound, upper_bound, step):
  return (upper_bound - lower_bound) // step + 1

def _get_value_by_index(current_index, lower_bound, step):
  return (current_index - 1) * step + lower_bound

def _bisect_once(current_index, lower_bound, step):
  new_index = current_index // 2 if (current_index % 2 == 0) else current_index // 2 + 1
  new_value = _get_value_by_index(new_index, lower_bound, step)
  return (new_index, new_value)

def _check_args_of_binary_search(lower_bound, upper_bound, step, conditional):
  if(upper_bound < lower_bound):
    raise ValueError(BINARY_SEARCH_BOUNDS_MIXED_UP)
  elif not isinstance(lower_bound, int) or not isinstance(upper_bound, int) or not isinstance(step, int):
    raise ValueError(BINARY_SEARCH_INTS_OF_WRONG_TYPE)
  elif step <= 0:
    raise ValueError(BINARY_SEARCH_STEP_MUST_BE_POSITIVE)
  elif not hasattr(conditional, "check") or not callable(conditional.check):
    raise ValueError(BINARY_SEARCH_CONDITION_NOT_CALLABLE)

  index = _get_initial_index(lower_bound, upper_bound, step)
  last_element = _get_value_by_index(index, lower_bound, step)
  if not float((upper_bound - lower_bound) / step + 1).is_integer() or last_element != upper_bound:
    raise ValueError(BINARY_SEARCH_INTS_DONT_MAKE_PROGRESSION)
