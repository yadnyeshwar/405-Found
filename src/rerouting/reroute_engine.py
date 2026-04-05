def suggest_reroute(a, b):

    # simple strategy: raise element A above B

    clearance = 0.3  # 30cm engineering clearance

    new_z = b.max_z + clearance

    suggestion = {
        "action": "RAISE_PIPE",
        "element": a.element_id,
        "old_z": a.min_z,
        "new_z": new_z
    }

    return suggestion


def generate_rerouting(elements, clashes):

    id_map = {e.element_id: e for e in elements}

    suggestions = []

    for clash in clashes:

        a = id_map[clash["element1"]]
        b = id_map[clash["element2"]]

        suggestion = suggest_reroute(a, b)

        suggestions.append(suggestion)

    return suggestions