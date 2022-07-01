import copy

from graph.evaluation_functions import goal_function, evaluation_of_the_result, get_score, make_figure_for_results


def hill_climbing_random(start_graph, number_of_iteration):
    best_graph = copy.deepcopy(start_graph)
    random_graph = copy.deepcopy(start_graph)
    iteration = 0
    best_result = goal_function(start_graph)
    results = []

    for _ in range(number_of_iteration):
        random_graph.change_random_vertices_color()
        random_result = goal_function(random_graph)
        results.append(get_score(random_graph))

        if evaluation_of_the_result(best_result, random_result) != best_result:
            best_graph = copy.deepcopy(random_graph)
            best_graph.update_vertices_colors()
            best_result = random_result

        iteration = _
        if best_result[1] == 0:
            break

    best_graph.update_vertices_colors()
    best_result = goal_function(best_graph)
    best_graph.send_parameters_to_file(file_name="graph_representation/best_graph_hill_random.txt")
    print(f"Best result: {best_result}")
    print(f"Best score: {get_score(best_graph)}")
    print(f"Number of iteration: {iteration + 1}")
    make_figure_for_results(results=results, plot_name="hill_climbing_random")


def hill_climbing_best(start_graph, number_of_iteration):
    best_graph = copy.deepcopy(start_graph)
    random_graph = copy.deepcopy(start_graph)
    iteration = 0
    results = []

    best_result = goal_function(start_graph)

    for _ in range(number_of_iteration):
        random_graph.change_random_bad_vertices_color()
        random_result = goal_function(random_graph)
        results.append(get_score(random_graph))

        if evaluation_of_the_result(best_result, random_result):
            best_graph = copy.deepcopy(random_graph)
            best_graph.update_vertices_colors()
            best_result = random_result

        iteration = _
        if best_result[1] == 0:
            break

    best_graph.update_vertices_colors()
    best_result = goal_function(best_graph)
    best_graph.send_parameters_to_file(file_name="graph_representation/best_graph_hill_best.txt")
    print(f"Best result: {best_result}")
    print(f"Best score: {get_score(best_graph)}")
    print(f"Number of iteration: {iteration + 1}")
    make_figure_for_results(results=results, plot_name="hill_climbing_best")







