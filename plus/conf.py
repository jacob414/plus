# yapf

import os
import glob

from funcy import namespace

from os.path import expanduser as u
from string import Template as T


class values(namespace):
    src = os.path.dirname(os.path.dirname(__file__))
    defaults_path = os.path.join(src, 'plusenv')
    mine_path = u('~/.config/plusrc')


def varsfile(path):
    # type: (path) -> None
    "Does varsfile"
    lines = None
    with open(path) as fp:
        lines = fp.readlines()
        return dict({'SCRIPTPATH': values.src}, **{
            key: val
            for (key, val) in [
                l.split('=') for l in lines
                if l.strip() and not l.startswith('#')
            ]
        })


def expand(env):
    # type: (env) -> None
    "Does expand"
    for key, value in env.items():
        value = value.replace('$1', '').strip()
        env[key] = T(value).substitute(def_env)
    return env


def_env = varsfile(values.defaults_path)
if os.path.exists(values.mine_path):
    my_env = varsfile(values.mine_path)
else:
    my_env = {'PLUS_MINE': ''}

def_env = dict(os.environ, **expand(def_env))
my_env = expand(my_env)
values.mine = my_env['PLUS_MINE']

if not hasattr(values, 'mine'):
    values.mine = os.environ.get('PLUS_MINE', False)

for k, v in [(k.split('PLUS_')[1].lower(), u(v)) for k, v in def_env.items()
             if k.startswith('PLUS_')]:
    setattr(values, k, v)


def plus_path(*segs):
    # type: (*str) -> str
    "Calculate a path inside the Plus installation directory."
    return os.path.join(values.base, *segs)


globcands = {
    '+{}*.py': 'python',
    '+{}': 'shell',
}


def reconsile(name, many):
    # type: (name, many) -> None
    "Does reconsile"
    raise NotImplementedError('tbd: reconsile')


exp_order_fns = lambda: filter(
    None,
    (
        # hidden relative to CWD
        './.+{}'.format,

        # in a directory named ./bin relative to CDW
        './bin/+{}'.format,

        # in the user's ~/bin directory
        u('~/bin/+{}').format,

        # if a 'hidden' directory have been specified, add the bin/
        # direcotry of it
        values.mine and '{}/bin/+{}'.format(values.mine, '{}').format or False,

        # The bin/ directory of the Python virtualenv
        '{}/bin/{}'.format(values.pyenv, '{}').format,
    )
)  # yapf: disable

interpreters = {
    'py': values.vpython,
    'js': values.node,
    'rb': values.ruby,
    'pl': values.perl
}


def shortcut_path(name):
    # type: (str) -> str
    "Finds the path of a shortcut"

    for pat in exp_order_fns():
        shortcut_path = pat(name)
        if os.path.exists(shortcut_path):
            return shortcut_path
        script_path = glob.glob(shortcut_path + '.??')
        if script_path:
            script_path = script_path[0]
            _, script_type = script_path.split('.')
            return '{} {}'.format(interpreters[script_type], script_path)

    raise ValueError('{} shortcut not found.'.format(name))
