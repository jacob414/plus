#!/usr/bin/env python3
import click
from plus import template
import plus
from plus import conf
from typing import Any
import os
import subprocess
from micropy import testing
from funcy import flow


@click.command()
@click.argument("name", nargs=1)
@click.argument("args", nargs=-11)
def main(name: str, args: Any) -> None:
    "Creates script"
    if name.endswith('.py'):
        template_ = 'plus_python_script'
    else:
        template_ = 'shell-template'

    priobin, priopath = conf.values.path('bin/'), conf.values.path(
        f'bin/{name}')
    source = template.expand(template_, sname=name, args=args)

    try:
        import ipdb
        ipdb.set_trace()
        pass
        with open(name, 'w') as fp:
            fp.write(source)
            os.chmod(name, 0o744)
            plus.edit(name)
    except:
        pass

    if name.endswith('.py') and os.path.exists(priopath):
        bare, _ = name.split('.py')
        nopy = conf.values.path(f'bin/{bare}')
        with plus.cd(conf.values.base), flow.suppress(OSError):
            os.symlink(priopath, nopy)
    else:
        template_ = 'skal-mall.sh'


if __name__ == '__main__':
    import ipdb
    testing.hook_uncatched(ipdb.post_mortem)
    main()
