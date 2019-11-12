import argparse

class ArithmeticParser:

  def _get_help_for_positional_argument(self, position):
    return '{0} positional arithmetic operation argument.'.format(position)

  def _add_arguments(self, parser):
    parser.add_argument("operation", help="Arithmetic operation to perform.", choices=self.operations.keys())
    parser.add_argument('first', type=int, help=self._get_help_for_positional_argument("First"))
    parser.add_argument('second', type=int, help=self._get_help_for_positional_argument("Second"))

  def run_operation(self, op_type, first, second):
    return self.operations[op_type](first, second)

  def add(self, a, b):
    return a + b

  def mul(self, a, b):
    return a * b

  def sub(self, a, b):
    return a - b

  def div(self, a, b):
    return a / b

  def __init__(self):
    self.operations = {"add": self.add, "sub": self.sub, "mul": self.mul, "div": self.div}
    self.parser = argparse.ArgumentParser()
    self._add_arguments(self.parser)

  def run(self):
    parsing_result = self.parser.parse_args()
    return self.run_operation(parsing_result.operation, parsing_result.first, parsing_result.second)


if __name__ == "__main__":
  print(ArithmeticParser().run())