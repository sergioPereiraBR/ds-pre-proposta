# Copyright (c) Pereira Dev Analytics, Inc. and its affiliates.
#
# This source code is licensed under the Pereira Dev Analytics license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("pre-proposta/__init__.py") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split('"')[1]

with open("requirements.txt") as f:
    requires = f.read().strip().splitlines()

setup(
    name="pre-proposta",
    description="Geração de Pré-proposta para projetos de Energia Solar no formato PDF",
    long_description=readme,
    long_description_content_type="text/markdown",
    version=version,
    author="Sérgio Pereira, Pereira Dev Analytics",
    author_email="sergiopereira.br@hotmail.com",
    url="https://github.com/sergioPereiraBR/ds-pre-proposta.git",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: Restrict :: Pereira Dev License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    license="Pereira Dev",
    packages=["pre-proposta", "pre-proposta.tests"],
    test_suite="pre-proposta.tests",
    setup_requires=[">=75.3.0"],
    install_requires=requires,
    entry_points={"console_scripts": ["pre-proposta = pre-proposta.main:main"]},
)