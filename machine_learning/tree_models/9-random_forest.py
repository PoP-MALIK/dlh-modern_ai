#!/usr/bin/env python3
"""Build a random forest classifier."""
from sklearn import ensemble


def random_forest(n_estimators, random_state):
    """Create a RandomForestClassifier.

    Returns:
        model: A Scikit-learn RandomForestClassifier instance.
    """
    return ensemble.RandomForestClassifier(n_estimators=n_estimators,
                                            random_state=random_state)
