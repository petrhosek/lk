#!/usr/bin/env python

import argparse
import sys

def ConfigLdScript(defines, infile, outfile):
  for line in infile:
    for key in defines:
      line = line.replace(key, defines[key])
    outfile.write(line)

def main(argv):
  parser = argparse.ArgumentParser(description='Generate kernel.ld')
  parser.add_argument('--defines', nargs='+', required=True)
  parser.add_argument('--infile', nargs='?', type=argparse.FileType('r'),
                      required=True)
  parser.add_argument('--outfile', nargs='?', type=argparse.FileType('w'),
                      required=True)
  args = parser.parse_args()

  defines = dict()
  for arg in vars(args)['defines']:
    kv = arg.split('=')
    defines['%' + kv[0] + '%'] = kv[1]

  ConfigLdScript(defines, args.infile, args.outfile)
  return 0

if __name__ == '__main__':
  sys.exit(main(sys.argv))
