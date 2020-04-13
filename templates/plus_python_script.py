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
def _xc_name_xc_(ctx):
    "Docstring for {sname}"
    print(f"Implement the {{name}} python script.")
    
if __name__ == '__main__':
    _xc_name_xc_()
