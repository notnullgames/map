#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from requests import get

parser = ArgumentParser(description='Download map tile-images from a map-server.')
parser.add_argument('url', metavar='URL', type=str, nargs=1, help='the URL of the tile-server')
parser.add_argument('out', metavar='OUT', type=str, nargs=1, help='the output directory')
parser.add_argument('zoom', metavar='ZOOM', type=int, nargs=1, help='the zoom-level of the map-tiles')

args = parser.parse_args()
url = args.url[0]
out = args.out[0]
zoom = args.zoom[0]

maxTile = pow(2, zoom) - 1

for x in range(0, maxTile):
  for y in range(0, maxTile):
    Path('%s/%d/%d' % (out, zoom, x)).mkdir(parents=True, exist_ok=True)
    r = get(url.replace('{x}', str(x)).replace('{y}', str(y)).replace('{z}', str(zoom)))
    with open('%s/%d/%d/%d.jpg' % (out, zoom, x, y), 'wb') as out_file:
      out_file.write(r.content)