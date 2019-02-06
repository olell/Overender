def render_way(way, draw, style_config, bbox):
    if "tags" in way.keys():
        if "building" in way["tags"].keys():
            render_building(way, draw, style_config, bbox)
        elif "natural" in way["tags"].keys():
            render_natural(way, draw, style_config, bbox)

def render_building(way, draw, style_config, bbox):
    render_polygon(way, draw, style_config, bbox, style_config.building_fill, style_config.building_border)

def render_natural(way, draw, style_config, bbox):
    render_polygon(way, draw, style_config, bbox, style_config.natural_fill, style_config.natural_border)


def render_polygon(way, draw, style_config, bbox, fill, border):
    pixel_points = []
    for i in range(0, len(way["geometry"])):
        point = way["geometry"][i]
        pixel_points.append( bbox.convert(point["lon"], point["lat"]) )
    
    draw.polygon(pixel_points, fill=fill, outline=border)