import copy
import time

from evaluation_functions import goal_function, check_graph, evaluation_of_the_result
from random_graph_generator import RandomGraph


def hill_climbing_random(number_of_iteration, num_of_vertices):
    start_graph = RandomGraph(numbers_of_vertex=num_of_vertices)
    best_graph = copy.copy(start_graph)
    best_result = goal_function(best_graph)
    print(f"First result: {best_result}")
    best_graph.send_parameters_to_file()
    check_graph(best_graph)

    for _ in range(number_of_iteration):
        best_graph.change_random_vertices_color()
        random_result = goal_function(best_graph)
        best_result, best_graph = evaluation_of_the_result(best_result, random_result, start_graph, best_graph)

    print(f"Best result: {best_result}")
    check_graph(best_graph)
