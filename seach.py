import numpy as np
from collections import deque
from heapq import heappop, heappush
from heuristics import h_manhattan
from search_utilities import get_neighbors


def find_path_bfs(world_nparray):
    """
    :param world_nparray:
    :type world_nparray: ndarray
    :return:
    :rtype: str
    """
    world_ndarray = np.copy(world_nparray)
    start = tuple(np.argwhere(world_ndarray == -2)[0])
    goal = tuple(np.argwhere(world_ndarray == -3)[0])

    world_ndarray[world_ndarray == -2] = 0
    world_ndarray[world_ndarray == -3] = 0

    world_tuple = tuple(map(tuple, world_ndarray))

    queue = deque([("", start)])
    visited = set()
    graph = get_neighbors(world_tuple)
    route_str = ""

    while queue:
        path, current = queue.popleft()
        if current == goal:
            route_str = path
            break
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current].iteritems():
            queue.append((path + direction, neighbour))

    print route_str
    print "Visited nodes: ", len(visited)
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    return route_coord


def find_path_dfs(world_nparray):
    """
    :param world_nparray:
    :type world_nparray: ndarray
    :return:
    :rtype: str
    """
    world_ndarray = np.copy(world_nparray)
    start = tuple(np.argwhere(world_ndarray == -2)[0])
    goal = tuple(np.argwhere(world_ndarray == -3)[0])

    world_ndarray[world_ndarray == -2] = 0
    world_ndarray[world_ndarray == -3] = 0

    world_tuple = tuple(map(tuple, world_ndarray))

    stack = deque([("", start)])
    visited = set()
    graph = get_neighbors(world_tuple)
    route_str = ""

    while stack:
        path, current = stack.pop()
        if current == goal:
            route_str = path
            break
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current].iteritems():
            stack.append((path + direction, neighbour))

    print route_str
    print "Visited nodes: ", len(visited)
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    return route_coord


def find_path_astar(world_nparray):
    world_ndarray = np.copy(world_nparray)
    start = tuple(np.argwhere(world_ndarray == -2)[0])
    goal = tuple(np.argwhere(world_ndarray == -3)[0])

    world_ndarray[world_ndarray == -2] = 0
    world_ndarray[world_ndarray == -3] = 0

    world_tuple = tuple(map(tuple, world_ndarray))

    pr_queue = []
    heappush(pr_queue, (0 + h_manhattan(start, goal), 0, "", start))
    visited = set()
    graph = get_neighbors(world_tuple)
    route_str = ""

    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            route_str=path
            break
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current].iteritems():
            heappush(pr_queue, (cost + h_manhattan(neighbour, goal), cost + 1,
                                path + direction, neighbour))

    print route_str
    print "Visited nodes(A*): ", len(visited)
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    return route_coord
