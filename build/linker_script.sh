#!/bin/bash

for i in "$@"; do
  case $i in
    *=*)
      declare "${i%=*}"="${i#*=}"
      ;;
  esac
done

sed "s/%MEMBASE%/${MEMBASE}/;s/%MEMSIZE%/${MEMSIZE}/;s/%KERNEL_BASE%/${KERNEL_BASE}/;s/%KERNEL_LOAD_OFFSET%/${KERNEL_LOAD_OFFSET}/" <${1} >${2}
