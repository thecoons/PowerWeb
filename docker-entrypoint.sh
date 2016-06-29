#!/bin/bash
python manage.py makemigrations HearthDeepApi
python manage.py migrate                  # Apply database migrations
echo Starting Gunicorn.
exec gunicorn --bind 0.0.0.0:8000 HearthDeepWeb.wsgi:application
