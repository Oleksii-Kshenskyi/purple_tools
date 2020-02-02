import unittest

class TestDummySuccess1(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_dummy_success(self):
    self.assertEqual(True, True)

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)