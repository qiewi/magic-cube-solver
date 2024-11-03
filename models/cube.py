class Cube:
    def __init__(self):
        # Inisialisasi kubus 5x5x5 dengan angka dari 1 hingga 125
        self.n = 5
        self.magic_number = self.calculate_magic_number()
        self.cube = [[[num + 1 + x * self.n**2 + y * self.n for num in range(self.n)] 
                      for y in range(self.n)] 
                     for x in range(self.n)]
    
    def calculate_magic_number(self):
        # Menghitung magic number untuk kubus 5x5x5
        return (self.n * (self.n**3 + 1)) // 2
    
    def objective_function(self):
        # Jumlah dari selisih absolut dari magic number untuk setiap aturan
        f_s = 0
        f_s += sum(abs(self.magic_number - self.sum_row(i, j)) for i in range(self.n) for j in range(self.n))
        f_s += sum(abs(self.magic_number - self.sum_column(i, j)) for i in range(self.n) for j in range(self.n))
        f_s += sum(abs(self.magic_number - self.sum_pillar(i, j)) for i in range(self.n) for j in range(self.n))
        f_s += sum(abs(self.magic_number - self.sum_diagonal(i)) for i in range(4)) # Ada empat diagonal 3D
        f_s += sum(abs(self.magic_number - self.sum_slice(i, j)) for i in range(self.n) for j in range(3))
        return f_s

    def sum_row(self, layer, row):
        # Jumlah elemen pada baris tertentu di satu lapisan 5x5
        return sum(self.cube[layer][row][col] for col in range(self.n))

    def sum_column(self, layer, col):
        # Jumlah elemen pada kolom tertentu di satu lapisan 5x5
        return sum(self.cube[layer][row][col] for row in range(self.n))

    def sum_pillar(self, row, col):
        # Jumlah elemen pada tiang tertentu di semua lapisan
        return sum(self.cube[layer][row][col] for layer in range(self.n))

    def sum_diagonal(self, diag_type):
        # Jumlah elemen pada diagonal ruang utama berdasarkan diag_type
        # diag_type: 0-3, masing-masing mewakili salah satu dari empat diagonal 3D
        if diag_type == 0:
            return sum(self.cube[i][i][i] for i in range(self.n))
        elif diag_type == 1:
            return sum(self.cube[i][i][self.n - 1 - i] for i in range(self.n))
        elif diag_type == 2:
            return sum(self.cube[i][self.n - 1 - i][i] for i in range(self.n))
        elif diag_type == 3:
            return sum(self.cube[self.n - 1 - i][i][i] for i in range(self.n))

    def sum_slice(self, axis, index):
        # Jumlah elemen pada potongan (irisan 2D) dari kubus
        if axis == 0:  # Irisan sumbu x (lapisan tetap)
            return sum(self.cube[index][i][j] for i in range(self.n) for j in range(self.n))
        elif axis == 1:  # Irisan sumbu y (baris tetap)
            return sum(self.cube[i][index][j] for i in range(self.n) for j in range(self.n))
        elif axis == 2:  # Irisan sumbu z (kolom tetap)
            return sum(self.cube[i][j][index] for i in range(self.n) for j in range(self.n))
