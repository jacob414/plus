# yapf

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = (
    'Jinja2==2.10',
    'PyMonad==1.3',
    'PyYAML==5.1',
    'funcy>=1.10.2',
    'pysistence>=0.4.1',
    'altered_states==1.0.9',
    'arrow==0.12',
    'click>=7.0',
    'crayons>=0.2.0',
    'clipboard',
    'datadiff==2.0.0',
    'docker[tls]==3.7.2',
    'hypothesis==4.24.3',
    'importmagic==0.1.7',
    'invoke==1.2.0',
    'ipdb==0.12',
    'jsonpickle==1.1',
    'keyboard==0.13.2',
    'meta',
    'mock==3.0.5',
    'paramiko==2.5.0',
    'patterns==0.3',
    'psutil==5.6.3',
    'pytest>=4.4',
    'redbaron==0.9.2',
    'scp==0.13.2',
    'yapf==0.27.0',
    'beautifulsoup4>=4.8',
    'jupyter_core==4.5.0',
    'jupyter>=1.0.0',
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
