__author__ = 'ferdous'

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname('../../')))
from scripts import  setup_django, utils


def run(args):
    print args

if __name__ == '__main__':
    print sys.path
#    utils.cli(sys.argv[1:], run, os.path.basename(__file__))