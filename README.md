# django-htmx-starterkit

A simple Django starterkit with **Django**, **HTMX** and **Hyperscript**.

## About

This project is just a basic todo list.

However, it is made using a combination of [Django](https://www.djangoproject.com/), [HTMX](https://htmx.org/) and [Hyperscript](https://hyperscript.org) and shows how you can get the reactivity of a frontend JS framework without sacrificing the benefits of your server-side framework (session authentication, templating, etc).

## Features

- ✔️ Supports latest Python 3.12
- ✔️ [Poetry](https://python-poetry.org/) for managing dependencies.
- ✔️ [Django](https://www.djangoproject.com/) (latest version 5).
- ✔️ [HTMX](https://htmx.org/) to build modern and reactive user interfaces without the complexity of a JS frontend framework.
- ✔️ [Hyperscript](https://hyperscript.org/docs/) is a Javascript library as an companion to HTMX to compose behavior directly in HMTL.
- ✔️ [Tailwindcss](https://tailwindcss.com/) a utility-first CSS framework for styling.
- ✔️ [DaisyUI](https://daisyui.com/) a Tailwind component library.
- ✔️ [django-allauth](https://docs.allauth.org/en/latest/) for user authentication, registration and account management.
- ✔️ [django-split-settings](https://github.com/wemake-services/django-split-settings) to organize Django settings into multiple files and directories.
  ✔️ - Support for multiple environments (e.g. development or production).
- ✔️ [python-decouple](https://github.com/HBNetwork/python-decouple) to decouple config from and loading env variables and `.env` files.
- ✔️ [mypy](https://mypy.readthedocs.io/en/stable/index.html) and [django-stubs](https://github.com/typeddjango/django-stubs) for static typing.
- ✔️ [pytest](https://docs.pytest.org/en/7.4.x/) and [hypothesis](https://hypothesis.readthedocs.io/en/latest/) for unit tests.
- ✔️ [ruff](https://github.com/astral-sh/ruff) for code linting and formatting (replaces flake8, black and isort).
- ✔️ [Docker](https://www.docker.com/) support using [docker-compose](https://docs.docker.com/compose/) configuration for local development (incl. Postgres).
- ✔️ No complex frontend build pipeline. Only `Postcss` is used for Tailwindcss. Frontend reacivity is handled with HTMX and Hyperscript. Both doesn't require a build step.

## Getting Up and Running Locally

This guide describes how you can quickly setup the project for local development.

**Minimum requirements**: Python 3.10, pip, pdm, & PostgreSQL (installed via docker), setup is tested on Mac OSX only.

The steps below will get you up and running with a local development environment. All of these commands assume you are at the root of your generated project.

### Prerequisites

- Install [Python](https://www.python.org/downloads/) and [PDM](https://pdm-project.org/latest/).
- Install [NodeJS](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs) and [Yarn](https://yarnpkg.com/getting-started/install).
- `Docker`; if you don’t have it yet, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms).
- `Docker Compose`; refer to the official documentation for the [installation guide](https://docs.docker.com/compose/install/).

To install Python, PDM, NodeJS and Yarn run the following command on Mac OS:

```shell
brew install python3 pdm node yarn
```

For installing Docker and docker-compose refer to the official documentation.

### Clone the repository

```shell
git clone https://github.com/hypebeast/django-htmx-starterkit
```

### Setup environment variables

Before you can start the project you need to set some environment variables. This can be done via creating an `.env` file:

```shell
cp .env.template .env
```

Now open the `.env` file and add the required configuration.

Here is an example with the minimum required config:

```env
DOMAIN_NAME=localhost

DJANGO_SECRET_KEY=<yoursecretekey>

POSTGRES_DB=starterkit
POSTGRES_USER=starterkit
POSTGRES_PASSWORD=password

DJANGO_DATABASE_HOST=localhost
DJANGO_DATABASE_PORT=5432
```

Generate the secret key with:

```shell
python3 -c 'from django.utils.crypto import get_random_string; print(get_random_string(50))'
```

### Build the Docker stack

Build all docker-compose services with:

```shell
docker compose build
```

### Run the database with Docker and Docker-Compose

Run the database with the following command:

```shell
docker compose up -d
```

### Install Dependencies

Install all dependencies with PDM:

```shell
make install
```

### Run Migrations

Run the migrations with:

```shell
make migrate
```

#### Frontend Setup

The frontend project is located in the `themes` app. This Django app handles the This is required because of TailwindCSS.

Install the dependencies:

```shell
make frontend-install
```

Now, you can start the frontend dev server with the following command:

```shell
make frontend-dev
```

### Start the Django server

Now, you can start the development server with the following command:

```shell
make dev
```

Now you can open the site: [Homepgae](http://localhost:8080).

## Basic Commands

Some useful commands:

- `make run` - start django server
- `make test` - run the test locally with ipdb

**Note**: Run `make help` to see a list with all available commands.

**NOTE**: Checkout Makefile for all the options available and how they do it.

## Project Struture

```shell
├── apps
│  ├── accounts
│  │  ├── migrations
│  │  └── templates
│  ├── core
│  ├── main
│  │  ├── logic
│  │  ├── migrations
│  │  └── templates
│  ├── tasks
│  │  ├── migrations
│  │  └── templates
│  └── theme
│     ├── migrations
│     ├── static
│     ├── templates
│     └── templatetags
├── config
│  └── settings
│     ├── components
│     └── environments
└── docker
   ├── caddy
   ├── django
   └── frontend
```

## Managing Dependencies

### PDM

For managing the dependencies [PDM](https://pdm-project.org/latest/) is used. PDM, is a modern Python package and dependency manager supporting the latest PEP standards. But it also helps you with your development worklfow and boosts your development workflow in various aspects.

Please, refere to the [PDM Documentation](https://pdm-project.org/latest/) for more information.

#### Some basic commands

Install all dependecies:

```shell
pdm sync
```

Add a new package

```shell
pdm add <packagename>
```

Create a `virtualenv`:

```shell
pdm venv create 3.10
pdm venv activate # Copy the printed command and run it to activate the virtualenv
```

## Settings

TODO: Add description for how to configure the application.

## Frontend

TODO: Add description how to work with the frontend code.

## Deploying the Project

TODO: Add instructions for deployment on `fly.io`.

## Open Tasks

- [ ] Add tests
- [ ] Add support for production deployment
- [ ] black
- [ ] mypy & django-stubs

## License

The MIT License (MIT). See the [LICENSE](./LICENSE) for more information.

## Author

Copyright 2024 Sebastian Ruml <sebastian.ruml@gmail.com>.
