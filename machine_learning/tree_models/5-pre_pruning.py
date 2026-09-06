#!/usr/bin/env python3
"""Grid-search pre-pruning hyperparameters for a decision tree."""
from sklearn import model_selection


def prepruning(X, y, clf):
    """Return the best pre-pruning hyperparameter combination."""
    param_grid = {
        'criterion': ['gini', 'entropy'],
        'max_depth': range(2, 5),
        'min_samples_leaf': range(2, 5),
        'min_samples_split': range(2, 5),
    }
    grid = model_selection.GridSearchCV(clf, param_grid)
    grid.fit(X, y)
    return grid.best_params_
