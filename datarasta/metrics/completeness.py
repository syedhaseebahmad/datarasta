"""Completeness metrics for data quality testing."""

from typing import Optional
import pandas as pd
import numpy as np


def COUNT_NULL(df: pd.DataFrame, column: str) -> int:
    """
    Count the number of rows with null values in the column.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze
        
    Returns:
        Count of null values
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    return int(df[column].isna().sum())


def COUNT_NOT_NULL(df: pd.DataFrame, column: str) -> int:
    """
    Count the number of rows with non-null values in the column.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze
        
    Returns:
        Count of non-null values
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    return int(df[column].notna().sum())


def PERCENT_NULL(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the percentage of rows with null values in the column.
    
    This metric is suggested as a basic autometric on all column types.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze
        
    Returns:
        Percentage of null values (0-100)
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    total_rows = len(df)
    if total_rows == 0:
        return 0.0
    
    null_count = COUNT_NULL(df, column)
    percent = (null_count / total_rows) * 100.0
    
    return float(percent)


def PERCENT_NOT_NULL(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the percentage of rows with non-null values in the column.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze
        
    Returns:
        Percentage of non-null values (0-100)
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    total_rows = len(df)
    if total_rows == 0:
        return 0.0
    
    not_null_count = COUNT_NOT_NULL(df, column)
    percent = (not_null_count / total_rows) * 100.0
    
    return float(percent)


def COUNT_EMPTY_STRING(df: pd.DataFrame, column: str) -> int:
    """
    Count the number of rows with empty strings (0-length strings) in the column.
    
    Applicable to STRING columns only.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be string type)
        
    Returns:
        Count of empty strings
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    # Convert to string and check for empty strings
    # Filter out null values first, then check for empty strings
    non_null_mask = df[column].notna()
    empty_string_mask = df.loc[non_null_mask, column].astype(str) == ""
    
    return int(empty_string_mask.sum())


def PERCENT_EMPTY_STRING(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the percentage of rows with empty strings in the column.
    
    Applicable to STRING columns only.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be string type)
        
    Returns:
        Percentage of empty strings (0-100)
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    total_rows = len(df)
    if total_rows == 0:
        return 0.0
    
    empty_string_count = COUNT_EMPTY_STRING(df, column)
    percent = (empty_string_count / total_rows) * 100.0
    
    return float(percent)


def COUNT_NAN(df: pd.DataFrame, column: str) -> int:
    """
    Count the number of rows where the column value is NaN.
    
    This metric will only be available for source types where NaN is a 
    valid value for a column (typically NUMERIC columns).
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Count of NaN values
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    # Check if column is numeric
    if not pd.api.types.is_numeric_dtype(df[column]):
        # Return 0 for non-numeric columns as NaN is not applicable
        return 0
    
    return int(pd.isna(df[column]).sum())


def PERCENT_NAN(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the percentage of rows where the column value is NaN.
    
    This metric will only be available for source types where NaN is a 
    valid value for a column (typically NUMERIC columns).
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Percentage of NaN values (0-100)
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    total_rows = len(df)
    if total_rows == 0:
        return 0.0
    
    nan_count = COUNT_NAN(df, column)
    percent = (nan_count / total_rows) * 100.0
    
    return float(percent)

