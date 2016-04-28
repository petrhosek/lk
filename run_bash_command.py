#!/usr/bin/env python

import sys
import subprocess
import os

def main(argv):
  command = ' '.join(argv[1:])
  # Admittedly, using "shell=True" here is somewhat risky, but it enables
  # GN actions using this script to act exactly like calls into bash.
  process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
  process.communicate()
  return process.returncode

if __name__ == '__main__':
  sys.exit(main(sys.argv))
