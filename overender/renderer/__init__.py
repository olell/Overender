from overender.renderer.node import render_node
from overender.renderer.way import render_way

def render(element, draw):
    
    if element["type"] == "node":
        render_node(element, draw)
    
    elif element["type"] == "way":
        render_way(element, draw)

    else:
        pass # Will not be rendered