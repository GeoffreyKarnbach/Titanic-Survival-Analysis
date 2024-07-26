# First run all cells in "survival_analysis.ipynb" to generate the survival analysis results
# Then run "DecisionTree/build_decision_tree.py" to generate the decision tree
# Then run "DecisionTree/evaluate_decision_tree.py" to evaluate the decision tree
# Finally run "compare_own_prediction_to_reference.py" to generate the evaluation results

#!/bin/bash

# Ask the user to confirm
read -p "This script will run several processes and may take some time. Do you want to proceed? (yes/no): " confirm

# Convert the input to lowercase
confirm=$(echo "$confirm" | tr '[:upper:]' '[:lower:]')

# Check if the user confirmed
if [[ "$confirm" != "yes" ]]; then
    echo "Script aborted."
    exit 0
fi

# Install Python dependencies
echo "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

# Check if the previous command was successful
if [ $? -eq 0 ]; then
    echo "Python dependencies installed successfully."
else
    echo "Failed to install Python dependencies."
    exit 1
fi

# Run the survival analysis
jupyter nbconvert --to notebook --execute survival_analysis.ipynb --output executed_survival_analysis.ipynb

# Check if the previous command was successful
if [ $? -eq 0 ]; then
    echo "Survival notebook analysis completed successfully."
else
    echo "Survival notebook analysis failed."
    exit 1
fi

# Run the decision tree
python ModelTraining/build_decision_tree.py

# Check if the previous command was successful
if [ $? -eq 0 ]; then
    echo "Decision tree model build completed successfully."
else
    echo "Decision tree model build failed."
    exit 1
fi

# Evaluate the decision tree
python ModelTraining/evaluate_decision_tree.py

# Check if the previous command was successful
if [ $? -eq 0 ]; then
    echo "Decision tree model evaluation to csv files completed successfully."
else
    echo "Decision tree model evaluation to csv files failed."
    exit 1
fi

# Compare the own prediction to the reference
python compare_own_prediction_to_reference.py

# Check if the previous command was successful
if [ $? -eq 0 ]; then
    echo "Comparison to reference completed successfully."
else
    echo "Comparison to reference failed."
    exit 1
fi

# Delete the intermediate files
rm executed_survival_analysis.ipynb

echo "All tasks completed successfully."
