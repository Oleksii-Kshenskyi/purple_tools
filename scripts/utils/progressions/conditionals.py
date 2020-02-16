from enum import Enum, auto

class BinaryResult(Enum):
  MOVE_LEFT = auto()
  OK = auto()
  MOVE_RIGHT = auto()

class EqualityConditional:
  def __init__(self, condition_value):
    self.equal_to = condition_value

  def check(self, checked_value):
    if checked_value < self.equal_to:
      return BinaryResult.MOVE_RIGHT
    elif checked_value == self.equal_to:
      return BinaryResult.OK
    elif checked_value > self.equal_to:
      return BinaryResult.MOVE_LEFT