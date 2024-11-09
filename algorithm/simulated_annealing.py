# Import library yang dibutuhkan
import numpy as np
import random, math, time
import Visual
import matplotlib.pyplot as plt

# Import model Cube dari models.cube
from models.cube import Cube

class SimulatedAnnealing():
    '''-------------------- Konstruktor Kelas --------------------'''
    def __init__(self):
        self.best_cube = None
        self.best_value = float('inf')
    '''-------------------- Konstruktor Kelas --------------------'''

    '''-------------------- Set State dan Objetive Value --------------------'''
    def set_state(self, cube, objective_value):
        cubeInstance = Cube()
        cubeInstance.cube = cube
        self.best_cube = cubeInstance
        self.best_value = objective_value
    '''-------------------- Set State dan Objetive Value --------------------'''

    '''-------------------- Generate Neighbor --------------------'''
    def generate_neighbor(self, current_state, ):
        # Melakukan copy pada current state
        neighbor_state = np.copy(current_state)

        # Melakukan swap pada dua angka secara acak
        x1, y1, z1 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
        x2, y2, z2 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
        neighbor_state[x1, y1, z1], neighbor_state[x2, y2, z2] = neighbor_state[x2, y2, z2], neighbor_state[x1, y1, z1]
        
        # Menghitung nilai objektif dari neighbor
        cube_instance = Cube()
        cube_instance.cube = neighbor_state
        neighbor_objective = cube_instance.objective_function()

        # Mengembalikan neighbor state dan objective
        return neighbor_state, neighbor_objective
    '''-------------------- Generate Neighbor --------------------'''
    

    '''-------------------- Fungsi Utama Simulated Annealing --------------------'''
    def simulated_annealing(self, cube_instance, initial_temperature, cooling_rate, min_temperature, max_iterations):
        # Inisialisasi variabel
        T = initial_temperature
        current_state = np.copy(cube_instance.cube)
        current_score = cube_instance.objective_function()
        display_text = []
        
        # Set state awal
        self.set_state(current_state, current_score)

        # Inisialisasi list untuk menyimpan nilai objective function dan acceptance probability
        objective_values = []
        acceptance_probabilities = []
        
        # Inisialisasi counter stuck dan unchanged iterations
        stuck_counter = 0
        unchanged_iterations = 0

        # Melakukan iterasi sebanyak iterasi maksimal yang di-input
        for iteration in range(max_iterations):
            # Jika temperatur kurang dari temperatur minimum, maka stop iterasi
            if T < min_temperature:
                break

            # Generate neighbor dengan memanggil fugnsi
            neighbor_state, neighbor_objective = self.generate_neighbor(current_state)

            # Menghitung ΔE
            delta_E = neighbor_objective - current_score

            # Menghitung acceptance probability
            acceptance_probability = math.exp(-delta_E / T) if delta_E > 0 else 1

            # Menerima neighbor jika acceptance probability lebih besar dari random uniform
            if random.uniform(0, 1) < acceptance_probability:
                current_state = neighbor_state
                current_score = neighbor_objective

                # Update best state jika nilai objective lebih kecil
                if current_score < self.best_value:
                    self.set_state(current_state, current_score)


            # Menyimpan nilai objective function
            objective_values.append(current_score)

            # Menyimpan acceptance probability jika ΔE > 0
            if delta_E > 0:  
                acceptance_probabilities.append(acceptance_probability)

            # Jika ΔE = 0, maka tambah unchanged iterations dan stuck counter
            if delta_E == 0:
                unchanged_iterations += 1
                stuck_counter += 1
        
            else:
                unchanged_iterations = 0

            # Mengurangi temperatur dengan cooling rate
            T *= cooling_rate

            # Menampilkan nilai objective function setiap iterasi
            display_text = Visual.display_iteration(display_text, iteration, current_score, "simulated_annealing")

        # Mengembalikan kubus terbaik, nilai objektif terbaik, nilai objektif, acceptance probability, dan stuck counter
        return self.best_cube, self.best_value, objective_values, acceptance_probabilities, stuck_counter
    '''-------------------- Fungsi Utama Simulated Annealing --------------------'''