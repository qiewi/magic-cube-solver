import numpy as np
import random

class Cube:
    # Konstruktor kelas Cube
    def __init__(self):
        # Inisialisasi besar kubus dan magic numbernya
        self.n = 5
        self.magic_number = 315

        # Mengisi kubus 5x5x5 dengan angka acak dari 1 hingga 125
        numbers = list(range(1, self.n ** 3 + 1))
        random.shuffle(numbers)
        self.cube = np.array([[[numbers.pop() for _ in range(self.n)] for _ in range(self.n)] for _ in range(self.n)])

    # Fungsi objektif untuk menghitung jumlah perbedaan antara jumlah setiap baris, kolom, dan diagonal dengan magic number
    def objective_function(self):
        # Mengambil magic number
        magic_number = self.magic_number
        total_difference = 0 # Nilai objektif paling optimal

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

    # Display Kubus 5x5x5 dengan efek-efek 3 dimensi
    def display_layered(self): 
        for layer in range(self.n):
            print(f"\nLayer {layer + 1}:\n")
            for row in range(self.n):
                print(" " * (8 + 15 - (3*row)), end="") 
                for col in range(self.n):
                    print(f"{self.cube[layer][row][col]:>4}", end="   ")  
                print("")  
    