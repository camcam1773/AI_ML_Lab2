import path_planning as pp
from search_utilities import coord_to_x_y
from search import find_path_astar, find_path_best_first

my_map = pp.generateMap2d([60, 60])

coord_astar_m = find_path_astar(my_map, "manhattan")
coord_astar_e = find_path_astar(my_map, "euclidian")
coord_gbf_m = find_path_best_first(my_map, "manhattan")
coord_gbf_e = find_path_best_first(my_map, "euclidian")

plt_list = [[pp.generate_colormap(coord_astar_m[1]), coord_to_x_y(coord_astar_m[0]), "A* + Manhattan"],
            [pp.generate_colormap(coord_astar_e[1]), coord_to_x_y(coord_astar_e[0]), "A* + Euclidian"],
            [pp.generate_colormap(coord_gbf_m[1]), coord_to_x_y(coord_gbf_m[0]), "Greedy Best First + Manhattan H"],
            [pp.generate_colormap(coord_gbf_e[1]), coord_to_x_y(coord_gbf_e[0]), "Greedy Best First + Euclidian H"]
            ]

pp.multi_plot(plt_list)
