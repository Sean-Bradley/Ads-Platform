VENV   := .venv
PYTHON := $(VENV)/bin/python
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

.PHONY: help setup pull push clean

help:
	@echo "make setup  - create venv and install requirements"
	@echo "make pull   - git pull --rebase from origin/$(BRANCH)"
	@echo "make push   - git push to origin/$(BRANCH)"
	@echo "make clean  - remove venv and cache files"

$(PYTHON):
	python3 -m venv $(VENV)

setup: $(PYTHON)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

pull:
	git pull --rebase origin $(BRANCH)

push:
	git push origin $(BRANCH)

clean:
	rm -rf $(VENV) .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov
	find . -path ./.git -prune -o -type d -name __pycache__ -exec rm -rf {} +
	find . -path ./.git -prune -o -type f -name '*.py[co]' -exec rm -f {} +
