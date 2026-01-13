# Radiant Server

Backend server for Radiant Meshtastic administration platform.

## Features

- FastAPI-based REST API with WebSocket support
- PostgreSQL database for historical data
- Persistent monitoring service
- Alert system with multiple notification channels
- OpenAPI documentation

## Requirements

- Python 3.12+
- PostgreSQL 16+

## Installation

```bash
pip install radiant-server
```

## Development

### Setup

```bash
cd server
poetry install

# Install pre-commit hooks (from repository root)
pip install pre-commit
pre-commit install
```

### Running

```bash
poetry run uvicorn radiant_server.api.main:app --reload
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

- Python 3.12+
- FastAPI (web framework)
- SQLAlchemy (ORM)
- Alembic (database migrations)
- PostgreSQL (database)

### Testing

- Coverage: 55% minimum, 90% for new code
- CI: 3 OS × 2 Python versions (3.12-3.13)
