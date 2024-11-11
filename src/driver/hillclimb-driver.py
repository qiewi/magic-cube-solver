# Import class HillClimbing dari algorithm.hill_climbing
from algorithm.hill_climbing import HillClimbing

# Import class Cube dari models.cube
from models.cube import Cube

# Import semua library yang dibutuhkan
import matplotlib.pyplot as plt
import time

# Driver untuk Hill Climbing
def run_experiment(algorithm_choice):
    # Inisialisasi result
    results = {
        'algorithm': algorithm_choice,
        'initial_state': [],
        'final_state': [],
        'initial_value': [],
        'final_value': [],
        'iterations': [],
        'duration': []
    }

    # Melakukan inisialisasi cube instance
    cube_instance = Cube()
    results['initial_state'] = cube_instance  
    results['initial_value'] = cube_instance.objective_function()

    # Inisialisasi search dengan algoritma Hill Climbing
    search = HillClimbing()

    # Start timer
    start_time = time.time()

    # Menjalankan algoritma random restart
    if algorithm_choice == "random_restart":
        max_restarts = int(input("Enter maximum restarts: "))
        max_iterations = int(input("Enter maximum iterations per restart: "))
        final_state, final_value, iterations, best_scores = search.random_restart(cube_instance, max_restarts, max_iterations)

    # Menjalankan algoritma steepest
    elif algorithm_choice == "steepest":
        max_iterations = int(input("Enter maximum iterations: "))
        final_state, final_value, iterations, best_scores = search.steepest_ascent(cube_instance, max_iterations)

    # Menjalankan algoritma sideways
    elif algorithm_choice == "sideways":
        max_sideways = int(input("Enter the maximum number of sideways iterations: "))
        final_state, final_value, iterations, best_scores = search.sideways_move(cube_instance, max_sideways)

    # Menjalankan algoritma stochastic
    elif algorithm_choice == "stochastic":
        max_iterations = int(input("Enter maximum iterations for stochastic: "))
        final_state, final_value, iterations, best_scores = search.stochastic(cube_instance, max_iterations)

    # Ketika user memilih algoritma selain algoritma yang ada
    else:
        print("Invalid algorithm choice!")
        return

    # Menyelesaikan timer
    end_time = time.time()

    # Menyimpan hasil driver
    results['final_state'] = final_state
    results['final_value'] = final_value
    results['iterations'] = iterations
    results['duration'] = end_time - start_time

    # Plot nilai objektif terhadap jumlah iterasi
    plt.plot(best_scores, label=algorithm_choice.capitalize() + " Algorithm")
    
    # Memberikan label pada plot
    plt.xlabel("Iterations")
    plt.ylabel("Objective Function Value")

    # Menampilkan grafik plot nilai objektif terhadap jumlah iterasi
    plt.title("Objective Function vs Iterations")
    plt.legend()
    plt.show()

    # Menampilkan semua hasil dari algoritma search yang dipilih
    print("-" * 40)
    print(f"Algorithm: {results['algorithm']}")

    # Menampilkan state awal
    results['initial_state'].display_layered()
    print(f"Initial Objective Value: {results['initial_value']}")
    
    # Menampilkan state akhir
    results['final_state'].display_layered()
    print(f"Final Objective Value: {results['final_value']}")

    # Menampilkan hasil algoritma
    print(f"Iterations: {results['iterations']}")
    print(f"Duration: {results['duration']:.4f} seconds")
    print("-" * 40)

# Memilih algoritma yang akan dijalankan
def main():
    algorithm_choice = input("Choose algorithm (steepest/sideways/random_restart/stochastic): ").strip().lower()
    run_experiment(algorithm_choice)

# Menjalankan driver
if __name__ == "__main__":
    main()