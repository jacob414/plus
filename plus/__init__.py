import os
import subprocess

from . import conf


from contextlib import contextmanager

def edit(path, line:int = -1) -> None:
    "Does edit"
    if line > -1:
        subprocess.Popen(['emacsclient', path, f"+{line}:1"], stdout=subprocess.PIPE)
    else:
        subprocess.Popen(['emacsclient', path], stdout=subprocess.PIPE)

@contextmanager
def cd(path):
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_dir)

def monitored() -> None:
    "Does monitored"
    from kingston import testing
    testing.hook_uncatched(ipdb.post_mortem)
