#!/usr/bin/env python3
"""Build an ordinary least squares linear regression model."""
from sklearn import linear_model


def Linear_Regression():
    """Create an untrained LinearRegression instance.

    Returns:
        model: A Scikit-learn LinearRegression instance.
    """
    return linear_model.LinearRegression()
