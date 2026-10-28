#!/usr/bin/env bash
# Build the frontend and serve the whole site from one process: ./start.sh [port]
set -euo pipefail
cd "$(dirname "$0")"
PORT="${1:-8787}"

if [ ! -x backend/.venv/bin/uvicorn ]; then
  python3 -m venv backend/.venv
  backend/.venv/bin/pip install -q -r backend/requirements.txt
fi
if [ ! -d frontend/node_modules ]; then
  (cd frontend && npm ci)
fi
(cd frontend && npm run build)

echo "展示站点：http://127.0.0.1:${PORT}"
cd backend && exec .venv/bin/uvicorn app:app --host 127.0.0.1 --port "${PORT}"
