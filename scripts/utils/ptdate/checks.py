import re

from scripts.utils.ptdate.constants import VALID_DATE_STRING_REGEX
from scripts.utils.ptdate.constants import DAYS_IN_MONTHS

def is_valid_date_string(date_string):
  search_result = re.search(VALID_DATE_STRING_REGEX, date_string)
  if not search_result:
    return False

  (month_string, day_string, year_string) = date_string.split(sep = "/")
  month = int(month_string)
  day = int(day_string)
  year = int(year_string)
  if day < 1 or year < 1:
    return False
  if month not in DAYS_IN_MONTHS.keys() or day > DAYS_IN_MONTHS[month]:
    return False

  return True
  