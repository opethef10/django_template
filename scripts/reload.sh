#! /usr/bin/env bash

cd "$(dirname "$0")"/.. || exit 1

# Load only the PROJECT_SLUG from the .env file
export $(grep -v '^#' .env | grep 'PROJECT_SLUG' | xargs)

touch "/var/www/${PROJECT_SLUG}_pythonanywhere_com_wsgi.py"
for i in {1..3}; do
  echo -n "."
  sleep 1
done
echo "Server is reloaded"
