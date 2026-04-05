def check_clash(a, b):

    return (
        a.max_x > b.min_x and
        a.min_x < b.max_x and
        a.max_y > b.min_y and
        a.min_y < b.max_y and
        a.max_z > b.min_z and
        a.min_z < b.max_z
    )


def detect_clashes(elements):

    clashes = []

    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):

            a = elements[i]
            b = elements[j]

            if check_clash(a, b):

                clashes.append({
                    "element1": a.element_id,
                    "element2": b.element_id,
                    "type1": a.element_type,
                    "type2": b.element_type
                })

    return clashes