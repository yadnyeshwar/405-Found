from src.parser.ifc_parser import IFCParser
from src.core.aabb_clash import detect_clashes
from src.report.clash_report import generate_clash_report
from src.rerouting.reroute_engine import generate_rerouting
from src.rerouting.auto_reroute import auto_reroute


def run():

    file_path = "data/sample2.ifc"

    parser = IFCParser(file_path)

    elements = parser.extract_elements()

    print("\nLoaded elements:", len(elements))

    clashes = detect_clashes(elements)

    print("\nDetected clashes:", len(clashes))

    report = generate_clash_report(elements, clashes)

    print("\n---- CLASH REPORT ----\n")

    for r in report[:10]:
        print(r)

    reroutes = generate_rerouting(elements, clashes)

    print("\n---- REROUTING SUGGESTIONS ----\n")

    for r in reroutes[:10]:
        print(r)

    if clashes:

        clash = clashes[0]

        e1 = next(e for e in elements if e.element_id == clash["element1"])
        e2 = next(e for e in elements if e.element_id == clash["element2"])

        start = (e1.min_x, e1.min_y, e1.min_z)
        goal  = (e1.max_x+5, e1.max_y+5, e1.max_z+5)

        path = auto_reroute(start,goal,elements,e1.element_id)

        print("\n---- AUTO REROUTED PATH ----\n")

        if path:
            print("New route:", path[:10],"...")
        else:
            print("No path found")


if __name__ == "__main__":
    run()


# from src.parser.ifc_parser import IFCParser
# from src.core.aabb_clash import detect_clashes


# def run():

#     file_path = "data/sample2.ifc"

#     parser = IFCParser(file_path)

#     elements = parser.extract_elements()

#     print("\nLoaded elements:", len(elements))

#     clashes = detect_clashes(elements)

#     print("\nDetected clashes:", len(clashes))

#     for c in clashes[:10]:
#         print(c)


# if __name__ == "__main__":
#     run()