import re
from scripts.utils.time.constants import VALID_TIMESTRING_REGEX

def is_valid_time_string(checked_string):
  the_match = re.search(VALID_TIMESTRING_REGEX, checked_string)

  return True if the_match != None else False

def is_of_type(the_value, the_type):
  return type(the_value) == the_type