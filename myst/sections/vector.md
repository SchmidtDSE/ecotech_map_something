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

```{embed} #nb:vector:filetypes
:remove-output: false
:remove-input: false
```

Read more about them here: [guide.cloudnativegeo.org](https://guide.cloudnativegeo.org/) Here is a performance comparison: https://cloudnativegeo.org/blog/2023/08/performance-explorations-of-geoparquet-and-duckdb/


[Geoparquet](https://geoparquet.org/) is exciting! smaller file sizes and faster reads. TLDR; columnar data format with row grouping and good compression


---

## GEOPANDAS


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


```{image} ../../assets/leafmap_vector
:alt: vector data with leafmap
:width: 100%
:align: center
```

---

## LONBOARD

```{image} ../../assets/lonboard_vector
:alt: vector data with lonboard
:width: 100%
:align: center
```