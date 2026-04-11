#! /usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

# Load only the PROJECT_SLUG from the .env file
export $(grep -v '^#' .env | grep 'PROJECT_SLUG' | xargs)

WSGI_PATH="/var/www/${PROJECT_SLUG}_pythonanywhere_com_wsgi.py"

if [[ ! -f "$WSGI_PATH" ]]; then
    echo "Error: WSGI file not found at $WSGI_PATH"
    echo "Are you running on PythonAnywhere?"
    exit 1
fi

touch "$WSGI_PATH"
for i in {1..3}; do
  echo -n "."
  sleep 1
done
echo "Server is reloaded"
