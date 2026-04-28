#!/bin/sh
set -e

echo "[entrypoint] running migrations"
python manage.py migrate --noinput

echo "[entrypoint] collecting static files"
python manage.py collectstatic --noinput

echo "[entrypoint] launching: $*"
exec "$@"
