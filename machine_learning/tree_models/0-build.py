#!/usr/bin/env python3
"""Build an unpruned decision tree classifier."""
from sklearn import tree


def build_decision_tree(min_samples_leaf, min_samples_split, random_state):
    """Create a DecisionTreeClassifier with Gini impurity, no max depth."""
    return tree.DecisionTreeClassifier(
        criterion='gini',
        min_samples_leaf=min_samples_leaf,
        min_samples_split=min_samples_split,
        random_state=random_state
    )
