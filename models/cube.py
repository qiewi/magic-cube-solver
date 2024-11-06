import numpy as np
import random

class Cube:
    def __init__(self):
        self.n = 5
        self.magic_number = 315

        # Mengisi kubus 5x5x5 dengan angka acak dari 1 hingga 125
        numbers = list(range(1, self.n ** 3 + 1))
        random.shuffle(numbers)
        self.cube = np.array([[[numbers.pop() for _ in range(self.n)] for _ in range(self.n)] for _ in range(self.n)])

        # self.cube = np.array([
        #     [
        #         [78, 109, 15, 41, 72],
        #         [45, 71, 77, 108, 14],
        #         [107, 13, 44, 75, 76],
        #         [74, 80, 106, 12, 43],
        #         [11, 42, 73, 79, 110]
        #     ],
        #     [
        #         [40, 66, 97, 103, 9],
        #         [102, 8, 39, 70, 96],
        #         [69, 100, 101, 7, 38],
        #         [6, 37, 68, 99, 105],
        #         [98, 104, 10, 36, 67]
        #     ],
        #     [
        #         [122, 3, 34, 65, 91],
        #         [64, 95, 121, 2, 33],
        #         [1, 32, 63, 94, 125],
        #         [93, 124, 5, 31, 62],
        #         [35, 61, 92, 123, 4]
        #     ],
        #     [
        #         [59, 90, 116, 22, 28],
        #         [21, 27, 58, 89, 120],
        #         [88, 119, 25, 26, 57],
        #         [30, 56, 87, 118, 24],
        #         [117, 23, 29, 60, 86]
        #     ],
        #     [
        #         [16, 47, 53, 84, 115],
        #         [83, 114, 20, 46, 52],
        #         [50, 51, 82, 113, 19],
        #         [112, 18, 49, 55, 81],
        #         [54, 85, 111, 17, 48]
        #     ]
        # ])


    def objective_function(self):
        # Mengambil magic number
        magic_number = self.magic_number
        total_difference = 0

        # Perbedaan jumlah di setiap baris
        for layer in self.cube:
            for row in layer:
                row_sum = np.sum(row)
                total_difference += abs(magic_number - row_sum)

        # Perbedaan jumlah di setiap kolom
        for layer in self.cube:
            for col in range(self.n):
                col_sum = np.sum(layer[:, col])
                total_difference += abs(magic_number - col_sum)

        # Perbedaan jumlah di setiap tiang (melintasi layer)
        for row in range(self.n):
            for col in range(self.n):
                pillar_sum = np.sum(self.cube[:, row, col])
                total_difference += abs(magic_number - pillar_sum)

        # Perbedaan jumlah di setiap diagonal ruang
        diagonals = [
            np.sum([self.cube[i, i, i] for i in range(self.n)]),
            np.sum([self.cube[i, i, self.n - i - 1] for i in range(self.n)]),
            np.sum([self.cube[i, self.n - i - 1, i] for i in range(self.n)]),
            np.sum([self.cube[i, self.n - i - 1, self.n - i - 1] for i in range(self.n)]),
        ]
        total_difference += sum(abs(magic_number - diag_sum) for diag_sum in diagonals)

        # Perbedaan jumlah di setiap diagonal bidang
        for layer in self.cube:
            diagonal1 = np.sum([layer[i, i] for i in range(self.n)])  # Diagonal dari kiri atas ke kanan bawah di setiap layer
            diagonal2 = np.sum([layer[i, self.n - i - 1] for i in range(self.n)])  # Diagonal dari kanan atas ke kiri bawah di setiap layer
            total_difference += abs(magic_number - diagonal1)
            total_difference += abs(magic_number - diagonal2)

        for row in range(self.n):
            diagonal1 = np.sum([self.cube[row, i, i] for i in range(self.n)])  # Diagonal dari kiri atas ke kanan bawah di setiap baris (3D)
            diagonal2 = np.sum([self.cube[row, i, self.n - i - 1] for i in range(self.n)])  # Diagonal dari kanan atas ke kiri bawah di setiap baris (3D)
            total_difference += abs(magic_number - diagonal1)
            total_difference += abs(magic_number - diagonal2)

        for col in range(self.n):
            diagonal1 = np.sum([self.cube[i, i, col] for i in range(self.n)])  # Diagonal dari kiri atas ke kanan bawah di setiap kolom (3D)
            diagonal2 = np.sum([self.cube[i, self.n - i - 1, col] for i in range(self.n)])  # Diagonal dari kanan atas ke kiri bawah di setiap kolom (3D)
            total_difference += abs(magic_number - diagonal1)
            total_difference += abs(magic_number - diagonal2)

        return total_difference

    def display_layered(self):
        for layer in range(self.n):
            print(f"\nLayer {layer + 1}:\n")
            for row in range(self.n):
                print(" " * (8 + 15 - (3*row)), end="") 
                for col in range(self.n):
                    print(f"{self.cube[layer][row][col]:>4}", end="   ")  
                print("")  
    

# cube_instance = Cube()
# objective_value = cube_instance.objective_function()

# cube_instance.display_layered()
# print("\n\nNilai fungsi objektif:", objective_value)
