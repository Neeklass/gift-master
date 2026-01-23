#!/bin/bash

echo "Starting GiftMaster deployment..."

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn --bind=0.0.0.0 --timeout 600 giftmaster.wsgi
