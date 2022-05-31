# Skrypt do tworzenia randomowego grafu
import argparse
import collections
import random


class RandomGraphException(Exception):
    pass


class RandomGraph:
    def __init__(self, numbers_of_vertex):
        self.numbers_of_vertex = numbers_of_vertex
        self.numbers_of_edges = self.get_number_of_edges(numbers_of_vertex)
        self.vertices = []
        for num in range(self.numbers_of_vertex):
            self.vertices.append(Vertex(num+1))

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
                return int((3*numbers_of_vertex)/2)
            elif numbers_of_vertex % 2 == 1:
                return int((3*numbers_of_vertex-1)/2)
        else:
            raise RandomGraphException(f'Unable to define number of edges, '
                                       f'number of vertices passed: {numbers_of_vertex}')

    def create_edge(self):
        vertex_with_edges = collections.defaultdict(list)
        for vertex in self.vertices:
            vertex_with_edges.setdefault(vertex, [])
        while self.numbers_of_edges > 0:
            chosen_main_vertex = random.choice(list(vertex_with_edges))
            values = vertex_with_edges[chosen_main_vertex]
            if len(values) < 3:
                vertex_to_join = random.choice(list(vertex_with_edges))
                while vertex_to_join is chosen_main_vertex:
                    vertex_to_join = random.choice(list(vertex_with_edges))
                if vertex_to_join not in vertex_with_edges[chosen_main_vertex] \
                        and chosen_main_vertex not in vertex_with_edges[vertex_to_join]:
                    if vertex_to_join.number_of_edges < 3 and chosen_main_vertex.number_of_edges < 3:
                        vertex_with_edges[chosen_main_vertex].append(vertex_to_join)
                        vertex_to_join.number_of_edges = vertex_to_join.number_of_edges + 1
                        chosen_main_vertex.number_of_edges = chosen_main_vertex.number_of_edges + 1
                        self.numbers_of_edges = self.numbers_of_edges - 1
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

    def send_parameters_to_file(self):
        raw_graph = self.prepare_graph_parameters()
        graph_data = ""
        for first_vertex, second_vertex in raw_graph:
            raw_graph_data = f"{first_vertex.replace('vertex_', '')} -- {second_vertex.replace('vertex_', '')}"
            graph_data = f"{graph_data}\n{raw_graph_data}".strip()
        with open('graph.txt', 'w') as file_with_edges:
            file_with_edges.write(graph_data)


class Vertex:
    def __init__(self, vertex_num):
        self.number_of_edges = 0
        self.vertex_num = vertex_num

    def __str__(self):
        return f"vertex_{self.vertex_num}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-vn", "--vertex_number", default=15, help="Vertex number in graph")
    args = parser.parse_args()
    graph = RandomGraph(int(args.vertex_number))
    graph.send_parameters_to_file()


