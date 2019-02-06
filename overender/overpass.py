import requests
import json
import os

def request_json(query, bbox, server="https://overpass.kumi.systems/api/interpreter", use_cache=False):
    if os.path.exists(".cache.json") and use_cache:
        with open(".cache.json", "r") as target:
            return json.load(target)
    else:
        query = query.format(sbbox=bbox.as_string())
        req = requests.get(server, data=query)

        with open(".cache.json", "w+") as target:
            target.write(req.text)

        if req.status_code == 200:
            return json.loads(req.text)
        else:
            return req.text