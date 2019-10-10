from datetime import timedelta

from scripts.time.utils.checks import is_of_type
from scripts.time.utils.checks import is_valid_time_string
from scripts.time.utils.constants import TIME_UNIT_LENGTH_IN_SECONDS

def check_float_validity_and_convert_from_string(source):
  try:
    return float(source)
  except:
    return None

def convert_float_to_timedelta(source):
  if not is_of_type(source, float) or source < 0:
    return None

  return timedelta(seconds = source * TIME_UNIT_LENGTH_IN_SECONDS)

def convert_time_string_to_timedelta(source):
  if not is_valid_time_string(source):
    return None

  (new_hours, new_minutes, new_seconds) = source.split(sep = ":")
  return timedelta(hours = int(new_hours), minutes = int(new_minutes), seconds = int(new_seconds))

def convert_to_timedelta(source):
  if is_of_type(source, float):
    return convert_float_to_timedelta(source)
  elif is_of_type(source, str):
    return convert_time_string_to_timedelta(source)
  else:
    return None