# Import library yang dibutuhkan
from collections import Counter
from copy import deepcopy
import numpy as np
import random
import Visual

# Import class Cube dari models.cube
from models.cube import Cube

class GeneticAlgorithm:
    '''-------------------- Konstruktor Kelas --------------------'''
    def __init__(self):
        self.best_cube = Cube()
        self.best_value = float('inf')
        self.display_text = []
    '''-------------------- Konstruktor Kelas --------------------'''
    
    '''-------------------- Inisiasi Populasi Genetik --------------------'''
    # Inisialisasi populasi
    def populate(self, population_size):
        population = [Cube() for _ in range(population_size)]
        return population
    '''-------------------- Inisiasi Populasi Genetik --------------------'''

    '''-------------------- Selection Process --------------------'''
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
    '''-------------------- Selection Process --------------------'''

    '''-------------------- Cross-Over Process --------------------'''
    # Crossover function ensuring unique elements in parentren
    def crossover(self, parents):
        new_population = []

        # Proses crossover untuk setiap pasangan parents
        for i in range(0, len(parents), 2):  
            parent1 = parents[i]
            parent2 = parents[i + 1]

            # Menentukan titik crossover secara acak
            crossover_point = random.randint(0, 124)

            # Membuat dua kubus baru sebagai child
            child1 = Cube()
            child2 = Cube()

            # Melakukan crossover pada titik yang telah ditentukan
            child1.cube.flat[crossover_point:], child2.cube.flat[crossover_point:] = parent2.cube.flat[crossover_point:], parent1.cube.flat[crossover_point:]

            # Mengisi sisa elemen yang belum terisi pada child1 dan memastikan elemen yang diisi unik
            currentIndex = 0
            for j in range(crossover_point, 125):
                for k in range(currentIndex, 125):
                    if parent2.cube.flat[k] not in child1.cube.flat:
                        child1.cube.flat[j] = parent2.cube.flat[k]
                        currentIdx = k
                        break
            
            # Mengisi sisa elemen yang belum terisi pada child2 dan memastikan elemen yang diisi unik
            currentIndex = 0
            for j in range(crossover_point, 125):
                for k in range(currentIndex, 125):
                    if parent1.cube.flat[k] not in child2.cube.flat:
                        child2.cube.flat[j] = parent1.cube.flat[k]
                        currentIdx = k
                        break

            # Menambahkan parents yang telah di-cross-over ke populasi baru
            new_population.append(parent1)
            new_population.append(parent2)

        return new_population
    '''-------------------- Cross-Over Process --------------------'''

    '''-------------------- Mutation Process --------------------'''
    # Proses Mutasi
    def mutation(self, new_population):
        for individual in new_population:
            # Melakukan swap pada dua elemen secara acak
            idx1, idx2 = random.randint(0, 124), random.randint(0, 124)
            individual.cube.flat[idx1], individual.cube.flat[idx2] = individual.cube.flat[idx2], individual.cube.flat[idx1]

        return new_population
    '''-------------------- Mutation Process --------------------'''

    '''-------------------- Fungsi Utama Genetic Algorithm --------------------'''
    # Proses pencarian menggunakan algoritma genetik
    def genetic_search(self, population_size, max_iterations):    
        # Inisialisasi array skor
        min_scores = []
        avg_scores = []

        # Inisialisasi populasi
        population = self.populate(population_size)

        for iteration in range(max_iterations):
            # Proses seleksi
            parents = self.selection(population)
            
            # Proses crossover
            crossover_result = self.crossover(parents)

            # Proses mutasi
            population = self.mutation(crossover_result)

            # Menghitung nilai objektif untuk setiap kubus dalam populasi
            scores = [cube.objective_function() for cube in population]
            min_score = min(scores)
            max_score = max(scores)

            # Memperbarui skor terbaik dan cube terbaik
            if min_score < self.best_value:
                self.best_value = min_score
                self.best_cube = deepcopy(population[scores.index(self.best_value)])

            # Menyimpan skor minimum dan rata-rata
            min_scores.append(self.best_value)
            avg_scores.append(sum(scores) / len(scores))

            # Menampilkan informasi iterasi
            self.display_text = Visual.display_iteration(self.display_text, iteration, self.best_value, "genetic")

        # Mengembalikan kubus terbaik, nilai objektif terbaik, populasi, skor minimum, dan skor rata-rata
        return self.best_cube, self.best_value, population, min_scores, avg_scores
    '''-------------------- Fungsi Utama Genetic Algorithm --------------------'''
