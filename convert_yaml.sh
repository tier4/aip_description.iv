#!/bin/sh

for f in $(find . -name "*calibration.yaml"); do
  python convert_yaml.py "$f"
done
