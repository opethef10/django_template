#!/bin/bash
# Copies wsgi.py to PythonAnywhere's /var/www directory
# Username is read from PROJECT_SLUG in .env (or falls back to $USER)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Load only the PROJECT_SLUG from the .env file (absolute path)
ENV_FILE="$PROJECT_ROOT/.env"
if [[ ! -f "$ENV_FILE" ]]; then
    echo "[ERROR] .env file not found at $ENV_FILE"
    exit 1
fi
export $(grep -v '^#' "$ENV_FILE" | grep 'PROJECT_SLUG' | xargs)

# Use PROJECT_SLUG from env, or fall back to USER
USERNAME="${PROJECT_SLUG:-$USER}"

if [ -z "$USERNAME" ]; then
    echo "Error: PROJECT_SLUG or USER not set"
    exit 1
fi

# Destination: /var/www/USERNAME_pythonanywhere_com_wsgi.py
DEST_DIR="/var/www"
DEST_FILE="$DEST_DIR/${USERNAME}_pythonanywhere_com_wsgi.py"

mkdir -p "$DEST_DIR"

# Write wsgi.py with hardcoded username
cat > "$DEST_FILE" << EOF
import os
import sys

username = '$USERNAME'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.production')

path = f'/home/{username}/{username}.pythonanywhere.com'
if path not in sys.path:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
EOF

echo "Created $DEST_FILE"
