# yapf

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = (
    'Jinja',
    'PyMonad',
    'PyYAML',
    'funcy',
    'pysistence',
    'altereds==1.0.9',
    'arrow',
    'click',
    'crayons',
    'clipboard',
    'datadiff',
    'docker[tls]',
    'hypothesis',
    'importmagic',
    'invoke',
    'ipdb2',
    'jsonpickle',
    'keyboard',
    'meta',
    'mock',
    'paramiko',
    'patterns',
    'psutil',
    'pytest',
    'redbaron',
    'scp2',
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