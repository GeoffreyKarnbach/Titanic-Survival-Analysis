#!/bin/bash

# Loop through and run all Python scripts in the ModelTraining folder with prefix "evaluate_"

for script in ModelTraining/evaluate_*.py; do
    echo "Running $script..."
    python "$script"
    
    # Check if the previous command was successful
    if [ $? -eq 0 ]; then
        echo "$script completed successfully."
    else
        echo "$script failed."
        exit 1
    fi
done

# Compare the own prediction to the reference
python compare_own_prediction_to_reference.py

# Check if the previous command was successful
if [ $? -eq 0 ]; then
    echo "Comparison to reference completed successfully."
else
    echo "Comparison to reference failed."
    exit 1
fi

echo "All tasks completed successfully."
