# main.py

#This file is the main entry point for the project.
#Bu dosya, projenin ana giriş noktasını içerir.

from genetic_algorithm import initialize_population, fitness, selection, crossover, mutation
from n_queens_problem import visualize_board
from config import population_size, board_size, generations, num_parents, num_offsprings, mutation_rate

def genetic_algorithm_solver():
    #Solve the N Queen problem using a genetic algorithm.
    #Genetik algoritma kullanarak N Vezir problemini çözer.
    
    population = initialize_population(population_size, board_size)
    
    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        parents = selection(population, num_parents)
        offsprings = crossover(parents, num_offsprings)
        population = parents + offsprings
        population = [mutation(ind, mutation_rate) for ind in population]

    best_solution = max(population, key=fitness)
    visualize_board(best_solution)

if __name__ == "__main__":
    genetic_algorithm_solver()
