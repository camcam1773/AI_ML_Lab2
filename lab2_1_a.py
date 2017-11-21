import numpy as np
import path_planning as pp
from collections import deque
from pprint import pprint


def get_neighbors(world):
    """
    :param world:
    :type world: tuple
    :return:
    :rtype: dict
    """
    height = len(world)
    width = len(world[0]) if height else 0

    graph = {(i, j): {} for j in range(width)
             for i in range(height) if not world[i][j]}

    for row, col in graph.keys():
        if row < height - 1 and not world[row + 1][col]:
            graph[(row, col)]["S"] = (row + 1, col)
            graph[(row + 1, col)]["N"] = (row, col)
        if col < width - 1 and not world[row][col + 1]:
            graph[(row, col)]["E"] = (row, col + 1)
            graph[(row, col + 1)]["W"] = (row, col)
    return graph


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


def coord_to_x_y(coordinates):
    coord_x_y = [[], []]
    for i in coordinates:
        coord_x_y[0].append(i[1])
        coord_x_y[1].append(i[0])
    return coord_x_y


my_map = pp.generateMap2d([30, 30])
# pprint(my_map)
coord_bfs = find_path_bfs(my_map)
coord_dfs = find_path_dfs(my_map)

pp.plotMap(my_map, coord_to_x_y(coord_bfs))
pp.plotMap(my_map, coord_to_x_y(coord_dfs))
