import unittest

def run_tests_in_directory(dir_name, out_stream = None):
  loader = unittest.TestLoader()
  suite = loader.discover(dir_name)

  runner = unittest.TextTestRunner(verbosity=2, stream=out_stream)
  return runner.run(suite)