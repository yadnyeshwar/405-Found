import json
from src.parser.ifc_parser import IFCParser
from src.core.aabb_clash import detect_clashes
from src.report.clash_report import generate_clash_report
from src.rerouting.reroute_engine import reroute_clash


def run_pipeline(ifc_file):

    print("\n---- MEP CLASH DETECTION PIPELINE ----\n")

    # STEP 1 — Parse IFC
    parser = IFCParser(ifc_file)
    elements = parser.extract_elements()

    print("Loaded elements:", len(elements))

    element_map = {e.element_id: e for e in elements}

    # STEP 2 — Detect clashes
    clashes = detect_clashes(elements)

    print("Detected clashes:", len(clashes))

    # STEP 3 — Rerouting
    reroutes = []

    print("\n---- REROUTING SUGGESTIONS ----\n")

    for clash in clashes:

        a = element_map[clash["element1"]]
        b = element_map[clash["element2"]]

        suggestions = reroute_clash(a, b)

        reroutes.extend(suggestions)

    for r in reroutes[:10]:
        print(r)

    # STEP 4 — Generate clash report
    report = generate_clash_report(elements, clashes)

    print("\n---- CLASH REPORT ----\n")

    for r in report[:10]:
        print(r)

    # STEP 5 — Save JSON
    output = {
        "clashes": report,
        "reroutes": reroutes
    }

    with open("clash_results.json", "w") as f:
        json.dump(output, f, indent=4)

    print("\nJSON saved: clash_results.json")


# ENTRY POINT
if __name__ == "__main__":

    IFC_FILE = "data/RVT_Model_MEP_for_Orkathon_detached.ifc"

    run_pipeline(IFC_FILE)