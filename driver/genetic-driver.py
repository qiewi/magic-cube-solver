import numpy as np
import random
import time
import matplotlib.pyplot as plt
from algorithm.GeneticAlgorithm import geneticAlgorithm
from models.cube import Cube

def geneticAlgorithmDriver(population_size, max_iterations):
    # Initialize initial population and measure initial state
    initial_population = [Cube() for _ in range(population_size)]
    initial_states = [cube.cube.copy() for cube in initial_population]

    # Start timing the algorithm execution
    start_time = time.time()

    # Run the genetic algorithm
    best_cube, max_objective_values, avg_objective_values = geneticAlgorithm(
        Cube, population_size=population_size, max_iterations=max_iterations
    )

    # Capture end time and calculate duration
    end_time = time.time()
    duration = end_time - start_time

    # Final state of the best cube
    final_state = best_cube.cube

    # Final objective function value
    final_objective_value = best_cube.objective_function()

    # Plot objective function values over iterations
    iterations = max_iterations
    plt.figure(figsize=(10, 5))
    plt.plot(iterations, max_objective_values, label='Max Objective Value')
    plt.plot(iterations, avg_objective_values, label='Average Objective Value')
    plt.xlabel('Iterations')
    plt.ylabel('Objective Function Value')
    plt.title('Objective Function Values over Iterations')
    plt.legend()
    plt.show()

    # Print out the required details
    print("Initial State (First Cube):")
    print(initial_states[0])
    print("\nFinal State of Best Cube:")
    print(final_state)
    print(f"\nFinal Objective Function Value: {final_objective_value}")
    print(f"Population Size: {population_size}")
    print(f"Number of Iterations: {max_iterations}")
    print(f"Duration of Search Process: {duration:.2f} seconds")

# Execute the driver function
geneticAlgorithmDriver(population_size=10, max_iterations=100)
