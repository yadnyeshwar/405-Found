from src.parser.ifc_parser import IFCParser
from src.core.aabb_clash import detect_clashes


def run_ifc_test():

    parser = IFCParser("sample.ifc")

    elements = parser.extract_mep_elements()

    print(f"\nLoaded {len(elements)} MEP elements\n")

    clashes = detect_clashes(elements)

    print(f"Detected {len(clashes)} clashes\n")

    for clash in clashes[:10]:
        print(clash)


if __name__ == "__main__":
    run_ifc_test()