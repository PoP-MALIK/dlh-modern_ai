#!/usr/bin/env python3
"""Plot correlation heatmap of numeric features."""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """Annotated heatmap of pairwise correlations."""
    plt.figure(figsize=(6, 5))

    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)

    plt.show()
