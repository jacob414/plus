# yapf

from plus import conf

import click
from os.path import join
import os
import subprocess
import sys
from functools import partial

import funcy as fy

from plumbum.commands.processes import ProcessExecutionError
from plumbum import local, FG, BG
from plumbum.cmd import grep


mdfind_ = local.get('mdfind')
SKIP = {'Application Support', 'ichat', 'agilebits', 'ics'}
import re
SKIPRX = re.compile('[Application Support|ichat|agilebits|ics]')

def skip(txt):
    for pat in SKIP:
        if pat in txt: return True
    return False


@click.command()
@click.argument('phrase', nargs=1)
@click.option('--short/--long', default=False)
@click.pass_context
def find(ctx, phrase:str, short:bool):
    "Docstring for find"
    for path in filter(lambda v: not skip(v), fy.compact(mdfind_[f'"{phrase}"']().split('\n'))):
        if short:
            print(path)
        else:
            try:
                with open(path, 'r') as fp:
                    lines = fp.readlines()
                    for line, txt in enumerate(lines):
                        if phrase in txt:
                            print(f"{path}:{line+1}")
            except UnicodeDecodeError:
                pass


if __name__ == '__main__':
    find()
