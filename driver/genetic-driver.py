import time
import matplotlib.pyplot as plt
from models.cube import Cube
from algorithm.genetic_algorithm import GeneticAlgorithm  # Import the GeneticAlgorithm class

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
    results['initial_state'] = cube_instance.cube.copy()
    results['initial_value'] = cube_instance.objective_function()

    if algorithm_choice == "genetic":
        population_size = int(input("Enter population size: "))
        max_iterations = int(input("Enter maximum iterations: "))

        # Initialize and run genetic algorithm
        search = GeneticAlgorithm()
        start_time = time.time()
        
        # Run genetic search with tracking of max and average scores
        min_scores = []
        avg_scores = []
        for _ in range(max_iterations):
            final_state, final_value, population = search.genetic_search(population_size, max_iterations)
            
            # Calculate max and average scores from the current population
            fitness_scores = [cube.objective_function() for cube in population]
            min_scores.append(min(fitness_scores))
            avg_scores.append(sum(fitness_scores) / len(fitness_scores))
        
        end_time = time.time()

        results['final_state'] = final_state.cube if hasattr(final_state, 'cube') else final_state
        results['final_value'] = final_value
        results['iterations'] = max_iterations
        results['duration'] = end_time - start_time

        # Plot maximum and average scores over iterations
        plt.plot(min_scores, label="Max Objective Function")
        plt.plot(avg_scores, label="Average Objective Function")
        plt.title("Objective Function vs Iterations")
        plt.xlabel("Iterations")
        plt.ylabel("Objective Function Value")
        plt.legend()
        plt.show()

    else:
        # Existing code for other algorithms (steepest, sideways, random_restart)
        start_time = time.time()
        # Handling for other algorithm choices
        if algorithm_choice == "steepest":
            final_state, final_value, iterations, scores = steepest_ascent_hill_climbing(cube_instance, max_iterations=100)
        elif algorithm_choice == "sideways":
            final_state, final_value, iterations, scores = sideways_move(cube_instance, max_iterations=100)
        elif algorithm_choice == "random_restart":
            max_restarts = int(input("Enter maximum restarts: "))
            max_iterations = int(input("Enter maximum iterations per restart: "))
            final_state, final_value, iterations, scores = random_restart_hill_climbing(cube_instance, max_restarts, max_iterations)
        else:
            print("Invalid algorithm choice!")
            return
        end_time = time.time()

    # Display experiment results
    print(f"Algorithm: {results['algorithm']}")
    print(f"Initial State:\n{results['initial_state']}")
    print(f"Initial Objective Value: {results['initial_value']}")
    print(f"Final State:\n{results['final_state']}")
    print(f"Final Objective Value: {results['final_value']}")
    print(f"Iterations: {results['iterations']}")
    print(f"Duration: {results['duration']:.4f} seconds")
    print("-" * 40)

# Main function to choose the algorithm
def main():
    algorithm_choice = input("Choose algorithm (steepest/sideways/random_restart/genetic): ").strip().lower()
    run_experiment(algorithm_choice)

# Run main function
if __name__ == "__main__":
    main()
