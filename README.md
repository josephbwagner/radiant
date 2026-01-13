# Radiant

**Professional administration platform for Meshtastic radio networks**

[![CI](https://github.com/josephbwagner/radiant/workflows/CI/badge.svg)](https://github.com/josephbwagner/radiant/actions)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Clean, succinct, professional administration tools for Meshtastic mesh networks. No emojis, enterprise-grade quality.

## Features

### CLI Tools (radiant-cli)
- Comprehensive device diagnostics with auto-fix recommendations
- Real-time network monitoring
- Device backup and configuration management
- Cross-platform support (Linux, macOS, Windows)
- Multiple output formats (table, JSON, YAML)

### Server Backend (radiant-server)
- FastAPI-based REST API with WebSocket support
- PostgreSQL database for historical data
- Background monitoring service
- Alert system with multiple notification channels
- OpenAPI documentation

### Web Dashboard (frontend)
- React 18 + TypeScript + Vite
- Real-time network monitoring
- Historical data visualization
- Node management and diagnostics
- Mobile-responsive design

## Quick Start

### CLI Only

```bash
pip install radiant-cli
radiant doctor  # Run diagnostics
radiant monitor # Monitor network
```

### Full Platform (Docker)

```bash
git clone https://github.com/josephbwagner/radiant.git
cd radiant/docker
docker-compose up
```

Access the web interface at `http://localhost:3000`

## Installation

### Requirements
- **CLI:** Python 3.9+
- **Server:** Python 3.12+
- **Frontend:** Node.js 20+
- **Database:** PostgreSQL 16+ (for server)

### CLI Package

```bash
pip install radiant-cli
```

### Server Package

```bash
pip install radiant-server
```

### From Source

```bash
git clone https://github.com/josephbwagner/radiant.git
cd radiant

# CLI
cd cli
poetry install
poetry run pytest

# Server
cd ../server
poetry install
poetry run pytest

# Frontend
cd ../frontend
npm install
npm run dev
```

## Development

### Setup

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Clone repository
git clone https://github.com/josephbwagner/radiant.git
cd radiant

# Install pre-commit hooks
pip install pre-commit
pre-commit install
```

### CLI Development

```bash
cd cli
poetry install
poetry run ruff check .
poetry run mypy src
poetry run pytest
```

### Server Development

```bash
cd server
poetry install
poetry run uvicorn radiant_server.api.main:app --reload
```

### Frontend Development

```bash
cd frontend
npm install
npm run dev
```

## Architecture

This project uses a monorepo structure:

```
radiant/
├── cli/          # Python CLI tools (3.9+)
├── server/       # FastAPI backend (3.12+)
├── frontend/     # React + TypeScript
├── docker/       # Multi-arch Docker configs
├── docs/         # Sphinx documentation
└── .github/      # CI/CD workflows
```

## Documentation

- [Full Documentation](https://josephbwagner.github.io/radiant/)
- [CLI Reference](docs/user/cli-reference.md)
- [API Documentation](https://josephbwagner.github.io/radiant/api/)
- [Contributing Guide](CONTRIBUTING.md)

## Technology Stack

- **CLI:** Python 3.9+, Click, Pydantic, Rich
- **Server:** Python 3.12+, FastAPI, SQLAlchemy, Alembic, PostgreSQL
- **Frontend:** React 18, TypeScript, Vite, Zustand, TanStack Query
- **Code Quality:** Ruff, MyPy, Pytest, pre-commit
- **CI/CD:** GitHub Actions, Codecov, Dependabot
- **Deployment:** Docker, Docker Compose, Multi-arch (AMD64 + ARM64)

## Testing

- **Coverage:** 55% minimum, 90% for new code
- **CLI Tests:** 3 OS × 5 Python versions (3.9-3.13)
- **Server Tests:** 3 OS × 2 Python versions (3.12-3.13)
- **Frontend Tests:** TypeScript type checking, ESLint, build validation

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Project Status

**Current Phase:** Phase 0 - Technology Setup Complete

Ready for Phase 1: CLI Foundation + Diagnostics implementation.

## Support

- [GitHub Issues](https://github.com/josephbwagner/radiant/issues)
- [Discussions](https://github.com/josephbwagner/radiant/discussions)

## Acknowledgments

- Built for the Meshtastic community
- Inspired by professional enterprise tooling practices
- Powered by modern Python and TypeScript ecosystems
