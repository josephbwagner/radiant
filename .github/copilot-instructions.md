# Radiant workspace agent guidelines

Use this as the shared Copilot instructions for this repo.

- Style: professional; ask when uncertain or ambiguous; add relevant details.
- Safety: never run destructive commands or delete files without explicit ask.
- Python: use poetry env per module; use strong typing.
- Frontend: TypeScript + Vite. Use prettier. Keep UI suggestions purposeful (avoid generic layouts).
- MCP: prefer MCP tools before guessing; optimize tool selection for each task.
- Testing: when code changes add unit tests and verify they pass.
- Comments: use docstrings for functions/classes; brief comments for complex logic; conventional commit message style.
- Editing: avoid touching unrelated changes.
- Security: never expose secrets; ask for explicit direction when making security decisions.
- Output: mention file paths with line links; keep summaries short and actionable.
