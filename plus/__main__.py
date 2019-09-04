# yapf

import sys
import os
from plus import conf


def cli_line(argvstring):
    # type: (argvstring) -> None
    "Does cli_line"
    first = argvstring.split(' ')[0]
    return conf.shortcut_path(first)


if __name__ == '__main__':
    if '-p' in sys.argv:
        shortcut = sys.argv[sys.argv.index('-p') + 1]
        cmd = cli_line(shortcut)
        rest = shortcut.replace(cmd.split('/')[-1], '').strip()
        print("{cmd} {rest}".format(**locals()))
