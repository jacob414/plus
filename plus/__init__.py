import os
import subprocess

from contextlib import contextmanager

def edit(path) -> None:
    "Does edit"
    return subprocess.Popen(['emacsclient', path], stdout=subprocess.PIPE)

@contextmanager
def cd(path):
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_dir)
