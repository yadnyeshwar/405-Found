from element import MEPElement
from aabb_clash import detect_clashes


def run_test():

    pipe_1 = MEPElement(
        "P001",
        "pipe",
        (1000, 500, 2375),
        (5000, 525, 2425)
    )

    duct_1 = MEPElement(
        "D001",
        "duct",
        (3000, 200, 2200),
        (8000, 800, 2500)
    )

    tray_1 = MEPElement(
        "T001",
        "cable_tray",
        (9000, 1000, 2000),
        (11000, 1200, 2100)
    )

    elements = [pipe_1, duct_1, tray_1]

    clashes = detect_clashes(elements)

    print("Detected Clashes:\n")

    if not clashes:
        print("No clashes found")

    for clash in clashes:
        print(clash)


if __name__ == "__main__":
    run_test()