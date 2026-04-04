def check_aabb_clash(elem_a, elem_b):

    x_overlap = (
        elem_a.max_x > elem_b.min_x and
        elem_a.min_x < elem_b.max_x
    )

    y_overlap = (
        elem_a.max_y > elem_b.min_y and
        elem_a.min_y < elem_b.max_y
    )

    z_overlap = (
        elem_a.max_z > elem_b.min_z and
        elem_a.min_z < elem_b.max_z
    )

    return x_overlap and y_overlap and z_overlap


def detect_clashes(elements):

    clashes = []

    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):

            a = elements[i]
            b = elements[j]

            if check_aabb_clash(a, b):

                clash_data = {
                    "element_1": a.element_id,
                    "element_2": b.element_id,
                    "type_1": a.element_type,
                    "type_2": b.element_type
                }

                clashes.append(clash_data)

    return clashes