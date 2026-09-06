#!/usr/bin/env python3
"""Print the textual structure of a trained decision tree."""
from sklearn import tree


def draw(clf, feature_names, class_names):
    """Print a readable text representation of the tree's decision rules."""
    print(tree.export_text(clf, feature_names=feature_names,
                            class_names=class_names))
