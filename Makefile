.PHONY: dev lint test migrate db-up db-down docker-up

dev:
	uvicorn src.main:app --reload --port 8000

lint:
	ruff check src/

lint-fix:
	ruff check --fix src/

test:
	pytest

test-coverage:
	pytest --cov=src --cov-report=html

migrate:
	alembic upgrade head

migration:
	alembic revision --autogenerate -m "$(message)"

db-up:
	docker compose up -d db

db-down:
	docker compose down

docker-up:
	docker compose up -d

docker-down:
	docker compose down
