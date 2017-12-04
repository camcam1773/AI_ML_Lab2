def get_neighbors(world):
    """
    Converts 2D tuple to 2D dictionary which reprents the graph
    :param world: special 2D tuple that reprents the map with obstacles
    :type world: tuple
    :return: graph
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


def coord_to_x_y(coordinates):
    """
    Modifies the list of coordinates to format neccesary for path representation
    :param coordinates: a list of coordinates
    :type coordinates: list
    :return: a list of 2 inner lists which the X and Y coordinates separately
    :rtype: list
    """
    coord_x_y = [[], []]
    for i in coordinates:
        coord_x_y[0].append(i[1])
        coord_x_y[1].append(i[0])
    return coord_x_y
