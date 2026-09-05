#!/usr/bin/env python3
"""Visualize the churn class distribution."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Bar plot of Churn value counts with skyblue/salmon colors."""
    plt.figure(figsize=(12, 8))

    counts = df['Churn'].value_counts()
    color_map = {'No': 'skyblue', 'Yes': 'salmon'}
    colors = [color_map[label] for label in counts.index]
    plt.bar(counts.index, counts.values, color=colors)

    plt.show()
