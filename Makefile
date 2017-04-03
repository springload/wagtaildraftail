.PHONY: help init start lint load-data test test-coverage test-ci clean-pyc dist publish
.DEFAULT_GOAL := help

help: ## See what commands are available.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36mmake %-15s\033[0m # %s\n", $$1, $$2}'

init: ## Install dependencies and initialise for development.
	clean-pyc
	pip install -e .[testing,docs] -U
	nvm install || echo "nvm is not available"
	npm install
	make load-data
	make dist

start: ## Starts the development server.
	python ./tests/testapp/manage.py runserver

lint: ## Lint the project.
	flake8 wagtaildraftail tests setup.py
	isort --check-only --diff --recursive wagtaildraftail tests setup.py

load-data: ## Prepares the database for usage.
	python ./tests/testapp/manage.py migrate
	python ./tests/testapp/manage.py loaddata tests/testapp/fixtures/test_data.json

test: ## Test the project.
	python ./runtests.py

test-coverage: ## Run the tests while generating test coverage data.
	coverage run ./runtests.py && coverage report
	npm run test:coverage

test-ci: ## Continuous integration test suite.
	tox

clean-pyc: ## Remove Python file artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

dist: ## Compile the JS and CSS for release.
	npm run dist

publish: ## Publishes a new version to pypi.
	dist
	rm dist/* && python setup.py sdist && twine upload dist/* && echo 'Success! Go to https://pypi.python.org/pypi/wagtaildraftail and check that all is well.'
