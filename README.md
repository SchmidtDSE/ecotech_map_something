## Map Something

_A quick overview of putting things on maps_

This repo contains the (myst) markdown, code and data used to produce [this](https://schmidtdse.github.io/ecotech_map_something/) talk.

The presentation is part of DSE's [EcoTech Series](https://dse.berkeley.edu/news/ecotech-connect
) for 2024.


Visit https://dse.berkeley.edu to learn more

--- 

#### INSTALL

1. clone the repository

```bash
git clone https://github.com/SchmidtDSE/ecotech_map_something.git
cd ecotech_map_something
```

2. fetch the data

The data can be downloaded from google-cloud-storage, as a zip-file, or file by file:

zip-file: https://storage.googleapis.com/ecotech-map-something/data.zip
folder: https://console.cloud.google.com/storage/browser/ecotech-map-something/data

The "data" directory should be place at the root of the repo with this structure:
```
data
├── raster
│	├── cogs
│	├── tahoe-dem.tif
│	└── tahoe-mean-s2-20210101_20210301.tif
└── vector
    └── CalFires_Boundaries21
        ├── CalFires_Boundaries21.cpg
        ├── CalFires_Boundaries21.dbf
        ├── CalFires_Boundaries21.prj
        ├── CalFires_Boundaries21.shp
        └── CalFires_Boundaries21.shx
```

3. install requirements

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


