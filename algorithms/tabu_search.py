import collections
import copy
import itertools

from evaluation_functions import goal_function, evaluation_of_the_result
from random_graph_generator import RandomGraph


def tabu_search(number_of_iteration, num_of_vertices, tabu_size=10):
    tabu_list = {}

    start_graph = RandomGraph(numbers_of_vertex=num_of_vertices)
    best_graph = copy.deepcopy(start_graph)
    best_result = goal_function(start_graph)

    print(f"Start results: {best_result}\n")

    for _ in range(number_of_iteration):
        neighbors_scores = {}
        for _ in range(tabu_size):
            random_neighbor = copy.deepcopy(start_graph)
            random_neighbor.change_random_bad_vertices_color()
            neighbors_scores.update({random_neighbor: goal_function(random_neighbor)})

        best_neighbor_graph, best_neighbor_score = get_best_score_from_neighbors(neighbors_scores)
        

        if best_neighbor_score not in tabu_list.values():
            if best_neighbor_graph not in tabu_list.keys():
                if evaluation_of_the_result(best_result, best_neighbor_score):
                    best_result = best_neighbor_score
                    best_graph = copy.deepcopy(best_neighbor_graph)
                tabu_list.update({best_graph: best_result})





        # print(best_result)
        # print(best_graph)
        print(tabu_list)







def get_best_score_from_neighbors(neighbors_scores):
    best_graph = list(neighbors_scores.keys())[0]
    best_score = list(neighbors_scores.values())[0]

    for first_score, second_score in itertools.combinations(neighbors_scores.values(), 2):
        if evaluation_of_the_result(best_score, second_score) != best_score:
            best_score = second_score
            best_graph = [k for k, v in neighbors_scores.items() if v == best_score][0]

    return best_graph, best_score


