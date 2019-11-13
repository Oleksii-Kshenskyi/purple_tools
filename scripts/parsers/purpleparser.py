import argparse

from scripts.parsers.basic_throwing_parser import BasicThrowingParser

class PurpleParser:

  def run(self, arguments):
    return self._parser.parse_args(arguments if arguments else [])

  def __init__(self):
    self._parser = BasicThrowingParser()
    self._parser.add_argument("kek", help="The notorious kek argument.")
