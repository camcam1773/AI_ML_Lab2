def h_manhattan(start, end):
    return int(abs(start[0] - end[0]) + abs(start[1] - end[1]))


def h_euclidian(start, end):
    a2 = (start[0] - end[0]) ** 2
    b2 = (start[1] - end[1]) ** 2
    return int((a2 + b2) ** 0.5)


def get_h(start, end, h_name="manhattan"):
    if h_name.lower() == "manhattan":
        return h_manhattan(start, end)
    elif h_name.lower() == "euclidian":
        return h_euclidian(start, end)
    else:
        print "Unknown heuristic. Using manhattan instead."
        return h_manhattan(start, end)