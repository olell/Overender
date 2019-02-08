import utm

class BoundingBox(object):

    def __init__(self, lon0, lat0, lon1, lat1):
        self.lon0 = lon0
        self.lat0 = lat0
        self.lon1 = lon1
        self.lat1 = lat1

        self.x0, self.y0, _, _ = utm.from_latlon(self.lat0, self.lon0)
        self.x1, self.y1, _, _ = utm.from_latlon(self.lat1, self.lon1)

        self.d_x = self.x1 - self.x0
        self.d_y = self.y1 - self.y0

        self.p_width = self.d_x
        self.p_height = self.d_y

    def as_list(self):
        return [self.lat0, self.lon0, self.lat1, self.lon1]

    def as_string(self):
        return ','.join(map(str, self.as_list()))

    def get_pixel_size(self):
        return self.p_width, self.p_height

    def convert(self, lon, lat):
        x, y, _, _ = utm.from_latlon(lat, lon)
        x -= self.x0
        y = self.p_height - (y - self.y0)
        return x, y