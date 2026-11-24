#!/bin/bash
set -e

python manage.py migrate --noinput

python manage.py collectstatic --noinput

# Workers/threads are configurable per deployment (e.g. 4x4 for prod, 1x1 for staging).
# GUNICORN_THREADS > 1 switches gunicorn to the gthread worker class automatically.
exec gunicorn --bind "0.0.0.0:8000" \
    --workers "${GUNICORN_WORKERS:-2}" \
    --threads "${GUNICORN_THREADS:-1}" \
    --access-logfile - src.wsgi:application
