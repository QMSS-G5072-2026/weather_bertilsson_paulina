"""Tests for the weather_pmb2170 package."""

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from weather_pmb2170 import (
    celsius_to_fahrenheit,
    clean_readings,
    summarize_temperatures,
)

# =============================================================================
# UNIT TESTS
# =============================================================================


@pytest.mark.parametrize("celsius, expected", [
    (0, 32.0),           # freezing
    (100, 212.0),        # boiling
    (-40, -40.0),        # both scales meet
    (37, 98.6),          # body temperature
    (-273.15, -459.67),  # absolute zero is allowed
])
def test_celsius_to_fahrenheit(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)


@pytest.mark.parametrize("bad_input, expected_error", [
    ("hot", TypeError),       # string
    (None, TypeError),        # None
    (-273.16, ValueError),    # just below absolute zero
    (-1000, ValueError),      # far below absolute zero
])
def test_celsius_to_fahrenheit_invalid(bad_input, expected_error):
    with pytest.raises(expected_error):
        celsius_to_fahrenheit(bad_input)


def test_summarize_temperatures():
    readings = [10.0, float("nan"), 20.0]

    result = summarize_temperatures(readings)

    assert result["mean"] == pytest.approx(15.0)
    assert result["min"] == pytest.approx(10.0)
    assert result["max"] == pytest.approx(20.0)
    assert result["n_missing"] == 1


def test_summarize_temperatures_all_missing():
    """A list with no valid readings raises ValueError, as the docstring says."""
    with pytest.raises(ValueError):
        summarize_temperatures([float("nan"), float("nan")])


# =============================================================================
# FIXTURES
# =============================================================================


@pytest.fixture
def raw_readings():
    return pd.DataFrame({
        "station": ["JFK", "CPK", "JFK", "CPK", "LGA"],
        "date": ["2026-07-02", "2026-07-01", "2026-07-01", "2026-07-02", "2026-07-01"],
        "temp_c": [30.0, 25.0, float("nan"), 999.0, 28.0],
    })


def test_raw_readings_fixture(raw_readings):
    assert list(raw_readings.columns) == ["station", "date", "temp_c"]
    assert len(raw_readings) == 5
    assert raw_readings["temp_c"].isna().sum() == 1


# =============================================================================
# TESTING DATAFRAMES
# =============================================================================


def test_clean_readings(raw_readings):
    expected = pd.DataFrame({
        "station": ["CPK", "JFK", "LGA"],
        "date": ["2026-07-01", "2026-07-02", "2026-07-01"],
        "temp_c": [25.0, 30.0, 28.0],
        "temp_f": [77.0, 86.0, 82.4],
    })

    result = clean_readings(raw_readings)

    assert_frame_equal(result, expected)