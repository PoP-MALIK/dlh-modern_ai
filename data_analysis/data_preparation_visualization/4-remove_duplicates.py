#!/usr/bin/env python3
"""Remove duplicate rows from a DataFrame."""


def remove_duplicates(df):
    """Return the DataFrame with duplicate rows removed."""
    return df.drop_duplicates()
