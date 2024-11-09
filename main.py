# Import library yang dibutuhkan
from handlers.algorithm import run_algorithm
import time

'''-------------------- Kode Warna --------------------'''
white = "\033[97m"
reset = "\033[96m"
'''-------------------- Kode Warna --------------------'''

'''-------------------- Menu Awal --------------------'''
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
'''-------------------- Menu Awal --------------------'''


'''---------------------------------------------------------- Starting Point ----------------------------------------------------------'''
if __name__ == "__main__":

    process = True

    while process:
        import Visual
        
        Visual.printascii("home")
        menu = input(f"{white}>>> {reset}") 

        if menu.upper() == "OK" : 
            Visual.render_screen(algorithm_menu, 10)
            algorithm_choice = input(f"{white}>>> {reset}")
            run_algorithm(algorithm_choice)

        elif menu.upper() == "QUIT" :
            Visual.render_screen([f"{white}Goodbye!{reset}"], 1)
            time.sleep(1)
            process = False

        else:
            Visual.render_screen([f"{white}Invalid command! Choose between 'OK' or 'QUIT.{reset}"], 1)
            input(f">>> {white}Press ENTER to go back to HOME{reset}")

'''---------------------------------------------------------- Starting Point ----------------------------------------------------------'''