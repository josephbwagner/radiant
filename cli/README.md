# Radiant CLI

Professional CLI tools for Meshtastic radio administration.

## Features

- Cross-platform support (Linux, macOS, Windows via WSL)
- Device diagnostics with auto-fix recommendations
- Real-time network monitoring
- Device backup and configuration management
- Multiple output formats (table, JSON, YAML)

## Requirements

- Python 3.9+

## Installation

```bash
pip install radiant-cli
```

## Quick Start

```bash
radiant doctor  # Run diagnostics
radiant monitor # Monitor network
```

## Development

### Setup

```bash
cd cli
poetry install

# Install pre-commit hooks (from repository root)
pip install pre-commit
pre-commit install
```

### Testing & Quality

```bash
# Run linter
poetry run ruff check .

# Run type checker
poetry run mypy src

# Run tests
poetry run pytest
```

### Technology Stack

- Python 3.9+
- Click (CLI framework)
- Pydantic (data validation)
- Rich (terminal formatting)

### Testing

- Coverage: 55% minimum, 90% for new code
- CI: 3 OS × 5 Python versions (3.9-3.13)
