def h_manhattan(start, end):
    """
    Manhattan heuristic distance
    :param start: starting coordinate (array of 2 ints)
    :type start: tuple
    :param end: end coordinate (array of 2 ints)
    :type end: tuple
    :return: manhattan heuristic distance
    :rtype: int
    """
    return int(abs(start[0] - end[0]) + abs(start[1] - end[1]))


def h_euclidian(start, end):
    """
    Euclidian heuristic distance
    :param start: starting coordinate (array of 2 ints)
    :type start: tuple
    :param end: end coordinate (array of 2 ints)
    :type end: tuple
    :return: manhattan heuristic distance
    :rtype: int
    """
    a2 = (start[0] - end[0]) ** 2
    b2 = (start[1] - end[1]) ** 2
    return int(round((a2 + b2) ** 0.5))


def get_h(start, end, h_name):
    """
    Gets the heuristic distance based on the input name
    :param start: starting coordinate (array of 2 ints)
    :type start: tuple
    :param end: end coordinate (array of 2 ints)
    :type end: tuple
    :param h_name: name of the heuristic type
    :type h_name: str
    :return: gets the specified type of heuristic distance
    :rtype: int
    """
    if h_name.lower() == "manhattan":
        return h_manhattan(start, end)
    elif h_name.lower() == "euclidian":
        return h_euclidian(start, end)
    else:
        print "Unknown heuristic. Using manhattan instead."
        return h_manhattan(start, end)