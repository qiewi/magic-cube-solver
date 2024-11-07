# Import library yang dibutuhkan
import time
import matplotlib.pyplot as plt

# Import cube model
from models.cube import Cube

# Import algoritma genetik
from algorithm.genetic_algorithm import GeneticAlgorithm  


# Driver untuk menjalankan algoritma genetik
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

    # Ketika user memilih algoritma genetik
    if algorithm_choice == "genetic":
        # Meminta input dari user
        population_size = int(input("Enter population size: "))
        max_iterations = int(input("Enter maximum iterations: "))

        # Inisialisasi search menggunakan algoritma genetik
        search = GeneticAlgorithm()

        # Memulai timer algoritma genetik
        start_time = time.time()
        
        # Inisialisasi list untuk menyimpan nilai objektif terbaik dan rata-rata
        min_scores = []
        avg_scores = []

        # Menjalankan algoritma genetik
        final_state, final_value, population, min_scores, avg_scores = search.genetic_search(population_size, max_iterations)

        # Mengakhiri timer
        end_time = time.time()

        # Menyimpan semua hasil
        results['final_state'] = final_state
        results['final_value'] = final_value
        results['iterations'] = max_iterations
        results['duration'] = end_time - start_time

        # Melakukan plot nilai objektif terbaik dan rata-rata terhadap jumlah iterasi
        plt.plot(min_scores, label="Max Objective Function")
        plt.plot(avg_scores, label="Average Objective Function")

        # Memberikan label pada plot
        plt.xlabel("Iterations")
        plt.ylabel("Objective Function Value")

        # Menampilkan grafik 
        plt.title("Objective Function vs Iterations")
        plt.legend()
        plt.show()
    
    # Ketika user memilih algoritma selain algoritma yang ada
    else:
        print("Invalid algorithm choice!")
        return

    # Menampilkan semua hasil dari algoritma genetik
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

# Driveru untuk menjalankan algoritma
def main():
    algorithm_choice = input("Choose algorithm (genetic): ").strip().lower()
    run_experiment(algorithm_choice)

# Menjalankan driver
if __name__ == "__main__":
    main()
