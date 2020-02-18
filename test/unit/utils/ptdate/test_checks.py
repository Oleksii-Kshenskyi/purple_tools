import unittest

from scripts.utils.ptdate.checks import is_valid_date_string

class TestDateChecks(unittest.TestCase):
  def setUp(self):
    pass

  def test_checks_for_valid_date_string(self):
    self.assertEqual(True, is_valid_date_string("01/01/0001"))
    self.assertEqual(True, is_valid_date_string("1/1/1"))
    self.assertEqual(True, is_valid_date_string("02/18/2020"))
    self.assertEqual(True, is_valid_date_string("02/18/20"))
    self.assertEqual(True, is_valid_date_string("2/18/20"))
    self.assertEqual(True, is_valid_date_string("5/3/2017"))
    self.assertEqual(True, is_valid_date_string("12/31/9999"))

    self.assertEqual(False, is_valid_date_string("2.18.20"))
    self.assertEqual(False, is_valid_date_string("2020-02-18"))
    self.assertEqual(False, is_valid_date_string("-3/11/2020"))
    self.assertEqual(False, is_valid_date_string("3/11/20200"))
    self.assertEqual(False, is_valid_date_string("02/30/2020"))
    self.assertEqual(False, is_valid_date_string("04/31/1991"))
    self.assertEqual(False, is_valid_date_string("13/02/2001"))
    self.assertEqual(False, is_valid_date_string("12/32/2002"))

    self.assertEqual(False, is_valid_date_string("01/32/2001"))
    self.assertEqual(False, is_valid_date_string("02/30/2002"))
    self.assertEqual(False, is_valid_date_string("03/32/2003"))
    self.assertEqual(False, is_valid_date_string("04/31/2004"))
    self.assertEqual(False, is_valid_date_string("05/32/2005"))
    self.assertEqual(False, is_valid_date_string("06/31/2006"))
    self.assertEqual(False, is_valid_date_string("07/32/2007"))
    self.assertEqual(False, is_valid_date_string("08/32/2008"))
    self.assertEqual(False, is_valid_date_string("09/31/2009"))
    self.assertEqual(False, is_valid_date_string("10/32/2010"))
    self.assertEqual(False, is_valid_date_string("11/31/2011"))
    self.assertEqual(False, is_valid_date_string("12/32/2012"))

    self.assertEqual(False, is_valid_date_string("00/00/00"))
    self.assertEqual(False, is_valid_date_string("00/01/0001"))
    self.assertEqual(False, is_valid_date_string("01/00/0001"))
    self.assertEqual(False, is_valid_date_string("01/01/0000"))

    self.assertEqual(False, is_valid_date_string("01/01/00.1"))

  def tearDown(self):
    pass


  if __name__ == "__main__":
    unittest.main(verbosity = 2)