import unittest

from scripts.parsers.time.time_parser import TimeParser

class TestTimeParser(unittest.TestCase):
  
  def setUp(self):
    self.wrapper = TimeParser()
    self.parser = self.wrapper._parser

  def test_parser_processes_arguments(self):
    self.wrapper._parser.parse_args(["print", "3"])

  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)