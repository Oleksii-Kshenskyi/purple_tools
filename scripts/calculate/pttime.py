from scripts.utils.time.conversions import convert_to_timedelta
from scripts.utils.time.conversions import convert_timedelta_to_uniform_time_string
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT
from scripts.utils.time.constants import labeled_uniform_time_string_default

def construct_uniform_time_string(source, label=None):
  source_timedelta = convert_to_timedelta(source)

  if not source_timedelta and not label:
    return UNIFORM_TIME_STRING_DEFAULT
  elif not source_timedelta and label:
    return labeled_uniform_time_string_default(label)

  return convert_timedelta_to_uniform_time_string(source_timedelta, label)