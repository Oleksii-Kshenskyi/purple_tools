import re
from scripts.time.utils.constants import VALID_TIMESTRING_REGEX

def is_valid_time_string(checked_string):
  the_match = re.search(VALID_TIMESTRING_REGEX, checked_string)

  return True if the_match != None else False