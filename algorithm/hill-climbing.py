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
        
        print(f"iterations: {iterations + 1} - current score: {current_score}")
        iterations += 1

    return current_state, current_score, iterations, scores

def sideways_move(cube, max_sideways):
    current_state = cube
    current_score = current_state.objective_function()
    best_scores = []  # Stores only the best score from each iteration
    sideways_count = 0  # Counter for sideways moves

    while True:
        best_scores.append(current_score)

        # Get the best neighbor from the current state
        neighbor = get_neighbors(current_state, current_score)

        # Check if a better neighbor was found (get_neighbors returns only the best cube)
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

        print(f"Current score: {current_score}, Iterations: {len(best_scores)}")

        # Stop if the sideways moves reach the max allowed
        if sideways_count >= max_sideways:
            print("Reached max sideways moves, stopping.")
            break

    return current_state, current_score, len(best_scores), best_scores

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
    results['initial_state'] = cube_instance.cube.copy()  # Save initial cube state
    results['initial_value'] = cube_instance.objective_function()

    # Start timer
    start_time = time.time()

    # Run selected algorithm
    if algorithm_choice == "random_restart":
        max_restarts = int(input("Enter maximum restarts: "))
        max_iterations = int(input("Enter maximum iterations per restart: "))
        final_state, final_value, iterations, best_scores = random_restart_hill_climbing(cube_instance, max_restarts, max_iterations)
        
    elif algorithm_choice == "steepest":
        max_iterations = int(input("Enter maximum iterations per restart: "))
        final_state, final_value, iterations, best_scores = steepest_ascent_hill_climbing(cube_instance, max_iterations)
        
    elif algorithm_choice == "sideways":
        max_sideways = int(input("Enter the maximum number of sideways iterations: "))
        final_state, final_value, iterations, best_scores = sideways_move(cube_instance, max_sideways)
        
    elif algorithm_choice == "stochastic":
        max_iterations = int(input("Enter maximum iterations for stochastic: "))
        final_state, final_value, iterations, best_scores = stochastic_hill_climbing(
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

    # Plotting only the best score for each iteration
    plt.plot(best_scores, label=algorithm_choice.capitalize() + " Algorithm")
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