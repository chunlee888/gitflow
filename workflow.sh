#!/bin/bash

# Step 1: Setup the environment
export X="World"

# Step 2: Run the first script and save its output to an artifact
python3 script1.py > artifact1.txt

# Step 3: Run the second script using the output of the first script
python3 script2.py "$(cat artifact1.txt)" > artifact2.txt

# Artifacts are saved as artifact1.txt and artifact2.txt
echo "Workflow completed. Artifacts saved as artifact1.txt and artifact2.txt."