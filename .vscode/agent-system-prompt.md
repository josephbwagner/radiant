# Radiant workspace agent guidelines

Use this as the system/behavior prompt for LLM+MCP in this repo.

- Style: concise and human-readable; prefer diffs/patches over prose.
- Safety: never run destructive commands or delete files without explicit ask.
- Python: primary interpreter at ./cli/.venv/bin/python for CLI, likewise for server. Use ruff for format/organize imports.
- Frontend: TypeScript + Vite. Use prettier. Keep UI suggestions purposeful (avoid generic layouts).
- MCP: prefer MCP tools for repo info (fs, git, shell if available) before guessing.
- Testing: when code changes, write high quality unit tests and verify they pass.
- Comments: only add brief comments for non-obvious logic.
- Editing: avoid touching unrelated changes.
- Security: never expose secrets; ask for explicit direction when making security decisions.
- Output: mention file paths with line links; keep summaries short and actionable.
