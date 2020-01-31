import unittest

def run_tests_in_directory(dir_name):
  loader = unittest.TestLoader()
  suite = loader.discover(dir_name)

  runner = unittest.TextTestRunner(verbosity=2)
  runner.run(suite)