"""CLI command definitions."""

from __future__ import annotations

import click

from radiant import __version__


@click.group()
@click.version_option(version=__version__)
def cli() -> None:
    """Radiant - Professional administration platform for Meshtastic radio networks."""
    pass


@cli.command()
def doctor() -> None:
    """Run diagnostic checks on Meshtastic devices."""
    click.echo("Doctor command not yet implemented.")


@cli.command()
def monitor() -> None:
    """Monitor Meshtastic network in real-time."""
    click.echo("Monitor command not yet implemented.")


@cli.command()
def backup() -> None:
    """Backup Meshtastic device configuration."""
    click.echo("Backup command not yet implemented.")


@cli.group()
def config() -> None:
    """Manage Radiant configuration."""
    pass


@config.command()
def show() -> None:
    """Show current configuration."""
    click.echo("Config show command not yet implemented.")


@config.command()
def init() -> None:
    """Initialize default configuration."""
    click.echo("Config init command not yet implemented.")
