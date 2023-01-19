build:
	isort vuash
	black vuash
	ruff vuash
	./manage.py makemigrations --check --dry-run --settings=vuash.settings.tests
