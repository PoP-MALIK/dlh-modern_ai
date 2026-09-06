#!/usr/bin/env python3
"""Evaluate classifier performance with a classification report."""
from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    """Return a classification report string (precision/recall/F1)."""
    return metrics.classification_report(true_labels, predicted_labels,
                                          target_names=class_names)
