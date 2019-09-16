# yapf

import os
import sys
import glob
from os.path import expanduser as u
from plus import conf

from tempfile import mkstemp
from shutil import move
from os import fdopen, remove


def replace(file_path, pattern, subst):
    """
    Thanks Thomas Watnedal!
    https://stackoverflow.com/a/39110/288672
    """
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


if __name__ == '__main__':
    correct_shebang = '#!{}{}'.format(conf.values.vpython, os.linesep)
    for script in (
            fn for fn in glob.glob(os.path.join(conf.values.pyenv, 'bin', '*'))
            if 'bin/python' not in fn and '__pycache__' not in fn):
        with open(script) as fp:
            firstline = fp.readline()

        if firstline != correct_shebang:
            replace(script, firstline, correct_shebang)
