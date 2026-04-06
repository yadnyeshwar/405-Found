import ifcopenshell
import ifcopenshell.geom
from src.core.element import MEPElement


class IFCParser:

    def __init__(self, file_path):

        self.model = ifcopenshell.open(file_path)

        self.settings = ifcopenshell.geom.settings()
        self.settings.set(self.settings.USE_WORLD_COORDS, True)


    # ------------------------------
    # CLASSIFY SYSTEM TYPE
    # ------------------------------
    def classify_system(self, element):

        name = element.is_a().lower()

        # Direct IFC classes
        if "pipesegment" in name or "pipefitting" in name:
            return "PIPE"

        if "ductsegment" in name or "ductfitting" in name:
            return "DUCT"

        if "cablecarrier" in name:
            return "CABLE_TRAY"


        # IFC2X3 fallback (FlowSegment / FlowFitting)
        if name in ["ifcflowsegment", "ifcflowfitting"]:

            # try predefined type
            try:
                if element.PredefinedType:
                    pt = str(element.PredefinedType).lower()

                    if "duct" in pt:
                        return "DUCT"

                    if "pipe" in pt:
                        return "PIPE"

                    if "cable" in pt:
                        return "CABLE_TRAY"
            except:
                pass

            # try object type
            try:
                if element.ObjectType:
                    obj = element.ObjectType.lower()

                    if "duct" in obj:
                        return "DUCT"

                    if "pipe" in obj:
                        return "PIPE"

                    if "cable" in obj:
                        return "CABLE_TRAY"
            except:
                pass

            # try name
            try:
                if element.Name:
                    nm = element.Name.lower()

                    if "duct" in nm:
                        return "DUCT"

                    if "pipe" in nm:
                        return "PIPE"

                    if "cable" in nm:
                        return "CABLE_TRAY"
            except:
                pass

        return "UNKNOWN"


    # ------------------------------
    # EXTRACT ELEMENTS
    # ------------------------------
    def extract_elements(self):

        elements = []
        candidates = []

        for t in [
            "IfcPipeSegment",
            "IfcPipeFitting",
            "IfcDuctSegment",
            "IfcDuctFitting",
            "IfcCableCarrierSegment",
            "IfcCableCarrierFitting",
            "IfcFlowSegment",
            "IfcFlowFitting"
        ]:

            try:
                candidates += self.model.by_type(t)
            except:
                pass

        print("Total candidates:", len(candidates))

        for element in candidates:

            try:

                shape = ifcopenshell.geom.create_shape(self.settings, element)

                verts = shape.geometry.verts

                xs = verts[0::3]
                ys = verts[1::3]
                zs = verts[2::3]

                bbox_min = (min(xs), min(ys), min(zs))
                bbox_max = (max(xs), max(ys), max(zs))

                system = self.classify_system(element)

                mep = MEPElement(
                    element.GlobalId,
                    element.is_a(),
                    system,
                    bbox_min,
                    bbox_max
                )

                elements.append(mep)

            except:
                continue

        print("Valid MEP elements:", len(elements))

        return elements