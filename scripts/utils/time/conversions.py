from datetime import timedelta
import re

from scripts.utils.time.checks import is_of_type
from scripts.utils.time.checks import is_valid_time_string
from scripts.utils.time.checks import is_valid_duration_string
from scripts.utils.time.constants import TIME_UNIT_LENGTH_IN_SECONDS
from scripts.utils.time.constants import UNIFORM_TIME_STRING
from scripts.utils.time.constants import LABELED_UNIFORM_TIME_STRING
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT
from scripts.utils.time.constants import labeled_uniform_time_string_default
from scripts.utils.time.constants import ROUND_UNITS_TO
from scripts.utils.time.constants import SECONDS_IN_MINUTE
from scripts.utils.time.constants import MINUTES_IN_HOUR
from scripts.utils.time.constants import FINDALL_DURATION_REGEX
from scripts.utils.utypes.ufloat.fractional import is_fractional_part_significant

def check_float_validity_and_convert_from_string(source):
  try:
    return float(source)
  except:
    return None

def convert_float_to_timedelta(source):
  if not is_of_type(source, float) or source < 0:
    return None

  return timedelta(seconds = round(round(source, ROUND_UNITS_TO) * TIME_UNIT_LENGTH_IN_SECONDS))

def convert_time_string_to_timedelta(source):
  if not is_valid_time_string(source):
    return None

  (new_hours, new_minutes, new_seconds) = source.split(sep = ":")
  return timedelta(hours = int(new_hours), minutes = int(new_minutes), seconds = int(new_seconds))

def convert_duration_string_to_timedelta(source):
  if not is_valid_duration_string(source):
    return None

  output = re.findall(FINDALL_DURATION_REGEX, source)
  hrs = 0
  mins = 0
  secs = 0
  for i in range(0, len(output)):
    if 'h' in output[i][0]:
      hrs = int((output[i][0])[:-1]) # drop the last character [h|m|s] and convert to int
    elif 'm' in output[i][0]:
      mins = int((output[i][0])[:-1])
    elif 's' in output[i][0]:
      secs = int((output[i][0])[:-1])
  
  return timedelta(hours = hrs, minutes = mins, seconds = secs)

def convert_to_timedelta(source):
  if is_of_type(source, int):
    return convert_float_to_timedelta(float(source))
  elif is_of_type(source, float):
    return convert_float_to_timedelta(source)
  elif is_of_type(source, str) and is_valid_time_string(source):
    return convert_time_string_to_timedelta(source)
  elif is_of_type(source, str) and is_valid_duration_string(source):
    return convert_duration_string_to_timedelta(source)
  else:
    return None

def convert_timedelta_to_uniform_time_string(source_timedelta, label = None):
  if not is_of_type(source_timedelta, timedelta):
    return UNIFORM_TIME_STRING_DEFAULT if not label else labeled_uniform_time_string_default(label)

  total_seconds = round(source_timedelta.total_seconds())
  raw_units = total_seconds / TIME_UNIT_LENGTH_IN_SECONDS
  if is_fractional_part_significant(raw_units):
    units = round(raw_units, ROUND_UNITS_TO)    
  else:
    units = int(raw_units)

  (rest, secs) = divmod(total_seconds, SECONDS_IN_MINUTE)
  (hrs, mins) = divmod(rest, MINUTES_IN_HOUR)

  return UNIFORM_TIME_STRING.format(units, hrs, mins, secs) if not label else LABELED_UNIFORM_TIME_STRING.format(label, units, hrs, mins, secs)