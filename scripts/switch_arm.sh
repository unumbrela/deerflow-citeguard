#!/usr/bin/env bash
# Switch the local DeerFlow deployment between the two eval arms, then restart the gateway.
#
#   scripts/switch_arm.sh v3        custom skill + scholar plugin on + allow_host_bash: false
#   scripts/switch_arm.sh baseline  upstream skill + scholar plugin off + allow_host_bash: true
#
# The upstream skill needs host bash to run its arXiv script; the plugin is turned off in the
# baseline arm so its extra tools cannot change the baseline agent's behaviour.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
df="$root/deer-flow"
arm="${1:?usage: switch_arm.sh v3|baseline}"

case "$arm" in
  v3) bash_on=false plugin_on=true ;;
  baseline) bash_on=true plugin_on=false ;;
  *) echo "unknown arm: $arm" >&2; exit 2 ;;
esac

python3 -I - "$df/config.yaml" "$bash_on" "$plugin_on" <<'EOF'
import re, sys
path, bash_on, plugin_on = sys.argv[1:]
text = open(path, encoding="utf-8").read()
text, n1 = re.subn(r"(?m)^  allow_host_bash: (true|false)$", f"  allow_host_bash: {bash_on}", text)
# The outer `enabled` of the scholar plugins: entry (the line right after `use:`) controls loading.
text, n2 = re.subn(r"(?m)^(  use: deerflow_extension_scholar:install\n  enabled: )(true|false)$", rf"\g<1>{plugin_on}", text)
if (n1, n2) != (1, 1):
    sys.exit(f"config.yaml layout not recognised (allow_host_bash: {n1}, scholar entry: {n2})")
open(path, "w", encoding="utf-8").write(text)
EOF

if [ "$arm" = v3 ]; then
  "$root/scripts/install_skill.sh" "$df" >/dev/null
else
  rm -rf "$df/skills/custom/systematic-literature-review"
fi

since="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
docker restart deer-flow-gateway >/dev/null
until docker exec deer-flow-gateway curl -sf -o /dev/null http://localhost:8001/health 2>/dev/null; do sleep 2; done
echo "arm=$arm allow_host_bash=$bash_on scholar_plugin=$plugin_on (gateway up)"
docker logs --since "$since" deer-flow-gateway 2>&1 | grep -m1 "Extensions loaded" || grep "Extensions loaded" "$df/logs/gateway.log" | tail -1
