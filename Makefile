.DEFAULT_GOAL:=help

.PHONY: help
help:  ## Display this help
	$(info Makefile for django-htmx)
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: server
dev: ## Run migrations and start the development server
	pdm run python manage.py migrate && pdm run python manage.py runserver

.PHONY:
frontend-install: ## Runs the frontend dev pipeline and watches for changes
	cd apps/theme && yarn install

.PHONY:
frontend-run: ## Runs the frontend dev pipeline and watches for changes
	cd apps/theme && npm run theme:dev

.PHONY: migrate
migrate: ## Run migrations
	pdm run python manage.py migrate

.PHONY: makemigrations
makemigrations: ## Generate migration files
	pdm run python manage.py makemigrations

.PHONY: createsuperuser
ceratesuperuser: ## Creates a super user
	pdm run python manage.py createsuperuser

.PHONY: install
install: ## Installs all packages
	pdm install

clean: ## Clean up
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

test:
	pytest -n 4 -x

.PHONY: lint
lint: ## Run linter
	pdm run ruff check .

.PHONY: lint-fix
lint-fix: ## Fix found linter errors
	pdm run ruff check --fix .

.PHONY: format
format: ## Format the code with ruff
	pdm run ruff format .

clean-lint: format lint

checkmigrations:
	pdm run python manage.py makemigrations --check --no-input --dry-run

# build:
# 	@if [ -z ${VERSION} ]; then echo Usage: make build-production VERSION=0.0.0 && exit 1; fi;
# 	docker build --file Dockerfile.production --tag {{ cookiecutter.project_name }}:latest .
# 	docker tag {{ cookiecutter.project_name }}:latest {{ cookiecutter.project_name }}:${VERSION}

# push:
# 	@if [ -z ${VERSION} ]; then echo Usage: make push-production VERSION=0.0.0 && exit 1; fi;
# 	docker tag {{ cookiecutter.project_name }}:latest ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}:latest
# 	docker tag {{ cookiecutter.project_name }}:latest ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}:${VERSION}
# 	docker push ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}:latest
# 	docker push ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}:${VERSION}

# Commands for Docker version
# docker_setup:
# 	docker volume create {{project_name}}_dbdata
# 	docker-compose build --no-cache backend
# 	docker-compose run frontend npm install

# docker_test:
# 	docker-compose run backend python manage.py test $(ARG) --parallel --keepdb

# docker_test_reset:
# 	docker-compose run backend python manage.py test $(ARG) --parallel

docker_up:
	docker compose up -d

# docker_update_dependencies:
# 	docker-compose down
# 	docker-compose up -d --build

docker_down:
	docker compose down

docker_logs: ## Show docker logs
	docker compose logs -f $(ARG)

docker_makemigrations: ## Make migrations with docker
	docker compose run --rm app pdm run python manage.py makemigrations

docker_migrate: ## Run migrations with docker
	docker compose run --rm app pdm run python manage.py migrate

docker_create_superuser: ## Create a super user with docker
	docker compose run --rm app pdm run python manage.py createsuperuser


# install-hooks:
#     echo "make lint && make checkmigrations" > .git/hooks/pre-commit && chmod 777 .git/hooks/pre-commit

# pip-install-dev:
# 	pip install --upgrade pip pip-tools
# 	pip-sync requirements.txt requirements-dev.txt

# pip-install:
# 	pip install --upgrade pip pip-tools
# 	pip-sync requirements.txt

# pip-update:
# 	pip install --upgrade pip pip-tools
# 	pip-compile requirements.in
# 	pip-compile requirements-dev.in
# 	pip-sync requirements.txt requirements-dev.txt

#$(VERBOSE).SILENT:
