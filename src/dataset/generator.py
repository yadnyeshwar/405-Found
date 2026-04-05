import random
from src.core.element import MEPElement


ELEMENT_TYPES = ["pipe", "duct", "cable_tray"]


def generate_random_bbox():

    x = random.randint(0, 10000)
    y = random.randint(0, 10000)
    z = random.randint(0, 3000)

    width = random.randint(50, 400)
    length = random.randint(500, 2000)
    height = random.randint(50, 400)

    min_xyz = (x, y, z)
    max_xyz = (x + length, y + width, z + height)

    return min_xyz, max_xyz


def generate_elements(n=50):

    elements = []

    for i in range(n):

        element_type = random.choice(ELEMENT_TYPES)

        min_xyz, max_xyz = generate_random_bbox()

        element = MEPElement(
            element_id=f"E{i}",
            element_type=element_type,
            min_xyz=min_xyz,
            max_xyz=max_xyz
        )

        elements.append(element)

    return elements