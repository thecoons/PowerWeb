#!/bin/bash
python manage.py makemigrations HearthDeepApi
python manage.py migrate                  # Apply database migrations
python manage.py runserver 0.0.0.0:8000
