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
    """Calculate the length of visible characters, ignoring ANSI codes."""
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return len(ansi_escape.sub('', text))

def render_screen(ascii: list, height_of_ascii: int):
    os.system("cls||clear")  # Clear terminal before rendering

    ws = window_size()  # Get window size

    number_of_lines = height_of_ascii  # Number of lines to print
    vertical_padding_before_divided = ws[1] - number_of_lines  # Total top and bottom padding

    if vertical_padding_before_divided % 2 != 0:  # If the total padding is odd
        vertical_padding_before_divided -= 1

    vertical_padding = vertical_padding_before_divided // 2  # Split padding evenly
    line_of_sentence_start = vertical_padding  # Line number where text begins

    for i in range(ws[1]):  # Loop to print each line of the terminal size

        # First and last lines print a full row of '-'
        if i == 0 or i == ws[1] - 1:
            print("-" * ws[0])

        # Empty lines (not for printing text)
        elif i < line_of_sentence_start or i >= line_of_sentence_start + number_of_lines:
            print("|" + " " * (ws[0] - 2) + "|")

        # Lines with text
        else:
            sentence = ascii[i - line_of_sentence_start]  # Sentence from the list

            # Calculate padding, considering only visible characters
            horizontal_padding_before_divided = ws[0] - visible_length(sentence) - 2  # Padding for left and right

            # Even or odd padding check
            if horizontal_padding_before_divided % 2 == 0:
                horizontal_padding = horizontal_padding_before_divided // 2  # Both sides equal
                is_odd = False
            else:
                horizontal_padding = (horizontal_padding_before_divided - 1) // 2  # Adjust for odd padding
                is_odd = True

            # Print text with borders and padding
            print("|" + " " * horizontal_padding + sentence, end="")
            if is_odd:
                print(" " * (horizontal_padding + 1) + "|")  # Extra space for odd padding
            else:
                print(" " * horizontal_padding + "|")  # Even padding

'''-------------------- Render Screen --------------------'''

def printascii(typegambar: str):
    '''-------------------- Atur Warna Terminal--------------------'''
    os.system("cls||clear")

    cmd = 'color 3' # Warna Aqua

    os.system(cmd)
    '''-------------------- Atur Warna Terminal --------------------'''


    '''-------------------- Tipe Animasi --------------------'''

    if typegambar == "home": # Menampilkan Animasi Main Menu (Saat awal sebelum login)
        render_screen(Home, 35) # Untuk menampilkan ascii
        time.sleep(0.5)
        time.sleep(1)
    '''-------------------- Tipe Animasi --------------------'''

'''------------------------------------------------------------ Print Animasi ------------------------------------------------------------'''
