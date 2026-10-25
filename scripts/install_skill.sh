#!/usr/bin/env bash
# Deploy the skills in ./skills into a DeerFlow checkout as *custom* skills.
# A custom skill shadows a built-in skill of the same name, so the improved
# systematic-literature-review replaces the upstream one without touching core.
#
#   scripts/install_skill.sh [path/to/deer-flow]      (default: ./deer-flow)
#
# Afterwards restart the gateway so it drops its cached skill list:
#   docker restart deer-flow-gateway
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target="${1:-$root/deer-flow}/skills/custom"
[ -d "${1:-$root/deer-flow}/skills" ] || { echo "not a DeerFlow checkout: ${1:-$root/deer-flow}" >&2; exit 1; }

mkdir -p "$target"
for skill in "$root"/skills/*/; do
  name="$(basename "$skill")"
  rm -rf "$target/$name"
  cp -R "$skill" "$target/$name"
  find "$target/$name" -name __pycache__ -prune -exec rm -rf {} +
  echo "installed $name -> $target/$name"
done
echo "now run: docker restart deer-flow-gateway"
