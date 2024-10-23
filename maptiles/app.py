""" example of creating a dynamic map tiler using rio-tiler

Note: this code base has been copied with minimal alteration from
https://cogeotiff.github.io/rio-tiler/advanced/dynamic_tiler
"""

import os

from fastapi import FastAPI, Query
from starlette.requests import Request
from starlette.responses import Response

from rio_tiler.profiles import img_profiles
from rio_tiler.io import Reader


DEFAULT_URL = '../data/raster/tahoe-dem.tif'


app = FastAPI(
    title="rio-tiler",
    description="A lightweight Cloud Optimized GeoTIFF tile server",
)


@app.get(
    r"/{z}/{x}/{y}.png",
    responses={
        200: {
            "content": {"image/png": {}}, "description": "Return an image.",
        }
    },
    response_class=Response,
    description="Read COG and return a tile",
)
def tile(
    z: int,
    x: int,
    y: int,
    url: str = Query(default=DEFAULT_URL, description="Cloud Optimized GeoTIFF URL."),
):
    """Handle tile requests."""
    with Reader(url) as cog:
        img = cog.tile(x, y, z)

    content = img.render(img_format="PNG", **img_profiles.get("png"))
    return Response(content, media_type="image/png")


@app.get("/tilejson.json", responses={200: {"description": "Return a tilejson"}})
def tilejson(
    request: Request,
    url: str = Query(default=DEFAULT_URL, description="Cloud Optimized GeoTIFF URL."),
):
    """Return TileJSON document for a COG."""
    tile_url = str(request.url_for("tile", z="{z}", x="{x}", y="{y}"))
    tile_url = f"{tile_url}?url={url}"

    with Reader(url) as cog:
        return {
            "bounds": cog.geographic_bounds,
            "minzoom": cog.minzoom,
            "maxzoom": cog.maxzoom,
            "name": os.path.basename(url),
            "tiles": [tile_url],
        }