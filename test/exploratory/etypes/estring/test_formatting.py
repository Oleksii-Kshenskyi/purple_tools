import unittest

class TestStringFormatting(unittest.TestCase):
  
  def setUp(self):
    self.pre_set_up_format_string = '{} meets {} equals {}!'

  def test_string_format_method(self):
    self.assertEqual("beetle meets boots equals squash!", 
      self.pre_set_up_format_string.format("beetle", "boots", "squash"))
    self.assertNotEqual("beetle meets boots equals squash!", 
      self.pre_set_up_format_string) # Does the str.format() change the source format string? (no)

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)