import argparse
import sys

from scripts.parsers.basic_throwing_parser import BasicThrowingParser

class PurpleParser:

  def __init__(self):
    self._parser = BasicThrowingParser()
    self._parser.add_argument("kek", help="The notorious kek argument.")

  def run(self, arguments):
    return self._parser.parse_args(arguments if arguments else sys.argv[1:])