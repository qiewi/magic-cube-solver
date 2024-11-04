
import numpy as np
import random

def geneticAlgorithm(cube, population_size=10, max_iterations=1000):
    # Initialize population
    population = [cube() for _ in range(population_size)]
    n = 0

    # Track the best cube found
    best_cube = None
    best_fitness = float('inf')

    while n < max_iterations:
        # Calculate fitness for each cube in population
        fitness_scores = [cube.objective_function() for cube in population]
        
        # Check for global maximum (objective function = 0)
        if 0 in fitness_scores:
            print("Found a perfect magic cube!")
            return population[fitness_scores.index(0)]

        # Update the best cube if a better one is found
        min_fitness = min(fitness_scores)
        if min_fitness < best_fitness:
            best_fitness = min_fitness
            best_cube = population[fitness_scores.index(min_fitness)]

        # Calculate selection probabilities (inverse of fitness scores) and cumulative ranges
        total_fitness = sum(fitness_scores)
        selection_probs = [(total_fitness - score) / total_fitness for score in fitness_scores]
        cumulative_probs = np.cumsum(selection_probs) / np.sum(selection_probs) * 100

        # Select parents based on cumulative ranges to create a pool of population_size parents
        parents = []
        for _ in range(population_size):
            random_percentage = random.uniform(0, 100)
            for i, cum_prob in enumerate(cumulative_probs):
                if random_percentage <= cum_prob:
                    parents.append(population[i])
                    break

        # Generate new population through crossover and mutation
        new_population = []
        for i in range(0, population_size, 2):  # Process parents in pairs
            parent1 = parents[i]
            parent2 = parents[i + 1] if i + 1 < population_size else parents[0]

            # Cross-over
            crossover_point = random.randint(1, parent1.n ** 3 - 1)
            child1 = cube()
            child2 = cube()
            child1.cube.flat[:crossover_point] = parent1.cube.flat[:crossover_point]
            child1.cube.flat[crossover_point:] = parent2.cube.flat[crossover_point:]
            child2.cube.flat[:crossover_point] = parent2.cube.flat[:crossover_point]
            child2.cube.flat[crossover_point:] = parent1.cube.flat[crossover_point:]

            # Mutation
            if random.random() < 0.1:  # 10% mutation rate
                mutate(child1)
            if random.random() < 0.1:
                mutate(child2)

            # Add children to the new population
            new_population.extend([child1, child2])

        # Replace the old population with the new one
        population = new_population[:population_size]

        n += 1
        print(f"Iteration {n}, best objective function: {min_fitness}")

    print("Max iterations reached without finding a perfect magic cube.")
    return best_cube, best_fitness, best_fitness

def mutate(cube):
    n = cube.n
    layer = random.randint(0, n - 1)
    row = random.randint(0, n - 1)
    col = random.randint(0, n - 1)
    new_value = random.randint(1, n ** 3)
    cube.cube[layer, row, col] = new_value 
