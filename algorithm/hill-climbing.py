import random
import time
import numpy as np
import matplotlib.pyplot as plt
from models.cube import Cube  

# Function untuk mengambil neighbor dari current state
def get_neighbors(cube):
    neighbors = []
    n = cube.n  # Ukuran cube
    # Generate neighbors dengan swapping dua elemen
    for i in range(n):
        for j in range(n):
            for k in range(n):
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
            if score < next_score:  # Cek current dan neighbor
                next_state = neighbor
                next_score = score

        if next_state is None:  # Berhenti jika tidak ada neighbor yang lebih baik
            break
        else:
            current_state = next_state
            current_score = next_score
        
        iterations += 1

    return current_state, current_score, iterations, scores

# Sideways Move Algorithm
def sideways_move(cube, max_iterations=1000):
    current_state = cube
    current_score = current_state.objective_function()
    iterations = 0
    scores = []
    no_improvement_count = 0  # Counter untuk iterations yang tidak ada improvement

    while iterations < max_iterations:  
        scores.append(current_score)
        neighbors = get_neighbors(current_state)
        next_state = None
        next_score = current_score
        found_better = False

        for neighbor in neighbors:
            score = neighbor.objective_function()
            if score < next_score:  # Neighbor lebih baik dari current
                next_state = neighbor
                next_score = score
                found_better = True
                break  # Exit loop ketika neighbor lebih baik

        if not found_better:  # Jika tidak ada neighbor yang lebih baik
            for neighbor in neighbors:
                score = neighbor.objective_function()
                if score == next_score:  # Ketika neighbor sama dengan current
                    next_state = neighbor
                    break

        if next_state is None:
            print("No valid moves found, stopping.")
            break  # Ketika neighbor tidak lebih baik dari current
        else:
            current_state = next_state
            current_score = next_score
            iterations += 1  

            if found_better:
                no_improvement_count = 0  # Reset jika iterasinya improve
            else:
                no_improvement_count += 1  # Counter bertambah jika iterasi tidak improve

            # Check jika terlalu banyak iterasi tanpa improvement
            if no_improvement_count > 20:  # Jika tidak ada improvement selama 20 iterasi
                print("No improvement for 20 iterations, stopping.")
                break

    return current_state, current_score, iterations, scores

def random_restart_hill_climbing(cube, max_restarts, max_iterations):
    current_state = cube
    current_score = current_state.objective_function()

    best_state = None
    best_score = float('inf')
    scores = []

    # Lakukan restart beberapa kali hingga mencapai max_restarts
    for restart in range(max_restarts):
        print(f"\nRestart {restart + 1}/{max_restarts}")
        
        # Menghasilkan instance cube baru dari cube awal untuk setiap restart
        cube_instance = Cube()
        current_state, current_score, _, current_scores = steepest_ascent_hill_climbing(cube_instance, max_iterations)

        scores.extend(current_scores)

        # Cek jika neighbor lebih baik dari current
        if current_score < best_score:
            best_state = current_state
            best_score = current_score

        print(f"End of Restart {restart + 1}: Best score = {best_score}")
        
        # Berhenti jika ditemukan solusi optimal (skor 0)
        if current_score == 0:
            print("Optimal solution found!")
            break

    return best_state, best_score, len(scores), scores

def run_experiment(algorithm_choice):
    results = {
        'algorithm': algorithm_choice,
        'initial_state': [],
        'final_state': [],
        'initial_value': [],
        'final_value': [],
        'iterations': [],
        'duration': []
    }

    # Generate initial cube instance
    cube_instance = Cube()
    results['initial_state'] = cube_instance.cube.copy()  # Menyimpan kondisi awal kubus
    results['initial_value'] = cube_instance.objective_function()

    if algorithm_choice == "random_restart":
        max_restarts = int(input("Enter maximum restarts: "))
        max_iterations = int(input("Enter maximum iterations per restart: "))
        start_time = time.time()
        final_state, final_value, iterations, scores = random_restart_hill_climbing(cube_instance, max_restarts, max_iterations)
    else:
        start_time = time.time()

        if algorithm_choice == "steepest":
            final_state, final_value, iterations, scores = steepest_ascent_hill_climbing(cube_instance, max_iterations=100)
        elif algorithm_choice == "sideways":
            final_state, final_value, iterations, scores = sideways_move(cube_instance, max_iterations=100)
        else:
            print("Invalid algorithm choice!")
            return

    end_time = time.time()

    results['final_state'] = final_state.cube
    results['final_value'] = final_value
    results['iterations'] = iterations
    results['duration'] = end_time - start_time

    # Plotting the objective function value against iterations
    plt.plot(scores, label=algorithm_choice.capitalize() + " Algorithm")
    plt.title("Objective Function vs Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Objective Function Value")
    plt.legend()
    plt.show()

    # Display hasil experiment 
    print(f"Algorithm: {results['algorithm']}")
    print(f"Initial State:\n{results['initial_state']}")
    print(f"Initial Objective Value: {results['initial_value']}")
    print(f"Final State:\n{results['final_state']}")
    print(f"Final Objective Value: {results['final_value']}")
    print(f"Iterations: {results['iterations']}")
    print(f"Duration: {results['duration']:.4f} seconds")
    print("-" * 40)

# Main function untuk memilih algoritma
def main():
    algorithm_choice = input("Choose algorithm (steepest/sideways/random_restart): ").strip().lower()
    run_experiment(algorithm_choice)

# Run main function
if __name__ == "__main__":
    main()