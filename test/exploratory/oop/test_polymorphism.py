import unittest

class ParentClass:
  def __init__(self):
    self.param = "parent"

  def overloaded_method(self):
    return "CALL: parent"

  def overloaded_returns(self):
    return self._returns_impl()

  def _returns_impl(self):
    return "returns parent..."

class ChildClass(ParentClass):
  def __init__(self):
    super(ChildClass, self).__init__()
    self.parents_backed_up_param = self.param
    self.param = "child"

  def overloaded_method(self):
    return "CALL: child"

  def _returns_impl(self):
    return "returns child..."

class TestPolymorphism(unittest.TestCase):
  def setUp(self):
    self.the_parent = ParentClass()
    self.the_child = ChildClass()

  def test_polymorphism_overloads_variables_and_methods(self):
    self.assertEqual("parent", self.the_parent.param)
    self.assertEqual("CALL: parent", self.the_parent.overloaded_method())
    self.assertEqual("parent", self.the_child.parents_backed_up_param)
    self.assertEqual("child", self.the_child.param)
    self.assertEqual("CALL: child", self.the_child.overloaded_method())

  def test_return_is_polymorphic(self):
    self.assertEqual("returns parent...", self.the_parent.overloaded_returns())
    self.assertEqual("returns child...", self.the_child.overloaded_returns())

  def tearDown(self):
    pass