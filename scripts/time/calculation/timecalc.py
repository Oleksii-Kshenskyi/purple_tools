from scripts.utils.time.conversions import convert_to_timedelta
from scripts.utils.time.conversions import convert_timedelta_to_uniform_time_string
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT

def construct_uniform_time_string(source):
  source_timedelta = convert_to_timedelta(source)

  if not source_timedelta:
    return UNIFORM_TIME_STRING_DEFAULT

  return convert_timedelta_to_uniform_time_string(source_timedelta)