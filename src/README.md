# README for a new package

Do the following for building with poetry

Create the following directory structure:
```
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── example_package_YOUR_USERNAME_HERE/
│       ├── __init__.py
│       └── example.py
└── tests/
```

Create pyproject.toml file:

```
[tool.poetry]
name = "new_package"
version = "0.1.0"
description = ""
authors = ["Jannetta Steyn <6432530+jsteyn@users.noreply.github.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Run `poetry update` to create a poetry.lock file

Run `poetry add pytest`

### Links
- [How to create a Python Package with __init__.py ](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html)
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [How to install, download and build Python wheels](https://www.activestate.com/resources/quick-reads/python-install-wheel/)
- 