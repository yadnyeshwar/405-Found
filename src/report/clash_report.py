def calculate_clash_location(a, b):

    cx = (max(a.min_x, b.min_x) + min(a.max_x, b.max_x)) / 2
    cy = (max(a.min_y, b.min_y) + min(a.max_y, b.max_y)) / 2
    cz = (max(a.min_z, b.min_z) + min(a.max_z, b.max_z)) / 2

    return (cx, cy, cz)


def calculate_severity(a, b):

    overlap_x = min(a.max_x, b.max_x) - max(a.min_x, b.min_x)
    overlap_y = min(a.max_y, b.max_y) - max(a.min_y, b.min_y)
    overlap_z = min(a.max_z, b.max_z) - max(a.min_z, b.min_z)

    volume = max(0, overlap_x) * max(0, overlap_y) * max(0, overlap_z)

    if volume > 1:
        return "HIGH"
    elif volume > 0.1:
        return "MEDIUM"
    else:
        return "LOW"


def generate_clash_report(elements, clashes):

    id_map = {e.element_id: e for e in elements}

    report = []

    for i, clash in enumerate(clashes):

        a = id_map[clash["element1"]]
        b = id_map[clash["element2"]]

        location = calculate_clash_location(a, b)

        severity = calculate_severity(a, b)

        report.append({
            "clash_id": i + 1,
            "type": f"{clash['type1']} vs {clash['type2']}",
            "location": location,
            "element1": clash["element1"],
            "element2": clash["element2"],
            "severity": severity
        })

    return report