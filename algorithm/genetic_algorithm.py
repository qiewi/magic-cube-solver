import numpy as np
import random

from models.cube import Cube

class GeneticAlgorithm:
    def __init__(self):
        self.best_cube = None
        self.best_value = float('inf')
        
    # Initialize population
    def populate(self, population_size):
        population = [Cube() for _ in range(population_size)]
        return population

    # Selection Process
    def selection(self, population):
        # Calculate fitness for each cube in population
        fitness_scores = [cube.objective_function() for cube in population]

        # Calculate selection probabilities (inverse of fitness scores) and cumulative ranges
        total_fitness = sum(fitness_scores)
        selection_probs = [(total_fitness - score) / total_fitness for score in fitness_scores]
        cumulative_probs = np.cumsum(selection_probs) / np.sum(selection_probs) * 100

        # Select parents based on cumulative ranges to create a pool of population_size parents
        parents = []
        for cube in range(len(population)):
            random_percentage = random.uniform(0, 100)
            for i, prob in enumerate(cumulative_probs):
                if random_percentage <= prob:
                    parents.append(population[i])
                    break
        
        return parents

    # Crossover Process
    def crossover(self, parents):
        new_population = []
        for i in range(0, len(parents), 2):  # Process parents in pairs
            parent1 = parents[i]
            parent2 = parents[i + 1]

            # Cross-over
            crossover_point = random.randint(1, 126)
            temp_1 = Cube()
            temp_2 = Cube()

            # Store the last part of the cube to temporary cubes
            temp_1.cube.flat[crossover_point:] = parent1.cube.flat[crossover_point:]
            temp_2.cube.flat[crossover_point:] = parent2.cube.flat[crossover_point:]

            # Swap the last part of the cube from the temporary cubes
            parent1.cube.flat[crossover_point:] = temp_2.cube.flat[crossover_point:]
            parent2.cube.flat[crossover_point:] = temp_1.cube.flat[crossover_point:]

            # Append the cubes to the new population
            new_population.append(parent1)
            new_population.append(parent2)
        
        return new_population

    # Mutation Process
    def mutation(self, new_population):
        # Mutate each of the cubes on a random index
        for i in range(len(new_population)):
            new_population[i].cube.flat[random.randint(0, 124)] = random.randint(0, 125)
        
        return new_population

    # Genetic Search 
    def genetic_search(self, population_size, max_iterations):    
        for i in range(max_iterations):

            # Initialize population
            population = self.populate(population_size)

            # Selection Process
            parents = self.selection(population)
            
            # Crossover Process
            crossover_result = self.crossover(parents)

            # Mutation Process
            new_population = self.mutation(crossover_result)

            # Calculate objective value for each cube in population
            objective_values = [cube.objective_function() for cube in new_population]

            # Check for global maximum (objective function = 0)
            if (min(objective_values) < self.best_value):
                self.best_value = min(objective_values)
                self.best_cube = population[objective_values.index(self.best_value)]

        # Return the best cube and its objective value
        return self.best_cube, self.best_value

      
if __name__ == "__main__":
    search = GeneticAlgorithm()
    cube_instance, objective_value = search.genetic_search(10, 100)

    cube_instance.display_cube()
    print("Nilai fungsi objektif:", objective_value)
        
