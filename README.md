# DataRasta

A comprehensive Python library for data quality testing with a wide range of metrics for analyzing data completeness, uniqueness, distributions, validity, and freshness.

## Features

DataRasta provides a comprehensive set of data quality metrics organized into five main categories:

### 1. Freshness and Volume Metrics
- **FRESHNESS_DATA**: Measure data freshness (based on data, not metadata)
- **VOLUME_DATA**: Measure data volume (based on data, not metadata)
- **HOURS_SINCE_MAX_TIMESTAMP**: Hours since the maximum timestamp value
- **COUNT_ROWS**: Total number of rows in a table
- **COUNT_READ_QUERIES**: Number of SELECT queries (placeholder for database integration)

### 2. Uniqueness Metrics
- **COUNT_DISTINCT**: Count of distinct elements in a column
- **PERCENT_DISTINCT**: Percentage of distinct elements
- **COUNT_DUPLICATES**: Count of duplicate rows
- **PERCENT_DUPLICATES**: Percentage of duplicate rows

### 3. Completeness Metrics
- **COUNT_NULL**: Count of null values
- **COUNT_NOT_NULL**: Count of non-null values
- **PERCENT_NULL**: Percentage of null values
- **PERCENT_NOT_NULL**: Percentage of non-null values
- **COUNT_EMPTY_STRING**: Count of empty strings (STRING columns)
- **PERCENT_EMPTY_STRING**: Percentage of empty strings
- **COUNT_NAN**: Count of NaN values (NUMERIC columns)
- **PERCENT_NAN**: Percentage of NaN values

### 4. Distribution Metrics
- **MIN**: Minimum value (NUMERIC)
- **MAX**: Maximum value (NUMERIC)
- **AVERAGE**: Mean value (NUMERIC)
- **VARIANCE**: Statistical variance (NUMERIC)
- **SKEW**: Statistical skewness (NUMERIC)
- **KURTOSIS**: Excess kurtosis (NUMERIC)
- **GEOMETRIC_MEAN**: Geometric mean (NUMERIC)
- **HARMONIC_MEAN**: Harmonic mean (NUMERIC)
- **MEDIAN**: Median value (NUMERIC)
- **PERCENTILE**: Statistical percentile (NUMERIC)
- **SUM**: Sum of all values (NUMERIC)
- **COUNT_TRUE**: Count of True values (BOOLEAN)
- **COUNT_FALSE**: Count of False values (BOOLEAN)
- **PERCENT_TRUE**: Percentage of True values (BOOLEAN)
- **PERCENT_FALSE**: Percentage of False values (BOOLEAN)

### 5. Validity Metrics
- **STRING_LENGTH_MAX**: Maximum string length (STRING)
- **STRING_LENGTH_MIN**: Minimum string length (STRING)
- **STRING_LENGTH_AVERAGE**: Average string length (STRING)

## Installation

```bash
pip install datarasta
```

For development:

```bash
pip install -e ".[dev]"
```

## Quick Start

### Basic Usage

```python
import pandas as pd
from datarasta import DataQualityMetrics

# Create a sample DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', None, 'Eve'],
    'age': [25, 30, None, 35, 40],
    'score': [85.5, 92.0, 78.5, 88.0, 95.0],
    'is_active': [True, False, True, True, False]
})

# Initialize the metrics calculator
metrics = DataQualityMetrics(df)

# Compute a single metric
null_count = metrics.compute_metric('COUNT_NULL', column='name')
print(f"Null count: {null_count}")

# Compute multiple metrics at once
all_metrics = metrics.compute_all_metrics()
print(all_metrics)
```

### Using Individual Metrics

```python
import pandas as pd
from datarasta import (
    COUNT_NULL, PERCENT_NULL, COUNT_DISTINCT,
    AVERAGE, MIN, MAX, STRING_LENGTH_MAX
)

df = pd.DataFrame({
    'product': ['A', 'B', 'C', 'A', 'B'],
    'price': [10.5, 20.0, 15.5, 10.5, 25.0]
})

# Calculate specific metrics
null_count = COUNT_NULL(df, 'product')
distinct_count = COUNT_DISTINCT(df, 'product')
avg_price = AVERAGE(df, 'price')
min_price = MIN(df, 'price')
max_price = MAX(df, 'price')

print(f"Null count: {null_count}")
print(f"Distinct products: {distinct_count}")
print(f"Average price: {avg_price}")
print(f"Price range: {min_price} - {max_price}")
```

### Computing Percentiles

```python
import pandas as pd
from datarasta import DataQualityMetrics, PERCENTILE

df = pd.DataFrame({'values': range(1, 101)})  # 1 to 100

# Using the class interface
metrics = DataQualityMetrics(df)
percentile_90 = metrics.compute_metric('PERCENTILE', column='values', percentile=90)

# Using the function directly
percentile_75 = PERCENTILE(df, 'values', percentile=75)
```

### Timestamp Metrics

```python
import pandas as pd
from datetime import datetime, timedelta
from datarasta import HOURS_SINCE_MAX_TIMESTAMP

# Create DataFrame with timestamps
df = pd.DataFrame({
    'event_time': pd.date_range(
        start=datetime.now() - timedelta(days=5),
        periods=100,
        freq='H'
    )
})

# Calculate hours since latest timestamp
hours_since = HOURS_SINCE_MAX_TIMESTAMP(df, 'event_time')
print(f"Hours since latest event: {hours_since}")
```

## API Reference

### DataQualityMetrics Class

The main interface for computing data quality metrics.

#### Methods

- `compute_metric(metric_name, column=None, **kwargs)`: Compute a single metric
- `compute_all_metrics(columns=None)`: Compute all applicable metrics for specified columns

### Individual Metric Functions

All metrics are available as standalone functions that take a DataFrame and column name as arguments:

```python
metric_value = METRIC_NAME(df, column_name)
```

Some metrics accept additional parameters:
- `PERCENTILE(df, column, percentile=50.0)`: Specify the percentile (0-100 or 0.0-1.0)

## Requirements

- Python >= 3.7
- pandas >= 1.3.0
- numpy >= 1.20.0
- scipy >= 1.7.0

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black datarasta tests
```

### Type Checking

```bash
mypy datarasta
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This library is designed to provide comprehensive data quality metrics similar to those found in commercial data quality platforms, making them accessible as an open-source solution.

