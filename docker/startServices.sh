#! /bin/bash

## This is a start services script to only be used on the single docker image

cd /app/frontend
npm start &

cd /app/backend
gunicorn --config gunicorn_config.py wsgi:application
