def h_manhattan(start, end):
    return int(abs(start[0]-end[0])+abs(start[1]-end[1]))


def h_euclidian(start, end):
    a2=(start[0]-end[0])**2
    b2=(start[1]-end[1])**2
    return int((a2+b2)**0.5)
