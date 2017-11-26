import numpy as np
from collections import deque
from heapq import heappop, heappush
from heuristics import get_h
from search_utilities import get_neighbors


def find_path_bfs(world_nparray):
    """
    :param world_nparray:
    :type world_nparray: ndarray
    :return:
    :rtype: list
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
    cost = 0

    while queue:
        path, current = queue.popleft()
        if current == goal:
            route_str = path
            break
        if current in visited:
            continue
        visited.add(current)
        cost += 1
        for direction, neighbour in graph[current].iteritems():
            queue.append((path + direction, neighbour))
            world_ndarray[neighbour] = cost

    # print route_str
    print "Expanded nodes(BFS): ", len(visited)
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    world_ndarray[start] = -2
    world_ndarray[goal] = -3

    return route_coord, world_ndarray


def find_path_dfs(world_nparray):
    """
    :param world_nparray:
    :type world_nparray: ndarray
    :return:
    :rtype: list
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
    cost = 0

    while stack:
        path, current = stack.pop()
        if current == goal:
            route_str = path
            break
        if current in visited:
            continue
        visited.add(current)
        cost += 1
        for direction, neighbour in graph[current].iteritems():
            stack.append((path + direction, neighbour))
            world_ndarray[neighbour] = cost

    # print route_str
    print "Expanded nodes(DFS): ", len(visited)
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    world_ndarray[start] = -2
    world_ndarray[goal] = -3

    return route_coord, world_ndarray


def find_path_astar(world_nparray, heuristic_type="manhattan"):
    world_ndarray = np.copy(world_nparray)
    start = tuple(np.argwhere(world_ndarray == -2)[0])
    goal = tuple(np.argwhere(world_ndarray == -3)[0])

    world_ndarray[world_ndarray == -2] = 0
    world_ndarray[world_ndarray == -3] = 0

    world_tuple = tuple(map(tuple, world_ndarray))

    pr_queue = []
    heappush(pr_queue, (0 + get_h(start, goal, heuristic_type), 0, "", start))
    visited = set()
    graph = get_neighbors(world_tuple)
    route_str = ""

    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            route_str = path
            break
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current].iteritems():
            heappush(pr_queue, (cost + get_h(neighbour, goal, heuristic_type), cost + 1, path + direction, neighbour))
            world_ndarray[neighbour] = cost + 1

    # print route_str
    print "Expanded nodes(A*+", heuristic_type, "): ", len(visited)
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    world_ndarray[start] = -2
    world_ndarray[goal] = -3

    return route_coord, world_ndarray


def find_path_best_first(world_nparray, heuristic_type="manhattan"):
    world_ndarray = np.copy(world_nparray)
    start = tuple(np.argwhere(world_ndarray == -2)[0])
    goal = tuple(np.argwhere(world_ndarray == -3)[0])

    world_ndarray[world_ndarray == -2] = 0
    world_ndarray[world_ndarray == -3] = 0

    world_tuple = tuple(map(tuple, world_ndarray))

    pr_queue = []
    heappush(pr_queue, (get_h(start, goal, heuristic_type), 0, "", start))
    visited = set()
    graph = get_neighbors(world_tuple)
    route_str = ""

    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            route_str = path
            break
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current].iteritems():
            heappush(pr_queue, (get_h(neighbour, goal, heuristic_type), cost + 1, path + direction, neighbour))
            world_ndarray[neighbour] = cost + 1

    # print route_str
    print "Expanded nodes(Best First +", heuristic_type, "): ", len(visited)
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    world_ndarray[start] = -2
    world_ndarray[goal] = -3

    return route_coord, world_ndarray
