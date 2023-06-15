#!/bin/bash

i=1

while [ -f "input_file$i.txt" ]
do
  echo "Processing file$i"
  # Create a new output directory for the current run
  output_dir="output_$i"
  mkdir $output_dir
  # Run generator.py and move files to output dir
  python3 generator.py "input_file$i.txt"
  mv guard1 guard2 attack.spec $output_dir
  i=$((i+1))
done

echo "Done"
