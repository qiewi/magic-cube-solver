# Import library yang dibutuhkan
import random, time
import numpy as np
import Visual

# Import model Cube dari models.cube
from models.cube import Cube  

class HillClimbing:
    # Konstruktor 'pass' karena terdapat banyak variasi algoritma hill climbing
    def __init__(self):
        pass
        
    # Fungsi untuk mendapatkan neighbor terbaik dari suatu kubus
    def get_neighbor(self, cube, current_score):

        # Inisialisasi variabel untuk menyimpan skor terendah dan swap terbaik
        lowest_score = current_score
        best_swap = None 
        n = cube.n  
        
        # Looping untuk semua kemungkinan swap pada setiap state
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for x in range(i, n):  
                        for y in range(j if x == i else 0, n):
                            for z in range(k + 1 if x == i and y == j else 0, n):
                                # Melakukan swap pada kubus
                                cube.cube[i, j, k], cube.cube[x, y, z] = cube.cube[x, y, z], cube.cube[i, j, k]

                                # Menghitung skor dari kubus yang telah di-swap
                                new_score = cube.objective_function()

                                # Jika skor baru lebih rendah dari skor terendah, maka menyimpan swap tersebut
                                if new_score < lowest_score:
                                    lowest_score = new_score
                                    best_swap = (i, j, k, x, y, z)  
                                
                                # Mengembalikan kubus ke keadaan semula
                                cube.cube[i, j, k], cube.cube[x, y, z] = cube.cube[x, y, z], cube.cube[i, j, k]
        
        # Jika ditemukan swap terbaik, maka dilakukan swap tersebut pada kubus
        if best_swap:
            i, j, k, x, y, z = best_swap
            cube.cube[i, j, k], cube.cube[x, y, z] = cube.cube[x, y, z], cube.cube[i, j, k]

        # Mengembalikan kubus yang telah di-swap
        return cube

    # Fungsi untuk mendapatkan neighbor terbaik dari suatu kubus
    def get_all_neighbors(self, cube):
        # Inisialisasi variabel 
        n = cube.n  
        neighbors = []
        
        # Looping untuk semua kemungkinan swap pada setiap state
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for x in range(i, n):  
                        for y in range(j if x == i else 0, n):
                            for z in range(k + 1 if x == i and y == j else 0, n):
                                # Melakukan swap pada kubus
                                cube.cube[i, j, k], cube.cube[x, y, z] = cube.cube[x, y, z], cube.cube[i, j, k]

                                # Membuat kubus baru
                                new_cube = Cube()
                                new_cube.cube = np.copy(cube.cube)

                                # Menambahkan kubus yang telah di-swap ke dalam list neighbors
                                neighbors.append(new_cube)
                                
                                # Mengembalikan kubus ke keadaan semula
                                cube.cube[i, j, k], cube.cube[x, y, z] = cube.cube[x, y, z], cube.cube[i, j, k]

        # Mengembalikan semua neighbors
        return neighbors

    # Fungsi untuk algoritma steepest ascent
    def steepest_ascent(self, cube, max_iterations):
        # Inisialisasi variabel untuk menyimpan kubus saat ini dan objective function saat ini
        current_state = cube
        current_score = current_state.objective_function()
        iterations = 0
        scores = []
        display_text = []

        # Looping hingga mencapai maksimum iterasi
        while iterations < max_iterations:

            # Menyimpan skor pada iterasi saat ini
            scores.append(current_score)

            # Mendapatkan neighbor terbaik dari kubus saat ini
            neighbor = self.get_neighbor(current_state, current_score)
            
            # Jika tidak ditemukan neighbor terbaik, maka berhenti
            if neighbor is None:
                break  # Break loop ketika tidak ada neighbor yang lebih baik
            # Jika ditemukan neighbor terbaik, maka kubus saat ini diganti dengan neighbor terbaik
            else:
                current_state = neighbor
                current_score = current_state.objective_function()
            
            display_text = Visual.display_iteration(display_text, iterations, current_score, "stepest_ascent")

            iterations += 1

        # Mengembalikan kubus terbaik, nilai objektif terbaik, jumlah iterasi, dan semua objektif function
        return current_state, current_score, len(scores), scores

    # Fungsi untuk algoritma sideways move
    def sideways_move(self, cube, max_sideways):
        # Inisialisasi variabel untuk menyimpan kubus saat ini dan objective function saat ini
        current_state = cube
        current_score = current_state.objective_function()
        scores = []  
        display_text = []
        iterations = 0
        sideways_count = 0  

        # Looping hingga ditemukan solusi optimal
        while True:

            # Menyimpan skor pada iterasi saat ini
            scores.append(current_score)

            # Mendapatkan neighbor terbaik dari kubus saat ini
            neighbor = self.get_neighbor(current_state, current_score)

            # Mengambil neighbor dan menghitung skor dari neighbor terbaik
            next_state = neighbor
            next_score = next_state.objective_function()

            # Jika skor dari neighbor lebih baik dari skor saat ini, maka kubus saat ini diganti dengan neighbor terbaik
            if next_score < current_score:
                current_state = next_state
                current_score = next_score
                sideways_count = 0  
            # Jika skor dari neighbor sama dengan skor saat ini, maka kubus saat ini diganti dengan neighbor terbaik
            else:
                # Jika skor dari neighbor sama dengan skor saat ini, maka kubus saat ini diganti dengan neighbor terbaik
                if next_score == current_score:
                    current_state = next_state
                    current_score = next_score
                    sideways_count += 1  # Menambahkan jumlah sideways
                # Jika skor dari neighbor lebih buruk dari skor saat ini, maka berhenti
                else:
                    break
            
            display_text = Visual.display_iteration(display_text, iterations, current_score, "sideways_move")

            iterations += 1

            # Berhenti jika jumlah sideways lebih dari maksimum yang ditentukan
            if sideways_count >= max_sideways:
                print("Reached max sideways moves, stopping.")
                break
        
        # Mengembalikan kubus terbaik, nilai objektif terbaik, jumlah iterasi, dan semua objektif function
        return current_state, current_score, len(scores), scores

    # Fungsi untuk algoritma random restart
    def random_restart(self, cube, max_restarts, max_iterations):
        # Inisialisasi variabel untuk menyimpan kubus terbaik, nilai objektif terbaik, dan skor terbaik
        best_state = cube
        best_score = best_state.objective_function()
        scores = []  
        display_text = []

        # Looping untuk setiap restart
        for restart in range(max_restarts):
            
            
            # Inisialisasi kubus baru
            cube_instance = Cube()

            # Menjalankan algoritma steepest ascent
            current_state, current_score, _, current_scores = self.steepest_ascent(cube_instance, max_iterations)

            # Menyimpan skor dari iterasi saat ini
            scores.extend(current_scores)

            # Cek jika skor dari iterasi ini lebih baik dari best_score
            if current_score < best_score:
                best_state = current_state
                best_score = current_score

            display_text = Visual.display_iteration(display_text, restart, current_score, "random_restart", max_restarts)
            
            # Berhenti jika ditemukan solusi optimal (skor 0)
            if current_score == 0:
                print("Optimal solution found!")
                break

        # Mengembalikan hasil terbaik dan semua skor dari semua iterasi
        return best_state, best_score, len(scores), scores

    # Fungsi untuk algoritma stochastic
    def stochastic(self, cube, max_iterations):
        # Inisialisasi variabel untuk menyimpan kubus saat ini dan objective function saat ini
        current_state = cube
        current_score = current_state.objective_function()
        scores = []
        display_text = []

        # Looping hingga mencapai maksimum iterasi
        for iteration in range(max_iterations):

            # Menyimpan skor pada iterasi saat ini
            scores.append(current_score)

            # Mendapatkan neighbor terbaik dari kubus saat ini
            neighbors = self.get_all_neighbors(current_state)
            
            # Mengambil neighbor secara acak
            next_state = random.choice(neighbors)
            next_score = next_state.objective_function()

            # Jika skor dari neighbor lebih baik dari skor saat ini, maka kubus saat ini diganti dengan neighbor terbaik
            if next_score < current_score:
                current_state = next_state
                current_score = next_score
            # Jika skor dari neighbor sama dengan skor saat ini, maka kubus saat ini diganti dengan neighbor terbaik
            else:
                pass
            
            # Menampilkan skor dan iterasi saat ini
            display_text = Visual.display_iteration(display_text, iteration, current_score, "stochastic")

        # Mengembalikan kubus terbaik, nilai objektif terbaik, jumlah iterasi, dan semua objektif function
        return current_state, current_score, len(scores), scores
