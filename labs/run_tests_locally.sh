#!/bin/bash
LAB=$1
for file in `ls $LAB.ipynb`; do
  echo "Testing $file"
  name="${file%.*}"
  pytest ../tests/test_$name.py
done;

