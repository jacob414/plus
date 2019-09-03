#!/usr/bin/env python3
# yapf

import sys
import os
from os.path import expanduser as u
import subprocess

INSTALL = u('~/opt/plus')
BASE = os.path.basename(__file__)

abspath = lambda base, *subdirs: os.path.join(os.path.abspath(u(base)),
                                              *subdirs)
exists = lambda path: os.path.exists(u(path))


def vpython(*subdirs):
    # type: (*subdirs) -> None
    "Does vpython"
    return os.path.join(INSTALL, *(('py', ) + subdirs))


def pip(*params):
    # type: (*params) -> None
    "Does pip"
    subprocess.check_call((vpython('bin', 'pip'), *params))


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

    args = sys.argv[1:]

    if exists(vpython('bin', 'python')):
        print('venv exist')
        if args:
            print('args')
            os.execv(vpython('bin', 'python'), sys.argv[1:])
        else:
            print(vpython('bin', 'python'), ('-m plus.plus_exec', ))
            os.execvpe(vpython('bin', 'python'), ('-m plus.plus_exec', ))
    else:
        import venv
        eb = venv.EnvBuilder(system_site_packages=False,
                             clear=False,
                             symlinks=False,
                             upgrade=False,
                             with_pip=True,
                             prompt=True)
        eb.create(vpython())
        pip('install', '-e', BASE)
        os.execv(vpython('bin', 'python'), sys.argv[1:])


if __name__ == '__main__':
    bootstrap()
