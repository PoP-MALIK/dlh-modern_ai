#!/usr/bin/env python3
"""Handle missing values in the TotalCharges column."""
import pandas as pd


def clean_total_charges(df, method='drop'):
    """Clean TotalCharges by dropping, filling with median, or imputing."""
    if method == 'drop':
        return df.dropna(subset=['TotalCharges'])
    elif method == 'median':
        df = df.copy()
        median = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median)
        return df
    elif method == 'impute':
        df = df.copy()
        imputed = df['MonthlyCharges'] * df['tenure']
        df['TotalCharges'] = df['TotalCharges'].fillna(imputed)
        return df
