#!/bin/sh

repo_root=$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel 2>/dev/null) || {
  echo "Error: unable to determine repository root" >&2
  exit 1
}

call_dir=$(pwd)
project_dir=${RELEASE_PROJECT_DIR:-$call_dir}

# Pick a pyproject location: prefer caller directory, then cli/, then server/
if [ ! -f "$project_dir/pyproject.toml" ]; then
  if [ -f "$repo_root/cli/pyproject.toml" ]; then
    project_dir="$repo_root/cli"
  elif [ -f "$repo_root/server/pyproject.toml" ]; then
    project_dir="$repo_root/server"
  else
    echo "Error: no pyproject.toml found; set RELEASE_PROJECT_DIR" >&2
    exit 1
  fi
fi

cd "$repo_root" || {
  echo "Error: failed to change directory to repository root" >&2
  exit 1
}

last_tag=$(git describe --tags --abbrev=0 2>/dev/null || true)

if [ -n "$last_tag" ]; then
  echo "Last tag: $last_tag"
  commits_since=$(git rev-list --count "${last_tag}..HEAD")
else
  echo "Last tag: none"
  commits_since=$(git rev-list --count HEAD)
fi

echo "Commits since last tag: $commits_since"

echo "Next version (semantic-release):"
next_version_output=$(poetry -C "$project_dir" run semantic-release version --print 2>&1)
next_version_status=$?
echo "$next_version_output"

if [ "$next_version_status" -ne 0 ]; then
  echo "semantic-release exited with $next_version_status"
fi

echo "Next steps: git tag <version> && git push --tags"
