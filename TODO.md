# To do lists

## To add

1. [DONE] Add `tox-conda` to allow discovery of python versions installed under conda (both project and template)
2. [DONE] Add doc revision date with `mkdocs-git-revision-date-plugin` (both project and template)
3. Add test for `poetry install -E doc -E dev -E test` on project template to ensure no library version conflict


## To modify

1. [DONE] Move `CONTRIBUTING.rst` into markdown format under `docs` (project only)
2. [DONE] Update `tox` to test documentation building with mike (both project and template)
3. [DONE] Remove support for py36. Only support py37, py38, py39 (both project and template)
4. [DONE] Update test to remove warnings from `pytest-cookies` (project only)
5. [DONE] Remove options for `mypy` and `pre-commit`
