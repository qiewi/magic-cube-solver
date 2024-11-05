import numpy as np
import time
import matplotlib.pyplot as plt
from algorithm.SimulatedAnnealing import simulated_annealing
from models.cube import Cube

def simulatedAnnealingDriver(initial_temperature=1000, cooling_rate=0.99, min_temperature=0.1, max_iterations=10000):
    # Initialize the starting cube
    cube_instance = Cube()
    initial_state = cube_instance.cube.copy()

    # Start timing the execution
    start_time = time.time()

    # Run the simulated annealing algorithm
    best_state, best_objective, objective_values, acceptance_probabilities, stuck_counter = simulated_annealing(
        cube_instance,
        initial_temperature=initial_temperature,
        cooling_rate=cooling_rate,
        min_temperature=min_temperature,
        max_iterations=max_iterations
    )

    # End timing of execution
    end_time = time.time()
    duration = end_time - start_time

    # Plot objective function value over iterations
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(objective_values, label='Objective Function Value')
    plt.xlabel('Iterations')
    plt.ylabel('Objective Function Value')
    plt.title('Objective Function Value vs Iteration')
    plt.legend()

    # Plot e^(ΔE/T) values over iterations
    plt.subplot(1, 2, 2)
    plt.plot(acceptance_probabilities, label='Acceptance Probability e^(ΔE/T)', color='orange')
    plt.xlabel('Iterations (only for ΔE > 0)')
    plt.ylabel('Acceptance Probability')
    plt.title('Acceptance Probability e^(ΔE/T) vs Iteration')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Display results
    print("Initial State:")
    print(initial_state)
    print("\nFinal State (Best State Found):")
    print(best_state)
    print(f"\nFinal Objective Function Value: {best_objective}")
    print(f"Number of Iterations: {len(objective_values)}")
    print(f"Stuck Counter: {stuck_counter}")
    print(f"Duration of Search Process: {duration:.2f} seconds")

# Execute the driver function
simulatedAnnealingDriver(initial_temperature=1000, cooling_rate=0.99, min_temperature=0.1, max_iterations=10000)