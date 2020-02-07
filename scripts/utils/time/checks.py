import re
from scripts.utils.time.constants import VALID_TIMESTRING_REGEX
from scripts.utils.time.constants import VALID_DURATION_REGEX
from scripts.utils.time.constants import FINDALL_DURATION_REGEX

def is_valid_time_string(checked_string):
  the_match = re.search(VALID_TIMESTRING_REGEX, checked_string)

  return True if the_match != None else False

def is_valid_duration_string(checked_string):
  the_match = re.search(VALID_DURATION_REGEX, checked_string)

  if(the_match):
    output = re.findall(FINDALL_DURATION_REGEX, checked_string)
    return _is_findall_output_hms_balanced(output)

  return False

def is_of_type(the_value, the_type):
  return type(the_value) == the_type

def _is_findall_output_hms_balanced(output):
  hs = 0
  ms = 0
  ss = 0
  for i in range(0, len(output)):
    if 'h' in output[i][0]:
      hs += 1
    elif 'm' in output[i][0]:
      ms += 1
    elif 's' in output[i][0]:
      ss += 1
  return False if hs > 1 or ms > 1 or ss > 1 else True

