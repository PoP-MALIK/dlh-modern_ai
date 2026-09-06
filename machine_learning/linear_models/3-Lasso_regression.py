#!/usr/bin/env python3
"""Build a Lasso regression model with L1 regularization."""
from sklearn import linear_model


def lasso_regression(random_state):
    """Create an untrained Lasso regression instance.

    Args:
        random_state: Seed for reproducibility.

    Returns:
        model: A Scikit-learn Lasso instance.
    """
    return linear_model.Lasso(random_state=random_state)
