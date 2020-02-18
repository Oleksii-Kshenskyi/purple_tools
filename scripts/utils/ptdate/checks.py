import re

from scripts.utils.ptdate.constants import VALID_DATE_STRING_REGEX
from scripts.utils.ptdate.constants import DAYS_IN_MONTHS
from scripts.utils.ptdate.conversions import convert_date_string_to_month_day_year_tuple

def is_valid_date_string(date_string):
  search_result = re.search(VALID_DATE_STRING_REGEX, date_string)
  if not search_result:
    return False

  (month, day, year) = convert_date_string_to_month_day_year_tuple(date_string)
  if day < 1 or year < 1:
    return False
  if month not in DAYS_IN_MONTHS.keys() or day > DAYS_IN_MONTHS[month]:
    return False

  return True
  