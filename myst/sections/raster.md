(raster)=
# Raster Data

```{image} ../../assets/raster_types-tahoe
:alt: RGB, Satellite, DEM, LULC
:width: 100%
:align: center
```

Raster data is simply pixels with values. This can be an ordinary photograph, but much more. For example a digital elevation model may have 3-bands (elevation, slope, aspect), landuse classification will give a single int band representing the type of land use, and perhaps additional band representing other details such as classification confidence

## GEOTIFF


What makes a GeoTiff different than a traditional image.

- more bands: sentinel-2 for instance has 12 optical bands + others) as opposed to RGB.
- adds geospatial data
	- projection and coordinate-reference-system (CRS)
    - location (affine transform)

---

##### READING DATA WITH RASTERIO


```{embed} #nb:raster:readrio
:remove-output: false
:remove-input: false
```

---

##### COMMON COORDINATE REFERENCE SYSTEMS


* __EPSG:4326__: A global CRS (on WGS84) using latitude and longitude coordinates in degrees
* __UTM (EPSG:32HZZ)__: UTM CRS divide the northern and southern hemisphere up into 60 zones of 6$\degree$ longitude.  The EPSG codes are broken up 32 (UTM) [6,7] (north or south) [01-60] zone. Each EPSG uses x and y coordinates measured in meters.

```{figure} ../../assets/utm-grid
:width: 90%
:align: center
```

* __EPSG:3857__: A global CRS (on WGS84) using x and y coordinates in meters. This is a great choice for visualizations (online maps) but is only accurate near the equator and therefore shouldn't be used for calculations

---

##### STRUCTURE OF AFFINE TRANSFORMATIONS

:::{math}
:enumerated: false
\begin{pmatrix}
\text{resolution} & 0 & x\\
0 & -\text{resolution} & y
\end{pmatrix}
:::

---

##### READING DATA WITH RIOXARRAY


[rio-xarray](https://corteva.github.io/rioxarray/html/rioxarray.html) allows you to read the data directly into an `xr.DataArray`.

Some advantages:

* we now have access to the lat, lon values `da.x,y`
* we also have access to the band-names `da.long_name` whose order corresponds with the returned numpy array

```{embed} #nb:raster:s2_da
:remove-output: false
:remove-input: false
```

By transforming the `xr.DataArray` to a `xr.Dataset` the adavantages become more manifest

```{embed} #nb:raster:s2_ds
:remove-output: false
:remove-input: false
```

## MAPTILES

For interactive mapping often broken into map tiles: a url endpoint `http://.../{z}/{x}/{y}`, where z is the "ZOOM" level, and x and y are integers defining a tile on a coordinate grid.

```{figure}
:label: zooms
:width: 100%
:align: center

![zoom levels 0-3 (src https://docs.maptiler.com/google-maps-coordinates-tile-bounds-projection)](../../assets/zooms)

![number of tiles and tile sizes per zoom level (src: https://wiki.openstreetmap.org/wiki/Zoom_levels)](../../assets/map_tile_size)
```

[rio-tiler](https://cogeotiff.github.io/rio-tiler/) is a Rasterio plugin to read mercator tiles from Cloud Optimized GeoTIFF's. Used to create serverless tiles server with lambda-tiler. As an example [maptiles/app.py](../maptiles/app.py) creates a dynamic-tiler from cloud optimized geotiffs


### Whats a Cloud Optimized GeoTiff (COG)?

http://cogeo.org/

"A Cloud Optimized GeoTIFF (COG) is a regular GeoTIFF file, aimed at being hosted on a HTTP file server, with an internal organization that enables more efficient workflows on the cloud"

A (over) simplified way to think about this is a a geotiff that allows get requests so that

- one can get parts of the pixels without fetching all the data
- the aggregation at different zoom levels is already computed

COGs can be created from tifs using [rio-cogeo](https://cogeotiff.github.io/rio-cogeo/)

---

```{embed} #nb:raster:riocogeo-s2
:remove-output: false
:remove-input: false
```

---


### ZARR

Similar to COGs but uses a multiple file approach (metadata files + one file per data chunk) whereas uses a single file approach

They can be created from

```
.zattrs
.zgroup
.zmetadata
├── AOT
│   ├── 0.0
│   ├── 0.1
│   ├── 0.2
...
│   └── 9.7
├── B1 ...
├── B11 ...
├── B12 ...
├── B2 ...
├── B3 ...
├── B4 ...
├── B5 ...
├── B6 ...
├── B7 ...
├── B8 ...
├── B8A ...
├── B9 ...
├── MSK_CLASSI_CIRRUS ...
├── MSK_CLASSI_OPAQUE ...
├── MSK_CLASSI_SNOW_ICE ...
├── MSK_CLDPRB ...
├── MSK_SNWPRB ...
├── QA10 ...
├── QA20 ...
├── QA60 ...
├── SCL ...
├── TCI_B ...
├── TCI_G ...
├── TCI_R ...
├── WVP ...
├── x
│   └── 0
└── y
    └── 0
```

## MAP SOMETHING!

Let's make a map (finally). It's easy using [leafmap](https://leafmap.org/)

- leafmap has three plotting backends: folium, ipyleaflet, and here-map-widget-for-jupyter.
- provides an interactive graphical user interface (GUI) for loading geospatial datasets without any coding.


```{figure}
:alt: leafmap
:width: 100%
:align: center
![leafmap serving raster layers directly from cogs](../../assets/leafmap_s2)
![hiding sentinel-2 layer to reveal dem](../../assets/leafmap_dem)
```

