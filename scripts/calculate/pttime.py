from datetime import timedelta

from scripts.utils.time.conversions import convert_to_timedelta
from scripts.utils.time.conversions import convert_timedelta_to_uniform_time_string
from scripts.utils.time.conversions import forward_number_from_argparse
from scripts.utils.time.constants import UNIFORM_TIME_STRING_DEFAULT
from scripts.utils.time.constants import labeled_uniform_time_string_default

def construct_uniform_time_string(source, label = None):
  source_timedelta = convert_to_timedelta(source)

  if not source_timedelta and not label:
    return UNIFORM_TIME_STRING_DEFAULT
  elif not source_timedelta and label:
    return labeled_uniform_time_string_default(label)

  return convert_timedelta_to_uniform_time_string(source_timedelta, label)

def get_timedelta_sum_as_uniform_time_sting(source_list, label = None):
  timedelta_sum = timedelta(seconds = 0)
  for source_item in source_list:
    converted = convert_to_timedelta(forward_number_from_argparse(source_item))
    timedelta_item = converted if converted else timedelta(seconds = 0)
    timedelta_sum += timedelta_item

  return convert_timedelta_to_uniform_time_string(timedelta_sum, label)

def get_timedelta_diff_as_uniform_time_sting(source_list, label = None):
  basis = convert_to_timedelta(forward_number_from_argparse(source_list[0]))
  timedelta_diff = basis if basis else timedelta(seconds = 0)
  for source_item in source_list[1:]:
    converted = convert_to_timedelta(forward_number_from_argparse(source_item))
    timedelta_item = converted if converted else timedelta(seconds = 0)
    timedelta_diff -= timedelta_item

  return convert_timedelta_to_uniform_time_string(timedelta_diff, label)