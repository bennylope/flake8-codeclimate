from __future__ import with_statement
import setuptools

requires = [
    "flake8 > 3.0.0",
]

setuptools.setup(
    name="flake8_codeclimate",
    license="MIT",
    version="0.1.0",
    description="Code Climate reporting formatter plugin for Flake8",
    author="Ben Lopatin",
    author_email="ben@benlopatin.com",
    url="https://github.com/bennylope/flake8-codeclimate",
    py_modules=['flake_codeclimate'],
    install_requires=requires,
    entry_points={
        'flake8.report': [
            'codeclimate = flake8_codeclimate:JSONFormatter',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
