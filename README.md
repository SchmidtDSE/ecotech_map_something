#### Map Something

A quick overview of putting things on maps

--- 

#### REQUIREMENTS

Requirements are managed through a conda yaml [file](./conda-env.yaml). To create/update the `ENV_NAME` environment:

```bash
# create
mamba env create -f conda-env.yaml
# update
mamba env update -f conda-env.yaml --prune
```

--- 

#### OVERVIEW

```
├── LICENSE.md
├── README.md
├── __init__.py
├── conda-env.yaml
├── main.md
├── map_something
│	└── __init__.py
├── myst
│	├── sections
│	│	├── big.md
│	│	├── data.md
│	│	├── discussion.md
│	│	├── intro.md
│	│	├── raster.md
│	│	└── vector.md
│	└── supplemental
│		└── notes.md
├── myst.yml
├── notes
│	└── scratch.md
├── pyproject.toml
└── setup.cfg
```

---

#### DOCUMENTATION

API Docss

--- 

#### STYLE-GUIDE

Following PEP8. See [setup.cfg](./setup.cfg) for exceptions. Keeping honest with `pycodestyle .` and `mypy .`


