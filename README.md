# Radiant

## Offline-first software for Meshtastic hardware and networks

[![CI](https://github.com/josephbwagner/radiant/workflows/CI/badge.svg)](https://github.com/josephbwagner/radiant/actions)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## Features

### CLI Tools (radiant-cli)

- Cross-platform support (Linux, macOS, Windows via WSL)
- Device diagnostics with auto-fix recommendations
- Real-time network monitoring
- Device backup and configuration management
- Multiple output formats (table, JSON, YAML)

### Server Backend (radiant-server)

- FastAPI-based REST API with WebSocket support
- PostgreSQL database for historical data
- Persistent monitoring service
- Alert system with multiple notification channels
- OpenAPI documentation

### Web Dashboard (frontend)

- React 18 + TypeScript + Vite
- Real-time network monitoring dashboard
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

# See individual module READMEs for development setup:
# - cli/README.md
# - server/README.md
# - frontend/README.md
```

## Development

For development setup and guidelines, see the README in each module:

- [CLI Development](cli/README.md)
- [Server Development](server/README.md)
- [Frontend Development](frontend/README.md)

### Repository Setup

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

## Architecture

This project uses a monorepo structure:

```text
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
- [Development Blog](https://josephbwagner.github.io/radiant/blog.html)
- [CLI Reference](docs/user/cli-reference.md)
- [API Documentation](https://josephbwagner.github.io/radiant/api/)
- [Contributing Guide](CONTRIBUTING.md)

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
