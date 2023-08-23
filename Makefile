VENV     = _venv
PYTHON   = python3
PIP      = pip
PYLINT   = pylint
AUTOPEP8 = autopep8
PYTEST   = pytest
RM       = rm -rf

SOURCES  = src tests

DO-VENV  = . $(VENV)/bin/activate;

.PHONY: all http test dist lint clean distclean

all: lint test dist

$(VENV):
	$(PYTHON) -m venv $@
	$(DO-VENV) $(PIP) install --upgrade pip
	$(DO-VENV) $(PIP) install -r requirements.txt

http: $(VENV)
	$(DO-VENV) cd src && $(PYTHON) -m partibus.http_server

test: $(VENV)
	$(DO-VENV) $(PYTEST)

dist: $(VENV)
	$(DO-VENV) $(PYTHON) -m build

lint: $(VENV)
	$(DO-VENV) $(PYLINT) $(SOURCES)
	$(DO-VENV) $(AUTOPEP8) -aaa -r --in-place --exit-code $(SOURCES)

clean:
	$(RM) $(VENV) {.,./src}/partibus.egg-info

distclean: clean
	$(RM) dist
