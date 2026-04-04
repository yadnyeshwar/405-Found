import ifcopenshell
from src.core.element import MEPElement


class IFCParser:

    def __init__(self, file_path):
        self.model = ifcopenshell.open(file_path)

    def extract_mep_elements(self):

        elements = []

        pipe_segments = self.model.by_type("IfcPipeSegment")
        duct_segments = self.model.by_type("IfcDuctSegment")
        tray_segments = self.model.by_type("IfcCableCarrierSegment")

        all_segments = (
            [(p, "pipe") for p in pipe_segments] +
            [(d, "duct") for d in duct_segments] +
            [(t, "cable_tray") for t in tray_segments]
        )

        for element, element_type in all_segments:

            try:
                bbox = self.get_bbox(element)

                mep_element = MEPElement(
                    element_id=element.GlobalId,
                    element_type=element_type,
                    min_xyz=bbox["min"],
                    max_xyz=bbox["max"]
                )

                elements.append(mep_element)

            except:
                continue

        return elements

    def get_bbox(self, element):

        shape = element.Representation

        # Simplified bounding box placeholder
        # In real BIM extraction you'd use geometry engine

        min_xyz = (0, 0, 0)
        max_xyz = (100, 100, 100)

        return {
            "min": min_xyz,
            "max": max_xyz
        }