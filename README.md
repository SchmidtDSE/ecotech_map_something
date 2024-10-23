## Map Something

_A quick overview of putting things on maps_

This repo contains the (myst) markdown, code and data used to produce [this](https://schmidtdse.github.io/ecotech_map_something/) talk.

The presentation is part of DSE's [EcoTech Series](https://dse.berkeley.edu/news/ecotech-connect
) for 2024.


Visit https://dse.berkeley.edu to learn more

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

#### OUTLINE

1. Map Rasters!
    - geotiffs
    - projections, crs, and affine-transforms
    - xarray
    - cogs
    - zarr
    - leafmap
2. Map vectors!
    - geopandas
    - file-types
    - leafmap
    - lonboard
3. GEE
    - code editor
    - apps
    - geemap

--- 

#### STYLE-GUIDE

Following PEP8. See [setup.cfg](./setup.cfg) for exceptions. Keeping honest with `pycodestyle .` and `mypy .`


