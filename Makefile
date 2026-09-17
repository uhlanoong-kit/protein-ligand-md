.PHONY: download test clean

download:
	bash data/download_structures.sh

test:
	pytest

clean:
	rm -rf .pytest_cache build dist src/*.egg-info

