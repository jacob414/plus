#!/bin/sh
# Error codes, see http://tldp.org/LDP/abs/html/exitcodes.html

SCRIPTPATH=.
include plusenv
SYSPY=$(shell which python3)

all: $(PLUS_PYENV)

$(PLUS_PYENV):
	@echo "make pyenv"
	$(SYSPY) -m venv $(PLUS_VPYTHON_OPTS) $@
	$(PLUS_PIP) install -e $(PLUS_SRC)
	$(PLUS_VPYTHON) -m plus.post_install
	chmod +x $(PLUS_PYENV)/bin/*

clean:
	rm -rf $(PLUS_PYENV)

rebuild: clean all
