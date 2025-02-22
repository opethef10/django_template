#! /usr/bin/env bash

# Change to the parent directory of the script (Project root)
cd "$(dirname "$0")"/.. || exit 1

# Load environment variables from .env file in the project root
set -a && source .env && set +a

touch "/var/www/${PROJECT_SLUG}_pythonanywhere_com_wsgi.py"
for i in {1..3}; do
  echo -n "."
  sleep 1
done
echo "Server is reloaded"
