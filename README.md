# Cookiecutter PyPackage

Cookiecutter template for a Python package, built with popular develop tools and
conform to best practice.

[![CI Status](https://github.com/cheeyeelim/cookiecutter-pypackage/actions/workflows/dev.yml/badge.svg)](https://github.com/cheeyeelim/cookiecutter-pypackage/actions/workflows/dev.yml)
[![License](https://img.shields.io/pypi/l/ppw)](https://opensource.org/licenses/BSD-2-Clause)

* Documentation: <https://cheeyeelim.github.io/cookiecutter-pypackage>

## Features

This tool will create Python project with the following features:

* [Poetry](https://python-poetry.org/): Manage dependency, build and release
* [Pre-commit](https://pre-commit.com/): Formatting/linting anytime when commit your code
* [hydra](https://hydra.cc/) - Manage complex package configurations, command line interface and systematic logging
* [Mkdocs](https://www.mkdocs.org): Writing your docs in markdown style
* [Mkdocstrings](https://mkdocstrings.github.io/): Auto API doc generation
* [Pytest](https://pytest.org): Unit testing your codes
* [Codecov](https://codecov.io): Generate code coverage report
* [Tox](https://tox.readthedocs.io): Test your code against environment matrix, lint and artifact check
* [Mypy](http://mypy-lang.org/): Static type checking
* [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command
* [GitHub actions](https://github.com/features/actions): Continuous integration/deployment with the following actions
    - Publish dev build/official release to TestPyPI/PyPI automatically when CI success
    - Publish documents automatically when CI success
    - Extract changelog from CHANGELOG and integrate with release notes automatically
* [GitHub Pages](https://pages.github.com): Documentation hosting with zero-config

## How to use this template?

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/cheeyeelim/cookiecutter-pypackage.git
```

Then follow **[Tutorial](docs/tutorial.md)** to finish other configurations.

## How to develop this package further?

1. Update codes as needed.
2. (Test locally) Test that codes are working as intended.
   1. Test locally (all in one go)
      1. `poetry run tox`
      2. Internally `tox` will run unit testing, document generation and build tests.
   2. Test locally (one by one)
      1. `poetry run pytest` for unit testing
      2. `poetry run mike deploy vtest -m "test doc build" --ignore`
      3. `poetry run mike delete vtest -m "remove doc build" --ignore`
      4. `poetry run mkdocs serve` to see docs locally
    3. Test on cloud
       1. No need to do anything
       2. Follow later steps to push the codes to GitHub to trigger tests, as this repo has GitHub Workflows defined (in `.github/workflows`)
3. Run `pre-commit` by committing codes.
   1. `git add .`
   2. `git commit -m "a message"`
   3. Resolve any errors from `pre-commit` manually.
4. Rerun git add and commit to commit codes.
   1. Once happy with everything, `git push` the codes to cloud repo.
5. Done!

## Credits

This repo is forked from [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage/), which originally forked from [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage)
