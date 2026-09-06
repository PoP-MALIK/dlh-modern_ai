#!/usr/bin/env python3
"""Compute feature importances from a trained random forest."""
import numpy as np


def feature_importance(rf):
    """Return feature importances and their sort order (ascending).

    Args:
        rf: A trained RandomForestClassifier instance.

    Returns:
        importances: Array of feature importance scores.
        indices: Array of feature indices, least to most important.
    """
    importances = rf.feature_importances_
    indices = np.argsort(importances)
    return importances, indices
