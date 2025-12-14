"""Validity metrics for data quality testing."""

from typing import Optional
import pandas as pd
import numpy as np


def STRING_LENGTH_MAX(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the maximum string length in the column.
    
    Not valid for Oracle source type. It is suggested as a basic autometric 
    for all string columns.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be string type)
        
    Returns:
        Maximum string length, or None if column is empty
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    # Convert to string and calculate lengths (excluding NaN)
    non_null_mask = df[column].notna()
    if not non_null_mask.any():
        return None
    
    string_lengths = df.loc[non_null_mask, column].astype(str).str.len()
    max_length = string_lengths.max()
    
    if pd.isna(max_length):
        return None
    
    return float(max_length)


def STRING_LENGTH_MIN(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the minimum string length in the column.
    
    Not valid for Oracle source type. It is suggested as a basic autometric 
    for all string columns.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be string type)
        
    Returns:
        Minimum string length, or None if column is empty
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    # Convert to string and calculate lengths (excluding NaN)
    non_null_mask = df[column].notna()
    if not non_null_mask.any():
        return None
    
    string_lengths = df.loc[non_null_mask, column].astype(str).str.len()
    min_length = string_lengths.min()
    
    if pd.isna(min_length):
        return None
    
    return float(min_length)


def STRING_LENGTH_AVERAGE(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the average string length in the column.
    
    Not valid for Oracle source type. It is suggested as a basic autometric 
    for all string columns.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be string type)
        
    Returns:
        Average string length, or None if column is empty
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    # Convert to string and calculate lengths (excluding NaN)
    non_null_mask = df[column].notna()
    if not non_null_mask.any():
        return None
    
    string_lengths = df.loc[non_null_mask, column].astype(str).str.len()
    avg_length = string_lengths.mean()
    
    if pd.isna(avg_length):
        return None
    
    return float(avg_length)

