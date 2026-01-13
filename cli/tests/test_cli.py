"""Test CLI commands."""

from __future__ import annotations

from click.testing import CliRunner

from radiant.cli.main import cli


def test_cli_version() -> None:
    """Test that the CLI returns version information."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0


def test_doctor_command() -> None:
    """Test doctor command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["doctor"])
    assert result.exit_code == 0
    assert "not yet implemented" in result.output


def test_monitor_command() -> None:
    """Test monitor command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["monitor"])
    assert result.exit_code == 0


def test_backup_command() -> None:
    """Test backup command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["backup"])
    assert result.exit_code == 0
