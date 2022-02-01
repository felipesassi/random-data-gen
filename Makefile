.PHONY: check
check:
	poetry install -n
	poetry run black .
	poetry run pytest .