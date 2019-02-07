def render_node(node, draw):
    if "tags" in node.keys():
        if "natural" in node["tags"].keys():
            if node["tags"]["natural"] == "tree":
                render_tree(node, draw)

def render_tree(node, draw,):
    x, y = draw.bbox.convert(node["lon"], node["lat"])    
    r = draw.style.tree_radius
    draw.ellipse((x-r, y-r, x+r, y+r), fill=draw.style.tree_fill, outline=draw.style.tree_border)