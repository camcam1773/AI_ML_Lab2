import path_planning as pp
from search_utilities import coord_to_x_y
from search import find_path_dfs, find_path_bfs, find_path_random

my_map = pp.generateMap2d([60, 60])

coord_bfs = find_path_bfs(my_map)
coord_dfs = find_path_dfs(my_map)
coord_random = find_path_random(my_map)

plt_list = [[pp.generate_colormap(coord_bfs[1]), coord_to_x_y(coord_bfs[0]), 'BFS'],
            [pp.generate_colormap(coord_dfs[1]), coord_to_x_y(coord_dfs[0]), 'DFS'],
            [pp.generate_colormap(coord_random[1]), coord_to_x_y(coord_random[0]), 'Random']
            ]

pp.multi_plot(plt_list)
