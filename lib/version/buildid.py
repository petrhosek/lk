#!/usr/bin/env python

import argparse
import sys

HEADER_STUB = """\
#ifndef __%(filename)s_H
#define __%(filename)s_H
#define %(id)s
#endif\
"""

def ConfigHeader(file):
  #echo "#define $$d" | sed "s/=/\ /g;s/-/_/g;s/\//_/g;s/\./_/g;s/\//_/g;s/C++/CPP/g" >> $1.tmp;
  print >>file, HEADER_STUB % { 'filename': 'x', 'id': 'x' }


def main(argv):
  parser = argparse.ArgumentParser(description='Generate buildid.h')
  #parser.add_argument('infile', nargs='?', metavar='FILE', type=argparse.FileType('r'),
  #                    default=sys.stdin)
  parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                      default=sys.stdout)
  args = parser.parse_args()

  ConfigHeader(args.outfile)
  return 0


if __name__ == '__main__':
  sys.exit(main(sys.argv))
