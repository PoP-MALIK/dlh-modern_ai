#!/usr/bin/env python3
"""Build a Ridge regression model with L2 regularization."""
from sklearn import linear_model


def ridge_regression(random_state):
    """Create an untrained Ridge regression instance.

    Args:
        random_state: Seed for reproducibility.

    Returns:
        model: A Scikit-learn Ridge instance.
    """
    return linear_model.Ridge(random_state=random_state)
