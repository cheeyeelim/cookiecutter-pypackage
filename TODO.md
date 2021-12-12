# To do lists

## To add

1. Pre-commit hooks to do same checks to `cookiecutter-pypackage`
2. Add end to end project creation unit testing - Check `cookiecutter https://github.com/cheeyeelim/cookiecutter-pypackage.git` works
3. [DONE] Add `tox-conda` to allow discovery of python versions installed under conda (both project and template)
4. Add doc revision date with `mkdocs-git-revision-date-plugin` (both project and template)

## To modify

1. [DONE] Move `CONTRIBUTING.rst` into markdown format under `docs`.
2. [DONE] Update `tox` to test documentation building with mike (both project and template)
3. [DONE] Remove support for py36. Only support py37, py38, py39 (both project and template)