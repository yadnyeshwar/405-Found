CLEARANCE_RULES = {

    ("PIPE", "PIPE"): 0.1,
    ("PIPE", "DUCT"): 0.1,
    ("DUCT", "DUCT"): 0.2,
    ("PIPE", "CABLE_TRAY"): 0.15,
    ("CABLE_TRAY", "CABLE_TRAY"): 0.3

}


def get_clearance(a, b):

    pair = (a.system, b.system)

    if pair in CLEARANCE_RULES:
        return CLEARANCE_RULES[pair]

    pair = (b.system, a.system)

    if pair in CLEARANCE_RULES:
        return CLEARANCE_RULES[pair]

    return 0.1


def choose_element_to_move(a, b):

    priority = {
        "DUCT": 3,
        "CABLE_TRAY": 2,
        "PIPE": 1
    }

    if priority.get(a.system,0) < priority.get(b.system,0):
        return a, b
    else:
        return b, a


def reroute_clash(a, b):

    movable, obstacle = choose_element_to_move(a, b)

    clearance = get_clearance(a, b)

    suggestions = []

    # vertical reroute
    new_z = obstacle.max_z + clearance

    suggestions.append({

        "action": "RAISE",
        "element": movable.element_id,
        "old_z": movable.max_z,
        "new_z": new_z

    })

    # horizontal reroute X
    new_x = obstacle.max_x + clearance

    suggestions.append({

        "action": "SHIFT_X",
        "element": movable.element_id,
        "old_x": movable.max_x,
        "new_x": new_x

    })

    # horizontal reroute Y
    new_y = obstacle.max_y + clearance

    suggestions.append({

        "action": "SHIFT_Y",
        "element": movable.element_id,
        "old_y": movable.max_y,
        "new_y": new_y

    })

    return suggestions