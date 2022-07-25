#!/usr/bin/env sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

exec gunicorn application.wsgi --bind 0.0.0.0:8000 --reload -w 10