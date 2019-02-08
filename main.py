import argparse

from overender.overpass import request_json
from overender.bbox import BoundingBox
from overender.renderer import render
from overender.style_config import DefaultStyle
from overender.draw import Draw

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument("query", help="Path of query")

args = parser.parse_args()

# Stuff loading
with open(args.query, 'r') as target:
    query = target.read()

# BBOX Loading
## Hawerkamp 31
bbox = BoundingBox(7.634232,51.942003,7.647557,51.950137)

# Loading data from OSM
print("Start quering overpass API")
data = request_json(query, bbox, use_cache=True)
print("Overpass query done...")

# Creating image and draw
style = DefaultStyle

width, height = bbox.get_pixel_size()
draw = Draw(width, height, style, bbox)

print("MAP Start rendering")
for element in data["elements"]:
    render(element, draw)
print("MAP Rendering done...")

print("Image start rendering")
draw.render("out.svg", "SVG")
print("Image rendered")