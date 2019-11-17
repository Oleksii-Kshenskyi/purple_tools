import sys
import argparse

class BasicThrowingParser(argparse.ArgumentParser):
  def error(self, message):
    raise ValueError(message)