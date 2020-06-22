
import sys
import os
from argparse import ArgumentParser
import DataAnalysis

def parser():
  parser = ArgumentParser(description="World animal regulated trades")
  parser.add_argument("--sp", type=str , help="write the animal you want to know about")
  parser.add_argument("--info", type=str , help="Write what you want to know first: Class, Order, Phylum, Exporter, Importer, Purpose or Quantity ")
  return parser.parse_args()












