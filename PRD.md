# Release Automation PRD

## Purpose
Establish semantic versioning and automated releases for Radiant (CLI and Server) using conventional commits via `commitizen`, `python-semantic-release`, and GitHub Actions.

## Goals
- Consistent semantic versioning driven by conventional commits using `commitizen`.
- Automated changelog, tagging, and GitHub releases for CLI and Server.
- Minimal developer friction with clear local commands and VS Code task affordances.

## Non-Goals
- Publishing to PyPI (for now).
- Changing repo structure beyond required config files.
- Altering feature scope or runtime architecture.

## Scope
- Tooling: python-semantic-release, commitizen (cz), existing CI/release workflow.
- Documentation: CONTRIBUTING.md additions (developer workflow, commands, changelog policy).
- Optional helper scripts to validate release setup locally.

## Stakeholders
- Maintainers/developers shipping releases.
- CI/CD consumers (GitHub Actions).
- End users consuming tagged releases and changelog.

## Success Criteria
- Releases are cut via workflow with correct version bumps per commits.
- CHANGELOG.md updates automatically per release.
- Tags use cli-vX.Y.Z and server-vX.Y.Z without manual correction.
- Developers can preview next version locally and craft compliant commits easily.

## Constraints / Assumptions
- Conventional commits are followed (Angular style).
- GitHub Actions CI remains green prior to release job.
- GITHUB_TOKEN available for tagging and releases; no PyPI token required.

## Release Automation Tasks
- [ ] Enforce conventional commits in workflow and docs
  - Document `poetry run cz commit` as the recommended path.
- [ ] Add VS Code task alias for conventional commits.
- [ ] Version source of truth per package
  - Keep `pyproject.toml` and `__version__` in `src/radiant/__init__.py` and `src/radiant_server/__init__.py` synced via semantic-release config.
  - Maintain distinct tag formats: `cli-v{version}`, `server-v{version}`.
- [ ] Changelog policy
  - Single root `CHANGELOG.md` updated by semantic-release per release.
- [ ] Release workflow hardening
  - Keep `.github/workflows/release.yml` invoking CI then running semantic-release in `cli/` and `server/`.
  - Ensure CI success is a gate; fetch-depth=0 already set.
- [ ] Local validation commands
  - Document quick checks: `poetry run semantic-release version --print`, `poetry run cz commit`, `poetry run cz changelog`, `poetry build`.
- [ ] Tag seeding and baselines
  - If needed, seed initial `cli-v0.0.1` and `server-v0.0.1` tags to anchor history.
- [ ] Secrets and tokens
  - Confirm `GITHUB_TOKEN` scope is sufficient for tagging and releases; PyPI remains out of scope.
- [ ] Documentation update
  - Add a concise "Release Automation" section to CONTRIBUTING.md (workflow, commands, expectations, troubleshooting pointers).
- [ ] Optional helper script
  - `scripts/test-release.sh` to check last tag, commits since tag, and run `semantic-release version --print` for diagnostics if this cannot be achieved via VS Code Task.

## Risks / Mitigations
- Non-conventional commits block version bumps → mitigate with cz guidance and CI linting option.
- Tag collisions if formats change → document tag scheme and avoid retroactive edits.
- First-release edge cases (no tags) → seed baseline tags if needed before enabling automation.

## Milestones
1) Document developer workflow and commands (CONTRIBUTING).
2) Validate release workflow end-to-end on a dry run (version --print) and/or seeded tags.
3) Enable/confirm release workflow on main with a test conventional commit and observed changelog/tag.
