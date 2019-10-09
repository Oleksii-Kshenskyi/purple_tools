import unittest
import re

class TestTimeChecks(unittest.TestCase):
  
  def setUp(self):
    self.__timestring_regex = r'^(\d)+:(\d)+:(\d)+$'

  def test_timelike_string_is_parsed_correctly(self):
    self.assertNotEqual(None, re.search(self.__timestring_regex, "01:34:42"))
    self.assertNotEqual(None, re.search(self.__timestring_regex, "00:00:00"))
    self.assertNotEqual(None, re.search(self.__timestring_regex, "564845454:56456456:00003450"))

    self.assertEqual(None, re.search(self.__timestring_regex, "3k:0205548:795454"))
    self.assertEqual(None, re.search(self.__timestring_regex, "20:@4:13"))
    self.assertEqual(None, re.search(self.__timestring_regex, "99:11:5@"))

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)