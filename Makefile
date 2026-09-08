.PHONY: install start build test clean

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install

start:
	python main.py

build:
	cd frontend && npm run build

test:
	cd backend && python -m pytest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf dist frontend/dist
