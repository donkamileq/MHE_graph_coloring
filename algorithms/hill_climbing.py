from evaluation_functions import goal_function, check_graph, evaluation_of_the_result
from random_graph_generator import RandomGraph


def hill_climbing_random(number_of_iteration, num_of_verticies):
    start_graph = RandomGraph(numbers_of_vertex=num_of_verticies)
    start_graph.send_parameters_to_file()
    best_result = goal_function(start_graph)

    # print(best_result)
    # print(best_result[0])
    # print(best_result[1])

    for _ in range(number_of_iteration):
        random_graph = RandomGraph(numbers_of_vertex=num_of_verticies)
        random_graph.prepare_graph_parameters()
        random_result = goal_function(random_graph)
        best_result = evaluation_of_the_result(best_result, random_result)

    # print(best_result)
    # print(best_result[0])
    # print(best_result[1])





