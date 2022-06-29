import copy
import random
import math

from evaluation_functions import goal_function, evaluation_of_the_result, get_score
from random_graph_generator import RandomGraph


def simulated_annealing(number_of_iteration, num_of_vertices):
    start_graph = RandomGraph(numbers_of_vertex=num_of_vertices)
    start_graph.send_parameters_to_file(file_name="first_graph.txt")
    best_graph = copy.deepcopy(start_graph)
    best_result = goal_function(start_graph)
    final_graph = copy.deepcopy(start_graph)
    final_result = goal_function(start_graph)
    iteration_counter = 1
    temperature = lambda x: (number_of_iteration/2)/x

    print(f"Start result: {best_result}")

    for _ in range(number_of_iteration):
        random_graph = copy.deepcopy(best_graph)
        random_graph.change_random_vertices_color()
        random_result = goal_function(random_graph)

        if evaluation_of_the_result(best_result, random_result) != best_result:
            best_graph = copy.deepcopy(random_graph)
            best_result = random_result
        else:
            u = random.random()
            if u < math.exp(-abs(get_score(best_graph)-get_score(random_graph))/temperature(iteration_counter)):
                best_graph = copy.deepcopy(random_graph)
                best_result = random_result
        if evaluation_of_the_result(best_result, final_result) != final_result:
            final_result = best_result
            final_graph = copy.deepcopy(best_graph)
        iteration_counter += 1

    final_graph.send_parameters_to_file(file_name="best_graph.txt")
    print('\n-----')
    print(f"Best result: {final_result}")
    print(f"Best score: {get_score(final_graph)}")
