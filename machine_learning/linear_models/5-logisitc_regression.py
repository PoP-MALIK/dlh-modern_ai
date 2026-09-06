#!/usr/bin/env python3
"""Build a logistic regression classifier."""
from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Create an untrained LogisticRegression instance.

    Args:
        random_state: Seed for reproducibility.

    Returns:
        model: A Scikit-learn LogisticRegression instance.
    """
    return linear_model.LogisticRegression(random_state=random_state)
