#!/bin/bash
python manage.py makemigrations HearthDeepApi
python manage.py migrate                  # Apply database migrations
echo Starting Gunicorn.
exec gunicorn -c gunicorn_conf.py HearthDeepWeb.wsgi:application
