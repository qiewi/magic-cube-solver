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
            diagonal1 = np.sum([layer[i, i] for i in range(self.n)])
            diagonal2 = np.sum([layer[i, self.n - i - 1] for i in range(self.n)])
            total_difference += abs(magic_number - diagonal1)
            total_difference += abs(magic_number - diagonal2)

        for row in range(self.n):
            diagonal1 = np.sum([self.cube[row, i, i] for i in range(self.n)])
            diagonal2 = np.sum([self.cube[row, i, self.n - i - 1] for i in range(self.n)])
            total_difference += abs(magic_number - diagonal1)
            total_difference += abs(magic_number - diagonal2)

        for col in range(self.n):
            diagonal1 = np.sum([self.cube[i, i, col] for i in range(self.n)])
            diagonal2 = np.sum([self.cube[i, self.n - i - 1, col] for i in range(self.n)])
            total_difference += abs(magic_number - diagonal1)
            total_difference += abs(magic_number - diagonal2)

        return total_difference

# Contoh penggunaan
cube_instance = Cube()
objective_value = cube_instance.objective_function()
print("Nilai fungsi objektif:", objective_value)
