#!/bin/sh
# Error codes, see http://tldp.org/LDP/abs/html/exitcodes.html

SCRIPTPATH=.
include plusenv
SYSPY=$(shell which python3)

-include ~/.config/plusrc

ifneq ("$(wildcard ~/.config/plusrc)","")
  $(info using custom directory)
  include ~/.config/plusrc

  .PHONY: cust-pkg
  cust-pkg:
	$(PLUS_PIP) install -e $(PLUS_MINE)/python/
else
  $(info not using custom directory)
  .PHONY: cust-pkg
  cust-pkg:
	@echo no
endif

all: $(PLUS_PYENV) cust-pkg

REAL_PLUS_SRC=$(shell realpath $(PLUS_SRC))/

show:
	@echo $(REAL_PLUS_SRC)

$(PLUS_PYENV):
	$(SYSPY) -m venv $(PLUS_VPYTHON_OPTS) $@
	cd ~
	$(PLUS_PIP) install -e $(REAL_PLUS_SRC)
	$(PLUS_VPYTHON) -m plus.post_install
	chmod +x $(PLUS_PYENV)/bin/*

clean:
	rm -rf $(PLUS_PYENV)

rebuild: clean all
