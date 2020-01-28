# yapf

import os
import glob
from jinja2 import Template
from builtins import str
from datetime import datetime

import re
import itertools
from functools import reduce

from plus import conf

now = datetime.now()

BUILTINS = {
    'YYYY': now.year,
    'YY': now.year - 2000,
    'MM': str(now.month).zfill(2),
    'MM': str(now.month).zfill(2),
    'HH': str(now.hour).zfill(2),
    'DD': str(now.day).zfill(2),
    'hh': str(now.hour).zfill(2),
    'mm': str(now.minute).zfill(2),
    'ss': str(now.second).zfill(2),
    'isodate': now.strftime('%Y-%m-%d'),
    'isots': now.strftime('%Y-%m-%d %H:%M:%S'),
}


def myfind(name):
    # type: (name) -> None
    "Does myfind"
    sw = conf.values.src
    name = name.split('.')[0]
    pat = f"{sw}/templates/{name}.*"
    hits = glob.glob(pat)
    if len(hits) == 1: return hits[0]
    elif len(hits) == 0:
        raise Exception("Template {name} not found".format(**locals()))
    elif len(hits) > 1:
        raise Exception("Template {name} name ambigous".format(**locals()))

def preprocess_python(fp):
    # type: (str) -> str
    "Does preprocess_python"
    alt = ''
    exp = ''
    res = ''

    lines = fp.readlines()

    symreplaced = ''.join(line for line in lines if '# skipline' not in line)
    for line in symreplaced.split(os.linesep):
        if '#%' in line:
            tagline = line.strip().replace('#%', '{%') + ' %}'
            alt += line.split('#%')[0] + tagline
        else:
            alt += line + os.linesep
    return alt


def expand(name_, **expansions):
    # type: (name, **expansions) -> None
    "Does expand"
    expansions.update(BUILTINS)
    expansions['tmplname'] = name_
    render = lambda raw: Template(raw).render(**dict(expansions,
                                                     tmplname=name_))
    path = myfind(name_)
    with open(path) as fp:
        if path.endswith('.py'):
            raw = preprocess_python(fp)
            pass
        else:
            raw = fp.read()
        try:
            return render(raw)
        except UnicodeDecodeError:
            return render(raw.decode('utf-8'))


def write(name, destination, **expansions):
    # type: () -> None
    "Does createfile"
    with open(destination, 'w') as fp:
        fp.write(expand(name, **expansions))
