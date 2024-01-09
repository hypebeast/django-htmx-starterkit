#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


pdm run python manage.py migrate
pdm run python manage.py runserver 0.0.0.0:8000
