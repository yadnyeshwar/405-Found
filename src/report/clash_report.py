CLEARANCE_RULES = {

    ("PIPE", "PIPE"): 100,
    ("PIPE", "DUCT"): 100,
    ("DUCT", "DUCT"): 200,
    ("PIPE", "CABLE_TRAY"): 150,
    ("DUCT", "CABLE_TRAY"): 150,
    ("CABLE_TRAY", "CABLE_TRAY"): 300

}


def compute_clash_location(a, b):

    cx = (max(a.min_x, b.min_x) + min(a.max_x, b.max_x)) / 2
    cy = (max(a.min_y, b.min_y) + min(a.max_y, b.max_y)) / 2
    cz = (max(a.min_z, b.min_z) + min(a.max_z, b.max_z)) / 2

    return (cx, cy, cz)


def classify_severity(system1, system2):

    pair = (system1, system2)

    if pair in CLEARANCE_RULES:
        clearance = CLEARANCE_RULES[pair]
    else:
        clearance = 100

    if clearance >= 200:
        return "CRITICAL"

    if clearance >= 100:
        return "MAJOR"

    return "MINOR"


def generate_clash_report(elements, clashes):

    report = []
    id_map = {e.element_id: e for e in elements}

    for i, clash in enumerate(clashes):

        a = id_map[clash["element1"]]
        b = id_map[clash["element2"]]

        location = compute_clash_location(a, b)

        severity = classify_severity(a.system, b.system)

        report.append({

            "clash_id": i + 1,
            "type": clash["type"],
            "location": location,
            "element1": clash["element1"],
            "element2": clash["element2"],
            "severity": severity

        })

    return report