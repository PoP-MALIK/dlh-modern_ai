#!/usr/bin/env python3
"""Build an SVM classifier with a specified kernel."""
from sklearn import svm


def get_SVM_model(name, random_state):
    """Create an untrained SVC instance with the given kernel.

    Args:
        name: One of 'linear', 'poly', 'rbf'.
        random_state: Seed for reproducibility.

    Returns:
        An untrained SVC instance.
    """
    if name == 'linear':
        return svm.SVC(kernel='linear', random_state=random_state)
    elif name == 'poly':
        return svm.SVC(kernel='poly', random_state=random_state)
    elif name == 'rbf':
        return svm.SVC(kernel='rbf', random_state=random_state)
    else:
        raise ValueError(f"Unknown kernel name '{name}'")
