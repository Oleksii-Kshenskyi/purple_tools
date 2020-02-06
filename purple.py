import traceback

from scripts.parsers.purpleparser import PurpleParser

def run_purple_tools():
  parser = PurpleParser()
  parser.create_parser()
  parse_result = parser.parser.parse_args()

  execution_result = parser.run_endpoint(parse_result)
  print(execution_result)

if __name__ == "__main__":
  try:
    run_purple_tools()
  except Exception:
    print(traceback.format_exc())