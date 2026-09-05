#!/usr/bin/env python3
"""Drop the customerID column from a DataFrame."""


def drop_customerID(df):
    """Return the DataFrame with the customerID column removed."""
    return df.drop('customerID', axis=1)
