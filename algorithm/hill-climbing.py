import random
import time
import numpy as np
import matplotlib.pyplot as plt
from models.cube import Cube  

# Function to find the best neighbor from the current state
def get_neighbors(cube, current_score):
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
def steepest_ascent_hill_climbing(cube, max_iterations):
    current_state = cube
    current_score = current_state.objective_function()
    iterations = 0
    scores = []

    while iterations < max_iterations:
        scores.append(current_score)
        neighbor = get_neighbors(current_state, current_score)
        
        # Check if a better neighbor was found
        if neighbor is None:
            break  # No improvement found, terminate early
        else:
            current_state = neighbor
            current_score = current_state.objective_function()
        
        print(f"iterations: {iterations} - current score: {current_score}")
        iterations += 1

    return current_state, current_score, iterations, scores

def sideways_move(cube, max_sideways):
    current_state = cube
    current_score = current_state.objective_function()
    scores = []
    sideways_count = 0  # Counter for sideways moves

    while True:
        scores.append(current_score)

        # Get neighbors of the current state in each iteration
        neighbors = get_neighbors(current_state)
        next_state = None
        next_score = current_score
        found_better = False

        # Look for any neighbor with a better objective score
        for neighbor in neighbors:
            score = neighbor.objective_function()
            if score < current_score:  # Found a better neighbor
                next_state = neighbor
                next_score = score
                found_better = True
                break  # Break immediately if a better neighbor is found

        # If no better neighbor, look for a sideways move (equal score)
        if not found_better:
            for neighbor in neighbors:
                score = neighbor.objective_function()
                if score == current_score:  # Consider this a sideways move
                    # Ensure state actually changes for sideways move
                    next_state = neighbor
                    next_score = score
                    break

        # If no valid move is found, exit
        if next_state is None:
            print("No valid moves found, stopping.")
            break
        
        # **Important**: If we made a move (even a sideways move), update state
        if next_state != current_state:  # If the state is actually different
            current_state = next_state
            current_score = next_score
        else:
            print("Warning: No state change, something might be wrong.")

        # Reset or increment sideways counter based on whether it was a better move
        if found_better:
            sideways_count = 0  # Reset sideways count after finding improvement
        else:
            sideways_count += 1  # Increment sideways count only for sideways moves

        # Stop if sideways moves reach the max allowed
        if sideways_count >= max_sideways:
            print("Reached max sideways moves, stopping.")
            break

    return current_state, current_score, len(scores), scores

def random_restart_hill_climbing(cube, max_restarts, max_iterations):
    best_state = None
    best_score = float('inf')
    scores_all = []  # Untuk menyimpan skor dari semua iterasi dalam semua restart

    # Lakukan restart beberapa kali hingga mencapai max_restarts
    for restart in range(max_restarts):
        print(f"\nRestart {restart + 1}/{max_restarts}")
        
        # Menghasilkan instance cube baru dari cube awal untuk setiap restart
        cube_instance = Cube()
        current_state, current_score, _, current_scores = steepest_ascent_hill_climbing(cube_instance, max_iterations)

        # Menyimpan semua scores dari iterasi ini ke dalam scores_all
        scores_all.extend(current_scores)

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
    return best_state, best_score, len(scores_all), scores_all

def stochastic_hill_climbing(cube, max_iterations=1000):
    current_state = cube
    current_score = current_state.objective_function()
    scores = []

    for iteration in range(max_iterations):
        scores.append(current_score)

        # Generate a single random neighbor
        next_state = random.choice(get_neighbors(current_state))
        next_score = next_state.objective_function()

        # Only accept the neighbor if it has a strictly lower score
        if next_score < current_score:
            current_state = next_state
            current_score = next_score

    return current_state, current_score, max_iterations, scores

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
    results['initial_state'] = cube_instance.cube.copy()  # Menyimpan kondisi awal kubus
    results['initial_value'] = cube_instance.objective_function()

    # Start timer
    start_time = time.time()

    # Run selected algorithm
    if algorithm_choice == "random_restart":
        max_restarts = int(input("Enter maximum restarts: "))
        max_iterations = int(input("Enter maximum iterations per restart: "))
        final_state, final_value, iterations, scores = random_restart_hill_climbing(cube_instance, max_restarts, max_iterations)
        
    elif algorithm_choice == "steepest":
        max_iterations = int(input("Enter maximum iterations per restart: "))
        final_state, final_value, iterations, scores = steepest_ascent_hill_climbing(cube_instance, max_iterations)
        
    elif algorithm_choice == "sideways":
        max_sideways = int(input("Enter the maximum number of sideways iterations: "))
        final_state, final_value, iterations, scores = sideways_move(cube_instance, max_sideways)
        
    elif algorithm_choice == "stochastic":
        max_iterations = int(input("Enter maximum iterations for stochastic: "))
        final_state, final_value, iterations, scores = stochastic_hill_climbing(
            cube_instance,
            max_iterations=max_iterations
        )
        
    else:
        print("Invalid algorithm choice!")
        return

    # End timer
    end_time = time.time()

    # Store results
    results['final_state'] = final_state.cube
    results['final_value'] = final_value
    results['iterations'] = iterations
    results['duration'] = end_time - start_time

    # Plotting the objective function value against iterations
    plt.plot(scores, label=algorithm_choice.capitalize() + " Algorithm")
    plt.title("Objective Function vs Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Objective Function Value")
    plt.legend()
    plt.show()

    # Display experiment results
    print(f"Algorithm: {results['algorithm']}")
    print(f"Initial State:\n{results['initial_state']}")
    print(f"Initial Objective Value: {results['initial_value']}")
    print(f"Final State:\n{results['final_state']}")
    print(f"Final Objective Value: {results['final_value']}")
    print(f"Iterations: {results['iterations']}")
    print(f"Duration: {results['duration']:.4f} seconds")
    print("-" * 40)

# Main function for selecting algorithm
def main():
    algorithm_choice = input("Choose algorithm (steepest/sideways/random_restart/stochastic): ").strip().lower()
    run_experiment(algorithm_choice)

# Run main function
if __name__ == "__main__":
    main()