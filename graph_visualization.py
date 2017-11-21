############################################
#  Helper function for visualizing a tree  #
############################################

import matplotlib.pyplot as plt
import networkx as nx

def hierarchy_pos(G, root, levels=None, width=1., height=1.):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node
       levels: a dictionary
               key: level number (starting from 0)
               value: number of nodes in this level
       width: horizontal space allocated for drawing
       height: vertical space allocated for drawing'''
    TOTAL = "total"
    CURRENT = "current"
    def make_levels(levels, node=root, currentLevel=0, parent=None):
        """Compute the number of nodes for each level
        """
        if not currentLevel in levels:
            levels[currentLevel] = {TOTAL : 0, CURRENT : 0}
        levels[currentLevel][TOTAL] += 1
        neighbors = G.neighbors(node)
        if parent is not None:
            neighbors.remove(parent)
        for neighbor in neighbors:
            levels =  make_levels(levels, neighbor, currentLevel + 1, node)
        return levels

    def make_pos(pos, node=root, currentLevel=0, parent=None, vert_loc=0):
        dx = 1./levels[currentLevel][TOTAL]
        left = dx/2
        pos[node] = ((left + dx*levels[currentLevel][CURRENT])*width, vert_loc)
        levels[currentLevel][CURRENT] += 1
        neighbors = G.neighbors(node)
        if parent is not None:
            neighbors.remove(parent)
        for neighbor in neighbors:
            pos = make_pos(pos, neighbor, currentLevel + 1, node, vert_loc-vert_gap)
        return pos
    if levels is None:
        levels = make_levels({})
    else:
        levels = {l:{TOTAL: levels[l], CURRENT:0} for l in levels}
    vert_gap = height / (max([l for l in levels])+1)
    return make_pos({})

# create a graph
G=nx.Graph()

# adding edges
G.add_edges_from([('start', 'a_bet_5'),
                  ('start', 'a_bet_10'),
                  ('start', 'a_bet_25'),
                  ('start', 'a_call_5'),
                  ('start', 'a_fold_0'),
                  ('a_bet_5', 'b_call_5'),
                  ('a_bet_5', 'b_fold_0'),
                  ('a_bet_5', 'b_bet_10'),
                  ('a_bet_10', 'b_bet_5'),
                  ('a_bet_10', 'b_bet_25'),
                  ('a_bet_25', '...'),
                  ('a_bet_25', '....'),
                  ('a_call_5', 'showdown'),
                  ('a_fold_0', 'hand_end')
                  ])

# get position of nodes
pos = hierarchy_pos(G,'start')

# draw a graph
nx.draw(G, pos=pos, with_labels=True)

plt.show()


