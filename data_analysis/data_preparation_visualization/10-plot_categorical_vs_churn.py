#!/usr/bin/env python3
"""Plot churn rate per category of a categorical column."""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """Bar plot of churn rate (Yes proportion) per category."""
    plt.figure(figsize=(12, 8))

    rates = df.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').mean())
    plt.bar(rates.index, rates.values)

    plt.title(f"Churn Rate by {col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)
    plt.show()
