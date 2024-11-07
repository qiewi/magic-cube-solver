# Import library yang dibutuhkan
import numpy as np
import random

# Import class Cube dari models.cube
from models.cube import Cube

class GeneticAlgorithm:
    # Konstruktor kelas algoritma genetik
    def __init__(self):
        self.best_cube = None
        self.best_value = float('inf')
        
    # Inisialisasi populasi
    def populate(self, population_size):
        population = [Cube() for _ in range(population_size)]
        return population

    # Proses seleksi
    def selection(self, population):
        # Menghitung nilai objektif untuk setiap kubus dalam populasi
        fitness_scores = [cube.objective_function() for cube in population]

        # Menghitung probabilitas seleksi secara kumulatif
        total_fitness = sum(fitness_scores)
        selection_probs = [(total_fitness - score) / total_fitness for score in fitness_scores]
        cumulative_probs = np.cumsum(selection_probs) / np.sum(selection_probs) * 100

        # Memilih parents berdasarkan probabilitas kumulatif
        parents = []
        for cube in range(len(population)):
            random_percentage = random.uniform(0, 100)
            for i, prob in enumerate(cumulative_probs):
                if random_percentage <= prob:
                    parents.append(population[i])
                    break
        
        # Mengembalikan parents yang telah dipilih
        return parents

    # Proses Crossover
    def crossover(self, parents):
        new_population = []

        # Proses crossover untuk setiap pasangan parents
        for i in range(0, len(parents), 2):  
            parent1 = parents[i]
            parent2 = parents[i + 1]

            # Menentukan titik crossover secara acak
            crossover_point = random.randint(1, 126)

            # Melakukan swap pada parents
            parent1.cube.flat[crossover_point:], parent2.cube.flat[crossover_point:] = parent2.cube.flat[crossover_point:], parent1.cube.flat[crossover_point:]

            # Menambahkan parents yang telah di-cross-over ke populasi baru
            new_population.append(parent1)
            new_population.append(parent2)
        
        # Mengembalikan populasi baru yang telah di-cross-over
        return new_population

    # Proses Mutasi
    def mutation(self, new_population):
        # Melakukan mutasi pada populasi baru pada indeks acak
        for i in range(len(new_population)):
            new_population[i].cube.flat[random.randint(0, 124)] = random.randint(0, 125)
        
        # Mengembalikan populasi baru yang telah dimutasi
        return new_population

    # Proses pencarian menggunakan algoritma genetik
    def genetic_search(self, population_size, max_iterations):    

        # Inisialisasi list untuk menyimpan nilai objektif terbaik dan rata-rata
        min_scores = []
        avg_scores = []

        for i in range(max_iterations):

            # Inisialisasi populasi
            population = self.populate(population_size)

            # Proses Seleksi
            parents = self.selection(population)
            
            # Proses Crossover
            crossover_result = self.crossover(parents)

            # Proses Mutasi
            new_population = self.mutation(crossover_result)

            # Menghitung nilai objektif untuk setiap kubus dalam populasi baru
            scores = [cube.objective_function() for cube in new_population]

            # Menyimpan nilai objektif terbaik dan rata-rata
            min_scores.append(min(scores))
            avg_scores.append(sum(scores) / len(scores))

            # Memperbarui nilai objektif terbaik dan kubus terbaik
            if (min(scores) < self.best_value):
                self.best_value = min(scores)
                self.best_cube = population[scores.index(self.best_value)]

            # Menampilkan nilai objektif terbaik setiap iterasi
            print(f"iterations: {i + 1} - current score: {self.best_value}")

        # Mengembalikan kubus terbaik, nilai objektif terbaik, populasi, nilai objektif terendah, dan nilai objektif rata-rata
        return self.best_cube, self.best_value, population, min_scores, avg_scores

        
