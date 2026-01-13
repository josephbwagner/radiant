# Radiant Server

Backend server for Radiant Meshtastic administration platform.

## Installation

```bash
pip install radiant-server
```

## Development

```bash
cd server
poetry install
poetry run pytest
```

## Running

```bash
poetry run uvicorn radiant_server.api.main:app --reload
```
