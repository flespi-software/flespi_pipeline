init:
	virtualenv -p python3.5 env
	env/bin/pip install -U setuptools
	env/bin/pip install -r requirements.txt

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*__pycache__' -exec rm --force --recursive {} +

clean-all: clean-pyc
	rm --force --recursive env/

test:
	env/bin/python3.5 pipeline.py
