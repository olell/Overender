class StyleConfig(object):
    pass

class DefaultStyle(StyleConfig):

    background_color = (242, 239, 233)

    building_fill = (217, 208, 201)
    building_border = (192, 183, 172) #(255, 255, 255)

    natural_fill = (173, 209, 158)
    natural_border = None #(255, 255, 255)

    parking_fill = (238,238,238)
    parking_border = None #(255, 255, 255)

    tree_fill = (167, 205, 167)
    tree_border = None
    tree_radius = 3

    residential_landuse = (224, 223, 223)
    industrial_landuse = (235, 219, 232)
    commercial_landuse = (242, 218, 217)
    railway_landuse = (235, 219, 232)
    brownfield_landuse = (199, 199, 180)

    waterway_fill = (170, 211, 223)
    waterway_border = None

    way_fill = (255, 255, 255)
    way_border = (217, 216, 215)