import random
import time
import numpy as np
import matplotlib.pyplot as plt
from models.cube import Cube  

class HillClimbing:
    def __init__(self):
        pass
        
    # Function to find the best neighbor from the current state
    def get_neighbor(self, cube, current_score):
        lowest_score = current_score
        best_swap = None  # Track the best swap instead of the entire cube
        n = cube.n  # Cube dimension size
        
        # Generate neighbors by swapping any two distinct elements in the cube
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for x in range(i, n):  # Avoid redundant swaps
                        for y in range(j if x == i else 0, n):
                            for z in range(k + 1 if x == i and y == j else 0, n):
                                # Swap elements
                                cube.cube[i, j, k], cube.cube[x, y, z] = cube.cube[x, y, z], cube.cube[i, j, k]
                                
                                # Calculate score of the new neighbor state
                                new_score = cube.objective_function()
                                if new_score < lowest_score:
                                    lowest_score = new_score
                                    best_swap = (i, j, k, x, y, z)  # Store swap coordinates
                                
                                # Revert the swap
                                cube.cube[i, j, k], cube.cube[x, y, z] = cube.cube[x, y, z], cube.cube[i, j, k]
        
        # Apply the best swap if found
        if best_swap:
            i, j, k, x, y, z = best_swap
            cube.cube[i, j, k], cube.cube[x, y, z] = cube.cube[x, y, z], cube.cube[i, j, k]

        return cube

    # Steepest Ascent Hill-Climbing with optimizations
    def steepest_ascent(self, cube, max_iterations):
        current_state = cube
        current_score = current_state.objective_function()
        iterations = 0
        scores = []

        while iterations < max_iterations:
            scores.append(current_score)
            neighbor = self.get_neighbor(current_state, current_score)
            
            # Check if a better neighbor was found
            if neighbor is None:
                break  # No improvement found, terminate early
            else:
                current_state = neighbor
                current_score = current_state.objective_function()
            
            print(f"iterations: {iterations + 1} - current score: {current_score}")
            iterations += 1

        return current_state, current_score, len(scores), scores

    def sideways_move(self, cube, max_sideways):
        current_state = cube
        current_score = current_state.objective_function()
        scores = []  # Stores only the best score from each iteration
        sideways_count = 0  # Counter for sideways moves

        while True:
            scores.append(current_score)

            # Get the best neighbor from the current state
            neighbor = self.get_neighbor(current_state, current_score)

            # Check if a better neighbor was found (self.get_neighbor returns only the best cube)
            next_state = neighbor
            next_score = next_state.objective_function()

            if next_score < current_score:
                # Found a better neighbor
                current_state = next_state
                current_score = next_score
                sideways_count = 0  # Reset sideways counter after finding improvement
            else:
                # If no better neighbor, check for sideways move (same score)
                if next_score == current_score:
                    current_state = next_state
                    current_score = next_score
                    sideways_count += 1  # Increment sideways count for equal score move
                else:
                    # No better or sideways move found, exit
                    break

            print(f"Current score: {current_score}, Iterations: {len(scores)}")

            # Stop if the sideways moves reach the max allowed
            if sideways_count >= max_sideways:
                print("Reached max sideways moves, stopping.")
                break

        return current_state, current_score, len(scores), scores

    def random_restart(self, cube, max_restarts, max_iterations):
        best_state = None
        best_score = float('inf')
        scores = []  # Untuk menyimpan skor dari semua iterasi dalam semua restart

        # Lakukan restart beberapa kali hingga mencapai max_restarts
        for restart in range(max_restarts):
            print(f"\nRestart {restart + 1}/{max_restarts}")
            
            # Menghasilkan instance cube baru dari cube awal untuk setiap restart
            cube_instance = Cube()
            current_state, current_score, _, current_scores = self.steepest_ascent(cube_instance, max_iterations)

            # Menyimpan semua scores dari iterasi ini ke dalam scores
            scores.extend(current_scores)

            # Cek jika skor dari iterasi ini lebih baik dari best_score
            if current_score < best_score:
                best_state = current_state
                best_score = current_score

            print(f"End of Restart {restart + 1}: Best score = {best_score}")
            
            # Berhenti jika ditemukan solusi optimal (skor 0)
            if current_score == 0:
                print("Optimal solution found!")
                break

        # Mengembalikan hasil terbaik dan semua skor dari semua iterasi
        return best_state, best_score, len(scores), scores

    def stochastic(self, cube, max_iterations=1000):
        current_state = cube
        current_score = current_state.objective_function()
        scores = []

        for iteration in range(max_iterations):
            scores.append(current_score)

            # Generate neighbors (assuming self.get_neighbor returns a list of Cube objects)
            neighbors = self.get_neighbor(current_state, current_score)

            # Ensure neighbors is a list (if self.get_neighbor returns a single Cube)
            if isinstance(neighbors, Cube):  # If it's a single Cube, put it in a list
                neighbors = [neighbors]

            # If there are no neighbors, stop the algorithm
            if not neighbors:
                break

            # Randomly select a neighbor
            next_state = random.choice(neighbors)
            next_score = next_state.objective_function()

            # Accept the neighbor only if it improves the objective value (lower score)
            if next_score < current_score:
                current_state = next_state
                current_score = next_score
                print(f"Iteration {iteration + 1}: Improved to score {current_score}")
            else:
                print(f"Iteration {iteration + 1}: No improvement, current score is {current_score}")

        return current_state, current_score, len(scores), scores
