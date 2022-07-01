import argparse
import time

from algorithms.genetic_algorithm import genetic_algorithm
from algorithms.hill_climbing import hill_climbing_random, hill_climbing_best
from algorithms.simulated_annealing import simulated_annealing
from algorithms.tabu_search import tabu_search, tabu_search_with_step_back
from graph.evaluation_functions import goal_function, make_figure_for_time
from graph.random_graph_generator import RandomGraph


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-vn", "--vertex_number", default=5, help="Vertex number in graph")
    parser.add_argument("-in", "--iteration_number", default=50, help="Iteration number")
    parser.add_argument("-pop", "--population_size", default=100, help="Population size")
    parser.add_argument("-al", "--algorithm", default=None, help="Name of Algorithm to run | If you want to run "
                                                                 "all algorithms to compare - pass \"all\"")
    args = parser.parse_args()

    graph = RandomGraph(int(args.vertex_number))
    graph.send_parameters_to_file(file_name="graph_representation/start_graph.txt")
    time_results = {}

    print(f"\nStart result: {goal_function(graph)}\n")

    if args.algorithm == 'hill_climbing_random':
        print(f"-----Hill Climbing Random-----")
        start = time.time()
        hill_climbing_random(graph, int(args.iteration_number))
        end = time.time()
        time_results.update({'hill_climbing_random': end-start})
        print(f"Execution time: {end-start}s")
        print("\n")

    elif args.algorithm == 'hill_climbing_best':
        print(f"-----Hill Climbing Best-----")
        start = time.time()
        hill_climbing_best(graph, int(args.iteration_number))
        end = time.time()
        time_results.update({'hill_climbing_best': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

    elif args.algorithm == 'tabu_search':
        print(f"-----Tabu Search-----")
        start = time.time()
        tabu_search(graph, int(args.iteration_number))
        end = time.time()
        time_results.update({'tabu_search': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

    elif args.algorithm == 'tabu_search_with_step_back':
        print(f"-----Tabu Search With Step Back-----")
        start = time.time()
        tabu_search_with_step_back(graph, int(args.iteration_number))
        end = time.time()
        time_results.update({'tabu_search_with_step_back': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

    elif args.algorithm == 'simulated_annealing':
        print(f"-----Simulated Annealing-----")
        start = time.time()
        simulated_annealing(graph, int(args.iteration_number))
        end = time.time()
        time_results.update({'simulated_annealing': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

    elif args.algorithm == 'genetic_algorithm':
        print(f"-----Genetic Algorithm-----\nParameters:\n-Crossover Single\n-Mutation Random\n")
        start = time.time()
        genetic_algorithm(graph, int(args.population_size), crossover_single=True, random_mutation=True)
        end = time.time()
        time_results.update({'genetic_algorithm_single_random': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Genetic Algorithm-----\nParameters:\n-Crossover Double\n-Mutation Random\n")
        start = time.time()
        genetic_algorithm(graph, int(args.population_size), crossover_double=True, random_mutation=True)
        end = time.time()
        time_results.update({'genetic_algorithm_double_random': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Genetic Algorithm-----\nParameters:\n-Crossover Single\n-Mutation Good\n")
        start = time.time()
        genetic_algorithm(graph, int(args.population_size), crossover_single=True, good_mutation=True)
        end = time.time()
        time_results.update({'genetic_algorithm_single_good': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Genetic Algorithm-----\nParameters:\n-Crossover Double\n-Mutation Good\n")
        start = time.time()
        genetic_algorithm(graph, int(args.population_size), crossover_double=True, good_mutation=True)
        end = time.time()
        time_results.update({'genetic_algorithm_double_good': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")
    elif args.algorithm == 'all':
        print(f"-----Hill Climbing Random-----")
        start = time.time()
        hill_climbing_random(graph, int(args.iteration_number))
        end = time.time()
        time_results.update({'hill_climbing_random': end-start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Hill Climbing Best-----")
        start = time.time()
        hill_climbing_best(graph, int(args.iteration_number))
        end = time.time()
        time_results.update({'hill_climbing_best': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Tabu Search-----")
        start = time.time()
        tabu_search(graph, int(args.iteration_number))
        end = time.time()
        time_results.update({'tabu_search': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Tabu Search With Step Back-----")
        start = time.time()
        tabu_search_with_step_back(graph, int(args.iteration_number))
        end = time.time()
        time_results.update({'tabu_search_with_step_back': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Simulated Annealing-----")
        start = time.time()
        simulated_annealing(graph, int(args.iteration_number))
        end = time.time()
        time_results.update({'simulated_annealing': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Genetic Algorithm-----\nParameters:\n-Crossover Single\n-Mutation Random\n")
        start = time.time()
        genetic_algorithm(graph, int(args.population_size), crossover_single=True, random_mutation=True)
        end = time.time()
        time_results.update({'genetic_algorithm_single_random': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Genetic Algorithm-----\nParameters:\n-Crossover Double\n-Mutation Random\n")
        start = time.time()
        genetic_algorithm(graph, int(args.population_size), crossover_double=True, random_mutation=True)
        end = time.time()
        time_results.update({'genetic_algorithm_double_random': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Genetic Algorithm-----\nParameters:\n-Crossover Single\n-Mutation Good\n")
        start = time.time()
        genetic_algorithm(graph, int(args.population_size), crossover_single=True, good_mutation=True)
        end = time.time()
        time_results.update({'genetic_algorithm_single_good': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        print(f"-----Genetic Algorithm-----\nParameters:\n-Crossover Double\n-Mutation Good\n")
        start = time.time()
        genetic_algorithm(graph, int(args.population_size), crossover_double=True, good_mutation=True)
        end = time.time()
        time_results.update({'genetic_algorithm_double_good': end - start})
        print(f"Execution time: {end - start}s")
        print("\n")

        make_figure_for_time(time_results, "Time results")




