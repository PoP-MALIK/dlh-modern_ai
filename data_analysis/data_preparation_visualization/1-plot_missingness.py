#!/usr/bin/env python3
"""Visualize missing values in a pandas DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Scatter-plot missing values as vertical bars per column."""
    plt.figure(figsize=(12, 8))

    for col_idx, col in enumerate(df.columns):
        missing = df[col].isnull()
        rows = np.where(missing)[0]
        plt.scatter(rows, [col_idx] * len(rows), marker='|', s=100)

    plt.yticks(range(len(df.columns)), df.columns)
    plt.xlabel('Row index')
    plt.ylabel('Column')

    plt.tight_layout()
    plt.show()
