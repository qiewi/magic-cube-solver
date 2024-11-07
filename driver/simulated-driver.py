import numpy as np
import time
import matplotlib.pyplot as plt
from algorithm.simulated_annealing import SimulatedAnnealing
from models.cube import Cube

# Driver untuk Simulated Annealing
def simulatedAnnealingDriver(initial_temperature=1000, cooling_rate=0.99, min_temperature=0.1, max_iterations=10000):
    # Inisialisasi cube instance
    cube_instance = Cube()
    initial_state = cube_instance
    search = SimulatedAnnealing()

    # Memulai timer
    start_time = time.time()

    # Menjalankan Simulated Annealing
    best_state, best_objective, objective_values, acceptance_probabilities, stuck_counter = search.simulated_annealing(
        cube_instance,
        initial_temperature,
        cooling_rate,
        min_temperature,
        max_iterations
    )

    # Mengakhiri timer
    end_time = time.time()

    # Durasi pencarian
    duration = end_time - start_time

    # Plot nilai objektif terhadap jumlah iterasi
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(objective_values, label='Objective Function Value')

    # Memberikan label pada plot
    plt.xlabel('Iterations')
    plt.ylabel('Objective Function Value')

    # Menampilkan grafik plot nilai objektif terhadap jumlah iterasi
    plt.title('Objective Function Value vs Iteration')
    plt.legend()

    # Plot e^(ΔE/T) values over iterations
    plt.subplot(1, 2, 2)
    plt.plot(acceptance_probabilities, label='Acceptance Probability e^(ΔE/T)', color='orange')

    # Memberikan label pada plot
    plt.xlabel('Iterations (only for ΔE > 0)')
    plt.ylabel('Acceptance Probability')

    # Menampilkan grafik plot nilai probabilitas penerimaan terhadap jumlah iterasi
    plt.title('Acceptance Probability e^(ΔE/T) vs Iteration')
    plt.legend()

    # Menampilkan grafik
    plt.tight_layout()
    plt.show()

    # Menampilkan state awal
    print("Initial State:")
    initial_state.display_layered()

    # Menampilkan state akhir
    print("\nFinal State (Best State Found):")
    best_state.display_layered()

    # Menampilkan hasil algoritma
    print(f"\nFinal Objective Function Value: {best_objective}")
    print(f"Number of Iterations: {len(objective_values)}")
    print(f"Stuck Counter: {stuck_counter}")
    print(f"Duration of Search Process: {duration:.2f} seconds")

# Menjalankan driver
simulatedAnnealingDriver(initial_temperature=1000, cooling_rate=0.99, min_temperature=0.1, max_iterations=10000)