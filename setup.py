import codecs
import os

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


setup(
    name='myvr-python',
    version=get_version('myvr/__init__.py'),
    description='Python wrapper for MyVR API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/myvr/myvr-python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GNU GENERAL PUBLIC LICENSE',
        'Operating System :: OS Independent',
    ],
    author='MyVR',
    packages=['myvr'],
    install_requires=[],
    python_requires='>=3.6, <4',
)
