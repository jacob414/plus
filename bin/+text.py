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
def text(ctx):
    "Docstring for text"
    print(f"Implement the text python script.")


if __name__ == '__main__':
    text()
