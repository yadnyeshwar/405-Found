import ifcopenshell
import ifcopenshell.geom

from src.core.element import MEPElement


class IFCParser:

    def __init__(self, file_path):

        self.model = ifcopenshell.open(file_path)

        self.settings = ifcopenshell.geom.settings()
        self.settings.set(self.settings.USE_WORLD_COORDS, True)


    def extract_elements(self):

        elements = []

        # UNIVERSAL MEP extraction (works for IFC2X3 + IFC4)
        candidates = self.model.by_type("IfcDistributionElement")

        print("Total IFC candidates:", len(candidates))

        for element in candidates:

            try:

                # Generate geometry
                shape = ifcopenshell.geom.create_shape(self.settings, element)

                verts = shape.geometry.verts

                xs = verts[0::3]
                ys = verts[1::3]
                zs = verts[2::3]

                bbox_min = (min(xs), min(ys), min(zs))
                bbox_max = (max(xs), max(ys), max(zs))

                mep = MEPElement(
                    element.GlobalId,
                    element.is_a(),
                    bbox_min,
                    bbox_max
                )

                elements.append(mep)

            except Exception:
                continue

        print("Valid elements extracted:", len(elements))

        return elements