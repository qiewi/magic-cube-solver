from handlers.algorithm import run_algorithm

# Main function to choose the algorithm
def main():
    print("""List of available algorithms:
    
    1. Steepest Ascent Hill Climbing
    2. Sideways Move
    3. Random Restart Hill Climbing
    4. Random Restart Hill Climbing
    5. Simulated Annealing
    6. Genetic Algorithm
    
    """)
    algorithm_choice = input("Choose algorithm by number: ").strip().lower()
    run_algorithm(algorithm_choice)

# Run main function
if __name__ == "__main__":
    main()
