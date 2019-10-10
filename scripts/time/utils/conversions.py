def check_float_validity_and_convert_from_string(source):
  try:
    return float(source)
  except:
    return None