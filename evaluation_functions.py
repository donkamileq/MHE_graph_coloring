from random_graph_generator import RandomGraph


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
    # print(f"Number of colors used: {number_of_colors}")
    # print(f"Number of incorrectly painted vertices: {number_of_bad_edges}")
    return number_of_colors, number_of_bad_edges


def evaluation_of_the_result(problem, solution):
    if solution[0] < problem[0] and solution[1] < problem[1]:
        better_result = solution
    elif solution[1] < problem[1]:
        better_result = solution
    else:
        better_result = problem
    return better_result


# TODO: Temp function to see graph
def check_graph(graph: RandomGraph):
    print("\nGRAPH\n")
    for x in graph.vertices:
        print(f"Vertex: {x} | Color: {x.vertex_color}\nConnected vertices:")
        for y in x.connected_vertices:
            print(f"{y} | {y.vertex_color}")
        print("\n------")
