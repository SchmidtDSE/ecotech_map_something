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

#### Outline

1. A very quick motivation for mapping
2. Raster vs. Vector Data
	- quick examples of basic versions of each
	- touch on file-types
		- tiff vs cog
		- csv, geojson, shape, geoparquet, zarr
3. Mapping Libraries
	- geopandas
	- xarray
	- leafmap
	- geemap
	- datashader
	- lonboard
4. Usage
	- geopandas/xarray
	- leafmap
		- maptiles
		- tif
		- cog
		- vector
	- gee
		- geemap
		- gee (app)
	- lonboard
	- kepler.gl
		- notebook
		- app
5. Maybe
	- localtileserver https://localtileserver.banesullivan.com/
	- geopy
	- datashader
6. Supplemental
	- install mamba or conda
	- install gee
	- more on file-types
	- graphs/charts
	- interactive graphs/charts
	- h3
	- geohash

--- 

#### STYLE-GUIDE

Following PEP8. See [setup.cfg](./setup.cfg) for exceptions. Keeping honest with `pycodestyle .` and `mypy .`


