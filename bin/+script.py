#!/usr/bin/env python3
import click
from plus import template
import plus
from plus import conf
from typing import Any
import os
import subprocess
import plus


@click.command()
@click.argument("name", nargs=1)
@click.argument("args", nargs=-11)
def main(name: str, args: Any) -> None:
    "Creates script"
    if name.endswith('.py'):
        template_ = 'plus_python_script'
        verb = name.replace('.py', '').replace('+', '')
    else:
        template_ = 'shell-template'
        verb= name.replace('+', '')

    source = template.expand(template_, name=name, verb=verb, args=args)
    path = os.path.join(os.path.dirname(__file__), name)

    # here
    with open(path, 'w') as fp:
        fp.write(source)
        os.chmod(path, 0o744)

    plus.edit(path)


if __name__ == '__main__':
    plus.monitored()
    main()
