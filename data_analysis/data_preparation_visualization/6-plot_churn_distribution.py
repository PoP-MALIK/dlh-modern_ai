#!/usr/bin/env python3
"""Visualize the churn class distribution."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Bar plot of Churn value counts with skyblue/salmon colors."""
    plt.figure(figsize=(12, 8))

    counts = df['Churn'].value_counts()
    counts.plot(kind='bar', color=['skyblue', 'salmon'])

    plt.show()
