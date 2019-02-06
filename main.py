import argparse
from overender.overpass import request_json

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument("query", help="Path of query")

args = parser.parse_args()

# Stuff loading
with open(args.query, 'r') as target:
    query = target.read()

# BBOX Loading
## Hawerkamp 31
bbox = [7.637615442,51.9430635895,7.6400723455,51.9447897396]
bbox = bbox[1], bbox[0], bbox[3], bbox[2] # Convert format from lat lon to lon lat and vice versa

# Loading data from OSM
data = request_json(query, bbox)

for element in data:
    pass