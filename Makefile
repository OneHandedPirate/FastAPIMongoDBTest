.PHONY: tests
include .env
export

up_db:
	docker compose -f docker-compose-dev.yaml up -d

fill_db:
	python -m src.utils.db_fill

tests:
	python -m tests.test

start_app:
	uvicorn src.main:app --port $(APP_PORT) --reload

down_db:
	docker compose -f docker-compose-dev.yaml down