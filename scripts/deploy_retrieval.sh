#!/usr/bin/env bash
# Deploy the scholar plugin and the literature-review skill from a checkout of this repo, then restart the gateway.
# Used to switch the coverage holdout arms (P2): the v3.2 arm deploys from a git worktree of its commit.
#
#   scripts/deploy_retrieval.sh [checkout]      (default: this repo's working tree)
#
# The plugin's config entry (including host_access) survives `deerflow extensions upgrade`; v3.2 ignores the
# keys it does not know and registers no screening service.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
src="$(cd "${1:-$root}" && pwd)"
df="$root/deer-flow"

version="$(sed -n 's/^version = "\(.*\)"/\1/p' "$src/extensions/scholar/pyproject.toml")"
docker exec deer-flow-gateway rm -rf /tmp/scholar-src
docker cp "$src/extensions/scholar" deer-flow-gateway:/tmp/scholar-src
docker exec deer-flow-gateway sh -c 'rm -rf /tmp/scholar-src/.pytest_cache /tmp/scholar-src/.ruff_cache; find /tmp/scholar-src -name __pycache__ -prune -exec rm -rf {} +'
docker exec -w /app/backend deer-flow-gateway uv run --no-sync deerflow extensions upgrade /tmp/scholar-src --yes | tail -1

target="$df/skills/custom/systematic-literature-review"
rm -rf "$target"
cp -R "$src/skills/systematic-literature-review" "$target"

docker restart deer-flow-gateway >/dev/null
until docker exec deer-flow-gateway curl -sf localhost:8001/health >/dev/null 2>&1; do sleep 2; done
installed="$(docker exec -w /app/backend deer-flow-gateway uv run --no-sync python -c 'import importlib.metadata as m; print(m.version("deerflow-extension-scholar"))')"
[ "$installed" = "$version" ] || { echo "installed $installed, expected $version" >&2; exit 1; }
grep -q "default: qwen3.5-plus-screen" "$df/config.yaml" || { echo "host_access grant missing from config.yaml" >&2; exit 1; }
echo "deployed scholar $version and the skill from $src"
