# genetic_algorithm.py

#This file contains functions related to the genetic alorithm.

#Bu dosya genetik algoritma ile ilgili fonksiyonları içerir.
import random

def initialize_population(population_size, board_size):
    #Initialize the population with random individuals.
    #Popülasyonu rastgele bireylerle başlatır.
    population = []
    for _ in range(population_size):
        individual = random.sample(range(board_size), board_size)
        population.append(individual)
    return population

def fitness(individual):
    #Calculate the fitness score of an individual.
    #Bir bireyin uygunluk skorunu hesaplar.
    fitness_score = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                fitness_score += 1
    return fitness_score

def selection(population, num_parents):
    #Perform selection of parents from the population.
    #Popülasyondan ebeveyn seçimini gerçekleştirir.

    # Turnuva seçimi veya başka bir seçim yöntemi uygulayabilirsiniz
    parents = []
    for _ in range(num_parents):
        selected = random.choice(population)
        parents.append(selected)
    return parents

def crossover(parents, num_offsprings):
    # Perform crossover to create offspring from parents.
    #Çaprazlama yaparak ebeveynlerden yeni bireyler oluşturur.
    offsprings = []
    for i in range(0, num_offsprings, 2):
        parent1 = parents[i % len(parents)]
        parent2 = parents[(i + 1) % len(parents)]
        crossover_point = random.randint(1, len(parent1) - 1)
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
        offsprings.extend([offspring1, offspring2])
    return offsprings

def mutation(individual, mutation_rate):
    #Perform mutation on an individual.
    #Bir birey üzerinde mutasyon gerçekleştirir.
    mutated_individual = individual.copy()
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            mutated_individual[i] = random.randint(0, len(mutated_individual) - 1)
    return mutated_individual

# Diğer genetik algoritma fonksiyonları da eklenebilir (örneğin, genetik çeşitlilik artırma, elitizm, vb.).
