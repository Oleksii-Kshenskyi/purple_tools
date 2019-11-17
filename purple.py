import traceback

import scripts.parsers.purpleparser as purple_parser

def run_purple_tools():
  parser = purple_parser.create_parser()
  parse_result = parser.parse_args()

  execution_result = purple_parser.run_endpoint(parse_result)
  print(execution_result)

if __name__ == "__main__":
  try:
    run_purple_tools()
  except Exception:
    print(traceback.format_exc())