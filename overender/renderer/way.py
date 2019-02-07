def render_way(way, draw):
    if "tags" in way.keys():
        keys = way["tags"].keys()
        if "building" in keys:
            render_building(way, draw)
        elif "natural" in keys:
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
            if landuse == "brownfield":
                render_brownfield_landuse(way, draw)
            if landuse == "grass":
                render_natural(way, draw)
        elif "waterway" in keys:
            if way["tags"]["waterway"] == "riverbank":
                render_waterway(way, draw)

def render_building(way, draw):
    render_polygon(way, draw, draw.style.building_fill, draw.style.building_border)

def render_natural(way, draw):
    render_polygon(way, draw, draw.style.natural_fill, draw.style.natural_border)

def render_parking(way, draw):
    render_polygon(way, draw, draw.style.parking_fill, draw.style.parking_border, z_index=-90)

def render_residential_landuse(way, draw):
    render_polygon(way, draw, draw.style.residential_landuse, z_index=-100)

def render_industrial_landuse(way, draw):
    render_polygon(way, draw, draw.style.industrial_landuse, z_index=-100)

def render_commercial_landuse(way, draw):
    render_polygon(way, draw, draw.style.commercial_landuse, z_index=-100)

def render_brownfield_landuse(way, draw):
    render_polygon(way, draw, draw.style.brownfield_landuse, z_index=-100)

def render_waterway(way, draw):
    render_polygon(way, draw, draw.style.waterway_fill, draw.style.waterway_border, z_index=-90)

def render_polygon(way, draw, fill, border=None, z_index=0):
    pixel_points = []
    for i in range(0, len(way["geometry"])):
        point = way["geometry"][i]
        pixel_points.append(draw.bbox.convert(point["lon"], point["lat"]) )
    
    draw.polygon(pixel_points, fill=fill, outline=border, z_index=z_index)