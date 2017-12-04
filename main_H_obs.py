import path_planning as pp
from search_utilities import coord_to_x_y
from search import find_path_astar,a_star_obs

h_obs = pp.generateMap2d_obstacle([60, 60])
obs_map = h_obs[0]
print h_obs[1]

coord_astar_obs = find_path_astar(obs_map, "manhattan")
coord_astar_obs_c = a_star_obs(h_obs)

plt_list_h = [[pp.generate_colormap(coord_astar_obs[1]), coord_to_x_y(coord_astar_obs[0]), "H: A* + Manhattan"],
              [pp.generate_colormap(coord_astar_obs_c[1]), coord_to_x_y(coord_astar_obs_c[0]), "H: A* + Custom"]]

pp.multi_plot(plt_list_h)
