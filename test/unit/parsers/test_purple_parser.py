import unittest
from scripts.parsers.purpleparser import PurpleParser 

class TestPurpleParser(unittest.TestCase):
  
  def setUp(self):
    self.parser = PurpleParser()

  def test_dummy_parameter_is_processed(self):
    parsing_result = self.parser.run(["azaz"])
    self.assertEqual("azaz", parsing_result.kek)

    with self.assertRaises(ValueError):
      self.parser.run(["azaz", "kazaz"])

    with self.assertRaises(ValueError):
      self.parser.run([])

  def tearDown(self):
    pass

if __name__ == "__main__":

    unittest.main(verbosity=2)