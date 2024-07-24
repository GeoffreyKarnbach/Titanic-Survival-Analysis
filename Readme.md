# Will John Doe survive the titanic? - Probably not!

## Overview

This project focuses on predicting the survival of passengers aboard the Titanic using machine learning techniques. By analyzing the Titanic dataset from Kaggle, we aim to determine whether a passenger would have survived the tragic accident based on various features. The analysis involves data cleaning, feature engineering, and model development to enhance prediction accuracy.

## Project Goals

The primary objective of this project is to identify patterns and correlations in the Titanic dataset that can be used to predict passenger survival. We employ both traditional statistical analysis and machine learning models to achieve this goal.

## Dataset

The Titanic dataset includes the following attributes for each passenger:

- **PassengerId**: Unique identifier for the passenger.
- **Passenger Class**: The class in which the passenger traveled (1st, 2nd, 3rd).
- **Name**: Name of the passenger.
- **Sex**: Gender of the passenger.
- **Age**: Age of the passenger.
- **Number of siblings/spouses on Titanic**: Number of siblings or spouses aboard the Titanic.
- **Number of parents/children on Titanic**: Number of parents or children aboard the Titanic.
- **Ticket Number**: The ticket number.
- **Fare**: Price paid for the ticket.
- **Cabin Number**: The cabin number where the passenger stayed.
- **Embarkation Port**: Port where the passenger boarded the Titanic.

## Data Preparation and Cleaning

### Attribute Selection

- **Excluded Attributes**: PassengerId, Ticket Number, and Cabin Number were excluded as they were deemed non-contributory to the survival prediction.
- **Key Attributes**: Focused on Passenger Class, Name, Sex, Age, Number of siblings/spouses, Number of parents/children, Fare, and Embarkation Port.

### Handling Missing Data

Missing values were addressed using various imputation techniques:

- **Mode Imputation**: Categorical variables had missing values filled with the most frequently occurring value.
- **Median Imputation**: Numeric attributes with missing values were replaced with the median value.
- **K-Nearest Neighbors (KNN) Imputation**: Missing values were estimated based on the values of the nearest neighbors.
- **Multivariate Imputation by Chained Equations (MICE)**: Used multiple iterations to estimate missing values based on other features.

### Feature Engineering

- **Categorization of Continuous Variables**: Age and Fare were categorized into meaningful ranges (e.g., Fare < 50, 50 - 100, 100 - 200, > 200).
- **New Features**: Added features such as `isAlone` (indicating whether a passenger was traveling alone) and `title` (extracted from the passenger’s name).

## Model Development and Evaluation

Decision tree models were developed and evaluated using the prepared dataset:

1. **Decision Tree Model v1**: Initial accuracy of 61%.
2. **Decision Tree Model v2**: Improved accuracy to 70% by categorizing continuous variables.
3. **Decision Tree Model v3**: Applied Mode Imputation with an accuracy of 66%.
4. **Decision Tree Model v4**: Used Median Imputation with an accuracy of 67%.
5. **Decision Tree Model v5**: Implemented KNN Imputation with an accuracy of 70%.
6. **Decision Tree Model v6**: Applied MICE with a consistent accuracy of 70%.
7. **Decision Tree Model v7**: Introduced feature engineering, achieving a final accuracy of 74%.

## Future Work

- **Machine Learning Models**: Plans to train additional machine learning models using TensorFlow to compare with the decision tree models and further enhance prediction accuracy.
- **Model Refinement**: Continual improvement of data preprocessing techniques and model tuning.

## Getting Started

To replicate or extend this project, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/GeoffreyKarnbach/Titanic-Survival-Analysis
   ```

2. **Run the initial build command to setup the development environment**

   ```bash
   sh build_all.sh
   ```

   This shell scripts installs all dependencies with pip, runs the notebook to generate the refined datasets for the decision tree inputs,
   builds the decision trees, evaluates them on the test dataset and ranks them according to the solution file.

3. **Run the frontend**

   ```bash
   cd Frontend
   npm install
   ng serve
   ```

4. **Run the prediction python backend service**

   ```bash
   python titanic_service.py
   ```

5. **Visit the frontend page**

   Go to: [http://localhost:4200/](http://localhost:4200/)

## Contact

For any questions or suggestions, please contact:
- Author: Geoffrey Karnbach
- GitHub: https://github.com/GeoffreyKarnbach

## Acknowledgements

The Titanic dataset is provided by Kaggle and is used here for educational and analytical purposes.

https://www.kaggle.com/competitions/titanic