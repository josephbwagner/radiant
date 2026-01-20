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

### Completed
- [x] Document conventional commits and recommend `poetry run cz commit`.
- [x] Add VS Code task alias for conventional commits.
- [x] Document local validation commands (`semantic-release version --print`, `cz commit`, `cz changelog`, `poetry build`).
- [x] Add helper script `scripts/test-release.sh` for tag/next-version diagnostics.
- [x] Add CONTRIBUTING "Release Automation" section covering workflow, commands, expectations.
- [x] Switch semantic-release commit parser to `conventional` in cli/ and server/.
- [x] Make release helper run from repo root to avoid semantic-release repo-dir warning.

### In Progress / Next (prioritized)
- [ ] Version source of truth per package stays in `pyproject.toml` and `__version__` modules; confirm semantic-release still updates both and preserves tag formats (`cli-v{version}`, `server-v{version}`).
- [ ] Changelog policy: converge on a single root `CHANGELOG.md` updated by semantic-release for both packages; document any per-package exceptions.
- [ ] Release workflow hardening: keep `.github/workflows/release.yml` invoking CI then semantic-release in `cli/` and `server/`; verify CI success remains a gate and `fetch-depth=0` persists.
- [ ] Tag seeding on main after parser switch (e.g., `cli-v0.1.0`, `server-v0.1.0`) to anchor history before enabling automation.
- [ ] Secrets and tokens: confirm `GITHUB_TOKEN` scope is sufficient for tagging and releases; PyPI remains out of scope.
- [ ] Post-switch validation: run `scripts/test-release.sh` from repo root, `cli/`, and `server/`; capture outputs to prove repo-dir change and version detection behave (current runs still emit repo-dir warning; need follow-up).

## Risks / Mitigations
- Non-conventional commits block version bumps → mitigate with cz guidance and CI linting option.
- Tag collisions if formats change → document tag scheme and avoid retroactive edits.
- First-release edge cases (no tags) → seed baseline tags if needed before enabling automation.

## Milestones
1) Document developer workflow and commands (CONTRIBUTING).
2) Validate release workflow end-to-end on a dry run (version --print) and/or seeded tags.
3) Enable/confirm release workflow on main with a test conventional commit and observed changelog/tag.
