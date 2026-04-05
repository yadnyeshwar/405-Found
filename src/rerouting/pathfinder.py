import heapq

SEARCH_LIMIT = 20   # max distance from start (meters / grid cells)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])


def get_neighbors(node):
    x,y,z = node
    return [
        (x+1,y,z),(x-1,y,z),
        (x,y+1,z),(x,y-1,z),
        (x,y,z+1),(x,y,z-1)
    ]


def within_limit(start, node):
    return (
        abs(node[0]-start[0]) <= SEARCH_LIMIT and
        abs(node[1]-start[1]) <= SEARCH_LIMIT and
        abs(node[2]-start[2]) <= SEARCH_LIMIT
    )


def a_star(start, goal, obstacles):

    open_set=[]
    heapq.heappush(open_set,(0,start))

    came_from={}
    g_score={start:0}

    while open_set:

        _,current=heapq.heappop(open_set)

        if current==goal:

            path=[]

            while current in came_from:
                path.append(current)
                current=came_from[current]

            path.append(start)
            path.reverse()

            return path

        for neighbor in get_neighbors(current):

            if neighbor in obstacles:
                continue

            if not within_limit(start,neighbor):
                continue

            tentative=g_score[current]+1

            if neighbor not in g_score or tentative<g_score[neighbor]:

                came_from[neighbor]=current
                g_score[neighbor]=tentative

                f=tentative+heuristic(neighbor,goal)

                heapq.heappush(open_set,(f,neighbor))

    return None