import os
import re
from setuptools import setup

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

version=get_version('s3_template_loader')

setup(
    name="django-s3-template-loader",
    version=version,
    description="Django app to load templates from a s3 bucket",
    long_description=open('README.rst').read(),
    author="Benjamin Oertel",
    author_email="benjamin.oertel@gmail.com",
    url="https://boertel.github.io/django-s3-template-loader",
    license="BSD-3-Clause",
    include_package_data=True,
    packages=['s3_template_loader'],
    install_requires=[
        "Django>=3.0",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)
