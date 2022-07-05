import copy
import itertools

from graph.evaluation_functions import goal_function, evaluation_of_the_result, make_figure_for_results, get_score


def tabu_search(start_graph, number_of_iteration):
    tabu_list = {}
    best_graph = copy.deepcopy(start_graph)
    best_result = goal_function(start_graph)
    temp_graph = copy.deepcopy(start_graph)
    iteration = 0
    results = []

    for it in range(number_of_iteration):
        neighbors_scores = {}

        for _ in range(best_graph.numbers_of_vertex * len(set(best_graph.vertex_colors))):
            random_neighbor = copy.deepcopy(temp_graph)
            random_neighbor.change_random_one_vertex_color()
            neighbors_scores.update({random_neighbor: goal_function(random_neighbor)})

        best_neighbor_graph, best_neighbor_score = get_best_score_from_neighbors(neighbors_scores)
        temp_graph = copy.deepcopy(best_neighbor_graph)
        results.append(get_score(best_neighbor_graph))

        if best_neighbor_score not in tabu_list.values():
            tabu_desc = get_description_of_tabu_list(tabu_list)
            if best_neighbor_graph.prepare_graph_description() not in tabu_desc:
                if evaluation_of_the_result(best_result, best_neighbor_score) != best_result:
                    best_result = best_neighbor_score
                    best_graph = copy.deepcopy(best_neighbor_graph)
                    best_graph.update_vertices_colors()
                if len(tabu_list) == 10:
                    for k in tabu_list.keys():
                        k_to_remove = k
                        tabu_list.pop(k_to_remove)
                        break
                tabu_list.update({best_graph: best_result})

        iteration = it
        if best_result[1] == 0:
            break

    best_graph.update_vertices_colors()
    best_graph.send_parameters_to_file(file_name="graph_representation/best_graph_tabu_search.txt")
    print(f"Tabu list: {tabu_list}")
    print(f"Best result: {best_result}")
    print(f"Best score: {get_score(best_graph)}")
    print(f"Number of iteration: {iteration + 1}")
    make_figure_for_results(results=results, plot_name="tabu_search")


def tabu_search_with_step_back(start_graph, number_of_iteration, number_of_neighbors=5):
    tabu_list = {}
    candidate_list = {}
    try_counter = 0
    best_graph = copy.deepcopy(start_graph)
    best_result = goal_function(start_graph)
    temp_graph = copy.deepcopy(start_graph)
    final_graph = copy.deepcopy(start_graph)
    final_result = goal_function(start_graph)
    iteration = 0
    results = []

    for it in range(number_of_iteration):
        neighbors_scores = {}

        for _ in range(best_graph.numbers_of_vertex * len(set(best_graph.vertex_colors))):
            random_neighbor = copy.deepcopy(temp_graph)
            random_neighbor.change_random_one_vertex_color()
            neighbors_scores.update({random_neighbor: goal_function(random_neighbor)})

        best_neighbor_graph, best_neighbor_score = get_best_score_from_neighbors(neighbors_scores)
        temp_graph = copy.deepcopy(best_neighbor_graph)
        candidate_list.update({best_neighbor_graph: best_neighbor_score})
        results.append(get_score(best_neighbor_graph))

        if best_neighbor_score not in tabu_list.values():
            tabu_desc = get_description_of_tabu_list(tabu_list)
            if best_neighbor_graph.prepare_graph_description() not in tabu_desc:
                if evaluation_of_the_result(best_result, best_neighbor_score) != best_result:
                    best_result = best_neighbor_score
                    best_graph = copy.deepcopy(best_neighbor_graph)
                    if evaluation_of_the_result(best_result, final_result) != final_result:
                        final_result = best_result
                        final_graph = copy.deepcopy(best_graph)
                        final_graph.update_vertices_colors()
                else:
                    try_counter = try_counter + 1
                    if try_counter == 3:
                        try_counter = 0
                        best_result = list(candidate_list.values())[-3]
                        best_graph = list(candidate_list.keys())[-3]
                if len(tabu_list) == 10:
                    for k in tabu_list.keys():
                        k_to_remove = k
                        tabu_list.pop(k_to_remove)
                        break
                tabu_list.update({best_graph: best_result})

        iteration = it
        if best_result[1] == 0:
            break

    final_graph.update_vertices_colors()
    final_graph.send_parameters_to_file(file_name="graph_representation/best_graph_tabu_search_step_back.txt")
    print(f"Tabu list: {tabu_list}")
    print(f"Best result: {final_result}")
    print(f"Best score: {get_score(final_graph)}")
    print(f"Number of iteration: {iteration + 1}")
    make_figure_for_results(results=results, plot_name="tabu_search_with_step_back")


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
