import copy
import math
import random

from evaluation_functions import get_score, goal_function
from random_graph_generator import RandomGraph, COLORS


def genetic_algorithm(num_of_vertices, population_size, crossover_single=False, crossover_double=False,
                      mutation_ten=False, mutation_half=False):
    start_graph = RandomGraph(numbers_of_vertex=num_of_vertices)
    start_graph.send_parameters_to_file(file_name="first_graph.txt")
    population = []
    crossover_probability = 0.9
    mutation_probability = 0.1
    num_of_generation = 0
    for _ in range(population_size):
        random_graph = copy.deepcopy(start_graph)
        random_graph.change_random_vertices_color()
        population.append(random_graph)

    population_fitness = calculate_population_fitness(population)
    print(f"First population fitness: {population_fitness}")
    while num_of_generation < 100:
        parents = []
        offspring = []

        for _ in range(population_size):
            parents.append(tournament_selection(population))

        for idx in range(0, len(parents), 2):
            if crossover_single:
                child_1, child_2 = crossover_single_point(parents[idx], parents[idx+1], crossover_probability)
            elif crossover_double:
                child_1, child_2 = crossover_single_point(parents[idx], parents[idx+1], crossover_probability)
            offspring.append(child_1)
            offspring.append(child_2)

        for child in offspring:
            if mutation_ten:
                mutation_ten_percent(child, mutation_probability)
            elif mutation_half:
                mutation_half_individual(child, mutation_probability)

        population = offspring
        num_of_generation += 1

    population_fitness = calculate_population_fitness(population)
    print(f"Best result: {max(population_fitness)}")
    population[population_fitness.index(max(population_fitness))].send_parameters_to_file(file_name="best_graph.txt")
    print(f"Final population fitness: {population_fitness}")


def tournament_selection(population):
    individual_1 = random.choice(population)
    individual_2 = random.choice(population)
    while individual_1 == individual_2:
        individual_2 = random.choice(population)
    return individual_1 if goal_function(individual_1) > goal_function(individual_2) else individual_2


def mutation_ten_percent(graph: RandomGraph, mutation_probability):
    u = random.random()
    if u < mutation_probability:
        number_of_mutation = math.ceil(graph.numbers_of_vertex/10)
        vertices = list(graph.vertices.keys())
        for _ in range(number_of_mutation):
            random.choice(vertices).vertex_color = random.choice(COLORS)
        graph.update_vertices_colors()
    return graph


def mutation_half_individual(graph: RandomGraph, mutation_probability):
    u = random.random()
    if u < mutation_probability:
        number_of_mutation = math.ceil(graph.numbers_of_vertex/2)
        vertices = list(graph.vertices.keys())
        for _ in range(number_of_mutation):
            random.choice(vertices).vertex_color = random.choice(COLORS)
        graph.update_vertices_colors()
    return graph


def crossover_single_point(parent_1: RandomGraph, parent_2: RandomGraph, crossover_probability):
    u = random.random()
    if u < crossover_probability:
        child_1 = copy.deepcopy(parent_1)
        child_2 = copy.deepcopy(parent_1)
        crossover_pt = int(len(parent_1.vertices)/2)

        child_1_vertices = list(child_1.vertices.keys())
        child_2_vertices = list(child_2.vertices.keys())

        for idx in range(crossover_pt):
            child_1_vertices[idx].vertex_color = parent_1.vertex_colors[idx]
            child_2_vertices[idx].vertex_color = parent_2.vertex_colors[idx]

        for idx in range(crossover_pt, len(parent_1.vertices)):
            child_1_vertices[idx].vertex_color = parent_2.vertex_colors[idx]
            child_2_vertices[idx].vertex_color = parent_1.vertex_colors[idx]

        child_1.update_vertices_colors()
        child_2.update_vertices_colors()

        return child_1, child_2

    else:
        return parent_1, parent_2


def crossover_double_point(parent_1: RandomGraph, parent_2: RandomGraph, crossover_probability):
    u = random.random()
    if u < crossover_probability:
        child_1 = copy.deepcopy(parent_1)
        child_2 = copy.deepcopy(parent_1)
        crossover_pt = int(len(parent_1.vertices) / 3)

        child_1_vertices = list(child_1.vertices.keys())
        child_2_vertices = list(child_2.vertices.keys())

        for idx in range(crossover_pt):
            print(idx)
            child_1_vertices[idx].vertex_color = parent_1.vertex_colors[idx]
            child_2_vertices[idx].vertex_color = parent_2.vertex_colors[idx]

        for idx in range(crossover_pt, len(parent_1.vertices) - crossover_pt):
            print(idx)
            child_1_vertices[idx].vertex_color = parent_2.vertex_colors[idx]
            child_2_vertices[idx].vertex_color = parent_1.vertex_colors[idx]

        for idx in range(2*crossover_pt, len(parent_1.vertices)):
            print(idx)
            child_1_vertices[idx].vertex_color = parent_1.vertex_colors[idx]
            child_2_vertices[idx].vertex_color = parent_2.vertex_colors[idx]

        child_1.update_vertices_colors()
        child_2.update_vertices_colors()

        child_1.send_parameters_to_file("child_1")
        child_2.send_parameters_to_file("child_2")

        return child_1, child_2

    else:
        return parent_1, parent_2


def calculate_population_fitness(population):
    population_fitness = []
    for individual in population:
        population_fitness.append(get_score(individual))
    return population_fitness
