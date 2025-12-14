"""Core data quality metrics interface."""

from typing import Any, Dict, Optional, Union
import pandas as pd
import numpy as np
from datetime import datetime

from datarasta.metrics.freshness import (
    FRESHNESS_DATA,
    VOLUME_DATA,
    HOURS_SINCE_MAX_TIMESTAMP,
    HOURS_SINCE_MAX_DATE,
    COUNT_ROWS,
)
from datarasta.metrics.uniqueness import (
    COUNT_DISTINCT,
    PERCENT_DISTINCT,
    COUNT_DUPLICATES,
    PERCENT_DUPLICATES,
)
from datarasta.metrics.completeness import (
    COUNT_NULL,
    COUNT_NOT_NULL,
    PERCENT_NULL,
    PERCENT_NOT_NULL,
    COUNT_EMPTY_STRING,
    PERCENT_EMPTY_STRING,
    COUNT_NAN,
    PERCENT_NAN,
)
from datarasta.metrics.distribution import (
    MIN,
    MAX,
    AVERAGE,
    VARIANCE,
    SKEW,
    KURTOSIS,
    GEOMETRIC_MEAN,
    HARMONIC_MEAN,
    MEDIAN,
    PERCENTILE,
    SUM,
    COUNT_TRUE,
    COUNT_FALSE,
    PERCENT_TRUE,
    PERCENT_FALSE,
)
from datarasta.metrics.validity import (
    STRING_LENGTH_MAX,
    STRING_LENGTH_MIN,
    STRING_LENGTH_AVERAGE,
)


class DataQualityMetrics:
    """Main interface for computing data quality metrics."""

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize with a pandas DataFrame.

        Args:
            dataframe: The pandas DataFrame to analyze.
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame")
        self.df = dataframe.copy()

    def compute_metric(
        self,
        metric_name: str,
        column: Optional[str] = None,
        **kwargs
    ) -> Union[float, int, Dict[str, Any]]:
        """
        Compute a data quality metric.

        Args:
            metric_name: Name of the metric to compute (e.g., 'COUNT_NULL', 'AVERAGE')
            column: Column name (required for column-specific metrics)
            **kwargs: Additional parameters for specific metrics (e.g., percentile for PERCENTILE)

        Returns:
            Metric value(s)

        Raises:
            ValueError: If metric name is invalid or required parameters are missing
        """
        metric_map = {
            # Freshness/Volume
            "FRESHNESS_DATA": lambda: FRESHNESS_DATA(self.df),
            "VOLUME_DATA": lambda: VOLUME_DATA(self.df),
            "HOURS_SINCE_MAX_TIMESTAMP": lambda: HOURS_SINCE_MAX_TIMESTAMP(
                self.df, column
            ),
            "HOURS_SINCE_MAX_DATE": lambda: HOURS_SINCE_MAX_DATE(self.df, column),
            "COUNT_ROWS": lambda: COUNT_ROWS(self.df),
            # Uniqueness
            "COUNT_DISTINCT": lambda: COUNT_DISTINCT(self.df, column),
            "PERCENT_DISTINCT": lambda: PERCENT_DISTINCT(self.df, column),
            "COUNT_DUPLICATES": lambda: COUNT_DUPLICATES(self.df, column),
            "PERCENT_DUPLICATES": lambda: PERCENT_DUPLICATES(self.df, column),
            # Completeness
            "COUNT_NULL": lambda: COUNT_NULL(self.df, column),
            "COUNT_NOT_NULL": lambda: COUNT_NOT_NULL(self.df, column),
            "PERCENT_NULL": lambda: PERCENT_NULL(self.df, column),
            "PERCENT_NOT_NULL": lambda: PERCENT_NOT_NULL(self.df, column),
            "COUNT_EMPTY_STRING": lambda: COUNT_EMPTY_STRING(self.df, column),
            "PERCENT_EMPTY_STRING": lambda: PERCENT_EMPTY_STRING(self.df, column),
            "COUNT_NAN": lambda: COUNT_NAN(self.df, column),
            "PERCENT_NAN": lambda: PERCENT_NAN(self.df, column),
            # Distribution
            "MIN": lambda: MIN(self.df, column),
            "MAX": lambda: MAX(self.df, column),
            "AVERAGE": lambda: AVERAGE(self.df, column),
            "VARIANCE": lambda: VARIANCE(self.df, column),
            "SKEW": lambda: SKEW(self.df, column),
            "KURTOSIS": lambda: KURTOSIS(self.df, column),
            "GEOMETRIC_MEAN": lambda: GEOMETRIC_MEAN(self.df, column),
            "HARMONIC_MEAN": lambda: HARMONIC_MEAN(self.df, column),
            "MEDIAN": lambda: MEDIAN(self.df, column),
            "PERCENTILE": lambda: PERCENTILE(
                self.df, column, kwargs.get("percentile", 50)
            ),
            "SUM": lambda: SUM(self.df, column),
            "COUNT_TRUE": lambda: COUNT_TRUE(self.df, column),
            "COUNT_FALSE": lambda: COUNT_FALSE(self.df, column),
            "PERCENT_TRUE": lambda: PERCENT_TRUE(self.df, column),
            "PERCENT_FALSE": lambda: PERCENT_FALSE(self.df, column),
            # Validity
            "STRING_LENGTH_MAX": lambda: STRING_LENGTH_MAX(self.df, column),
            "STRING_LENGTH_MIN": lambda: STRING_LENGTH_MIN(self.df, column),
            "STRING_LENGTH_AVERAGE": lambda: STRING_LENGTH_AVERAGE(self.df, column),
        }

        if metric_name not in metric_map:
            raise ValueError(f"Unknown metric: {metric_name}")

        return metric_map[metric_name]()

    def compute_all_metrics(
        self, columns: Optional[list] = None
    ) -> Dict[str, Dict[str, Any]]:
        """
        Compute all applicable metrics for specified columns.

        Args:
            columns: List of column names. If None, computes for all columns.

        Returns:
            Dictionary mapping column names to their computed metrics
        """
        if columns is None:
            columns = self.df.columns.tolist()

        results = {}
        for column in columns:
            results[column] = {}
            col_type = self._get_column_type(column)

            # Always compute row count once
            if column == columns[0]:
                results["_table_level"] = {"COUNT_ROWS": COUNT_ROWS(self.df)}

            # Completeness metrics (any column type)
            results[column]["COUNT_NULL"] = COUNT_NULL(self.df, column)
            results[column]["COUNT_NOT_NULL"] = COUNT_NOT_NULL(self.df, column)
            results[column]["PERCENT_NULL"] = PERCENT_NULL(self.df, column)
            results[column]["PERCENT_NOT_NULL"] = PERCENT_NOT_NULL(self.df, column)

            # Uniqueness metrics (any column type)
            results[column]["COUNT_DISTINCT"] = COUNT_DISTINCT(self.df, column)
            results[column]["PERCENT_DISTINCT"] = PERCENT_DISTINCT(self.df, column)
            results[column]["COUNT_DUPLICATES"] = COUNT_DUPLICATES(self.df, column)
            results[column]["PERCENT_DUPLICATES"] = PERCENT_DUPLICATES(self.df, column)

            # String-specific metrics
            if col_type == "STRING":
                results[column]["COUNT_EMPTY_STRING"] = COUNT_EMPTY_STRING(
                    self.df, column
                )
                results[column]["PERCENT_EMPTY_STRING"] = PERCENT_EMPTY_STRING(
                    self.df, column
                )
                results[column]["STRING_LENGTH_MAX"] = STRING_LENGTH_MAX(
                    self.df, column
                )
                results[column]["STRING_LENGTH_MIN"] = STRING_LENGTH_MIN(
                    self.df, column
                )
                results[column]["STRING_LENGTH_AVERAGE"] = STRING_LENGTH_AVERAGE(
                    self.df, column
                )

            # Numeric-specific metrics
            if col_type == "NUMERIC":
                results[column]["COUNT_NAN"] = COUNT_NAN(self.df, column)
                results[column]["PERCENT_NAN"] = PERCENT_NAN(self.df, column)
                results[column]["MIN"] = MIN(self.df, column)
                results[column]["MAX"] = MAX(self.df, column)
                results[column]["AVERAGE"] = AVERAGE(self.df, column)
                results[column]["VARIANCE"] = VARIANCE(self.df, column)
                results[column]["SKEW"] = SKEW(self.df, column)
                results[column]["KURTOSIS"] = KURTOSIS(self.df, column)
                results[column]["GEOMETRIC_MEAN"] = GEOMETRIC_MEAN(self.df, column)
                results[column]["HARMONIC_MEAN"] = HARMONIC_MEAN(self.df, column)
                results[column]["MEDIAN"] = MEDIAN(self.df, column)
                results[column]["SUM"] = SUM(self.df, column)

            # Boolean-specific metrics
            if col_type == "BOOLEAN":
                results[column]["COUNT_TRUE"] = COUNT_TRUE(self.df, column)
                results[column]["COUNT_FALSE"] = COUNT_FALSE(self.df, column)
                results[column]["PERCENT_TRUE"] = PERCENT_TRUE(self.df, column)
                results[column]["PERCENT_FALSE"] = PERCENT_FALSE(self.df, column)

            # Date/Timestamp-specific metrics
            if col_type in ["DATE_LIKE", "TIMESTAMP_LIKE"]:
                results[column]["HOURS_SINCE_MAX_TIMESTAMP"] = (
                    HOURS_SINCE_MAX_TIMESTAMP(self.df, column)
                )
                results[column]["HOURS_SINCE_MAX_DATE"] = HOURS_SINCE_MAX_DATE(
                    self.df, column
                )

        return results

    def _get_column_type(self, column: str) -> str:
        """Determine the type of a column for metric applicability."""
        dtype = self.df[column].dtype

        if pd.api.types.is_datetime64_any_dtype(dtype):
            return "TIMESTAMP_LIKE"
        elif pd.api.types.is_bool_dtype(dtype):
            return "BOOLEAN"
        elif pd.api.types.is_numeric_dtype(dtype):
            return "NUMERIC"
        elif pd.api.types.is_string_dtype(dtype) or dtype == "object":
            # Check if it's actually datetime strings
            try:
                pd.to_datetime(self.df[column].dropna().iloc[0])
                return "DATE_LIKE"
            except (ValueError, IndexError, TypeError):
                return "STRING"
        else:
            return "STRING"  # Default to string

