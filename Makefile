DOCKER_CMD := docker compose -f docker-compose.yml
API_CMD := ${DOCKER_CMD} exec api
DB_CMD := ${DOCKER_CMD} exec mysql
DOCKER_ENV := --env-file .local/docker-compose.env

setup:
	${MAKE} build
	${MAKE} up

build:
	${DOCKER_CMD} build

up:
	${DOCKER_CMD} ${DOCKER_ENV} up -d

down:
	${DOCKER_CMD} down

api:
	${API_CMD} /bin/bash

db/init:
	${DB_CMD} mysql -u super_fast -D super_fast -ppassword -NBe"drop database if exists super_fast;create database super_fast;"

migrate:
	${API_CMD} alembic upgrade head

makemigrations:
	${API_CMD} alembic revision --autogenerate -m "$(message)"

test:
	${API_CMD} pytest tests