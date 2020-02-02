import unittest
import os

from scripts.utils.testing.batch.execute import run_tests_in_directory

class TestExecute(unittest.TestCase):
  
  def setUp(self):
    pass

  def _batch_execute_and_test_dummies(self, folder_name, error_count, failure_count, run_count):
    spath = os.path.join(os.path.dirname(os.path.realpath(__file__)), folder_name)
    redirected_output_filename = os.path.join(spath, "output.txt")
    with open(redirected_output_filename, "w") as f:
      result = run_tests_in_directory(spath, f)
      self.assertEqual(len(result.errors), error_count)
      self.assertEqual(len(result.failures), failure_count)
      self.assertEqual(result.testsRun, run_count)

    os.unlink(redirected_output_filename)

  def test_batch_execution_of_successful_dummies_is_ok(self):
    self._batch_execute_and_test_dummies("successful_dummies", 0, 0, 2)

  def test_batch_execution_of_failed_dummies_fails(self):
    self._batch_execute_and_test_dummies("failed_dummies", 0, 1, 2)

  def tearDown(self):
      pass

if __name__ == "__main__":

    unittest.main(verbosity=2)