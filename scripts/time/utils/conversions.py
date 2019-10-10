from datetime import timedelta

from scripts.time.utils.checks import is_of_type
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