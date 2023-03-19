from setuptools import setup, find_packages
from os import path

from t3_cli import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().split()

setup(
    name="T3 Labs CLI",
    version=__version__,
    description='Command line client and utilities for T3 Labs and evaluate models Deep Learning',
    classifiers=[
        "Development Status :: Alpha",
        "Topic :: Utilities :: CLI",
        "Framework :: Click",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='T3 Labs CLI',
    author="Andre Emidio",
    author_email='andresjc2008@gmail.com',
    url='https://github.com/T3-Labs/t3-cli',
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    zip_safe=True,
    install_requires=requirements,
    entry_points='''
        [console_scripts]
            t3 = t3_cli.__main__:cli
            ''',
)
