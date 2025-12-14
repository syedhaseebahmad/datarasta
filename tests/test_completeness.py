"""Tests for completeness metrics."""

import pandas as pd
import numpy as np
import pytest
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


class TestCompleteness:
    def test_count_null(self):
        df = pd.DataFrame({"col": [1, 2, None, 4, None]})
        assert COUNT_NULL(df, "col") == 2

    def test_count_not_null(self):
        df = pd.DataFrame({"col": [1, 2, None, 4, None]})
        assert COUNT_NOT_NULL(df, "col") == 3

    def test_percent_null(self):
        df = pd.DataFrame({"col": [1, 2, None, 4, None]})
        assert PERCENT_NULL(df, "col") == 40.0

    def test_percent_not_null(self):
        df = pd.DataFrame({"col": [1, 2, None, 4, None]})
        assert PERCENT_NOT_NULL(df, "col") == 60.0

    def test_count_empty_string(self):
        df = pd.DataFrame({"col": ["hello", "", "world", "", "test"]})
        assert COUNT_EMPTY_STRING(df, "col") == 2

    def test_percent_empty_string(self):
        df = pd.DataFrame({"col": ["hello", "", "world", "", "test"]})
        assert PERCENT_EMPTY_STRING(df, "col") == 40.0

    def test_count_nan(self):
        df = pd.DataFrame({"col": [1.0, 2.0, np.nan, 4.0, np.nan]})
        assert COUNT_NAN(df, "col") == 2

    def test_percent_nan(self):
        df = pd.DataFrame({"col": [1.0, 2.0, np.nan, 4.0, np.nan]})
        assert PERCENT_NAN(df, "col") == 40.0

    def test_invalid_column(self):
        df = pd.DataFrame({"col": [1, 2, 3]})
        with pytest.raises(ValueError):
            COUNT_NULL(df, "nonexistent")

