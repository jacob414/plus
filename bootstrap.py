#!/usr/bin/env python3
# yapf

import sys
import os
from os.path import expanduser as u

abspath = lambda base, *subdirs: os.path.join(os.path.abspath(u(base)), *subdirs)
exists = lambda path: os.path.exists(u(path))

if 'defs':
    origin = os.path.dirname(os.path.abspath(__file__))
    base = abspath('~/opt/plus')
    target = lambda *dirs: os.path.join(base, *dirs)


def ensuredir(fromdir, *subdirs):
    # type: (*subpath) -> None
    "Does ensuredir"
    full = abspath(fromdir, *subdirs)
    if exists(full):
        pass
    else:
        os.makedirs(full)


def bootstrap():
    # type: () -> None
    "Does bootstrap"

    if exists('~/opt/plus/vgpy/bin/ipython'):
        print('venv exist')
    else:
        ensuredir('~/opt/plus')
        import pdb
        pdb.set_trace()
        pass  # no virtualenv


if __name__ == '__main__':
    bootstrap()
