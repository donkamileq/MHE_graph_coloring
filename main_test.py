from algorithms.hill_climbing import hill_climbing_random, hill_climbing_best
from algorithms.tabu_search import tabu_search, tabu_search_with_step_back
from evaluation_functions import goal_function, check_graph
from random_graph_generator import RandomGraph

# graph = RandomGraph(numbers_of_vertex=20)
# graph.send_parameters_to_file(file_name="graph.txt")

# tabu_search(number_of_iteration=10,
#             num_of_vertices=200)


tabu_search_with_step_back(number_of_iteration=20,
                           num_of_vertices=10)
