class MEPElement:

    def __init__(self, element_id, element_type, bbox_min, bbox_max):
        self.element_id = element_id
        self.element_type = element_type

        self.min_x, self.min_y, self.min_z = bbox_min
        self.max_x, self.max_y, self.max_z = bbox_max

    def __repr__(self):
        return (
            f"MEPElement(id={self.element_id}, "
            f"type={self.element_type}, "
            f"bbox=({self.min_x},{self.min_y},{self.min_z}) -> "
            f"({self.max_x},{self.max_y},{self.max_z}))"
        )