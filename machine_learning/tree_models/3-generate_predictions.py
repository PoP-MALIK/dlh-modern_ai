#!/usr/bin/env python3
"""Generate predictions from a trained classifier."""


def generate_predictions(clf, X):
    """Return predicted class labels for X."""
    return clf.predict(X)
