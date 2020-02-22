import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="settingsd",
    version="0.1.0",
    author="Nicholas Kostelnik",
    author_email="nkostelnik@gmail.com",
    description=("A dbus service to host desktop settings"),
    license="MIT",
    keywords="wayland dbus",
    url="http://packages.python.org/settingsd",
    packages=find_packages(where='.'),
    long_description=read('README.md'),
    scripts=['bin/settingsd'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: MIT License",
    ],
)
