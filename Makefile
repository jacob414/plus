#!/bin/sh
# Error codes, see http://tldp.org/LDP/abs/html/exitcodes.html

SCRIPTPATH=.
include plusenv
SYSPY=$(shell which python3)
ABS_PLUS_SRC=$(shell realpath $(PLUS_SRC))

include ~/.config/plusrc
-include ~/.config/plusrc

all: $(PLUS_PYENV) ruby

cust-pkg:
	cd $(PLUS_SRC)
	$(PLUS_PIP) -e install .

show:
	@echo $(ABS_PLUS_SRC)

$(PLUS_PYENV):
	$(SYSPY) -m venv $(PLUS_VPYTHON_OPTS) $@
	make cust-pkg
	$(PLUS_VPYTHON) -m plus.post_install
	chmod +x $(PLUS_PYENV)/bin/*

BUNDLER=$(PLUS_RUBY)/bin/

$(PLUS_RUBY)/bin/bundler:
	$(PLUS_RUBY)/bin/gem install bundler

gems: $(PLUS_RUBY)/bin/bundler
	(cd $(PLUS_SRC) ; $(PLUS_RUBY)/bin/bundler install)

.PHONY: bundler
bundler: $(PLUS_RUBY)/bin/bundler gems

~/.rbenv/versions/2.4.7:
	rbenv install 2.4.7

ruby: ~/.rbenv/versions/2.4.7 gems

clean:
	rm -rf $(PLUS_PYENV)

rebuild: clean all
