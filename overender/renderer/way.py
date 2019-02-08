def render_way(way, draw):
    if "tags" in way.keys():
        keys = way["tags"].keys()
        if "building" in keys:
            render_building(way, draw)
        elif "natural" in keys:
            if way["tags"]["natural"] == "water":
                render_waterway(way, draw)
            else:
                render_natural(way, draw)
        elif "amenity" in keys:
            if way["tags"]["amenity"] == "parking":
                render_parking(way, draw)
        elif "landuse" in keys:
            landuse = way["tags"]["landuse"]
            if landuse == "residential":
                render_residential_landuse(way, draw)
            if landuse == "industrial":
                render_industrial_landuse(way, draw)
            if landuse == "commercial":
                render_commercial_landuse(way, draw)
            if landuse == "railway":
                render_railway_landuse(way, draw)
            if landuse == "brownfield":
                render_brownfield_landuse(way, draw)
            if landuse == "grass":
                render_natural(way, draw)
        elif "waterway" in keys:
            if way["tags"]["waterway"] == "riverbank":
                render_waterway(way, draw)
        elif "highway" in keys:
            render_highway(way, draw)
            

def render_building(way, draw):
    render_polygon(way, draw, draw.style.building_fill, draw.style.building_border)

def render_natural(way, draw):
    render_polygon(way, draw, draw.style.natural_fill, draw.style.natural_border)

def render_parking(way, draw):
    render_polygon(way, draw, draw.style.parking_fill, draw.style.parking_border, z_index=-90)

    lats = []
    lons = []
    for point in way["geometry"]:
        lats.append(point["lat"])
        lons.append(point["lon"])
    min_lat = min(lats)
    min_lon = min(lons)
    max_lat = max(lats)
    max_lon = max(lons)
    x = (max_lon + min_lon) / 2
    y = (max_lat + min_lat) / 2
    render_text(draw, x, y, (0, 0, 255), "P")

def render_residential_landuse(way, draw):
    render_polygon(way, draw, draw.style.residential_landuse, z_index=-100)

def render_industrial_landuse(way, draw):
    render_polygon(way, draw, draw.style.industrial_landuse, z_index=-100)

def render_commercial_landuse(way, draw):
    render_polygon(way, draw, draw.style.commercial_landuse, z_index=-100)

def render_railway_landuse(way, draw):
    render_polygon(way, draw, draw.style.railway_landuse, z_index=-100)

def render_brownfield_landuse(way, draw):
    render_polygon(way, draw, draw.style.brownfield_landuse, z_index=-100)

def render_waterway(way, draw):
    render_polygon(way, draw, draw.style.waterway_fill, draw.style.waterway_border, z_index=-90)

def render_highway(way, draw):
    for i in range(0, len(way["geometry"]) - 1):
        x0, y0 = way["geometry"][i]["lon"], way["geometry"][i]["lat"]
        x1, y1 = way["geometry"][i+1]["lon"], way["geometry"][i+1]["lat"]
        render_line(draw, x0, y0, x1, y1, (255, 0, 0), 1)

def render_polygon(way, draw, fill, border=None, z_index=0):
    pixel_points = []
    for i in range(0, len(way["geometry"])):
        point = way["geometry"][i]
        pixel_points.append(draw.bbox.convert(point["lon"], point["lat"]))
    
    draw.polygon(pixel_points, fill=fill, outline=border, z_index=z_index)

def render_text(draw, x, y, fill, text, z_index=0):
    x, y = draw.bbox.convert(x, y)
    draw.text(x, y, text, fill=fill, z_index=z_index)

def render_line(draw, x0, y0, x1, y1, fill, width=1, border=None, z_index=0):
    x0, y0 = draw.bbox.convert(x0, y0)
    x1, y1 = draw.bbox.convert(x1, y1)
    draw.line(x0, y0, x1, y1, fill, width, border, z_index)