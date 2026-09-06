# dlh-modern_ai

Projects completed as part of the DLH AI Academy Machine Learning specialization.

## Projects

### 1. Data Preparation & Visualization
**Directory:** `data_analysis/data_preparation_visualization`

Cleans and explores the Telco Customer Churn dataset using pandas, matplotlib,
and seaborn. Covers:
- Loading and describing raw data (shape, dtypes, missing values, duplicates)
- Handling missing values via dropping, median imputation, and domain-based
  imputation (`MonthlyCharges * tenure`)
- Type conversion and cleanup (`TotalCharges`, `SeniorCitizen`)
- Visualizing missing data, target distribution, categorical and continuous
  feature distributions, and feature correlations
- Churn rate analysis per categorical feature

**Files:** `0-describe_data.py` through `10-plot_categorical_vs_churn.py`

### 2. Tree-Based Models
**Directory:** `machine_learning/tree_models`

Builds, trains, and evaluates decision tree classifiers on the Wine dataset
using Scikit-learn. Covers:
- Building an unpruned `DecisionTreeClassifier` (Gini impurity)
- Training, predicting, and generating classification reports
  (precision, recall, F1-score)
- Viewing a trained tree's decision rules as text
- Pre-pruning via `GridSearchCV` hyperparameter search
  (`criterion`, `max_depth`, `min_samples_leaf`, `min_samples_split`)

**Files:** `0-build.py` through `5-pre_pruning.py`

## Requirements

- Python 3.11
- Packages: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`,
  `scipy`, `xgboost`, `lightgbm`, `pillow`
- All scripts follow `pycodestyle` and are executable
  (`#!/usr/bin/env python3`, `chmod +x`)

## Author

Melek Jaffel ([PoP-MALIK](https://github.com/PoP-MALIK))
