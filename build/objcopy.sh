#!/bin/bash

readonly PREFIX="$1"
readonly INPUT="$2"
readonly OUTPUT="$3"

${PREFIX}objcopy -O binary ${INPUT} ${OUTPUT}
