#!/usr/bin/env python3
"""Visualize missing values in a pandas DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Scatter-plot missing values as vertical bars per column."""
    plt.figure(figsize=(12, 8))

    for col_idx, col in enumerate(df.columns):
        rows = np.where(df[col].isnull())[0]
        plt.scatter(rows, [col_idx] * len(rows), marker='|')

    plt.yticks(range(len(df.columns)), df.columns)

    plt.tight_layout()
    plt.show()
