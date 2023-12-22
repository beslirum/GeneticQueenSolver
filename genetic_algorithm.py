
# genetic_algorithm.py
import random

def initialize_population(population_size, board_size):
    # Popülasyonu başlat
    population = []
    for _ in range(population_size):
        individual = random.sample(range(board_size), board_size)
        population.append(individual)
    return population

def fitness(individual):
    # Uygunluk fonksiyonu
    # Vezirler birbirini tehdit etmiyorsa uygunluk daha yüksek olmalı
    fitness_score = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                fitness_score += 1
    return fitness_score

# Diğer genetik algoritma fonksiyonları da eklenebilir (seçim, çaprazlama, mutasyon, vb.).
