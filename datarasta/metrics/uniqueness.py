"""Uniqueness metrics for data quality testing."""

from typing import Optional
import pandas as pd
import numpy as np


def COUNT_DISTINCT(df: pd.DataFrame, column: str) -> int:
    """
    Count the number of distinct elements in the column.
    
    This metric should be used when you expect a fixed number of value options.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze
        
    Returns:
        Count of distinct values
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    return int(df[column].nunique())


def PERCENT_DISTINCT(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the percentage of distinct elements in the column.
    
    This metric should be used when you expect a fixed number of value options.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze
        
    Returns:
        Percentage of distinct values (0-100)
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    total_rows = len(df)
    if total_rows == 0:
        return 0.0
    
    distinct_count = df[column].nunique()
    percent = (distinct_count / total_rows) * 100.0
    
    return float(percent)


def COUNT_DUPLICATES(df: pd.DataFrame, column: str) -> int:
    """
    Count the number of rows with duplicate values in the column.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze
        
    Returns:
        Count of duplicate rows (rows with same value as another row)
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    # Count rows that have duplicate values
    duplicated = df[column].duplicated(keep=False)
    duplicate_count = int(duplicated.sum())
    
    return duplicate_count


def PERCENT_DUPLICATES(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the percentage of rows with duplicate values in the column.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze
        
    Returns:
        Percentage of duplicate rows (0-100)
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    total_rows = len(df)
    if total_rows == 0:
        return 0.0
    
    duplicate_count = COUNT_DUPLICATES(df, column)
    percent = (duplicate_count / total_rows) * 100.0
    
    return float(percent)

