from setuptools import setup

from greenery import __version__

setup(
    name = "greenery",
    version = __version__,
    tests_require = [ "pytest" ],
    packages = [ "greenery" ],
    package_dir = { "greenery": "greenery" },
    author = "Sam Hughes",
    author_email = "qntm <qntm@ferno>",
    description = "Greenery allows manipulation of Regular Expressions as Finite State Machines",
    license = "MIT License",
    keywords = "greenery regex fsm",
    url = "https://github.com/ferno/greenery",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ],
)
