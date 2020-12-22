import codecs
import os

from setuptools import find_packages
from setuptools import setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open('README.md') as readme:
    long_description = readme.read()


install_requires = [
    'requests==2.25.0',
]


setup(
    name='myvr-python',
    version=get_version('myvr/__init__.py'),
    description='Python wrapper for MyVR API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GNU',
    url='https://github.com/myvr/myvr-python',
    download_url='https://github.com/myvr/myvr-python/archive/0.0.3.tar.gz',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    key_words=['MyVR', 'API', 'client', 'wrapper'],
    author='MyVR',
    packages=find_packages(
        include=[
            'myvr',
            'myvr.*',
        ]
    ),
    install_requires=install_requires,
    python_requires='>=3.7, <4',
)
