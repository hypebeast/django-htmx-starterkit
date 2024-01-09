#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


#python manage.py migrate
#gunicorn -w 1 -b 127.0.0.1:8005 django_htmx_alpine.wsgi
# python /app/manage.py collectstatic --noinput
# /usr/local/bin/gunicorn asgi --bind 0.0.0.0:5000 --chdir=/app -k uvicorn.workers.UvicornWorker
# /usr/local/bin/gunicorn wsgi --bind 0.0.0.0:5000 --chdir=/app --access-logfile - --error-logfile -
