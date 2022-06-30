import copy
import random

from algorithms.genetic_algorithm import genetic_algorithm, crossover_single_point, mutation_ten_percent, \
    mutation_half_individual, crossover_double_point
from algorithms.hill_climbing import hill_climbing_random, hill_climbing_best
from algorithms.simulated_annealing import simulated_annealing
from algorithms.tabu_search import tabu_search, tabu_search_with_step_back
from evaluation_functions import goal_function, check_graph, get_score
from random_graph_generator import RandomGraph

# graph = RandomGraph(numbers_of_vertex=10)
# graph.send_parameters_to_file(file_name="graph.txt")

# tabu_search(number_of_iteration=10,
#             num_of_vertices=200)

#
# tabu_search_with_step_back(number_of_iteration=200,
#                            num_of_vertices=10)


# simulated_annealing(number_of_iteration=100, num_of_vertices=20)

# genetic_algorithm(num_of_vertices=20, population_size=10,
#                   crossover_single=True, mutation_ten=True)
#
# genetic_algorithm(num_of_vertices=20, population_size=10,
#                   crossover_single=True, mutation_half=True)

# genetic_algorithm(num_of_vertices=20, population_size=10,
#                   crossover_double=True, mutation_ten=True)

# genetic_algorithm(num_of_vertices=20, population_size=10,
#                   crossover_double=True, mutation_ten=True)