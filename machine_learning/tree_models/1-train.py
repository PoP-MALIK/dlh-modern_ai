#!/usr/bin/env python3
"""Train a tree-based classifier."""


def train_tree(clf, X, y):
    """Fit the classifier on X, y in place."""
    clf.fit(X, y)
