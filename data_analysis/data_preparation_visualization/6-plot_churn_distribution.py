#!/usr/bin/env python3
"""Visualize the churn class distribution."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Bar plot of Churn value counts with skyblue/salmon colors."""
    plt.figure(figsize=(12, 8))

    counts = df['Churn'].value_counts()
    colors = ['skyblue' if label == 'No' else 'salmon' for label in counts.index]

    plt.bar(counts.index, counts.values, color=colors)
    plt.xlabel('Churn')
    plt.ylabel('Count')
    plt.title('Churn Distribution')

    plt.tight_layout()
    plt.show()
