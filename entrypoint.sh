#!/bin/bash
set -e

echo "${0}: running migrations."
python manage.py migrate --noinput

echo "${0}: collecting statics."
python manage.py collectstatic --noinput

echo "${0}: starting gunicorn."

gunicorn pystokapp.wsgi:application \
  --name pystokapp \
  --bind 0.0.0.0:8000 \
  --timeout 600 \
  --reload \
  --workers 3 \
  --log-level=info
  "$@"
