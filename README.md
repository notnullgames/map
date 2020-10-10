# map

These are tools for creating maps at various zoom-levels for [pakemon](https://github.com/notnullgames/pakemon).

You will need to download a mbtile file.

sources for maps:

* [a lowres map from openmaptiles](https://openmaptiles.com/downloads/dataset/satellite-lowres) - it only does 5X
* more limited mbtile file from [hotosm](https://export.hotosm.org/) at various zoom-levels. You can get a really nice & detailed subset
* a detailed world-map from [openandromaps](https://www.openandromaps.org/en/downloads/general-maps) (under "Manual installation for any App")

Once you have your mbtiles file, load a map-server in docker:

```sh
docker run --rm -it -v $(pwd):/data -p 8080:80 maptiler/tileserver-gl /data/W1-10-J70.mbtiles
```

You can explore your map [here](http://localhost:8080)

Now, run the included python script to download tiles to `tiles/` with zoom-level 5:

```
python3 gettiles.py "http://localhost:8080/data/W1-10-J70/{z}/{x}/{y}.png" tiles 5
```

You can get the URL format to use by visiting [the map-server](http://localhost:8080), and right-clicking on a tile and say "open image in a new tab" then note the URL.

If you get an error about `requests` do this:

```
pip3 install requests
```