# map

These are tools for creating maps at various zoom-levels for [pakemon](https://github.com/notnullgames/pakemon).

You will need to download a mbtile file.

sources for maps:

* [a lowres map from openmaptimes](https://openmaptiles.com/downloads/dataset/satellite-lowres) - it only does 5X
* more limited mbtile file from [hotosm](https://export.hotosm.org/) at various zoom-levels.
* a detailed world-map from [openandromaps](https://www.openandromaps.org/en/downloads/general-maps) (under "Manual installation for any App")

Once you have your mbtiles file, load a map-server in docker:

```sh
docker run --rm -it -v $(pwd):/data -p 8080:80 maptiler/tileserver-gl /data/satellite-lowres-v1.2-z0-z5.mbtiles
```

You can explore your map [here](http://localhost:8080)

Now, run the included python script to download tiles to `tiles/` with zoom-level 5:

```
python3 gettiles.py "http://localhost:8080/data/openmaptiles_satellite_lowres/{z}/{x}/{y}.jpg" tiles 5
```

If you get an error about `requests` do this:

```
pip3 install requests
```