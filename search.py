import numpy as np
from collections import deque
from heapq import heappop, heappush
from heuristics import get_h
from search_utilities import get_neighbors
from random import shuffle


def find_path_bfs(world_nparray):
    """
    Breath first search algorithm
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

    queue = deque([("", start)])  # deque appends faster.
    visited = set()  # Each element has to be unique in a set
    graph = get_neighbors(world_tuple)
    route_str = ""
    cost = 0

    while queue:
        path, current = queue.popleft()  # LIFO : Last in, first out
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

    # print "Expanded nodes(BFS): ", len(visited), " Path length: ", len(route_str)
    # Convert string directions to 2D(x,y) coordinates
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    world_ndarray[start] = -2
    world_ndarray[goal] = -3

    return route_coord, world_ndarray, len(visited), len(route_str)


def find_path_dfs(world_nparray):
    """
    Depth first search algorithm
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

    stack = deque([("", start)])  # deque appends faster.
    visited = set()  # Each element has to be unique in a set
    graph = get_neighbors(world_tuple)
    route_str = ""
    cost = 0

    while stack:
        path, current = stack.pop()  # LIFO : Last in, first out
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

    # print "Expanded nodes(DFS): ", len(visited), " Path length: ", len(route_str)
    # Convert string directions to 2D(x,y) coordinates
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    world_ndarray[start] = -2
    world_ndarray[goal] = -3

    return route_coord, world_ndarray, len(visited), len(route_str)


def find_path_random(world_nparray):
    """
    Random search algorithm
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

    queue = deque([("", start)])  # deque appends faster.
    visited = set()  # Each element has to be unique in a set
    graph = get_neighbors(world_tuple)
    route_str = ""
    cost = 0

    while queue:
        path, current = queue.pop()  # FIFO
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
        shuffle(queue)

    # print "Expanded nodes(Random): ", len(visited), " Path length: ", len(route_str)
    # Convert string directions to 2D(x,y) coordinates
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    world_ndarray[start] = -2
    world_ndarray[goal] = -3

    return route_coord, world_ndarray, len(visited), len(route_str)


def find_path_astar(world_nparray, heuristic_type=""):
    """
    A-Star search algorith with different heuristic types
    :param world_nparray:
    :type world_nparray: ndarray
    :param heuristic_type:
    :type heuristic_type: str
    :return: list of coordinates and cost modified world map
    :rtype: list
    """
    world_ndarray = np.copy(world_nparray)
    start = tuple(np.argwhere(world_ndarray == -2)[0])
    goal = tuple(np.argwhere(world_ndarray == -3)[0])

    world_ndarray[world_ndarray == -2] = 0
    world_ndarray[world_ndarray == -3] = 0

    world_tuple = tuple(map(tuple, world_ndarray))

    pr_queue = []  # Use heapqueue as priority queue
    heappush(pr_queue, (0 + get_h(start, goal, heuristic_type), 0, "", start))
    visited = set()  # Each element has to be unique in a set
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

    # print "Expanded nodes(A*+", heuristic_type, "): ", len(visited), " Path length: ", len(route_str)
    # Convert string directions to 2D(x,y) coordinates
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    world_ndarray[start] = -2
    world_ndarray[goal] = -3

    return route_coord, world_ndarray, len(visited), len(route_str)


def find_path_best_first(world_nparray, heuristic_type=""):
    """
    Greedy best first search algorithm
    :param world_nparray:
    :type world_nparray: ndarray
    :param heuristic_type: heuristic functon name (default: manhattan)
    :type heuristic_type: str
    :return: list of coordinates and cost modified world map
    :rtype: list
    """
    world_ndarray = np.copy(world_nparray)
    start = tuple(np.argwhere(world_ndarray == -2)[0])
    goal = tuple(np.argwhere(world_ndarray == -3)[0])

    world_ndarray[world_ndarray == -2] = 0
    world_ndarray[world_ndarray == -3] = 0

    world_tuple = tuple(map(tuple, world_ndarray))

    pr_queue = []  # Use heapqueue as priority queue
    heappush(pr_queue, (get_h(start, goal, heuristic_type), 0, "", start))
    visited = set()  # Each element has to be unique in a set
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

    # print "Expanded nodes(Best First +", heuristic_type, "): ", len(visited), "Path length: ", len(route_str)
    # Convert string directions to 2D(x,y) coordinates
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    world_ndarray[start] = -2 # Mark the start and end coordinates again
    world_ndarray[goal] = -3

    return route_coord, world_ndarray, len(visited), len(route_str)


def a_star_obs(obs_map):
    """
    A Star search algorith modified for H obstacle which uses a custom specific heuristic
    :param obs_map:
    :type obs_map: ndarray
    :return:
    :rtype: list
    """
    world_ndarray = np.copy(obs_map[0])

    start = tuple(np.argwhere(world_ndarray == -2)[0])
    goal = tuple(np.argwhere(world_ndarray == -3)[0])

    world_ndarray[world_ndarray == -2] = 0
    world_ndarray[world_ndarray == -3] = 0

    world_tuple = tuple(map(tuple, world_ndarray))

    def h_custom_i(cur, end, obstacle):
        ytop, ybot, minx = obstacle
        cur_y, cur_x = cur
        end_y, end_x = end
        obs_bot = np.where(world_ndarray[ybot] == -1)[0][0]
        mid_y = ybot + (ytop - ybot) // 2
        if cur_y in range(ybot, ytop) and cur_x in range(max(obs_bot, start[1]), end_x):
            return 5000 - abs(minx - cur_x) ** 2 - abs(cur_y - mid_y) ** 2
        return abs(cur_x - end_x) + abs(cur_y - end_y)

    pr_queue = []  # Use heapqueue as priority queue
    heappush(pr_queue, (0 + h_custom_i(start, goal, obs_map[1]), 0, "", start))
    visited = set()  # Each element has to be unique in a set
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
            heappush(pr_queue, (cost + h_custom_i(neighbour, goal, obs_map[1]), cost + 1, path + direction, neighbour))
            world_ndarray[neighbour] = cost + 1

    # print "Expanded nodes(A*+Custom H): ", len(visited), " Path length: ", len(route_str)
    # Convert string directions to 2D(x,y) coordinates
    route_coord = [start]
    for p in route_str:
        route_coord.append(graph[route_coord[-1]][p])

    world_ndarray[start] = -2 # Mark the start and end coordinates again
    world_ndarray[goal] = -3

    return route_coord, world_ndarray, len(visited), len(route_str)
