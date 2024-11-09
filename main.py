from handlers.algorithm import run_algorithm

algorithm_menu = [
    "List of available algorithms:             ",
    "                                          ",
    "1. Steepest Ascent Hill Climbing          ",
    "2. Sideways Move                          ",
    "3. Random Restart Hill Climbing           ",
    "4. Stochastic Hill Climbing               ",
    "5. Simulated Annealing                    ",
    "6. Genetic Algorithm                      ",
    "                                          ",
    "Choose an algorithm by number:            "
]

# # Run main function
# if __name__ == "__main__":
#     main()

import time

'''---------------------------------------------------------- Starting Point ----------------------------------------------------------'''
if __name__ == "__main__":

    process = True

    while process: # Saat status process = True
        import Visual
        
        Visual.printascii("home")
        menu = input(">>> ") # Meminta input user

        if menu == "OK" : # Saat user memasukan command login namun user sudah login
            Visual.render_screen(algorithm_menu, 10)
            time.sleep(2)
            algorithm_choice = input(">>> ")
            run_algorithm(algorithm_choice)

'''---------------------------------------------------------- Starting Point ----------------------------------------------------------'''