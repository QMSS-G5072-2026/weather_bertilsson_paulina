# read version from installed package
from importlib.metadata import version

__version__ = version("weather_pmb2170")

from .weather_pmb2170 import (  # noqa: E402
    celsius_to_fahrenheit,
    clean_readings,
    summarize_temperatures,
)
