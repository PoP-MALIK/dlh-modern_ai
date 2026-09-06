#!/usr/bin/env python3
"""Return an untrained boosting classifier by name."""
from sklearn import ensemble
import xgboost as xgb
import lightgbm as lgb


def compare_boosting_classifiers(name, n_estimators, random_state):
    """Build an untrained boosting classifier matching name.

    Args:
        name: One of 'adaboost', 'gradientboosting', 'xgboost', 'lightgbm'.
        n_estimators: Number of boosting iterations.
        random_state: Seed for reproducibility.

    Returns:
        An untrained instance of the selected boosting classifier.
    """
    if name == 'adaboost':
        return ensemble.AdaBoostClassifier(n_estimators=n_estimators,
                                            random_state=random_state)
    elif name == 'gradientboosting':
        return ensemble.GradientBoostingClassifier(
            n_estimators=n_estimators, random_state=random_state)
    elif name == 'xgboost':
        return xgb.XGBClassifier(n_estimators=n_estimators,
                                  random_state=random_state)
    elif name == 'lightgbm':
        return lgb.LGBMClassifier(n_estimators=n_estimators,
                                   random_state=random_state, verbose=-1)
    else:
        raise ValueError(f"Unknown model name '{name}'")
