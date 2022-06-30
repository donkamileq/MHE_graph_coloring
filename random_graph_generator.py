# Skrypt do tworzenia randomowego grafu
import argparse
import collections
import copy
import re
import random


class RandomGraphException(Exception):
    pass


COLORS = ["red", "blue", "green", "yellow"]


class RandomGraph:
    def __init__(self, numbers_of_vertex):
        self.numbers_of_vertex = numbers_of_vertex
        self.numbers_of_edges = self.get_number_of_edges(numbers_of_vertex)
        self.numbers_of_edges_ = copy.deepcopy(self.numbers_of_edges)
        self.vertices = []
        for num in range(self.numbers_of_vertex):
            self.vertices.append(Vertex(num))
        self.graph_parameters = self.prepare_graph_parameters()
        self.vertex_colors = [x.vertex_color for x in self.vertices]

    @staticmethod
    def get_number_of_edges(numbers_of_vertex):
        if numbers_of_vertex == 1:
            return 0
        elif numbers_of_vertex == 2:
            return 1
        elif numbers_of_vertex == 3:
            return 3
        elif numbers_of_vertex > 3:
            if numbers_of_vertex % 2 == 0:
                return int((3 * numbers_of_vertex) / 2)
            elif numbers_of_vertex % 2 == 1:
                return int((3 * numbers_of_vertex - 1) / 2)
        else:
            raise RandomGraphException(f'Unable to define number of edges, '
                                       f'number of vertices passed: {numbers_of_vertex}')

    def create_edge(self):
        vertex_with_edges = collections.defaultdict(list)
        for vertex in self.vertices:
            vertex_with_edges.setdefault(vertex, [])
        self.vertices = vertex_with_edges.copy()
        while self.numbers_of_edges > 0:
            chosen_main_vertex = random.choice(list(vertex_with_edges))
            values = vertex_with_edges[chosen_main_vertex]
            if len(values) < 3:
                vertex_to_join = random.choice(list(vertex_with_edges))
                while vertex_to_join == chosen_main_vertex:
                    vertex_to_join = random.choice(list(vertex_with_edges))
                if vertex_to_join not in vertex_with_edges[chosen_main_vertex] \
                        and chosen_main_vertex not in vertex_with_edges[vertex_to_join]:
                    if vertex_to_join.number_of_edges < 3 and chosen_main_vertex.number_of_edges < 3:
                        vertex_with_edges[chosen_main_vertex].append(vertex_to_join)
                        chosen_main_vertex.connected_vertices.append(vertex_to_join)
                        # TODO:  if we want to get all vertices in the connected_vertices
                        # vertex_to_join.connected_vertices.append(chosen_main_vertex)
                        vertex_to_join.number_of_edges = vertex_to_join.number_of_edges + 1
                        chosen_main_vertex.number_of_edges = chosen_main_vertex.number_of_edges + 1
                        self.numbers_of_edges = self.numbers_of_edges - 1
            else:
                vertex_with_edges.pop(chosen_main_vertex)
        return vertex_with_edges

    def prepare_graph_parameters(self):
        raw_graph_parameters = []
        complete_graph_parameters = []
        for vertex, edges in self.create_edge().items():
            if len(edges) > 0:
                for edge in edges:
                    raw_graph_parameters.append((vertex, edge))
        for vertices in raw_graph_parameters:
            pair_of_vertices = []
            for vertex in vertices:
                pair_of_vertices.append(vertex.__str__())
            complete_graph_parameters.append(pair_of_vertices)
        return complete_graph_parameters

    def prepare_graph_description(self):
        graph_description = collections.defaultdict()
        for vert in self.vertices:
            graph_description.setdefault(f"{vert} | {vert.vertex_color}", [])
        for vert in self.vertices:
            for conn_vert in vert.connected_vertices:
                graph_description[f"{vert} | {vert.vertex_color}"].append(f"{conn_vert} | {conn_vert.vertex_color}")
        return graph_description

    def send_parameters_to_file(self, file_name):
        graph_data = ""
        vertex_desc = ""
        for first_vertex, second_vertex in self.graph_parameters:
            raw_graph_data = f"{first_vertex.replace('vertex_', '')} -- {second_vertex.replace('vertex_', '')}"
            graph_data = f"{graph_data}\n{raw_graph_data}".strip()

        for vert in self.vertices:
            raw_vertex_desc = f"{vert.vertex_num}[color=\"{vert.vertex_color}\"]"
            vertex_desc = f"{vertex_desc}\n{raw_vertex_desc}".strip()

        with open(file_name, 'w') as file_with_edges:
            file_with_edges.write("graph G {\n")
            file_with_edges.write(vertex_desc)
            file_with_edges.write("\n")
            file_with_edges.write(graph_data)
            file_with_edges.write("\n}")

        # TODO: uncomment after tests | graph generator for cpp
        # graph_data = graph_data.replace(" -- ", ',').replace("\n", ',')
        # with open('graph_cpp_data.txt', 'w') as file_with_edges_for_cpp:
        #     file_with_edges_for_cpp.write(graph_data)

    def change_random_vertices_color(self):
        for vert in self.vertices:
            vert.vertex_color = random.choice(COLORS)
        self.update_vertices_colors()

    def update_vertices_colors(self):
        self.vertex_colors = [x.vertex_color for x in self.vertices]

    def change_random_bad_vertices_color(self):
        for main_vert in self.vertices:
            for connected_vert in main_vert.connected_vertices:
                if main_vert.vertex_color == connected_vert.vertex_color:
                    new_color = random.choice(COLORS)
                    while new_color == connected_vert.vertex_color and new_color == main_vert.vertex_color:
                        new_color = random.choice(COLORS)
                    main_vert.vertex_color = new_color
                    break


class Vertex:
    def __init__(self, vertex_num):
        self.number_of_edges = 0
        self.vertex_num = vertex_num
        self.vertex_color = random.choice(COLORS)
        self.connected_vertices = []

    def __str__(self):
        return f"vertex_{self.vertex_num}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-vn", "--vertex_number", default=5, help="Vertex number in graph")
    args = parser.parse_args()

    graph = RandomGraph(int(args.vertex_number))
    graph.send_parameters_to_file()
