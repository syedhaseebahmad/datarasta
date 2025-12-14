"""
DataRasta - A Python library for data quality testing.

This library provides comprehensive data quality metrics including:
- Freshness and Volume metrics
- Uniqueness metrics
- Completeness metrics
- Distribution metrics
- Validity metrics
"""

__version__ = "0.1.0"
__author__ = "DataRasta Contributors"

from datarasta.metrics import DataQualityMetrics
from datarasta.metrics.freshness import (
    FRESHNESS_DATA,
    VOLUME_DATA,
    HOURS_SINCE_MAX_TIMESTAMP,
    HOURS_SINCE_MAX_DATE,
    COUNT_ROWS,
    COUNT_READ_QUERIES,
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

__all__ = [
    "DataQualityMetrics",
    # Freshness/Volume
    "FRESHNESS_DATA",
    "VOLUME_DATA",
    "HOURS_SINCE_MAX_TIMESTAMP",
    "HOURS_SINCE_MAX_DATE",
    "COUNT_ROWS",
    "COUNT_READ_QUERIES",
    # Uniqueness
    "COUNT_DISTINCT",
    "PERCENT_DISTINCT",
    "COUNT_DUPLICATES",
    "PERCENT_DUPLICATES",
    # Completeness
    "COUNT_NULL",
    "COUNT_NOT_NULL",
    "PERCENT_NULL",
    "PERCENT_NOT_NULL",
    "COUNT_EMPTY_STRING",
    "PERCENT_EMPTY_STRING",
    "COUNT_NAN",
    "PERCENT_NAN",
    # Distribution
    "MIN",
    "MAX",
    "AVERAGE",
    "VARIANCE",
    "SKEW",
    "KURTOSIS",
    "GEOMETRIC_MEAN",
    "HARMONIC_MEAN",
    "MEDIAN",
    "PERCENTILE",
    "SUM",
    "COUNT_TRUE",
    "COUNT_FALSE",
    "PERCENT_TRUE",
    "PERCENT_FALSE",
    # Validity
    "STRING_LENGTH_MAX",
    "STRING_LENGTH_MIN",
    "STRING_LENGTH_AVERAGE",
]

