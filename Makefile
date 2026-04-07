.PHONY: install dev lint test cov docker clean

VENV := .venv
PIP := $(VENV)/Scripts/pip.exe

install:
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e '.[dev]'

dev:
	$(VENV)/Scripts/activate && uvicorn vectorless_rag.api.main:app --reload --host 0.0.0.0 --port 8000

lint:
	ruff check src/ tests/
	ruff format src/ tests/

test:
	pytest tests/ -v

cov:
	pytest tests/ --cov=vectorless_rag --cov-report=html --cov-report=term-missing

docker:
	docker-compose up --build

clean:
	rm -rf $(VENV) .pytest_cache htmlcov/ dist/ *.egg-info/

