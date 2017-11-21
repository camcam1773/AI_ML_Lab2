class Point:
    """ Point class represents and manipulates x,y coordinates. """

    def __init__(self, ix=0, iy=0):
        """ Create a new point at the origin """
        self.x = int(ix)
        self.y = int(iy)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
