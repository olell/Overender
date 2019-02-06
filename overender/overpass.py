import requests
import json

def request_json(query, bbox, server="https://overpass.kumi.systems/api/interpreter"):
    query = query.format(sbbox=','.join(map(str, bbox)))
    req = requests.get(server, data=query)

    if req.status_code == 200:
        return json.loads(req.text)
    else:
        return req.text