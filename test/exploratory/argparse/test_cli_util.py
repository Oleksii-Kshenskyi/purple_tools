import argparse

def add(a, b):
  return a + b

def mul(a, b):
  return a * b

def sub(a, b):
  return a - b

def div(a, b):
  return a / b

operations = {"add": add, "sub": sub, "mul": mul, "div": div}

def main():
  main_parser = argparse.ArgumentParser()

  main_parser.add_argument("operation", help="Arithmetic operation to perform.", choices=operations.keys())
  help_string = '{0} positional arithmetic operation argument.'
  main_parser.add_argument('first', type=int, help=help_string.format("First"))
  main_parser.add_argument('second', type=int, help=help_string.format("Second"))
  parsing_result = main_parser.parse_args()

  print(operations[parsing_result.operation](parsing_result.first, parsing_result.second))


if __name__ == "__main__":
  main()