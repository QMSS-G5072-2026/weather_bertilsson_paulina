# weather_pmb2170

[![ci-cd](https://github.com/QMSS-G5072-2026/weather_bertilsson_paulina/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/QMSS-G5072-2026/weather_bertilsson_paulina/actions/workflows/ci-cd.yml)

weather data cleaning and processing

## Installation

```bash
$ uv add weather_pmb2170
```

or, without uv, `pip install weather_pmb2170`.

## Development

```bash
$ uv sync                       # create .venv and install the package with its dev and docs groups
$ uv run pytest                 # run the tests
$ uv run make html -C docs      # build the documentation
$ uv build                      # build the sdist and wheel into dist/
```

## Usage
# python import pmb2170_weather
# weather celsius to farenheit 68.0

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`weather_pmb2170` was created by Paulina Bertilsson. It is licensed under the terms of the MIT license.

## Credits

`weather_pmb2170` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `qmss-pkgs-cookiecutter` [template](https://github.com/QMSS-G5072-2026/qmss-pkgs-cookiecutter), a uv-based fork of [`py-pkgs-cookiecutter`](https://github.com/py-pkgs/py-pkgs-cookiecutter).
