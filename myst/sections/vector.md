(vector)=
# Vector
_points, lines, polygons_

---

## FILETYPES

There are lots of file-types!

- csv (point data)
- shapefile
- geojson
- geopackage
- flatgeobuf
- geoparquet


Read more about them here: [guide.cloudnativegeo.org](https://guide.cloudnativegeo.org/).
[Geoparquet](https://geoparquet.org/) is exciting! smaller file sizes and faster reads. TLDR; columnar data format with row grouping and great compression. In the dataset we'll be discussing one see improvement, though somewhat minor, for read, write, storage:


```{embed} #nb:vector:filetypes
:remove-output: false
:remove-input: false
```

However, this isn't capturing the performace gains captured by the columnar data + row grouping. A detailed performance comparison can be found here: https://cloudnativegeo.org/blog/2023/08/performance-explorations-of-geoparquet-and-duckdb/



```{image} ../../assets/vector-performance
:alt: performance of different data-type
:width: 100%
:align: center

source: https://cloudnativegeo.org/blog/2023/08/performance-explorations-of-geoparquet-and-duckdb
```


---

## GEOPANDAS

We'll start by loading historical CalFires data from 1898 through 2021. An updated version of this data can be found [here](https://www.fire.ca.gov/what-we-do/fire-resource-assessment-program/gis-mapping-and-data-analytics).


```{embed} #nb:vector:gpd
:remove-output: false
:remove-input: false
```

```{embed} #nb:vector:gpdplot
:remove-output: false
:remove-input: false
```

---

## LEAFMAP

[leafmap](https://leafmap.org/)

_\"Leafmap is a Python package for interactive mapping and geospatial analysis with minimal
coding in a Jupyter environment._

_Leafmap supports multiple mapping backends, including ipyleaflet, folium, kepler-gl, pydeck,
and bokeh. You can switch between these backends to create maps with different visualization
styles and capabilities.\"_

Our modest fires dataset has 16327 polygons is too big for leafmap. One could probably simplify the polygons, but we'll take the approach of filtering the data for 2016-2021 resulting in 2553 polygons (about 16\% of the entire dataset).  After about 20 seconds you will see a map.

```{embed} #nb:vector:leafmap
:remove-output: true
:remove-input: false
```

```{image} ../../assets/leafmap_vector
:alt: vector data with leafmap
:width: 100%
:align: center
```

---

## LONBOARD

[lonboard](https://developmentseed.org/lonboard/latest/)

_\"A Python library for fast, interactive geospatial vector data visualization in Jupyter._

_Building on cutting-edge technologies like GeoArrow and GeoParquet in conjunction with
GPU-based map rendering, Lonboard aims to enable visualizing large geospatial datasets
interactively through a simple interface.\"_

[Here](https://www.youtube.com/watch?v=NAjabS0GTdo) is a great discussion on Matt Forrest's GIS [youtube show](https://www.youtube.com/@MattForrest).

A quick overview:

- GEOARROW: enables sharing data between libaries (python to javascript). As an example GDAL speed up file reading 26x by using geoarrow on the backend
- GEOPARQUET: ipyleaflet & pydeck first byte object write to geojson. geoparquet will keep it in bytes. In ipyleaflet and pydeck a 300 million point database gets converted to 700MB geojson. geoparquet will be 60MB for the same data.
- DECK-GL: python rendering with the GPU

Here we'll plot the full dataset [1898-2021] using longboard.  After about 4 seconds you'll see a map

```{image} ../../assets/lonboard_vector
:alt: vector data with lonboard
:width: 100%
:align: center
```
