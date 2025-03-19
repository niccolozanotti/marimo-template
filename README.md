# Python project template with [marimo](https://marimo.io) notebooks + [uv](https://github.com/astral-sh/uv) package manager

> Customized inspired from [marimo-team/marimo-uv-starter-template](https://github.com/marimo-team/marimo-uv-starter-template) and [marimo-team/marimo-gh-pages-template](https://github.com/marimo-team/marimo-gh-pages-template)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A starter template for [marimo](https://marimo.io) notebooks using [uv](https://github.com/astral-sh/uv) for dependency and project management and with CI set up for notebooks deployement using marimo WebAssembly on GitHub pages. 

## Features

- 🚀 Python 3.12+ support
- 📦 Fast dependency management with `uv`
- 🎯 Code quality with Ruff (linting + formatting)
- 👷 CI/CD with GitHub Actions
- 📓 Interactive notebook development with marimo

## Prerequisites

- Python 3.12 or higher ( if not present in the system, `uv` can download it and [manage the installation](https://docs.astral.sh/uv/concepts/python-versions/#installing-a-python-version) )
- [uv](https://github.com/astral-sh/uv) installed

## Getting Started


1. Install the dependencies
```shell
uv pip install .
```
2. Run the marimo editor:

   ```bash
   uv run marimo edit
   ```

## Development

The development dependencies can be installed by running
```shell
uv pip install ".[dev]"
```

### Linting and formatting

```bash
uv run ruff check .
uv run ruff format .
```

## Project Structure

```
├── .github/
│   └── workflows/
│       ├── ci.yaml
│       └── deploy.yaml
├── notebooks/          # notebooks deployed as wasm-editable in the browser
│   └── notebook1.py
├── apps/               # notebooks deployed as apps
│   └── notebook1.py
├── src/
│   ├── __init__.py
│   ├── app.py
│   └── utils.py
├── scripts/
│   └── build.py        # helper for deployment
├── pyproject.toml
├── marimo.toml         # user config of marimo
├── ruff.toml
└── uv.lock
```

## License

This project is licensed under the MIT [License](./LICENSE).
