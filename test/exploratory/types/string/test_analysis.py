import unittest

class TestStringAnalysis(unittest.TestCase):
  def setUp(self):
    self.test_data = "I am a fun test data . also something !@$#%$#$^!"

  def test_find_method(self):
    self.assertEqual(21, self.test_data.find("."))
    self.assertEqual(-1, self.test_data.find("kek"))

  def tearDown(self):
    pass

if __name__ == "__main__":
  unittest.main(verbosity = 2)