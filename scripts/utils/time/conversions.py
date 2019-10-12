from datetime import timedelta

from scripts.utils.time.checks import is_of_type
from scripts.utils.time.checks import is_valid_time_string
from scripts.utils.time.constants import TIME_UNIT_LENGTH_IN_SECONDS
from scripts.utils.time.constants import UNIFORM_TIME_STRING
from scripts.utils.time.constants import ROUND_UNITS_TO
from scripts.utils.time.constants import SECONDS_IN_MINUTE
from scripts.utils.time.constants import MINUTES_IN_HOUR
from scripts.utils.types.float.fractional import is_fractional_part_significant

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

def convert_timedelta_to_uniform_time_string(source_timedelta):
  if not is_of_type(source_timedelta, timedelta):
    return UNIFORM_TIME_STRING.format(0, 0, 0, 0)

  total_seconds = round(source_timedelta.total_seconds())
  raw_units = total_seconds / TIME_UNIT_LENGTH_IN_SECONDS
  if is_fractional_part_significant(raw_units):
    units = round(raw_units, ROUND_UNITS_TO)    
  else:
    units = int(raw_units)

  (rest, secs) = divmod(total_seconds, SECONDS_IN_MINUTE)
  (hrs, mins) = divmod(rest, MINUTES_IN_HOUR)

  return UNIFORM_TIME_STRING.format(units, hrs, mins, secs)