from PIL import Image
from PIL import ImageDraw
from jinja2 import Template

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
    
    def render(self, path, image_type):
        if image_type != "SVG":
            image = Image.new('RGB', (self.width, self.height), self.style.background_color)
            draw = ImageDraw.Draw(image)

            for feature in self.features:
                if feature["type"] == "polygon":
                    draw.polygon(feature["points"], fill=feature["fill"], outline=feature["outline"])
                elif feature["type"] == "ellipse":
                    draw.ellipse(feature["box"], fill=feature["fill"], outline=feature["outline"])

            image.save(path, "PNG")
        else:
            self.render_svg(path)

    def _c_hex(self, color):
        if color is None:
            return "unset"
        return "#%02x%02x%02x" % color

    def render_svg(self, path):

        self.features.sort(key=lambda x: x["z_index"])

        with open("templates/svg.jinja", 'r') as target:
            template_text = target.read()
        template = Template(template_text)
        output = template.render(draw=self, conv=self._c_hex)

        with open(path, "w+") as target:
            target.write(output)