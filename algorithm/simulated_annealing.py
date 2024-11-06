import numpy as np
import random, math, time
import matplotlib.pyplot as plt

from models.cube import Cube

class SimulatedAnnealing():
    def __init__(self):
        self.best_cube = None
        self.best_value = float('inf')

    # Set the best state found
    def set_state(self, cube, objective_value):
        self.best_cube = cube
        self.best_value = objective_value
    
    # Generate a neighbor by swapping two numbers
    def generate_neighbor(self, current_state, ):
        # Generate a neighbor by swapping two numbers in the cube
        neighbor_state = np.copy(current_state)
        x1, y1, z1 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
        x2, y2, z2 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
        neighbor_state[x1, y1, z1], neighbor_state[x2, y2, z2] = neighbor_state[x2, y2, z2], neighbor_state[x1, y1, z1]
        
        # Set the modified state in the cube and calculate the objective value
        cube_instance = Cube()
        cube_instance.cube = neighbor_state
        neighbor_objective = cube_instance.objective_function()

        return neighbor_state, neighbor_objective
    

    # Simulated Annealing Algorithm
    def simulated_annealing(self, cube_instance, initial_temperature, cooling_rate, min_temperature, max_iterations):
        # Initialize the starting state
        T = initial_temperature
        current_state = np.copy(cube_instance.cube)
        current_objective = cube_instance.objective_function()
        
        # Set the best state found at first
        self.set_state(current_state, current_objective)

        # Initialize arrays to store objective values and acceptance probabilities
        objective_values = []
        acceptance_probabilities = []
        
        # Initialize stuck counter and unchanged iterations
        stuck_counter = 0
        unchanged_iterations = 0

        for iteration in range(max_iterations):
            if T < min_temperature:
                break

            # Generate a neighbor by swapping two numbers
            neighbor_state, neighbor_objective = self.generate_neighbor(current_state)

            # Calculate ΔE
            delta_E = neighbor_objective - current_objective

            # Calculate acceptance probability
            acceptance_probability = math.exp(-delta_E / T) if delta_E > 0 else 1

            # Decide whether to accept the neighbor
            if delta_E < 0 or random.uniform(0, 1) < acceptance_probability:
                current_state = neighbor_state
                current_objective = neighbor_objective

                # Update the best state if the current state is better
                if current_objective < self.best_value:
                    self.set_state(current_state, current_objective)


            # Store the objective value and acceptance probability
            objective_values.append(current_objective)

            # Store acceptance probability for worse solutions
            if delta_E > 0:  
                acceptance_probabilities.append(acceptance_probability)

            # Check if the algorithm is stuck in a local optimum
            if delta_E == 0:
                unchanged_iterations += 1
                if unchanged_iterations >= 100:
                    stuck_counter += 1
                    unchanged_iterations = 0
            else:
                unchanged_iterations = 0

            # Update the temperature
            T *= cooling_rate

        return self.best_cube, self.best_value, objective_values, acceptance_probabilities, stuck_counter