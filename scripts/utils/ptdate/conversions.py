from datetime import date

def convert_date_string_to_month_day_year_tuple(valid_date_string):
  (month_string, day_string, year_string) = valid_date_string.split(sep = "/")
  return (int(month_string), int(day_string), int(year_string))

def convert_date_string_to_date(valid_date_string):
  (month_string, day_string, year_string) = valid_date_string.split(sep = "/")
  return date(month = int(month_string), day = int(day_string), year = int(year_string))