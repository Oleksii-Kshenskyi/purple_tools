import unittest

class TestStringManipulations(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_string_splitting(self):
    self.assertEqual(["one", "two", "three"], "one:two:three".split(sep=":"))
    self.assertEqual(["o","", "", "", "t", "", "", "", "e"], "o::::t::::e".split(sep=":"))
    self.assertEqual(["o", "t", "e"], "    o    t       e    ".split())
    
    skip_empty_list = "o::::t::::e".split(sep=":")
    self.assertEqual(["o", "t", "e"], [item for item in skip_empty_list if item != ''])

    (just, three, items) = "one:two:three".split(sep=":")
    self.assertEqual(just, "one")
    self.assertEqual(three, "two")
    self.assertEqual(items, "three")

  def test_cropping_last_character(self):
    self.assertEqual("Hell", str("Hello")[:-1])
    self.assertEqual("Surpris", str("Surprise")[:-1])

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)