# Console Script Setup

# How It Works

Cookiecutter will add a file `cli.py` in the `pkg_name` subdirectory. 
An entry point is added to `pyproject.toml` that points to the main executable function.

# Usage

To use the console script in development:

``` bash
poetry install
```

Then execute:
```
$project_slug --help
```

it will show your package name, project short description and exit.
