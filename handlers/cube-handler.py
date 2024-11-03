from models.cube import Cube  # Import Cube from the models folder

def main():
    # Step 1: Construct the cube
    cube = Cube()
    
    # Step 2: Calculate the objective function
    objective_value = cube.objective_function()
    
    # Step 3: Display the cube structure
    print("5x5x5 Cube Structure:")
    for layer in range(cube.n):
        print(f"Layer {layer + 1}:")
        for row in cube.cube[layer]:
            print(" ", row)
        print()  # Blank line between layers
    
    # Display the objective function result
    print(f"Objective Function Value: {objective_value}")

if __name__ == "__main__":
    main()
