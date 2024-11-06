import time
import matplotlib.pyplot as plt
from models.cube import Cube
from algorithm.hill_climbing import HillClimbing
from algorithm.genetic_algorithm import GeneticAlgorithm
from algorithm.simulated_annealing import SimulatedAnnealing

def run_algorithm(algorithm_choice):
    results = {
        'algorithm':
        {   "1": "Steepest Ascent",
            "2": "Sideways",
            "3": "Random Restart",
            "4": "Stochastic",
            "5": "Simulated Annealing",
            "6": "Genetic Algorithm"
        }[algorithm_choice],
        'initial_state': [],
        'final_state': [],
        'initial_value': [],
        'final_value': [],
        'iterations': [],
        'duration': [],
        # Simulated Annealing
        'stuck': [], 
        # Genetic Algorithm
        'population_size': [],
    }

    # Generate initial cube instance
    cube_instance = Cube()
    
    results['initial_state'] = cube_instance  # Save initial cube state
    results['initial_value'] = cube_instance.objective_function()

    # Start timer
    start_time = time.time()

    if algorithm_choice == "6":
        population_size = int(input("Enter population size: "))
        max_iterations = int(input("Enter maximum iterations: "))
        
        search = GeneticAlgorithm()
        
        min_scores = []
        avg_scores = []
        
        # Run genetic search and record min and average scores
        for _ in range(max_iterations):
            final_state, final_value, population = search.genetic_search(population_size, max_iterations)
            fitness_scores = [cube.objective_function() for cube in population]
            min_scores.append(min(fitness_scores))
            avg_scores.append(sum(fitness_scores) / len(fitness_scores))

        # End timer
        end_time = time.time()
        
        results['final_state'] = final_state
        results['final_value'] = final_value
        results['iterations'] = max_iterations
        results['duration'] = end_time - start_time
        results['population_size'] = population_size

        # Plotting maximum and average scores
        plt.plot(min_scores, label="Max Objective Function")
        plt.plot(avg_scores, label="Average Objective Function")
        plt.title("Objective Function vs Iterations (Genetic Algorithm)")
        plt.xlabel("Iterations")
        plt.ylabel("Objective Function Value")
        plt.legend()
        plt.show()

    elif algorithm_choice == "5":
        initial_temperature = float(input("Enter initial temperature: "))
        cooling_rate = float(input("Enter cooling rate (0 < cooling rate < 1): "))
        min_temperature = float(input("Enter minimum temperature: "))
        max_iterations = int(input("Enter maximum iterations: "))
        
        search = SimulatedAnnealing()
        
        # Run simulated annealing and collect values
        best_state, best_objective, objective_values, acceptance_probabilities, stuck_counter = search.simulated_annealing(
            cube_instance,
            initial_temperature,
            cooling_rate,
            min_temperature,
            max_iterations
        )
        
        end_time = time.time()
        results['final_state'] = best_state
        results['final_value'] = best_objective
        results['iterations'] = len(objective_values)
        results['duration'] = end_time - start_time
        results['stuck'] = stuck_counter

        # Plot objective function values and acceptance probabilities
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.plot(objective_values, label='Objective Function Value')
        plt.xlabel('Iterations')
        plt.ylabel('Objective Function Value')
        plt.title('Objective Function Value vs Iteration (Simulated Annealing)')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(acceptance_probabilities, label='Acceptance Probability e^(ΔE/T)', color='orange')
        plt.xlabel('Iterations (only for ΔE > 0)')
        plt.ylabel('Acceptance Probability')
        plt.title('Acceptance Probability e^(ΔE/T) vs Iteration')
        plt.legend()

        plt.tight_layout()
        plt.show()

    else:
        search = HillClimbing()

        # Handling for hill climbing algorithms
        if algorithm_choice == "3":
            max_restarts = int(input("Enter maximum restarts: "))
            max_iterations = int(input("Enter maximum iterations per restart: "))
            final_state, final_value, iterations, best_scores = search.random_restart(cube_instance, max_restarts, max_iterations)
        
        elif algorithm_choice == "1":
            max_iterations = int(input("Enter maximum iterations: "))
            final_state, final_value, iterations, best_scores = search.steepest_ascent(cube_instance, max_iterations)
        
        elif algorithm_choice == "2":
            max_sideways = int(input("Enter the maximum number of sideways iterations: "))
            final_state, final_value, iterations, best_scores = search.sideways_move(cube_instance, max_sideways)
        
        elif algorithm_choice == "4":
            max_iterations = int(input("Enter maximum iterations: "))
            final_state, final_value, iterations, best_scores = search.stochastic(
                cube_instance,
                max_iterations=max_iterations
            )
        else:
            print("Invalid algorithm choice!")
            return

        end_time = time.time()
        results['final_state'] = final_state
        results['final_value'] = final_value
        results['iterations'] = iterations
        results['duration'] = end_time - start_time

        # Plot best scores over iterations
        plt.plot(best_scores, label=algorithm_choice.capitalize() + " Algorithm")
        plt.title("Objective Function vs Iterations (" + algorithm_choice.capitalize() + ")")
        plt.xlabel("Iterations")
        plt.ylabel("Objective Function Value")
        plt.legend()
        plt.show()

    # Display experiment results
    print(f"Algorithm: {results['algorithm']}")
    results['initial_state'].display_layered()
    print(f"\nInitial Objective Value: {results['initial_value']}")
    results['final_state'].display_layered()
    print(f"\nFinal Objective Value: {results['final_value']}")

    if algorithm_choice == "5":
        print(f"Stuck Counter: {results['stuck']}")
    elif algorithm_choice == "6":
        print(f"Population Size: {results['population_size']}")

    print(f"Iterations: {results['iterations']}")
    print(f"Duration: {results['duration']:.4f} seconds")
    print("-" * 40)

def main():
    algorithm_choice = input("Choose algorithm (steepest/sideways/random_restart/stochastic/simulated_annealing/genetic): ").strip().lower()
    run_experiment(algorithm_choice)

if __name__ == "__main__":
    main()