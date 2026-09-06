#!/usr/bin/env python3
"""Retrieve the cost-complexity pruning path of a decision tree."""


def get_pruning_path(clf, X, y):
    """Return the ccp_alphas and total leaf impurities for pruning.

    Args:
        clf: A DecisionTreeClassifier instance.
        X: Input features.
        y: Target labels.

    Returns:
        ccp_alphas: Array of effective alpha values.
        impurities: Array of total leaf impurity at each alpha.
    """
    path = clf.cost_complexity_pruning_path(X, y)
    return path.ccp_alphas, path.impurities
