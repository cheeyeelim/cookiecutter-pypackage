import os
import subprocess
import sys
from contextlib import contextmanager
from typing import List
from pathlib import Path

import pytest

# logging.basicConfig(level=logging.DEBUG)


_PYPROJECT_FILE = "pyproject.toml"
_LICENSE_FILE = "LICENSE"


# (A) Helper functions

@contextmanager
def inside_dir(dirpath):
    """Execute code from inside the given directory.

    Parameters
    ----------
    dirpath : str
        Path of the directory the command is being run.

    Returns
    -------
    None
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def execute(command: List[str], dirpath: str, timeout=30, supress_warning=True):
    """Run command inside given directory and returns output.

    If there's stderr, then it may raise exception according to supress_warning.

    Parameters
    ----------
    command : list[str]
        List of commands to be run.
        E.g. ["python main.py --help"]
    dirpath : str
        Path of the directory the command is being run.
    timeout : int
        Seconds to command timeout.
    supress_warning : bool
        Whether to suppress warning.

    Returns
    -------
    out : string
        Output from standard out.
    """
    with inside_dir(dirpath):
        proc = subprocess.Popen(
            command,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )

    out, err = proc.communicate(timeout=timeout)
    out = out.decode("utf-8")
    err = err.decode("utf-8")

    if err and not supress_warning:
        raise RuntimeError(err)
    else:
        print(err)
        return out



# (B) Tests

def test_bake_with_defaults(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "python-boilerplate"
    assert result.project_path.is_dir()

    # Test presence of key files/folders
    assert (result.project_path / _PYPROJECT_FILE).exists()
    assert (result.project_path / "python_boilerplate").exists()
    assert (result.project_path / "setup.cfg").exists()
    assert (result.project_path / "makefile").exists()
    assert (result.project_path / ".pre-commit-config.yaml").exists()
    assert (result.project_path / "mkdocs.yml").exists()
    assert (result.project_path / ".bumpversion.cfg").exists()
    assert (result.project_path / "docs").exists()
    assert (result.project_path / "tests").exists()
    assert (result.project_path / ".github").exists()

    # Test license creation
    assert "MIT " in (result.project_path / _LICENSE_FILE).read_text()
    assert "MIT" in (result.project_path / _PYPROJECT_FILE).read_text()

    # Test lint rule
    flake8_conf_file_path = (result.project_path / "setup.cfg")
    assert "docstring-convention = google" in flake8_conf_file_path.read_text()

    # Test doc build
    mkdocs_yml = result.project_path / "mkdocs.yml"
    with open(mkdocs_yml, "r") as f:
        lines = f.readlines()
        assert "  - Home: index.md\n" in lines


@pytest.mark.parametrize("license_info", [
    ("MIT", "MIT "),
    ("BSD-3-Clause", "Redistributions of source code must retain the " +
     "above copyright notice, this"),
    ("ISC", "ISC License"),
    ("Apache-2.0", "Licensed under the Apache License, Version 2.0"),
    ("GPL-3.0-only", "GNU GENERAL PUBLIC LICENSE"),
    ("Not open source", ""),
])
def test_bake_selecting_license(cookies, license_info):
    license, target_string = license_info

    result = cookies.bake(extra_context={"open_source_license": license})

    if license == "Not open source":
        assert (result.project_path / _PYPROJECT_FILE).exists()
        assert not (result.project_path / _LICENSE_FILE).exists()

        assert "License" not in (result.project_path / "README.md").read_text()
        assert "license" not in (result.project_path / _PYPROJECT_FILE).read_text()
    else:
        assert target_string in (result.project_path / _LICENSE_FILE).read_text()
        assert license in (result.project_path / _PYPROJECT_FILE).read_text()
