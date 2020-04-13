# yapf

from plus import conf

import click
from os.path import join
import os
import subprocess
import sys
from functools import partial


@click.command()
@click.pass_context
def _xo_verb_xc_(ctx):
    "Docstring for {{verb}}"
    print(f"Implement the {{verb}} python script.")


if __name__ == '__main__':
    _xo_verb_xc_()
