all: checkstyle test

test:
	python -m unittest discover tests

checkstyle:
	flake8 --show-source --max-line-length=120 .
