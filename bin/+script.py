#!/usr/bin/env python3
import click
from hs import template
import plus
from plus import conf
from typing import Any
import os
import subprocess


@click.command()
@click.argument("name", nargs=1)
@click.argument("args", nargs=-11)
def main(name: str, args: Any) -> None:
    "Creates script"
    if name.endswith('.py'):
        template_ = 'python-mall.py'
    else:
        template_ = 'shell-template'

    with open(name, 'w') as fp:
        fp.write(template.expand(template_, sname=name, args=args))
    os.chmod(name, 0o744)
    plus.emacs(name)

    priopath = conf.path(f'bin/{name}')
    if name.endswith('.py') and os.path.exists(priopath):
        bare, _ = name.split('.py')
        nopy = f'bin/{bare}'
        with plus.cd(conf.base):
            os.symlink(name, nopy)
            with open(conf.path('.gitignore'), 'a') as ignore:
                ignore.write(os.linesep + nopy)
    else:
        template_ = 'skal-mall.sh'


if __name__ == '__main__':
    main()
