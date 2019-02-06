def render_node(node, draw, style_config, bbox):
    pass

def render_simple_point(node, draw, style_config, bbox):
    x, y = bbox.convert(node["lon"], node["lat"])    
    r = 10
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(255, 0, 0, 255))