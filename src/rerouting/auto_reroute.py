from src.rerouting.pathfinder import a_star

GRID_SIZE = 2.0


def to_grid(v):
    return int(v / GRID_SIZE)


def bbox_to_grid(element):

    cells=set()

    x1,y1,z1=to_grid(element.min_x),to_grid(element.min_y),to_grid(element.min_z)
    x2,y2,z2=to_grid(element.max_x),to_grid(element.max_y),to_grid(element.max_z)

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                cells.add((x,y,z))

    return cells


def generate_obstacle_map(elements, ignore_id):

    obstacles=set()

    for e in elements:

        if e.element_id==ignore_id:
            continue

        obstacles |= bbox_to_grid(e)

    return obstacles


def auto_reroute(start,goal,elements,reroute_id):

    obstacles=generate_obstacle_map(elements,reroute_id)

    start=(to_grid(start[0]),to_grid(start[1]),to_grid(start[2]))
    goal=(to_grid(goal[0]),to_grid(goal[1]),to_grid(goal[2]))

    path=a_star(start,goal,obstacles)

    return path