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

  current_index = (upper_bound - lower_bound) // step + 1
  current_index = current_index // 2 if (current_index % 2 == 0) else current_index // 2 + 1
  current_value = (current_index - 1) * step + lower_bound
  current_condition = condition(current_value)
  current_lower = lower_bound
  current_upper = upper_bound
  absolute_index = current_index
  _dump(current_index, absolute_index, current_value, current_lower, current_upper, current_condition)
  while current_condition != BinaryResult.OK:
    current_condition = condition(current_value)
    if current_condition == BinaryResult.MOVE_LEFT:
      current_value = (current_index - 1) * step + current_lower
      current_upper = current_value
      # current_index = (current_upper - current_lower) // step + 1
      even_index = current_index % 2 == 0
      current_index = current_index // 2 if even_index else current_index // 2 + 1
      absolute_index = absolute_index - current_index if even_index else absolute_index - (current_index - 1)
      current_value = (current_index - 1) * step + current_lower
      _dump(current_index, absolute_index, current_value, current_lower, current_upper, current_condition)
    elif current_condition == BinaryResult.MOVE_RIGHT:
      # current_index += 1
      # current_value = (current_index - 1) * step + current_lower
      current_lower = ((current_index + 1) - 1) * step + current_lower # current_value
      # current_index = (current_upper - current_lower) // step + 1
      current_index = current_index // 2 if (current_index % 2 == 0) else current_index // 2 + 1
      absolute_index += current_index
      current_value = (current_index - 1) * step + current_lower
      _dump(current_index, absolute_index, current_value, current_lower, current_upper, current_condition)

  return absolute_index - 1


# def _get_pair(lower_bound, upper_bound, step):
#   current_index = (upper_bound - lower_bound) / step + 1
#   current_value = (current_index - 1) * step + lower_bound
#   return (current_index, current_value)

def _dump(current_index, absolute_index, current_value, current_lower, current_upper, current_condition):
  print(f"\n----\nindex: {current_index}\nabsolute index: {absolute_index}\nvalue: {current_value}\nlower: {current_lower}\nupper: {current_upper}\ncondition: {current_condition}\n----\n")

def _check_args_of_binary_search(lower_bound, upper_bound, step, condition):
  if(upper_bound < lower_bound):
    raise ValueError(BINARY_SEARCH_BOUNDS_MIXED_UP)
  elif not isinstance(lower_bound, int) or not isinstance(upper_bound, int) or not isinstance(step, int):
    raise ValueError(BINARY_SEARCH_INTS_OF_WRONG_TYPE)
  elif not callable(condition):
    raise ValueError(BINARY_SEARCH_CONDITION_NOT_CALLABLE)
  elif not float((upper_bound - lower_bound) / step + 1).is_integer():
    raise ValueError(BINARY_SEARCH_INTS_DONT_MAKE_PROGRESSION)