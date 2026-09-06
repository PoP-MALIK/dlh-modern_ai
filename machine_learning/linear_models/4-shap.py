#!/usr/bin/env python3
"""Generate SHAP explanations for a trained regression model."""
import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Build a SHAP explainer and compute SHAP values for X_test.

    Args:
        model: A trained regression model.
        X_train: Background data used to initialize the explainer.
        X_test: Data to explain.

    Returns:
        explainer: The SHAP explainer object.
        shap_values: SHAP values for X_test.
    """
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
