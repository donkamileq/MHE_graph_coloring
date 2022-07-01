import matplotlib.pyplot as plt

from graph.random_graph_generator import RandomGraph


def get_number_of_colors(graph: RandomGraph):
    colors = []
    for vert in graph.vertices:
        if vert.vertex_color not in colors:
            colors.append(vert.vertex_color)
    return len(colors)


def get_bad_edges(graph: RandomGraph):
    number_of_bad_edges = 0
    for vert in graph.vertices:
        for x in vert.connected_vertices:
            if vert.vertex_color == x.vertex_color:
                number_of_bad_edges = number_of_bad_edges + 1
    return number_of_bad_edges


def goal_function(graph: RandomGraph):
    number_of_colors = get_number_of_colors(graph)
    number_of_bad_edges = get_bad_edges(graph)
    return number_of_colors, number_of_bad_edges


def get_score(graph: RandomGraph):
    result = goal_function(graph)
    good_edges = graph.numbers_of_edges_ - result[1]
    score = ((good_edges/result[0])/graph.numbers_of_edges_)*100
    return round(score, 2)


def evaluation_of_the_result(problem, solution):
    if solution[0] < problem[0] and solution[1] < problem[1]:
        better_result = solution
    elif solution[1] < problem[1]:
        better_result = solution
    else:
        better_result = problem
    return better_result


def make_figure_for_results(results, plot_name):
    plt.plot(results)
    plt.title(plot_name)
    plt.ylabel("Scores")
    plt.xlabel("Number of result")
    plt.show()


def make_figure_for_time(results, plot_name):
    plt.bar(range(len(results)), list(results.values()), align='center')
    plt.xticks(range(len(results)), list(results.keys()))
    plt.title(plot_name)
    plt.show()

