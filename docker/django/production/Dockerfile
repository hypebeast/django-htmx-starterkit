FROM node:18-bullseye-slim as client-builder

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

COPY ./theme/package.json ${APP_HOME}
RUN npm install && npm cache clean --force
COPY ./theme ${APP_HOME}

RUN npm run theme:build

FROM python:3.11-slim-buster as python

FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=production

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy the entrypoint script
COPY ./docker/entrypoint.sh /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/dev.txt
RUN pip install uvicorn

COPY . /app

EXPOSE 8000

ENTRYPOINT ["/entrypoint"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
