from datetime import timedelta

def add_timedeltas(list_of_timedeltas):
  timedelta_sum = timedelta(seconds = 0)
  for td in list_of_timedeltas:
    timedelta_sum += td
  return timedelta_sum