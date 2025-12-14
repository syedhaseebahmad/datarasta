# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-XX

### Added
- Initial release of DataRasta
- Freshness and Volume metrics:
  - FRESHNESS_DATA
  - VOLUME_DATA
  - HOURS_SINCE_MAX_TIMESTAMP / HOURS_SINCE_MAX_DATE
  - COUNT_ROWS
  - COUNT_READ_QUERIES (placeholder)
- Uniqueness metrics:
  - COUNT_DISTINCT
  - PERCENT_DISTINCT
  - COUNT_DUPLICATES
  - PERCENT_DUPLICATES
- Completeness metrics:
  - COUNT_NULL / COUNT_NOT_NULL
  - PERCENT_NULL / PERCENT_NOT_NULL
  - COUNT_EMPTY_STRING / PERCENT_EMPTY_STRING
  - COUNT_NAN / PERCENT_NAN
- Distribution metrics:
  - MIN / MAX / AVERAGE / VARIANCE
  - SKEW / KURTOSIS
  - GEOMETRIC_MEAN / HARMONIC_MEAN
  - MEDIAN / PERCENTILE / SUM
  - COUNT_TRUE / COUNT_FALSE
  - PERCENT_TRUE / PERCENT_FALSE
- Validity metrics:
  - STRING_LENGTH_MAX / STRING_LENGTH_MIN / STRING_LENGTH_AVERAGE
- DataQualityMetrics class for easy metric computation
- Comprehensive documentation and examples

