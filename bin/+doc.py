# yapf

from plus import conf

import click
from os.path import join
import os
import subprocess
import sys
from functools import partial
import glob
from time import gmtime
from datetime import datetime


@click.command()
@click.pass_context
def doc(ctx):
    "Docstring for doc"
    for name in glob.glob('./*'):
        print(name)
        inf = os.stat(name)
        tt = gmtime(inf.st_atime)
        dt = datetime(tt.tm_year, tt.tm_mon, tt.tm_mday, tt.tm_hour, tt.tm_min,
                      tt.tm_sec)
        dtprefix = dt.strftime('%y-%m-%d')
        _, fn = os.path.split(name)
        fn, suff = fn.split('.')
        os.rename(name, ''.join((dtprefix, '-', fn, '.', suff)))


if __name__ == '__main__':
    doc()
