#!/usr/bin/env python

import argparse
import subprocess
import sys

def main(argv):
  parser = argparse.ArgumentParser(description='Run objcopy')
  parser.add_argument('--prefix', nargs='?', default='')
  parser.add_argument('infile')
  parser.add_argument('outfile')
  args = parser.parse_args()

  cmd = [args.prefix + "objcopy", "-O", "binary", args.infile, args.outfile]

  process = subprocess.Popen(' '.join(cmd), stdout=subprocess.PIPE, shell=True)
  process.communicate()
  return process.returncode


if __name__ == '__main__':
  sys.exit(main(sys.argv))
