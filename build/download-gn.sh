#!/usr/bin/env bash

set -o pipefail

readonly OS=`uname`
readonly ARCH=`uname -m`
readonly REPO="https://chromium.googlesource.com/chromium/buildtools/+/master"
readonly BUCKET="https://storage.googleapis.com/chromium-gn"

err() {
  echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2
}

if [[ "${ARCH}" != "x86_64" ]]; then
  err "Unsupported architecture: ${ARCH}"
  exit 1
fi

if [[ "${OS}" == "Linux" ]]; then
  HOST="linux64"
elif [[ "${OS}" == "Darwin" ]]; then
  HOST="mac"
fi

digest=$(curl "${REPO}/${HOST}/gn.sha1?format=TEXT" 2>/dev/null | base64 -d)
if [[ "$?" -ne 0 ]]; then
  err "Failed to find GN revision"
  exit 1
fi

curl -o gn "${BUCKET}/${digest}" 2>/dev/null
if [[ "$?" -ne 0 ]]; then
  err "Failed to download GN"
  exit 1
fi

chmod 0755 gn
