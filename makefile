help:
	@echo 'venv'
	@echo 'help'
	@echo 'setup'
	@echo 'dev'
	@echo 'release'
	@echo 'format'
	@echo 'lint'
	@echo 'test'
	@echo 'clean'
	@echo 'distclean'

venv:
	python3 -m venv .venv
	@echo 'run `source .venv/Scripts/activate` para ativar o virtualenv'

novenv:
	python3 -m venv .venv
	@echo 'run `source .venv/Scripts/deactivate` para desativar o virtualenv'

setup: venv
	source .venv/bin/activate && pip3 install -U black isort mypy pylint twine

dev: setup
	source .venv/bin/activate && python3 setup.py develop
	@echo 'run `source .venv/bin/activate` para o desenvolvimento da pre-proposta'

release: lint test clean
	python3 setup.py sdist
	python3 -m twine upload dist/*

format:
	black pre-proposta setup.py
	isort

lint:
	black --check pre-proposta setup.py
	mypy --ignore-missing-imports --python-version 3.12.

test:
	python3 -m unittest -v pre-proposta.tests

clean:
	rm -rf build dist README MANIFEST *.egg-info

distclean: clean
	rm -rf .venv