# Import semua library yang dibutuhkan
import time
import matplotlib.pyplot as plt

# Import cube model
from models.cube import Cube

# Import semua algoritma search
from algorithm.hill_climbing import HillClimbing
from algorithm.genetic_algorithm import GeneticAlgorithm
from algorithm.simulated_annealing import SimulatedAnnealing

# Fungsi untuk menjalankan algoritma search
def run_algorithm(algorithm_choice):
    #Inisiasi result apa saja yang akan ditampilkan
    results = {

        # Pilihan algoritma
        'algorithm':
        {   "1": "Steepest Ascent",
            "2": "Sideways",
            "3": "Random Restart",
            "4": "Stochastic",
            "5": "Simulated Annealing",
            "6": "Genetic Algorithm"
        }[algorithm_choice],

        # Semua data untuk setiap algoritma
        'initial_state': [],
        'final_state': [],
        'initial_value': [],
        'final_value': [],
        'iterations': [],
        'duration': [],

        # Khusus Simulated Annealing
        'stuck': [], 
        # Khusus Genetic Algorithm
        'population_size': [],
    }

    # Generate cube awal
    cube_instance = Cube()
    
    # Simpan semua data awal
    results['initial_state'] = cube_instance  
    results['initial_value'] = cube_instance.objective_function()

    # Ketika user memilih algoritma genetic
    if algorithm_choice == "6":
        # Meminta input dari user
        population_size = int(input("Enter population size: "))
        max_iterations = int(input("Enter maximum iterations: "))
        
        # Inisialisasi search menggunakan algoritma genetic
        search = GeneticAlgorithm()

        # Memulai timer algoritma genetic
        start_time = time.time()
        
        # Inisialisasi list untuk menyimpan nilai objektif terbaik dan rata-rata
        min_scores = []
        avg_scores = []
        
        # Menjalankan algoritma genetic search
        final_state, final_value, population, min_scores, avg_scores = search.genetic_search(population_size, max_iterations)

        # Menyelesaikan timer
        end_time = time.time()
        
        # Menyimpan semua hasil
        results['final_state'] = final_state
        results['final_value'] = final_value
        results['iterations'] = max_iterations
        results['duration'] = end_time - start_time
        results['population_size'] = population_size

        # Menampilkan grafik plot nilai objektif terbaik dan rata-rata terhadap jumlah iteasi
        plt.title("Objective Function vs Iterations (Genetic Algorithm)")

        # Melakukan plot nilai objektif terbaik dan rata-rata
        plt.plot(min_scores, label="Max Objective Function")
        plt.plot(avg_scores, label="Average Objective Function")

        # Memberikan label pada plot
        plt.xlabel("Iterations")
        plt.ylabel("Objective Function Value")

        # Menampilkan grafik
        plt.legend()
        plt.show()

    # Ketika user memilih algoritma simulated annealing
    elif algorithm_choice == "5":
        # Meminta input dari user
        initial_temperature = float(input("Enter initial temperature: "))
        cooling_rate = float(input("Enter cooling rate (0 < cooling rate < 1): "))
        min_temperature = float(input("Enter minimum temperature: "))
        max_iterations = int(input("Enter maximum iterations: "))
        
        # Inisialisasi search menggunakan algoritma simulated annealing
        search = SimulatedAnnealing()

        # Memulai timer algoritma simulated annealing
        start_time = time.time()
        
        # Menjalankan algoritma simulated annealing
        final_state, final_value, scores, acceptance_probabilities, stuck_counter = search.simulated_annealing(
            cube_instance,
            initial_temperature,
            cooling_rate,
            min_temperature,
            max_iterations
        )
        
        # Menyelesaikan timer
        end_time = time.time()

        # Menyimpan semua hasil
        results['final_state'] = final_state
        results['final_value'] = final_value
        results['iterations'] = len(scores)
        results['duration'] = end_time - start_time
        results['stuck'] = stuck_counter

        # Membuat plot nilai objektif terhadap jumlah iterasi
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.plot(scores, label='Objective Function Value')

        # Memberikan label pada plot
        plt.xlabel('Iterations')
        plt.ylabel('Objective Function Value')
        
        # Menampilkan grafik plot nilai objektif terhadap jumlah iterasi
        plt.title('Objective Function Value vs Iteration (Simulated Annealing)')
        plt.legend()

        # Membuat plot nilai probabilitas penerimaan terhadap jumlah iterasi
        plt.subplot(1, 2, 2)
        plt.plot(acceptance_probabilities, label='Acceptance Probability e^(ΔE/T)', color='orange')

        # Memberikan label pada plot
        plt.xlabel('Iterations (only for ΔE > 0)')
        plt.ylabel('Acceptance Probability')
        
        # Menaampilkan grafik plot nilai probabilitas penerimaan terhadap jumlah iterasi
        plt.title('Acceptance Probability e^(ΔE/T) vs Iteration')
        plt.legend()

        # Menampilkan grafik
        plt.tight_layout()
        plt.show()

    # Ketika user memilih algoritma hill climb atau selain angka 1-6
    else:
        # Inisialisasi search menggunakan algoritma hill climb
        search = HillClimbing()

        # Ketika user memilih algoritma stochastic
        if algorithm_choice == "4":
            # Meminta input dari user
            max_iterations = int(input("Enter maximum iterations: "))

            # Memulai timer algoritma stochastic
            start_time = time.time()

            # Menjalankan algoritma stochastic search
            final_state, final_value, iterations, best_scores = search.stochastic(
                cube_instance,
                max_iterations=max_iterations)

        # Ketika user memilih algoritma random restart
        elif algorithm_choice == "3":
            # Meminta input dari user
            max_restarts = int(input("Enter maximum restarts: "))
            max_iterations = int(input("Enter maximum iterations per restart: "))

            # Memulai timer algoritma random restart
            start_time = time.time()

            # Menjalankan algoritma random restart search
            final_state, final_value, iterations, best_scores = search.random_restart(cube_instance, max_restarts, max_iterations)
        
        # Ketika user memilih algoritma sideways
        elif algorithm_choice == "2":
            # Meminta input dari user
            max_sideways = int(input("Enter the maximum number of sideways iterations: "))

            # Memulai timer algoritma sideways
            start_time = time.time()

            # Menjalankan algoritma sideways search
            final_state, final_value, iterations, best_scores = search.sideways_move(cube_instance, max_sideways)

        # Ketika user memilih algoritma steepest
        elif algorithm_choice == "1":
            # Meminta input dari user
            max_iterations = int(input("Enter maximum iterations: "))

            # Memulai timer algoritma steepest
            start_time = time.time()

            # Menjalankan algoritma steepest search
            final_state, final_value, iterations, best_scores = search.steepest_ascent(cube_instance, max_iterations)
        
        # Ketika user memilih algoritma selain angka 1-6
        else:
            print("Invalid algorithm choice! Choose between 1-6.")
            return

        # Menyelesaikan timer
        end_time = time.time()

        # Menyimpan semua hasil
        results['final_state'] = final_state
        results['final_value'] = final_value
        results['iterations'] = iterations
        results['duration'] = end_time - start_time

        # Membuat plot nilai objektif terhadap jumlah iterasi
        plt.plot(best_scores, label=algorithm_choice.capitalize() + " Algorithm")
        
        # Memberikan label pada plot
        plt.xlabel("Iterations")
        plt.ylabel("Objective Function Value")

        # Menampilkan grafik
        plt.title("Objective Function vs Iterations (" + algorithm_choice.capitalize() + ")")
        plt.legend()
        plt.show()

    # Menampilkan semua hasil dari algoritma search yang dipilih
    print("-" * 40)
    print(f"Algorithm: {results['algorithm']}")

    # Menampilkan state awal dari cube
    results['initial_state'].display_layered()
    print(f"\nInitial Objective Value: {results['initial_value']}")

    # Menampilkan state akhir dari cube
    results['final_state'].display_layered()
    print(f"\nFinal Objective Value: {results['final_value']}")

    # Menampilkan stuck counter dari algoritma simulated annealing
    if algorithm_choice == "5":
        print(f"Stuck Counter: {results['stuck']}")

    # Menampilkan ukuran populasi dari algoritma genetic
    elif algorithm_choice == "6":
        print(f"Population Size: {results['population_size']}")

    # Menampilkan jumlah iterasi dan durasi dari algoritma search yang dipilih
    print(f"Iterations: {results['iterations']}")
    print(f"Duration: {results['duration']:.4f} seconds")
    print("-" * 40)