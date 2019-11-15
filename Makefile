init:
	virtualenv -p python3.5 env
	env/bin/pip install -U setuptools
	env/bin/pip install -r requirements.txt

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*__pycache__' -exec rm --force --recursive {} +

clean-all: clean-pyc
	rm --force --recursive env/

run:
	@env/bin/python3.5 pipeline.py

test: run

test-merge:
	@env/bin/python3.5 merging_pipeline.py

test-inject:
	@env/bin/python3.5 injecting_pipeline.py
