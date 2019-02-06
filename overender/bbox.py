class BoundingBox(object):

    def __init__(self, lon0, lat0, lon1, lat1, resolution=10000):
        self.lon0 = lon0
        self.lat0 = lat0
        self.lon1 = lon1
        self.lat1 = lat1

        self.resolution = resolution

        self.d_lat = self.lat1 - self.lat0
        self.d_lon = self.lon1 - self.lon0

        self.p_width = int(self.d_lon * self.resolution)
        self.p_height = int(self.d_lat * self.resolution)

    def as_list(self):
        return [self.lon0, self.lat0, self.lon1, self.lat1]

    def as_string(self):
        return ','.join(map(str, self.as_list()))

    def get_pixel_size(self):
        return self.p_width, self.p_height