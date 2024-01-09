FROM python:3.11-slim-buster

ARG BUILD_ENVIRONMENT=development
ARG APP_HOME=/app
ARG DJANGO_ENV=development

ENV DJANGO_ENV=${DJANGO_ENV}
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ${APP_HOME}

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django

# copy the entrypoint and start script
COPY --chown=django:django ./docker/django/production/entrypoint.sh /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY --chown=django:django ./docker/django/dev/start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Requirements are installed here to ensure they will be cached.
RUN python -m pip install --upgrade pip && pip install pdm psycopg2
COPY pdm.lock pyproject.toml ${APP_HOME}
RUN pdm install

# make django owner of the WORKDIR directory as well.
RUN chown -R django:django ${APP_HOME}

EXPOSE 8000
USER django

ENTRYPOINT ["/entrypoint"]
CMD ["/start"]
