import copy
import itertools

from evaluation_functions import goal_function, evaluation_of_the_result
from random_graph_generator import RandomGraph


def tabu_search(number_of_iteration, num_of_vertices, number_of_neighbors=5):
    tabu_list = {}
    start_graph = RandomGraph(numbers_of_vertex=num_of_vertices)
    start_graph.send_parameters_to_file(file_name='first_graph.txt')
    best_graph = copy.deepcopy(start_graph)
    best_result = goal_function(start_graph)

    print(f"Start results: {best_result}\n")

    for _ in range(number_of_iteration):
        neighbors_scores = {}

        for _ in range(number_of_neighbors):
            random_neighbor = copy.deepcopy(best_graph)
            random_neighbor.change_random_vertices_color()
            neighbors_scores.update({random_neighbor: goal_function(random_neighbor)})

        best_neighbor_graph, best_neighbor_score = get_best_score_from_neighbors(neighbors_scores)

        if best_neighbor_score not in tabu_list.values():
            tabu_desc = get_description_of_tabu_list(tabu_list)
            if best_neighbor_graph.prepare_graph_description() not in tabu_desc:
                if evaluation_of_the_result(best_result, best_neighbor_score) != best_result:
                    best_result = best_neighbor_score
                    best_graph = copy.deepcopy(best_neighbor_graph)
                tabu_list.update({best_graph: best_result})

    best_graph.send_parameters_to_file(file_name="best_graph.txt")
    print(f"Tabu list: {tabu_list}")
    print(f"Best result: {best_result}")


def tabu_search_with_step_back(number_of_iteration, num_of_vertices, number_of_neighbors=5):
    tabu_list = {}
    candidate_list = {}
    try_counter = 0
    start_graph = RandomGraph(numbers_of_vertex=num_of_vertices)
    start_graph.send_parameters_to_file(file_name='first_graph.txt')
    best_graph = copy.deepcopy(start_graph)
    best_result = goal_function(start_graph)
    final_graph = copy.deepcopy(start_graph)
    final_result = goal_function(start_graph)

    print(f"Start results: {best_result}\n")

    for _ in range(number_of_iteration):
        neighbors_scores = {}

        for _ in range(number_of_neighbors):
            random_neighbor = copy.deepcopy(best_graph)
            random_neighbor.change_random_vertices_color()
            neighbors_scores.update({random_neighbor: goal_function(random_neighbor)})

        best_neighbor_graph, best_neighbor_score = get_best_score_from_neighbors(neighbors_scores)
        candidate_list.update({best_neighbor_graph: best_neighbor_score})

        if best_neighbor_score not in tabu_list.values():
            tabu_desc = get_description_of_tabu_list(tabu_list)
            if best_neighbor_graph.prepare_graph_description() not in tabu_desc:
                if evaluation_of_the_result(best_result, best_neighbor_score) != best_result:
                    best_result = best_neighbor_score
                    best_graph = copy.deepcopy(best_neighbor_graph)
                    if evaluation_of_the_result(best_result, final_result) != final_result:
                        final_result = best_result
                        final_graph = copy.deepcopy(best_graph)
                else:
                    try_counter = try_counter + 1
                    if try_counter == 3:
                        try_counter = 0
                        best_result = list(candidate_list.values())[-3]
                        best_graph = list(candidate_list.keys())[-3]
                tabu_list.update({best_graph: best_result})

    final_graph.send_parameters_to_file(file_name="best_graph.txt")
    print(f"Best result: {final_result}")
    print(f"Tabu list: {tabu_list}")


def get_best_score_from_neighbors(neighbors_scores):
    best_graph = list(neighbors_scores.keys())[0]
    best_score = list(neighbors_scores.values())[0]

    for first_score, second_score in itertools.combinations(neighbors_scores.values(), 2):
        if evaluation_of_the_result(best_score, second_score) != best_score:
            best_score = second_score
            best_graph = [k for k, v in neighbors_scores.items() if v == best_score][0]
    return best_graph, best_score


def get_description_of_tabu_list(tabu_list):
    return [x.prepare_graph_description() for x in tabu_list.keys()]
