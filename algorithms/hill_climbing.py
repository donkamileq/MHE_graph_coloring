import copy

from evaluation_functions import goal_function, evaluation_of_the_result
from random_graph_generator import RandomGraph


def hill_climbing_random(number_of_iteration, num_of_vertices):
    start_graph = RandomGraph(numbers_of_vertex=num_of_vertices)
    best_graph = copy.deepcopy(start_graph)
    random_graph = copy.deepcopy(start_graph)

    best_result = goal_function(start_graph)
    print(f"First result: {best_result}")
    start_graph.send_parameters_to_file(file_name="first_graph.txt")

    for _ in range(number_of_iteration):
        random_graph.change_random_vertices_color()
        random_result = goal_function(random_graph)

        if evaluation_of_the_result(best_result, random_result) != best_result:
            best_graph = copy.deepcopy(random_graph)
            best_result = random_result

    best_result = goal_function(best_graph)
    best_graph.send_parameters_to_file(file_name="best_graph.txt")
    print(f"Best result: {best_result}")


def hill_climbing_best(number_of_iteration, num_of_vertices):
    start_graph = RandomGraph(numbers_of_vertex=num_of_vertices)
    best_graph = copy.deepcopy(start_graph)
    random_graph = copy.deepcopy(start_graph)

    best_result = goal_function(start_graph)
    print(f"First result: {best_result}")
    start_graph.send_parameters_to_file(file_name="first_graph.txt")

    for _ in range(number_of_iteration):
        random_graph.change_random_bad_vertices_color()
        random_result = goal_function(random_graph)

        if evaluation_of_the_result(best_result, random_result):
            best_graph = copy.deepcopy(random_graph)
            best_result = random_result

    best_result = goal_function(best_graph)
    best_graph.send_parameters_to_file(file_name="best_graph.txt")
    print(f"Best result: {best_result}")






