# Contributing to Radiant

Thank you for your interest in contributing to Radiant! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be professional, respectful, and constructive in all interactions.

## Development Setup

### Prerequisites

- Python 3.9+ (for CLI) or Python 3.12+ (for server)
- Poetry 2.2.1+
- Node.js 20+ (for frontend)
- Git

### Initial Setup

```bash
# Clone the repository
git clone https://github.com/josephbwagner/radiant.git
cd radiant

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Set up CLI package
cd cli
poetry install
cd ..

# Set up server package
cd server
poetry install
cd ..

# Set up frontend
cd frontend
npm install
cd ..
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

Follow the code style guidelines below.

### 3. Run Tests

```bash
# CLI tests
cd cli
poetry run pytest
poetry run ruff check .
poetry run mypy src

# Server tests
cd server
poetry run pytest
poetry run ruff check .
poetry run mypy src

# Frontend tests
cd frontend
npm run type-check
npm run lint
npm run build
```

### 4. Commit Changes

Use conventional commits:

```bash
git commit -m "feat: add diagnostic feature"
git commit -m "fix: resolve connection issue"
git commit -m "docs: update CLI reference"
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## Code Style Guidelines

### Python

- Use Ruff for linting and formatting (configured in pyproject.toml)
- Follow PEP 8 style guide
- Use type hints for all functions
- Write docstrings in Google style
- Line length: 88 characters
- Use modern Python syntax with `from __future__ import annotations`

Example:

```python
from __future__ import annotations

def diagnose_device(device_path: str, timeout: int = 30) -> DiagnosticReport:
    """Run diagnostic checks on a Meshtastic device.

    Args:
        device_path: Path to the device (e.g., /dev/ttyACM0)
        timeout: Maximum time to wait for device response in seconds

    Returns:
        DiagnosticReport containing all check results and recommendations

    Raises:
        DeviceNotFoundError: If device path does not exist
    """
    pass
```

### TypeScript

- Use TypeScript strict mode
- Follow ESLint rules (configured in eslint.config.js)
- Use functional components with hooks
- Prefer named exports over default exports

### Testing

- Write tests for all new features
- Aim for 90% coverage on new code
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)

Example:

```python
def test_diagnose_device_success() -> None:
    """Test successful device diagnostic."""
    # Arrange
    device_path = "/dev/ttyACM0"

    # Act
    result = diagnose_device(device_path)

    # Assert
    assert result.status == DiagnosticStatus.PASS
```

## Pull Request Process

1. Ensure all tests pass and coverage meets requirements
2. Update documentation if needed
3. Add entry to CHANGELOG.md (if applicable)
4. Request review from maintainers
5. Address review feedback
6. Maintainer will merge once approved

## Testing Requirements

- All tests must pass in CI
- Minimum 55% project coverage
- 90% coverage for new code (patch)
- No type errors from MyPy
- No linting errors from Ruff

## Documentation

- Update relevant documentation for new features
- Add docstrings to all public functions and classes
- Update README.md if user-facing changes
- Add examples for new CLI commands

## Release Process

Releases are automated using semantic versioning based on conventional commits:

- `feat:` → minor version bump (0.X.0)
- `fix:` → patch version bump (0.0.X)
- `BREAKING CHANGE:` → major version bump (X.0.0)

## Questions?

- Open an issue for bugs or feature requests
- Start a discussion for questions or ideas
- Contact maintainers directly for sensitive issues

## License

By contributing, you agree that your contributions will be licensed under the GPL v3 License.
