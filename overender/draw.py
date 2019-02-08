from PIL import Image
from PIL import ImageDraw
from jinja2 import Template

from cairosvg import svg2png
from cairosvg import svg2pdf

class Draw(object):

    def __init__(self, width, height, style_config, bbox):
        self.width = width
        self.height = height

        self.style = style_config
        self.bbox = bbox

        self.features = []

    def polygon(self, geometry, fill, outline=None, z_index=0):
        self.features.append({
            "type": "polygon",
            "points": geometry,
            "fill": fill,
            "outline": outline,
            "z_index": z_index
        })

    def ellipse(self, box, fill, outline=None, z_index=0):
        self.features.append({
            "type": "ellipse",
            "box": box,
            "fill": fill,
            "outline": outline,
            "z_index": z_index
        })
    
    def text(self, x, y, text, fill, z_index=0):
        self.features.append({
            "type": "text",
            "x": x,
            "y": y,
            "fill": fill,
            "text": text,
            "z_index": z_index
        })
        
    def polyline(self, points, fill, width, border, z_index):
        self.features.append({
            "type": "polyline",
            "points": points,
            "fill": fill,
            "width": width,
            "border": border,
            "z_index": z_index
        })
    
    def render(self, path, image_type):
        output = self.render_svg()
        if image_type == "PNG":
            svg2png(bytestring=output, write_to=path, scale=5)
        elif image_type == "PDF":
            svg2pdf(bytestring=output, write_to=path)
        elif image_type == "SVG":
            output = self.render_svg()
            with open(path, "w+") as target:
                target.write(output)

    def _c_hex(self, color):
        if color is None:
            return "transparent"
        return "#%02x%02x%02x" % color

    def render_svg(self):

        self.features.sort(key=lambda x: x["z_index"])

        with open("templates/svg.jinja", 'r') as target:
            template_text = target.read()
        template = Template(template_text)
        output = template.render(draw=self, conv=self._c_hex)

        return output