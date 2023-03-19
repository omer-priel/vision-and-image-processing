# build
clean-all: clean
	rm -rf .venv poetry.lock

install:
	poetry install

# CI / CD
clean:

# start
start-jupyterlab:
	poetry run jupyter lab
