
# main.py
from genetic_algorithm import initialize_population, fitness
from n_queens_problem import visualize_board

def genetic_algorithm_solver(population_size, board_size, generations):
    # Genetik algoritma çözümü
    population = initialize_population(population_size, board_size)
    
    for generation in range(generations):
        # Uygunluk skorlarına göre popülasyonu sırala
        population = sorted(population, key=lambda x: fitness(x), reverse=True)

        # Seçim, çaprazlama, mutasyon işlemleri uygula

    # En iyi çözümü al ve görselleştir
    best_solution = population[0]
    visualize_board(best_solution)

if __name__ == "__main__":
    # Proje ayarları
    population_size = 100
    board_size = 8
    generations = 1000

    genetic_algorithm_solver(population_size, board_size, generations)
