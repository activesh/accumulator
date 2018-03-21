.PHONY: black clean test

black:
	black ./ -l 79 --fast

clean: clean-pyc clean-cache

# clean-build:
#     rm -fr build/
#     rm -fr dist/
#     rm -fr *.egg-info

clean-cache:
	find ./.pytest_cache -type f -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test:
	pytest
