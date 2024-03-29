#! /usr/bin/env python3
"""Install script."""

from setuptools import setup


setup(
    name="contactmgr",
    use_scm_version={"local_scheme": "node-and-timestamp"},
    setup_requires=["setuptools_scm"],
    install_requires=[
        "configlib",
        "flask",
        "his",
        "mdb",
        "peewee",
        "peeweeplus",
        "wsgilib",
    ],
    author="HOMEINFO - Digitale Informationssysteme GmbH",
    author_email="<info@homeinfo.de>",
    maintainer="Richard Neumann",
    maintainer_email="<r.neumann@homeinfo.de>",
    packages=["contactmgr"],
    license="GPLv3",
    description="HIS microservice to handle contacts of customers.",
)
