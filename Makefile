PYTHON=python3
PYCODESTYLE=pycodestyle

.DEFAULT_GOAL = help

help:
	@echo "The following targets are supported:"
	@echo " setup   install required packages"
	@echo " test	run the tests"


setup:
	pip install -r requirements.txt


test:
	${PYCODESTYLE} *.py
#	${PYTHON} -m pytest

clean:
	@echo "cleaning"

.PHONY: setup test clean help
