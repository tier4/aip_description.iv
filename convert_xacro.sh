#!/bin/sh

for f in $(find . -name "*.xacro"); do
  python convert_xacro.py "$f"
done
