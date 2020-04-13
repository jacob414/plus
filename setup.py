# yapf

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = (
    'Jinja2',
    'PyMonad',
    'PyYAML',
    'funcy',
    'pysistence',
    'altered_states',
    'arrow',
    'click',
    'crayons',
    'clipboard',
    'datadiff',
    'docker[tls]',
    'hypothesis',
    'importmagic',
    'invoke',
    'ipdb',
    'jsonpickle',
    'keyboard',
    'meta',
    'mock',
    'paramiko',
    'patterns',
    'psutil',
    'pytest',
    'redbaron',
    'scp',
    'yapf',
    'beautifulsoup4',
    'jupyter_core',
    'jupyter',
)  # yapf: disable

if sys.version_info.major < 3:
    # Python 2 compatibility hack
    dependencies = dependencies + (
        'backports.lzma',
        'backports.shutil_which==3.5.2',
        'ipython>=5.8.0')  # yapf: disable
else:
    # Python 3 / 2 conflicting packages
    dependencies = dependencies + (
        'ipython_genutils>=0.2.0',
        'ipython>=7.8.0',
    )

setup(
    name='plus',
    version='0.0.1',
    description="jacob414's automation toolskit.",
    long_description="jacob414's automation toolskit.",
    install_requires=dependencies,
    packages=('plus',),
)  # yapf: disable
