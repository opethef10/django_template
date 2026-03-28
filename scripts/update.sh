#! /usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

# Check if the script is running inside a virtual environment
if [ -z "${VIRTUAL_ENV:-}" ]; then
    echo "Error: This script must be run inside a virtual environment." >&2
    exit 1
fi

# Check if the project is a git repository
if ! git -C "$PROJECT_ROOT" rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not a git repository" >&2
    exit 1
fi

# Load only the PROJECT_SLUG from the .env file (absolute path)
ENV_FILE="$PROJECT_ROOT/.env"
if [[ ! -f "$ENV_FILE" ]]; then
    echo "[ERROR] .env file not found at $ENV_FILE"
    exit 1
fi

export $(grep -v '^#' "$ENV_FILE" | grep 'PROJECT_SLUG' | xargs)

# Check if WSGI path shows the project is running on PythonAnywhere
WSGI_PATH="/var/www/${PROJECT_SLUG}_pythonanywhere_com_wsgi.py"
if [[ ! -f "$WSGI_PATH" ]]; then
    echo "Error: WSGI file not found at $WSGI_PATH"
    echo "Are you running on PythonAnywhere?"
    exit 1
fi

export DJANGO_SETTINGS_MODULE=src.settings.production

"$SCRIPT_DIR/backupdb.sh"
git pull
pip install -r requirements/production.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py compilemessages
python manage.py test --settings=src.settings.tests
"$SCRIPT_DIR/reload.sh"
