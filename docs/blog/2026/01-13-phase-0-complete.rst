Phase 0 Complete: Foundation for a Meshtastic Management Tool
=============================================================

:date: 2026-01-13
:author: Joseph Wagner
:tags: milestone, infrastructure, technical-decision, phase-0

Context
-------

Radiant will ship a CLI, server API, and web UI for Meshtastic networks. Phase 0 was about earning the right to build features: picking tools that keep all three layers moving together with minimal friction. This post focuses on *why* each choice was made.

Why These Foundations
---------------------

Monorepo by design
^^^^^^^^^^^^^^^^^^
- Keep CLI, server, and frontend versioned together so breaking changes land atomically.
- Share linting, testing, and CI/CD once instead of three times.
- Lower onboarding cost: one clone gives the whole stack.

Poetry for Python
^^^^^^^^^^^^^^^^^
- Reliable dependency resolution and lock files reduce “works on my machine.”
- Dev vs. runtime deps stay clean, which matters for slim Docker images.
- Built-in build/version tooling keeps releases consistent across CLI and server.

Tech stack fit
^^^^^^^^^^^^^^
- **FastAPI + SQLAlchemy (PostgreSQL)**: async-first, typed validation, and alembic migrations let the API evolve without schema surprises.
- **React + TypeScript + Vite**: type safety and fast feedback loops; Zustand + TanStack Query keep state simple without Redux overhead.

Quality Gates From Day One
--------------------------

- **Ruff** replaces multiple linters/formatters so contributors learn one tool and get quick feedback.
- **MyPy** runs in CI to force typed contracts across packages; safer refactors later.
- **Pytest** with a 55% floor today prevents “zero-coverage” regressions while we grow; targets rise as features arrive.

Shipping Safely, Quickly
------------------------

CI/CD matrix
^^^^^^^^^^^^
- Split Python support by need: CLI on 3.9-3.13 for widest user base; server on 3.12+ to use modern async features.
- Linux/macOS/Windows coverage catches platform quirks before users do.
- Weekly Bandit scans and Sphinx doc builds keep security and docs from drifting.

Multi-arch Docker
^^^^^^^^^^^^^^^^^
- BuildKit + multi-stage images keep runtimes small and consistent across x86_64 and ARM64 (Raspberry Pi is a key target).
- Cross-platform cache and a single tag avoid double maintenance.

Developer Experience
--------------------

- Pre-commit runs Ruff, MyPy, and whitespace cleanup so reviews focus on behavior, not style.
- VS Code settings and extension recommendations make a fresh clone “ready to code” without guesswork.

Outcomes
--------

- Coverage: CLI 80%, server 82% (above the 55% guardrail).
- Linting/typing: zero Ruff or MyPy failures in CI.
- CI: 20+ matrix builds green across OS and Python versions; docs build cleanly.
- Containers: multi-arch images build reliably via buildx.

What's Next
-----------

- Phase 1: CLI foundation + diagnostics engine.
- Phase 2: Server API expansion.
- Phase 3: Frontend workflows.

Lessons, Briefly
----------------

- Front-loading tooling reduced friction immediately—worth the upfront time.
- Templates would trim the initial setup cost next time.
- Next iteration: add integration tests earlier and stage CI workflows incrementally.
