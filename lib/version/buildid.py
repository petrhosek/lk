#!/usr/bin/env python

import argparse
import os
import subprocess
import sys


HEADER_STUB = """\
#ifndef __BUILDID_H
#define __BUILDID_H
#define %(id)s
#endif\
"""


def ConfigHeader(script, file):
  process = subprocess.Popen(script, stdout=subprocess.PIPE, shell=True)
  out, err = process.communicate()
  print >>file, HEADER_STUB % { 'id': out.strip() }


def main(argv):
  parser = argparse.ArgumentParser(description='Generate buildid.h')
  parser.add_argument('--script', default='buildid.sh')
  parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                      default=sys.stdout)
  args = parser.parse_args()

  if not os.path.isfile(args.script):
    parser.error("'%s' is not a valid file" % args.script)

  ConfigHeader(args.script, args.outfile)
  return 0


if __name__ == '__main__':
  sys.exit(main(sys.argv))
