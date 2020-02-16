from enum import Enum, auto
from scripts.utils.constants import PROGRESSION_SUM_INVALID_ARGUMENT_MESSAGE
from scripts.utils.constants import BINARY_SEARCH_BOUNDS_MIXED_UP
from scripts.utils.constants import BINARY_SEARCH_CONDITION_NOT_CALLABLE
from scripts.utils.constants import BINARY_SEARCH_INTS_DONT_MAKE_PROGRESSION
from scripts.utils.constants import BINARY_SEARCH_INTS_OF_WRONG_TYPE

class BinaryResult(Enum):
  MOVE_LEFT = auto()
  OK = auto()
  MOVE_RIGHT = auto()

def calculate_sum_of_arithmetic_progression(first_num, last_num):
  if first_num > last_num:
    raise ValueError(PROGRESSION_SUM_INVALID_ARGUMENT_MESSAGE)

  return int((last_num - first_num + 1) * ((first_num + last_num) / 2))

def find_progression_element_satisfying_condition(lower_bound, upper_bound, step, condition):
  _check_args_of_binary_search(lower_bound, upper_bound, step, condition)

  current_index = _get_initial_index(lower_bound, upper_bound, step)
  (current_index, current_value) = _bisect_once(current_index, lower_bound, step)  
  current_condition = condition(current_value)
  current_lower = lower_bound
  absolute_index = current_index

  while current_condition != BinaryResult.OK:
    current_condition = condition(current_value)
    
    if current_condition == BinaryResult.MOVE_LEFT:
      old_index = current_index
      (current_index, current_value) = _bisect_once(current_index, current_lower, step)
      absolute_index = _advance_absolute_index(absolute_index, current_index, current_condition, old_index)

    elif current_condition == BinaryResult.MOVE_RIGHT:
      current_lower = _get_value_by_index(current_index + 1, current_lower, step) 
      (current_index, current_value) = _bisect_once(current_index, current_lower, step)
      absolute_index = _advance_absolute_index(absolute_index, current_index, current_condition)

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

def _check_args_of_binary_search(lower_bound, upper_bound, step, condition):
  if(upper_bound < lower_bound):
    raise ValueError(BINARY_SEARCH_BOUNDS_MIXED_UP)
  elif not isinstance(lower_bound, int) or not isinstance(upper_bound, int) or not isinstance(step, int):
    raise ValueError(BINARY_SEARCH_INTS_OF_WRONG_TYPE)
  elif not callable(condition):
    raise ValueError(BINARY_SEARCH_CONDITION_NOT_CALLABLE)
  elif not float((upper_bound - lower_bound) / step + 1).is_integer():
    raise ValueError(BINARY_SEARCH_INTS_DONT_MAKE_PROGRESSION)