.PHONY: run install clean

run:
	@echo "Starting Flask app..."
	python app.py

install:
	pip install -r requirements.txt

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
