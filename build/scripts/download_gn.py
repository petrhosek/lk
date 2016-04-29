#!/usr/bin/env python
#
# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import platform
import sys
import urllib2


REPO = "https://chromium.googlesource.com/chromium/buildtools/+/master"
BUCKET = "https://storage.googleapis.com/chromium-gn"
PLATFORM_MAPPING = {
    ("darwin", "x86_64"): "mac",
    ("linux2", "x86_64"): "linux64",
}


def DownloadFile(url):
  try:
    return urllib2.urlopen(url).read()
  except urllib2.HTTPError as e:
    print("%s: %s" % (url, e))
  return None


def main(argv):
  host = sys.platform, platform.machine()
  try:
    host = PLATFORM_MAPPING[host]
  except KeyError:
    print("no gn available for the platform" % host)
    return 1

  digest = DownloadFile("%s/%s/gn.sha1?format=TEXT" % (REPO, host))
  data = DownloadFile("%s/%s" % (BUCKET, digest.decode("base64")))

  out = os.path.join(os.getcwd(), "gn")
  with open(out, "w") as f:
    f.write(data)
  os.chmod(out, 0o755)
  return 0


if __name__ == "__main__":
  sys.exit(main(sys.argv))
