install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vvvv

check:
	make lint
	make test

test-coverage:
	poetry run pytest --cov --cov-report term-missing --cov-report xml

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

bpp:
	make build
	make publish
	make package-install