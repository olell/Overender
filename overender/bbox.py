class BoundingBox(object):

    def __init__(self, lon0, lat0, lon1, lat1, resolution=300000):
        self.lon0 = lon0
        self.lat0 = lat0
        self.lon1 = lon1
        self.lat1 = lat1

        self.factor = 1.75

        self.nla0 = (self.lat0 + 84) * self.factor
        self.nla1 = (self.lat1 + 84) * self.factor
        self.nlo0 = (self.lon0 + 180)
        self.nlo1 = (self.lon1 + 180)

        self.resolution = resolution

        self.d_lat = self.nla1 - self.nla0
        self.d_lon = self.nlo1 - self.nlo0

        self.p_width = int(self.d_lon * self.resolution)
        self.p_height = int(self.d_lat * self.resolution)

    def as_list(self):
        return [self.lat0, self.lon0, self.lat1, self.lon1]

    def as_string(self):
        return ','.join(map(str, self.as_list()))

    def get_pixel_size(self):
        return self.p_width, self.p_height

    def convert(self, lon, lat):
        nla = (lat + 84) * self.factor
        nlo = (lon + 180)
        x = int((nlo - self.nlo0) * self.resolution)
        y = self.p_height - int((nla - self.nla0) * self.resolution)
        return x, y