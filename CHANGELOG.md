# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.2] - 2021-12-12

* Fixed CHANGELOG format to let mindsers/changelog-reader-action recognise version number correctly
* Updated mkdocs and urllib3 versions
* mkdocs - added light/dark mode toggle, navigation improvements
* mike - added multiple documentation versions support
* tox - added conda support (for multiple python versions)
* urllib3 - removed certain security vulnerabilities
* Replaced testing with mike, rather than mkdocs
* Updated tests to remove warnings from `pytest-cookies`
* Added tests to ensure template get built correctly
* Updated and cleaned up documentations
* Removed optionality for `mypy` and `pre-commit`
* Removed support for py36

## [1.1.1] - 2021-10-18

* Centralize most of the tool configuration in the `setup.cfg` file

## [1.1.0] - 2021-10-15

* Add `use_mypy` choice to make mypy optional

## [1.0.1] - 2021-04-22
***first release with the following features:***

* [Poetry](https://python-poetry.org/): Manage dependency, build and release
* [Mkdocs](https://www.mkdocs.org): Writing your docs in markdown style
* Testing with [Pytest](https://pytest.org) (unittest is still supported out of the box)
* Code coverage report and endorsed by [Codecov](https://codecov.io)
* [Tox](https://tox.readthedocs.io): Test your code against environment matrix, lint and artifact check
* Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
* Lint code with [Flake8](https://flake8.pycqa.org) and [Flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
* Check static type with [Mypy](http://mypy-lang.org/) (optional)
* [Pre-commit hooks](https://pre-commit.com/): Formatting/linting anytime when commit your code
* [Mkdocstrings](https://mkdocstrings.github.io/): Auto API doc generation
* Command line interface using [Click](https://click.palletsprojects.com/en/8.0.x/) (optional)
* [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command
* Continuous Integration/Deployment by [GitHub actions](https://github.com/features/actions), includes:
    - publish dev build/official release to TestPyPI/PyPI automatically when CI success
    - publish documents automatically when CI success
    - extract changelog from CHANGELOG and integrate with release notes automatically
* Host your documentation from [GitHub Pages](https://pages.github.com) with zero-config
