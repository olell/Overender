from overender.renderer.node import render_node
from overender.renderer.way import render_way

def render(element, draw, style_config, bbox):
    
    if element["type"] == "node":
        render_node(element, draw, style_config, bbox)
    
    elif element["type"] == "way":
        render_way(element, draw, style_config, bbox)

    else:
        pass # Will not be rendered