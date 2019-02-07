def render_node(node, draw, style_config, bbox):
    if "tags" in node.keys():
        if "natural" in node["tags"].keys():
            if node["tags"]["natural"] == "tree":
                render_tree(node, draw, style_config, bbox)

def render_tree(node, draw, style_config, bbox):
    x, y = bbox.convert(node["lon"], node["lat"])    
    r = style_config.tree_radius
    draw.ellipse((x-r, y-r, x+r, y+r), fill=style_config.tree_fill, outline=style_config.tree_border)