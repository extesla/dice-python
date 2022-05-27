from setuptools import setup
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, "README.md")).read()
    CHANGES = open(os.path.join(here, "CHANGELOG")).read()
except:
    README = """\
dice-python is a dice rolling library."""
    CHANGES = ""

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: No Input/Output (Daemon)",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Topic :: System :: Monitoring",
    "Topic :: System :: Utilities",
]

dist = setup(
    name="dice",
    version='0.5.0-dev',
    license="MIT License (http://opensource.org/licenses/MIT)",
    url="https://github.com/extesla/dice-python/",
    description="A dice rolling library",
    long_description=README + "\n\n" + CHANGES,
    classifiers=CLASSIFIERS,
    author="Sean W. Quinn",
    author_email="sean.quinn@extesla.com",
    packages=["dice"],
    install_requires=[
        "pyparsing>=2.2.0",
        "six==1.11.0"
    ],
    extras_require={
        "dev": [
            "pytest==3.3.2",
            "pytest-cov==2.5.1"
            "pytest-mock==1.6.3"
        ],
    },
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
)
