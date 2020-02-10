import unittest

class TestListManipulations(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_slicing_off_elements(self):
    self.assertEqual([2, 3, "kek"], [1, 2, 3, "kek"][1:])

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)