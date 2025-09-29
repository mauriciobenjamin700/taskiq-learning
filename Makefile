lint-fix:
	uv run black src
	uv run isort src
	uv run ruff check src --fix

start-scheduler:
	uv run taskiq scheduler src.tasks:scheduler

start-worker:
	uv run taskiq worker src.tasks:broker