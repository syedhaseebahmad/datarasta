"""Distribution metrics for data quality testing."""

from typing import Optional
import pandas as pd
import numpy as np
from scipy import stats


def MIN(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the minimum value of the column.
    
    It is suggested as a basic autometric for all numeric columns.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Minimum value, or None if column is empty or non-numeric
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    min_val = df[column].min()
    if pd.isna(min_val):
        return None
    
    return float(min_val)


def MAX(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the maximum value of the column.
    
    It is suggested as a basic autometric for all numeric columns.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Maximum value, or None if column is empty or non-numeric
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    max_val = df[column].max()
    if pd.isna(max_val):
        return None
    
    return float(max_val)


def AVERAGE(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the mean value of the column.
    
    It is always suggested as a basic autometric for numeric columns, 
    except for ID columns.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Mean value, or None if column is empty or non-numeric
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    mean_val = df[column].mean()
    if pd.isna(mean_val):
        return None
    
    return float(mean_val)


def VARIANCE(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the statistical variance of the column.
    
    The variance is used to track the spread of numbers beyond the average. 
    It is always suggested as a basic autometric for numeric columns, 
    except for ID columns.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Variance value, or None if column is empty or non-numeric
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    var_val = df[column].var()
    if pd.isna(var_val):
        return None
    
    return float(var_val)


def SKEW(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the statistical skew of the column.
    
    The skew is used to determine how evenly the values are distributed 
    about the mean. A negative skew means that there is a larger tail 
    below the mean, while a positive skew indicates a larger tail above 
    the mean.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Skewness value, or None if column is empty or non-numeric
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    # Remove NaN values for skew calculation
    values = df[column].dropna()
    if len(values) < 3:  # Need at least 3 values for meaningful skew
        return None
    
    skew_val = stats.skew(values)
    if pd.isna(skew_val):
        return None
    
    return float(skew_val)


def KURTOSIS(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the statistical kurtosis of the column.
    
    The kurtosis determines how much of a tail datasets have. The value 
    displayed is actually the excess kurtosis, where 3 is subtracted from 
    the kurtosis value, so a normal distribution would end up with a 
    metric value of 0.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Excess kurtosis value, or None if column is empty or non-numeric
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    # Remove NaN values for kurtosis calculation
    values = df[column].dropna()
    if len(values) < 4:  # Need at least 4 values for meaningful kurtosis
        return None
    
    # scipy.stats.kurtosis already returns excess kurtosis (subtracts 3)
    kurt_val = stats.kurtosis(values, fisher=True)
    if pd.isna(kurt_val):
        return None
    
    return float(kurt_val)


def GEOMETRIC_MEAN(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the geometric mean of the column.
    
    The geometric mean is the nth root of the product of n values.
    Only applicable to positive numeric values.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Geometric mean, or None if column is empty, non-numeric, or contains non-positive values
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    # Remove NaN values
    values = df[column].dropna()
    if len(values) == 0:
        return None
    
    # Geometric mean only works with positive values
    if (values <= 0).any():
        return None
    
    # Calculate geometric mean: (product)^(1/n)
    geometric_mean = np.exp(np.log(values).mean())
    
    if pd.isna(geometric_mean):
        return None
    
    return float(geometric_mean)


def HARMONIC_MEAN(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the harmonic mean of the column.
    
    The harmonic mean is the reciprocal of the arithmetic mean of reciprocals.
    Only applicable to positive numeric values.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Harmonic mean, or None if column is empty, non-numeric, or contains non-positive values
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    # Remove NaN values
    values = df[column].dropna()
    if len(values) == 0:
        return None
    
    # Harmonic mean only works with positive values
    if (values <= 0).any():
        return None
    
    # Calculate harmonic mean: n / sum(1/x)
    harmonic_mean = stats.hmean(values)
    
    if pd.isna(harmonic_mean):
        return None
    
    return float(harmonic_mean)


def MEDIAN(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the median of the column.
    
    The median is computed as the 50th percentile, and will only return 
    a value that is in the dataset.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Median value, or None if column is empty or non-numeric
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    median_val = df[column].median()
    if pd.isna(median_val):
        return None
    
    return float(median_val)


def PERCENTILE(df: pd.DataFrame, column: str, percentile: float = 50.0) -> Optional[float]:
    """
    Calculate the statistical percentile of the column.
    
    This metric takes a parameter to determine what percentile should be used. 
    Values less than one as well as less than 100 are accepted, where a 90th 
    percentile can be expressed as either 0.9 or 90.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        percentile: Percentile value (0-100 or 0.0-1.0)
        
    Returns:
        Percentile value, or None if column is empty or non-numeric
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    # Normalize percentile to 0-1 range if it's 0-100
    if percentile > 1.0:
        percentile = percentile / 100.0
    
    if not (0.0 <= percentile <= 1.0):
        raise ValueError(f"Percentile must be between 0 and 100 (or 0.0 and 1.0), got {percentile}")
    
    percentile_val = df[column].quantile(percentile)
    if pd.isna(percentile_val):
        return None
    
    return float(percentile_val)


def SUM(df: pd.DataFrame, column: str) -> Optional[float]:
    """
    Calculate the sum of all values in the column.
    
    It is always suggested as a basic autometric for numeric columns, 
    except for ID columns.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be numeric type)
        
    Returns:
        Sum of all values, or None if column is empty or non-numeric
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return None
    
    sum_val = df[column].sum()
    if pd.isna(sum_val):
        return None
    
    return float(sum_val)


def COUNT_TRUE(df: pd.DataFrame, column: str) -> int:
    """
    Count the number of rows where the column contains the boolean value of True.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be boolean type)
        
    Returns:
        Count of True values
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    # Convert to boolean if needed, handling various boolean representations
    bool_series = df[column].astype(bool)
    true_count = int((bool_series == True).sum())
    
    return true_count


def COUNT_FALSE(df: pd.DataFrame, column: str) -> int:
    """
    Count the number of rows where the column contains the boolean value of False.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be boolean type)
        
    Returns:
        Count of False values
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    # Convert to boolean if needed, handling various boolean representations
    bool_series = df[column].astype(bool)
    false_count = int((bool_series == False).sum())
    
    return false_count


def PERCENT_TRUE(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the percentage of rows where the column contains the boolean value of True.
    
    It is suggested as a basic autometric on all boolean columns.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be boolean type)
        
    Returns:
        Percentage of True values (0-100)
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    total_rows = len(df)
    if total_rows == 0:
        return 0.0
    
    true_count = COUNT_TRUE(df, column)
    percent = (true_count / total_rows) * 100.0
    
    return float(percent)


def PERCENT_FALSE(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the percentage of rows where the column contains the boolean value of False.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze (should be boolean type)
        
    Returns:
        Percentage of False values (0-100)
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    total_rows = len(df)
    if total_rows == 0:
        return 0.0
    
    false_count = COUNT_FALSE(df, column)
    percent = (false_count / total_rows) * 100.0
    
    return float(percent)

