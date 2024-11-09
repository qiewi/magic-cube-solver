import os, time

Home = [
"                                                                                ",
"                                                                                ",
"                                      (@@@*                                     ",
"                               .@@@@@#######@@@@@                               ",
"                         @@@@@@@@@(########## /@@@@@@@@@                        ",
"                  @@@@@#############@@@@@@@@&#############@@@@@                 ",
"           @@@@@#####&@@@@/####. @@@@@#####@@@@@##### /@@@@%#####@@@@@          ",
"       @@@@#############/ @@@@@@@(############ .@@@@@@@############# %@@@@      ",
"       @@....&@@@@,@@@@@###########@@@@@ @@@@@###########@@@@@*@@@@%(((,@@      ",
"       @@........ @@@@@@@(######/ @@@@@###@@@@@####### .@@@@@@@((((((((,@@      ",
"       @@........ @@.......@@@@@###############, @@@@@(((((((@@((((((((,@@      ",
"       @@........ @@........ @#...@@@@@#( @@@@@(((@@/((((((((@@((((((((,@@      ",
"       @@........ @@........ @#.........@(((((((((@@/((((((((@@(((((((( @@      ",
"       @@.@@@@@.. @@........ @#.........@(((((((((@@/((((((((@@(/ @@@@@.@@      ",
"       @@.......%@@@@....... @#.........@(((((((((@@/(((((* @@@@%((((((,@@      ",
"       @@........ @@...@@@@, @#.........@(((((((((@@ ,@@@@(((@@((((((((,@@      ",
"       @@........ @@........ @@@@@......@((((( @@@@@(((((((((@@((((((((,@@      ",
"       @@........ @@........ @#....@@@@@@@@@@&((((@@/((((((((@@((((((((.@@      ",
"       @@@@@@.... @@........ @#.........@(((((((((@@/((((((((@@(((( @@@@@@      ",
"       @@.....@@@@@@........ @#.........@(((((((((@@/((((((((@@@@@@/(((,@@      ",
"       @@........ @@@@@..... @#.........@(((((((((@@/(((/ @@@@@((((((((,@@      ",
"       @@........ @@....@@@@ @#.........@(((((((((@@ @@@@((((@@((((((((,@@      ",
"       @@........ @@........ @@@@.......@(((((/ @@@@/((((((((@@((((((( @@@      ",
"       @@@,...... @@........ @#...@@@@..@* @@@@(((@@/((((((((@@((( @@@#         ",
"           @@@@.. @@........ @#........@@@((((((((@@/((((((((@@@@@.             ",
"                @@@@........ @#.........@(((((((((@@/((((( @@@                  ",
"                     @@@.... @#.........@(((((((((@@/( @@@                      ",
"                         @@@@@#.........@((((((((/@@@@                          ",
"                              @@@#......@((((,,@@@                               ",
"                                  /@@@. @ #@@@                                   ",
"                                       @@@                                       ",
"                                                                                 ",
"                                                                                 ",
'Selamat datang di program “Magic Cube Solver”',
'Ketik "OK" untuk lanjut']

'''-------------------- Menghitung Panjang String --------------------'''
# Menggunakan metode sentinel
def length(arr: str,EOP: str) -> int:
    count = 0 # Inisialisasi awal jumlah character
    i = 0 # index string
    cek = True # Kondisi pemberhenti perhitungan

    while cek: # Saat kondisi True (sentinel belum ditemukan)
        if arr[i] == EOP: # Saat sentinel ditemukan
            cek = False # Kondisi berubah menjadi False
        else: # Saat sentinel belum ditemukan
            count +=1 # Panjang atau jumlah character bertambah 1
        i+=1 # index string bertambah 1

    return count # Mengembalikan nilai panjang string

'''------------------------------------------------------------ Print Animasi ------------------------------------------------------------'''

'''-------------------- Get Window Size --------------------'''
def window_size():
    # get size of the current terminal
    size = os.get_terminal_size()
    # set window width from terminal size
    window_width = size.columns
    # set initial window height from terminal size
    window_height = size.lines
    # we set five line in the bottom for the input, so modified window_height
    number_of_lines_for_input = 5
    window_height -= number_of_lines_for_input # (it is the same as window_height = window_height - number_of_lines_for_input)
    # return the function with dictionary data
    return [window_width, window_height]
'''-------------------- Get Window Size --------------------'''


'''-------------------- Render Screen --------------------'''
import re
import os

def visible_length(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return len(ansi_escape.sub('', text))

def render_screen(ascii: list, height_of_ascii: int):
    os.system("cls||clear")  

    ws = window_size() 

    number_of_lines = height_of_ascii  
    vertical_padding_before_divided = ws[1] - number_of_lines  

    if vertical_padding_before_divided % 2 != 0:  
        vertical_padding_before_divided -= 1

    vertical_padding = vertical_padding_before_divided // 2 
    line_of_sentence_start = vertical_padding  

    for i in range(ws[1]): 

        if i == 0 or i == ws[1] - 1:
            print("-" * ws[0])

        elif i < line_of_sentence_start or i >= line_of_sentence_start + number_of_lines:
            print("|" + " " * (ws[0] - 2) + "|")

        else:
            sentence = ascii[i - line_of_sentence_start]  

            horizontal_padding_before_divided = ws[0] - visible_length(sentence) - 2 

            if horizontal_padding_before_divided % 2 == 0:
                horizontal_padding = horizontal_padding_before_divided // 2  
                is_odd = False
            else:
                horizontal_padding = (horizontal_padding_before_divided - 1) // 2  
                is_odd = True

            print("|" + " " * horizontal_padding + sentence, end="")
            if is_odd:
                print(" " * (horizontal_padding + 1) + "|") 
            else:
                print(" " * horizontal_padding + "|") 

'''-------------------- Render Screen --------------------'''

def display_iteration(display_text, iterations, current_score, option, restarts=None):
        # ANSI color codes
        white = "\033[97m"
        reset = "\033[96m"

        if option == "random_restart":
            time.sleep(1)
            display_text.append(f"Restart {white}{iterations + 1}/{restarts}{reset}")
            display_text.append(f"End of Restart {white}{iterations + 1}{reset} | {white}Best score = {current_score}{reset}")
            display_text.append(" ")
        else:
            display_text.append(f"Iteration: {white}{iterations + 1}{reset}")
            display_text.append(f"Current Score: {white}{current_score}{reset}")
            display_text.append(" ")

        # Use render_screen to display the formatted text
        render_screen(display_text, len(display_text))

        # Clear the screen every 10 iterations
        if (iterations + 1) % 5 == 0:
            display_text = []

        return display_text

def printascii(typegambar: str):
    '''-------------------- Atur Warna Terminal--------------------'''
    os.system("cls||clear")

    cmd = 'color 3' # Warna Aqua

    os.system(cmd)
    '''-------------------- Atur Warna Terminal --------------------'''


    '''-------------------- Tipe Animasi --------------------'''

    if typegambar == "home": # Menampilkan Animasi Main Menu (Saat awal sebelum login)
        render_screen(Home, 35) # Untuk menampilkan ascii
    '''-------------------- Tipe Animasi --------------------'''

'''------------------------------------------------------------ Print Animasi ------------------------------------------------------------'''
