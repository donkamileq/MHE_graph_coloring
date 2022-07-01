import copy
import random
import math

from graph.evaluation_functions import goal_function, evaluation_of_the_result, get_score, make_figure_for_results


def simulated_annealing(start_graph, number_of_iteration):
    best_graph = copy.deepcopy(start_graph)
    best_result = goal_function(start_graph)
    final_graph = copy.deepcopy(start_graph)
    final_result = goal_function(start_graph)
    iteration_counter = 1
    temperature = lambda x: (number_of_iteration/2)/x
    results = []

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
        results.append(get_score(best_graph))
        if evaluation_of_the_result(best_result, final_result) != final_result:
            final_result = best_result
            final_graph = copy.deepcopy(best_graph)
            final_graph.update_vertices_colors()
        iteration_counter += 1

        if final_result[1] == 0:
            break

    final_graph.update_vertices_colors()
    final_graph.send_parameters_to_file(file_name="graph_representation/best_graph_simulated_annealing.txt")
    print(f"Best result: {final_result}")
    print(f"Best score: {get_score(final_graph)}")
    print(f"Number of iteration: {iteration_counter - 1}")
    make_figure_for_results(results=results, plot_name="simulated_annealing")
