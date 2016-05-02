import os
import sys

py_version = sys.version_info[:2]

if py_version < (2, 6):
    raise RuntimeError("On Python 2, dice-python requires Python 2.6 or later")
elif (3, 0) < py_version < (3, 2):
    raise RuntimeError("On Python 3, dice-python requires Python 3.2 or later")

tests_require = []
if py_version < (3, 3):
    tests_require.append("mock")

testing_extras = tests_require + [
    "nose",
    "nose-cov",
    ]

from setuptools import setup, find_packages
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
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: System :: Monitoring",
    "Topic :: System :: Utilities",
]

version_txt = os.path.join(here, "dice/version.txt")
dicepy_version = open(version_txt).read().strip()

dist = setup(
    name="dice-python",
    version=dicepy_version,
    license="MIT License (http://opensource.org/licenses/MIT)",
    url="https://github.com/extesla/dice-python/",
    description="A dice rolling library",
    long_description=README + "\n\n" + CHANGES,
    classifiers=CLASSIFIERS,
    author="Sean W. Quinn",
    author_email="sean.quinn@extesla.com",
    maintainer="Sean W. Quinn",
    maintainer_email="sean.quinn@extesla.com",
    packages=find_packages(),
    install_requires=requires,
    extras_require={
        "testing": testing_extras,
        },
    tests_require=tests_require,
    include_package_data=True,
    zip_safe=False,
    test_suite="test",
)
