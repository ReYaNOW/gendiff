install:
	poetry install
brain-games:
	poetry run gendiff
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