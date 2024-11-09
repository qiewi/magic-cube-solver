from handlers.algorithm import run_algorithm
import time

white = "\033[97m"
reset = "\033[96m"

algorithm_menu = [
    f"    {reset}LIST OF AVAILABLE ALGORITHMS                 ",
    "                                                         ",
    f"{white}1. Steepest Ascent Hill Climbing{reset}          ",
    f"{white}2. Sideways Move{reset}                          ",
    f"{white}3. Random Restart Hill Climbing{reset}           ",
    f"{white}4. Stochastic Hill Climbing{reset}               ",
    f"{white}5. Simulated Annealing{reset}                    ",
    f"{white}6. Genetic Algorithm{reset}                      ",
    "                                                         ",
    f"    {reset}CHOOSE ALGORITHM BY NUMBER                   "
]


'''---------------------------------------------------------- Starting Point ----------------------------------------------------------'''
if __name__ == "__main__":

    process = True

    while process: # Saat status process = True
        import Visual
        
        Visual.printascii("home")
        menu = input(">>> ") # Meminta input user

        if menu == "OK" : # Saat user memasukan command login namun user sudah login
            Visual.render_screen(algorithm_menu, 10)
            algorithm_choice = input(">>> ")
            run_algorithm(algorithm_choice)

'''---------------------------------------------------------- Starting Point ----------------------------------------------------------'''