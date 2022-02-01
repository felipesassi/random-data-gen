.PHONY: check
check:
	poetry install -n
	poetry run flake8 .
	poetry run pytest .

.PHONY: format
format:
	poetry install -n
	poetry run black .