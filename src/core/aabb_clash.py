def aabb_overlap(a, b):

    return (
        a.max_x > b.min_x and a.min_x < b.max_x and
        a.max_y > b.min_y and a.min_y < b.max_y and
        a.max_z > b.min_z and a.min_z < b.max_z
    )


def detect_clashes(elements):

    clashes = []
    n = len(elements)

    for i in range(n):

        for j in range(i + 1, n):

            a = elements[i]
            b = elements[j]

            if a.system == "UNKNOWN" or b.system == "UNKNOWN":
                continue

            if aabb_overlap(a, b):

                clash_type = f"{a.system} vs {b.system}"

                clashes.append({

                    "element1": a.element_id,
                    "element2": b.element_id,
                    "system1": a.system,
                    "system2": b.system,
                    "type": clash_type

                })

    return clashes