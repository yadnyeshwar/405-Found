from src.parser.ifc_parser import IFCParser
from src.core.aabb_clash import detect_clashes


def run():

    file_path = "data/sample.ifc"

    parser = IFCParser(file_path)

    elements = parser.extract_elements()

    print("\nLoaded elements:", len(elements))

    clashes = detect_clashes(elements)

    print("\nDetected clashes:", len(clashes))

    for c in clashes[:10]:
        print(c)


if __name__ == "__main__":
    run()