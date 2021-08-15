#!/usr/bin/env python

import os
import sys

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

_PATH_ROOT = os.path.realpath(os.path.dirname(__file__))
_PATH_REQUIRE = os.path.join(_PATH_ROOT, "requirements")

try:
    from pl_bolts import __about__ as about
    from pl_bolts import setup_tools
except ImportError:
    # alternative https://stackoverflow.com/a/67692/4521646
    sys.path.append("pl_bolts")
    import __about__ as about
    import setup_tools


def _prepare_extras():
    extras = {
        "loggers": setup_tools._load_requirements(path_dir=_PATH_REQUIRE, file_name="loggers.txt"),
        "models": setup_tools._load_requirements(path_dir=_PATH_REQUIRE, file_name="models.txt"),
        "test": setup_tools._load_requirements(path_dir=_PATH_REQUIRE, file_name="test.txt"),
    }
    extras["extra"] = extras["models"] + extras["loggers"]
    extras["dev"] = extras["extra"] + extras["test"]
    return extras


long_description = setup_tools._load_readme_description(
    _PATH_ROOT,
    homepage=about.__homepage__,
    ver=about.__version__,
)

# https://packaging.python.org/discussions/install-requires-vs-requirements /
# keep the meta-data here for simplicity in reading this file... it's not obvious
# what happens and to non-engineers they won't know to look in init ...
# the goal of the project is simplicity for researchers, don't want to add too much
# engineer specific practices
setup(
    name="lightning-bolts",
    version=about.__version__,
    description=about.__docs__,
    author=about.__author__,
    author_email=about.__author_email__,
    url=about.__homepage__,
    download_url="https://github.com/PyTorchLightning/lightning-bolts",
    license=about.__license__,
    packages=find_packages(exclude=["tests", "docs"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    keywords=["deep learning", "pytorch", "AI"],
    python_requires=">=3.6",
    setup_requires=["wheel"],
    install_requires=setup_tools._load_requirements(_PATH_ROOT),
    extras_require=_prepare_extras(),
    project_urls={
        "Bug Tracker": "https://github.com/PyTorchLightning/lightning-bolts/issues",
        "Documentation": "https://lightning-bolts.rtfd.io/en/latest/",
        "Source Code": "https://github.com/PyTorchLightning/lightning-bolts",
    },
    classifiers=[
        "Environment :: Console",
        "Natural Language :: English",
        # How mature is this project? Common values are
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Information Analysis",
        # Pick your license as you wish
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
