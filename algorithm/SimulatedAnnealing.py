import numpy as np
import random
import math
import time
import matplotlib.pyplot as plt
from models.cube import Cube

def simulated_annealing(cube_instance, initial_temperature=1000, cooling_rate=0.99, min_temperature=0.1, max_iterations=10000):
    current_state = np.copy(cube_instance.cube)
    current_objective = cube_instance.objective_function()
    best_state = np.copy(current_state)
    best_objective = current_objective

    objective_values = []
    acceptance_probabilities = []
    T = initial_temperature
    stuck_counter = 0
    unchanged_iterations = 0

    for iteration in range(max_iterations):
        if T < min_temperature:
            break

        # Generate a neighbor by swapping two numbers
        neighbor_state = np.copy(current_state)
        x1, y1, z1 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
        x2, y2, z2 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
        neighbor_state[x1, y1, z1], neighbor_state[x2, y2, z2] = neighbor_state[x2, y2, z2], neighbor_state[x1, y1, z1]

        # Update the temporary cube and calculate the objective value
        cube_instance.cube = neighbor_state
        neighbor_objective = cube_instance.objective_function()

        # Calculate ΔE
        delta_E = neighbor_objective - current_objective

        # Decide whether to accept the neighbor
        acceptance_probability = math.exp(-delta_E / T) if delta_E > 0 else 1
        if delta_E < 0 or random.uniform(0, 1) < acceptance_probability:
            current_state = neighbor_state
            current_objective = neighbor_objective
            if current_objective < best_objective:
                best_state = np.copy(current_state)
                best_objective = current_objective

        # Store the objective value and acceptance probability
        objective_values.append(current_objective)
        if delta_E > 0:  # Store acceptance probability for worse solutions
            acceptance_probabilities.append(acceptance_probability)

        # Check if the algorithm is stuck in a local optimum
        if delta_E == 0:
            unchanged_iterations += 1
            if unchanged_iterations >= 100:
                stuck_counter += 1
                unchanged_iterations = 0
        else:
            unchanged_iterations = 0

        T *= cooling_rate

    return best_state, best_objective, objective_values, acceptance_probabilities, stuck_counter
