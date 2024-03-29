import random
import numpy as np
import matplotlib.pyplot as plt

# sizeOfMap2D = [100, 50]
# percentOfObstacle = 0.9  # random.randrange(70, 90)/100.0  # 30% - 60%, random


# Generate 2D matrix of size x * y
# starting Point and Ending Point

def generateMap2d(size_, percentOfObstacle = 0.9):
    # Generates a random 2d map of size size_. You can choose your desired size but whatever solution you come up with
    # has to work independently of map size

    size_x, size_y = size_[0], size_[1]

    map2d = np.random.rand(size_y, size_x)
    perObstacles_ = percentOfObstacle
    map2d[map2d <= perObstacles_] = 0
    map2d[map2d > perObstacles_] = -1

    yloc, xloc = [np.random.random_integers(0, size_x - 1, 2), np.random.random_integers(0, size_y - 1, 2)]
    while (yloc[0] == yloc[1]) and (xloc[0] == xloc[1]):
        yloc, xloc = [np.random.random_integers(0, size_x - 1, 2), np.random.random_integers(0, size_y - 1, 2)]

    map2d[xloc[0]][yloc[0]] = -2
    map2d[xloc[1]][yloc[1]] = -3

    # print('start', xloc[0], yloc[0])
    # print('goal', xloc[1], yloc[1])

    # return map2d, [xloc[0], yloc[0]], [xloc[1], yloc[1]]
    return map2d


# Generate specific map
def generateMap2d_obstacle(size_, percentOfObstacle = 0.9):
    # Generates a special map with the middle blocked and passing from left to right being possible at the top or bottom
    # part of the map. If for some reason the map fails to generate like that rerun it as it is not foolproof
    size_x, size_y = size_[0], size_[1]
    map2d = generateMap2d(size_, percentOfObstacle)

    map2d[map2d == -2] = 0
    map2d[map2d == -3] = 0

    # add special obstacle
    xtop = [np.random.random_integers(5, 3 * size_x // 10 - 2),
            np.random.random_integers(7 * size_x // 10 + 3, size_x - 5)]
    ytop = np.random.random_integers(7 * size_y // 10 + 3, size_y - 5)
    xbot = np.random.random_integers(3, 3 * size_x // 10 - 5), np.random.random_integers(7 * size_x // 10 + 3,
                                                                                         size_x - 5)
    ybot = np.random.random_integers(5, size_y // 5 - 3)

    map2d[ybot, xbot[0]:xbot[1] + 1] = -1
    map2d[ytop, xtop[0]:xtop[1] + 1] = -1
    minx = (xbot[0] + xbot[1]) // 2
    maxx = (xtop[0] + xtop[1]) // 2
    if minx > maxx:
        tempx = minx
        minx = maxx
        maxx = tempx
    if maxx == minx:
        maxx = maxx + 1

    map2d[ybot:ytop, minx:maxx] = -1
    startp = [np.random.random_integers(0, size_x // 2 - 4), np.random.random_integers(ybot + 1, ytop - 1)]

    map2d[startp[1], startp[0]] = -2
    goalp = [np.random.random_integers(size_x // 2 + 4, size_x - 3), np.random.random_integers(ybot + 1, ytop - 1)]

    map2d[goalp[1], goalp[0]] = -3
    # return map2d, [startp[1], startp[0]], [goalp[1], goalp[0]], [ytop, ybot]
    return map2d, (ytop, ybot, minx)


def generateMap2d_swamp(size_):
    percentOfObstacle = 0.98
    # Generates a random 2d map of size size_. You can choose your desired size but whatever solution you come up with has
    # to work independently of map size
    size_x, size_y = size_[0], size_[1]
    cov_scale = 2
    samples_1 = np.random.multivariate_normal([-2.5, -2.5], [[cov_scale, 0], [0, cov_scale]], size_[0] * size_[1] * 20)
    samples_2 = np.random.multivariate_normal([2.5, 2.5], [[cov_scale, 0], [0, cov_scale]], size_[0] * size_[1] * 20)
    samples_3 = np.random.multivariate_normal([-1, 1], [[cov_scale, 0], [0, cov_scale]], size_[0] * size_[1] * 20)

    H, xedges, yedges = np.histogram2d(np.concatenate((samples_1[:, 1], samples_2[:, 1], samples_3[:, 1]), axis=0),
                                       np.concatenate((samples_1[:, 0], samples_2[:, 0], samples_3[:, 0]), axis=0),
                                       range=[[-8, 8], [-8, 8]], bins=[size_x, size_y], normed=True)

    map2d = np.random.rand(size_y, size_x)
    perObstacles_ = percentOfObstacle
    map2d[map2d <= perObstacles_] = 0
    indices_obstacles = map2d > perObstacles_

    scale = 300
    map2d = map2d + (H * scale)

    map2d[indices_obstacles > perObstacles_] = -1

    map2d[-1][0] = -2
    map2d[0][-1] = -3

    plt.figure()
    plt.title('Swamp')
    plt.imshow(map2d.T, interpolation='nearest', origin="lower")
    plt.colorbar()
    plt.draw()
    plt.show()

    center = [size_x * (10.5 / 16), size_y * (10.5 / 16)], \
             [size_x * (5.5 / 16), size_y * (5.5 / 16)], \
             [size_x * (7 / 16), size_y * (9 / 16)]

    return map2d, [H * scale, [[int(x), int(y)] for [x, y] in center]]


def generate_colormap(map2d_):
    """
    Generates the color map based on the provided path costs
    :param map2d_:
    :type map2d_: ndarray
    :return: a map as described in lab2 description containing integer numbers. Each number has a specific meaning.
    :rtype: list
    """

    import matplotlib.cm as cm
    plt.interactive(False)

    greennumber = map2d_.max()
    # greennumber = len(np.unique(map2d_))
    # print(greennumber)
    colors = cm.winter(np.linspace(0, 1, greennumber))

    colorsMap2d = [[[] for x in xrange(map2d_.shape[1])] for y in range(map2d_.shape[0])]
    # Assign RGB Val for starting point and ending point
    locStart = np.where(map2d_ == -2)
    locEnd = np.where(map2d_ == -3)

    colorsMap2d[locStart[0][0]][locStart[1][0]] = [.0, .0, .0, 1.0]  # black
    colorsMap2d[locEnd[0][0]][locEnd[1][0]] = [1.0, 1.0, .0, 1.0]  # gray

    # Assign RGB Val for obstacle
    locObstacle = np.where(map2d_ == -1)
    for iposObstacle in range(len(locObstacle[0])):
        colorsMap2d[locObstacle[0][iposObstacle]][locObstacle[1][iposObstacle]] = [1.0, .0, .0, 1.0]
    # Assign 0
    locZero = np.where(map2d_ == 0)

    for iposZero in range(len(locZero[0])):
        colorsMap2d[locZero[0][iposZero]][locZero[1][iposZero]] = [1.0, 1.0, 1.0, 1.0]

    # Assign Expanded nodes
    locExpand = np.where(map2d_ > 0)

    for iposExpand in range(len(locExpand[0])):
        a = locExpand[0][iposExpand]
        b = locExpand[1][iposExpand]
        colorsMap2d[a][b] = colors[int(round(map2d_[a][b])) - 1]

    for irow in range(len(colorsMap2d)):
        for icol in range(len(colorsMap2d[irow])):
            # print(map2d_[irow][icol], colorsMap2d[irow][icol])
            if colorsMap2d[irow][icol] == []:
                colorsMap2d[irow][icol] = [1.0, 0.0, 0.0, 1.0]
                # colorsMap2d[irow][icol] = [1.0, 1.0, 1.0, 1.0]
    return colorsMap2d


def multi_plot(plot_list):
    """
    Plots the paths found by provided by the search algoritms in seperates windows
    :param plot_list: A list that contains the colormap, coordinates
    :type plot_list: list
    :return: None
    :rtype: None
    """
    for c in plot_list:
        plt.figure()
        if len(c) == 1:
            c.append([[], []])
        elif len(c) == 2:
            c.append('')
        plt.title(c[2])
        plt.imshow(c[0], interpolation='nearest')
        plt.colorbar()
        path_ = c[1]
        plt.plot(path_[:][0], path_[:][1], color='magenta', linewidth=2.5)
        plt.ylim(-1, len(c[0][0]))
        plt.xlim(-1, len(c[0][1]))
    plt.draw()
    plt.show()
