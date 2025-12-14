"""
Basic usage example for DataRasta.

This example demonstrates how to use the library to compute various data quality metrics.
"""

import pandas as pd
from datetime import datetime, timedelta

# Import the main class and individual metrics
from datarasta import DataQualityMetrics
from datarasta import (
    COUNT_NULL,
    COUNT_DISTINCT,
    AVERAGE,
    MIN,
    MAX,
    PERCENT_NULL,
)


def main():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', None, 'Eve', 'Alice'],
        'age': [25, 30, None, 35, 40, 25],
        'score': [85.5, 92.0, 78.5, 88.0, 95.0, 85.5],
        'is_active': [True, False, True, True, False, True],
        'last_login': pd.date_range(
            start=datetime.now() - timedelta(days=10),
            periods=6,
            freq='D'
        )
    })

    print("Sample DataFrame:")
    print(df)
    print("\n" + "="*50 + "\n")

    # Method 1: Using the DataQualityMetrics class
    print("Method 1: Using DataQualityMetrics class")
    metrics = DataQualityMetrics(df)

    # Compute a single metric
    null_count = metrics.compute_metric('COUNT_NULL', column='name')
    print(f"Null count in 'name' column: {null_count}")

    # Compute percentile
    percentile_75 = metrics.compute_metric('PERCENTILE', column='score', percentile=75)
    print(f"75th percentile of 'score': {percentile_75}")

    # Compute all metrics for a column
    print("\nAll metrics for 'score' column:")
    score_metrics = metrics.compute_all_metrics(columns=['score'])
    for metric_name, value in score_metrics['score'].items():
        print(f"  {metric_name}: {value}")

    print("\n" + "="*50 + "\n")

    # Method 2: Using individual metric functions
    print("Method 2: Using individual metric functions")
    
    null_count = COUNT_NULL(df, 'name')
    print(f"Null count in 'name': {null_count}")

    distinct_count = COUNT_DISTINCT(df, 'name')
    print(f"Distinct values in 'name': {distinct_count}")

    percent_null = PERCENT_NULL(df, 'age')
    print(f"Percent null in 'age': {percent_null:.2f}%")

    avg_score = AVERAGE(df, 'score')
    print(f"Average score: {avg_score:.2f}")

    min_score = MIN(df, 'score')
    max_score = MAX(df, 'score')
    print(f"Score range: {min_score} - {max_score}")


if __name__ == "__main__":
    main()

