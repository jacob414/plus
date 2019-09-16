# yapf

import sys
import os
from plus import conf


def cli_line(argvstring, params):
    # type: (str, List[str]) -> str
    "Does cli_line"
    first = argvstring.split(' ')[0]
    return conf.shortcut_path(first, params)


if __name__ == '__main__':
    if '-p' in sys.argv:
        p_i_ = sys.argv.index('-p')
        shortcut = sys.argv[p_i_ + 1]
        cmd = cli_line(shortcut, sys.argv[p_i_ + 1:])
        print(cmd)
