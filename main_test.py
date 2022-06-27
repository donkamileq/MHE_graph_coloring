from algorithms.hill_climbing import hill_climbing_random, hill_climbing_best
from evaluation_functions import goal_function, check_graph
from random_graph_generator import RandomGraph

graph = RandomGraph(numbers_of_vertex=50)
graph.send_parameters_to_file(file_name="graph.txt")
# result = goal_function(graph)
# # print(f'Result: {result}\n')
# # for x in graph.vertices:
# #     print(f"Vertex: {x} | Color: {x.vertex_color}\nConnected vertices:")
# #     for y in x.connected_vertices:
# #         print(f"{y} | {y.vertex_color}")
# #     print("\n------")


hill_climbing_best(10, 10)
