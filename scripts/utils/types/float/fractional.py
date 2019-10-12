from scripts.utils.time.checks import is_of_type

def get_fractional_part_as_string(the_float):
  if not is_of_type(the_float, float):
    return ""

  string_float = str(the_float)
  dot_position = string_float.find(".")
  return "" if dot_position == -1 else string_float[dot_position + 1 : ]

def is_fractional_part_significant(the_float):
  if not is_of_type(the_float, float):
    return False

  return int(the_float) != the_float

  
