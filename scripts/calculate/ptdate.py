from scripts.utils.ptdate.conversions import convert_date_string_to_date

def calculate_date_difference_as_day_count(date_string_one, date_string_two):
  date_one = convert_date_string_to_date(date_string_one)
  date_two = convert_date_string_to_date(date_string_two)
  resulting_timedelta = abs(date_one - date_two)
  return resulting_timedelta.days