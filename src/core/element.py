class MEPElement:

    def __init__(self, element_id, element_type, min_xyz, max_xyz):
        self.element_id = element_id
        self.element_type = element_type

        self.min_x, self.min_y, self.min_z = min_xyz
        self.max_x, self.max_y, self.max_z = max_xyz

    def get_bbox(self):
        return {
            "min": (self.min_x, self.min_y, self.min_z),
            "max": (self.max_x, self.max_y, self.max_z)
        }