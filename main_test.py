from algorithms.hill_climbing import hill_climbing_random
from evaluation_functions import goal_function
from random_graph_generator import RandomGraph

# graph = RandomGraph(numbers_of_vertex=5)
# graph.send_parameters_to_file()
# result = goal_function(graph)
# print(f'Result: {result}\n')
# for x in graph.vertices:
#     print(f"Vertex: {x} | Color: {x.vertex_color}\nConnected vertices:")
#     for y in x.connected_verticies:
#         print(f"{y} | {y.vertex_color}")
#     print("\n------")

hill_climbing_random(number_of_iteration=1, num_of_verticies=5)
