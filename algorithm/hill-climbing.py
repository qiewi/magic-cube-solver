import random
import time
import numpy as np
import matplotlib.pyplot as plt
from models.cube import Cube  # Ensure that 'cube.py' is in the 'models' folder

# Fungsi untuk mendapatkan tetangga dari state saat ini
def get_neighbors(cube):
    neighbors = []
    n = cube.n  # Dapatkan ukuran kubus
    # Logika untuk menghasilkan tetangga (misalnya dengan menukar dua elemen)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # Coba swap dengan elemen lainnya
                for dx in [-1, 1]:
                    if 0 <= i + dx < n:
                        new_cube = cube.cube.copy()
                        new_cube[i, j, k], new_cube[i + dx, j, k] = new_cube[i + dx, j, k], new_cube[i, j, k]
                        new_neighbor = Cube()
                        new_neighbor.cube = new_cube
                        neighbors.append(new_neighbor)
    return neighbors

# Steepest Ascent Hill-Climbing
def steepest_ascent_hill_climbing(cube, max_iterations):
    current_state = cube
    current_score = current_state.objective_function()
    iterations = 0
    scores = []

    while iterations < max_iterations:
        scores.append(current_score)
        neighbors = get_neighbors(current_state)
        next_state = None
        next_score = current_score

        for neighbor in neighbors:
            score = neighbor.objective_function()
            if score < next_score:  # Minimizing total difference
                next_state = neighbor
                next_score = score

        if next_state is None:
            break  # No better neighbor found
        else:
            current_state = next_state
            current_score = next_score
        
        iterations += 1

    return current_state, current_score, iterations, scores

# Fungsi untuk menjalankan eksperimen
def run_experiments():
    results = {
        'algorithm': 'Steepest Ascent Hill-Climbing',
        'initial_state': [],
        'final_state': [],
        'final_value': [],
        'iterations': [],
        'duration': []
    }

    cube_instance = Cube()  # Inisialisasi Cube

    start_time = time.time()
    final_state, final_value, iterations, scores = steepest_ascent_hill_climbing(cube_instance, max_iterations=100)
    end_time = time.time()

    results['initial_state'] = cube_instance.cube
    results['final_state'] = final_state.cube
    results['final_value'] = final_value
    results['iterations'] = iterations
    results['duration'] = end_time - start_time

    # Plot nilai objective function terhadap banyak iterasi
    plt.plot(scores, label='Steepest Ascent Hill-Climbing')

    plt.title("Objective Function vs Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Objective Function Value")
    plt.legend()
    plt.show()

    # Tampilkan hasil eksperimen
    print(f"Algorithm: {results['algorithm']}")
    print(f"Initial State:\n{results['initial_state']}")
    print(f"Final State:\n{results['final_state']}")
    print(f"Final Objective Value: {results['final_value']}")
    print(f"Iterations: {results['iterations']}")
    print(f"Duration: {results['duration']:.4f} seconds")
    print("-" * 40)

# Jalankan eksperimen
run_experiments()