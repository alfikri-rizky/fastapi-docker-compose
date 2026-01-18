lint:
	uv run ruff format .
	uv run ruff check . --fix

dev:
	uv tun uvicorn app.main:app --reload