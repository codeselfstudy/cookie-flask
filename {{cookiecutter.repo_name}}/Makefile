.PHONY: clean-pyc docs clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	# @echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"

clean: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

lint:
	flake8 {{ cookiecutter.repo_name }} tests

test:
	python setup.py test

coverage:
	coverage run --source {{ cookiecutter.repo_name }} setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/{{ cookiecutter.repo_name }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.repo_name }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

